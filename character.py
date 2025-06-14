import pygame
import math
import constants
import weapon


class Character():
    def __init__(self, x, y, health, mob_animations, char_type, boss, size):
        self.char_type = char_type
        self.boss = boss
        self.score = 0
        self.flip = False
        self.animation_list = mob_animations[char_type]
        self.frame_index = 0
        self.action = 0 #0:idle, 1:run
        self.update_time = pygame.time.get_ticks()
        self.running = False
        self.health = health
        self.alive = True
        self.hit = False
        self.last_hit = pygame.time.get_ticks()
        self.last_attack = pygame.time.get_ticks()
        self.stunned = False
        
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(x, y, constants.TILE_SIZE * size, constants.TILE_SIZE * size)
        self.rect.center = (x, y)
        
    def move(self, dx, dy, obstacle_tiles, exit_tile = None):
        screen_scroll = [0, 0]
        level_complete = False
        self.running = False
        # control diagonal speed
        if dx != 0 or dy != 0:
            self.running = True
        if dx > 0:
            self.flip = False
        elif dx < 0:
            self.flip = True
            
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2) / 2)
            dy = dy * (math.sqrt(2) / 2)    
        # check for collition with map in x direction 
        self.rect.x += dx
        for obstacle in obstacle_tiles:
            # check for collision
            if obstacle[1].colliderect(self.rect):
                # check which side of the collition is from
                if dx > 0:
                    self.rect.right = obstacle[1].left
                elif dx < 0:
                    self.rect.left = obstacle[1].right
        
        # check for collition with map in y direction
        self.rect.y += dy
        for obstacle in obstacle_tiles:
            # check for collision
            if obstacle[1].colliderect(self.rect):
                # check which side of the collition is from
                if dy > 0:
                    self.rect.bottom = obstacle[1].top
                elif dy < 0:
                    self.rect.top = obstacle[1].bottom

        # logic only applcable to player
        if self.char_type == 0:
            # check if player has reached the exit tile
            if exit_tile[1].colliderect(self.rect):
                # ensure player is close to the center of the exit ladder
                exit_dist = math.sqrt(((self.rect.centerx - exit_tile[1].centerx) ** 2) + ((self.rect.centery - exit_tile[1].centery) ** 2))
                if exit_dist < 20:
                    level_complete = True
                    
            # update scroll based on player position
            # move camera left and right
            if self.rect.right > constants.SCREEN_WIDTH - constants.SCROLL_THRESH:
                screen_scroll[0] = (constants.SCREEN_WIDTH - constants.SCROLL_THRESH)  - self.rect.right
                self.rect.right = constants.SCREEN_WIDTH - constants.SCROLL_THRESH
            if self.rect.left < constants.SCROLL_THRESH:
                screen_scroll[0] = constants.SCROLL_THRESH - self.rect.left
                self.rect.left = constants.SCROLL_THRESH

            # move camera up and down
            if self.rect.bottom > constants.SCREEN_HEIGHT - constants.SCROLL_THRESH:
                screen_scroll[1] = (constants.SCREEN_HEIGHT - constants.SCROLL_THRESH)  - self.rect.bottom
                self.rect.bottom = constants.SCREEN_HEIGHT - constants.SCROLL_THRESH
            if self.rect.top < constants.SCROLL_THRESH:
                screen_scroll[1] = constants.SCROLL_THRESH - self.rect.top
                self.rect.top = constants.SCROLL_THRESH
            
            return screen_scroll, level_complete
        
    def ai(self, player, obstacle_tiles, screen_scroll, fireball_image):
        
        clipped_line = ()
        stunned_cooldown = 100
        ai_dx = 0
        ai_dy = 0
        fireball = None
        
        # reposition the mobs based on screen scroll
        self.rect.x += screen_scroll[0]
        self.rect.y += screen_scroll[1]
        
        # create a line of sight from the enemy to the player
        line_of_sight = ((self.rect.centerx, self.rect.centery), (player.rect.centerx, player.rect.centery))
        # check if line of sight passes through an obstacle line
        for obstacle in obstacle_tiles:
            if obstacle[1].clipline(line_of_sight):
                clipped_line = obstacle[1].clipline(line_of_sight)
        
        # check distance to player
        dist = math.sqrt(((self.rect.centerx - player.rect.centerx) ** 2) + ((self.rect.centery - player.rect.centery) ** 2))
        if not clipped_line and dist > constants.RANGE:
            if self.rect.centerx > player.rect.centerx:
                ai_dx = -constants.ENEMY_SPEED
            if self.rect.centerx < player.rect.centerx:
                ai_dx = constants.ENEMY_SPEED
            if self.rect.centerx > player.rect.centerx:
                ai_dy = -constants.ENEMY_SPEED
            if self.rect.centerx < player.rect.centerx:
                ai_dy = constants.ENEMY_SPEED
        
        if self.alive:
            if not self.stunned:
                # move towards player
                self.move(ai_dx, ai_dy, obstacle_tiles)
                # attack player
                if dist < constants.ATTACK_RANGE and player.hit == False:
                    player.health -= 10
                    player.hit = True
                    player.last_hit = pygame.time.get_ticks()
                # boss enemies shoot fireballs
                fireball_cooldown = 700
                if self.boss:
                    if dist < 500:
                        if pygame.time.get_ticks() - self.last_attack >= fireball_cooldown:
                            # create a fireball
                            fireball = weapon.Fireball(fireball_image, self.rect.centerx, self.rect.centery, player.rect.centerx, player.rect.centery)
                            self.last_attack = pygame.time.get_ticks()
                    
            # check if hit
            if self.hit == True:
                self.hit = False
                self.last_hit = pygame.time.get_ticks()
                self.stunned = True
                self.running = False
                self.update_action(0)
            
            if (pygame.time.get_ticks() - self.last_hit) > stunned_cooldown:
                self.stunned = False
        
        return fireball
            
        
    def update(self):
        # check if charcter has died
        if self.health <= 0:
            self.health = 0
            self.alive = False
        
        # time to reset player taking a hit
        hit_cooldown = 1000
        if self.char_type == 0:
            if self.hit == True and (pygame.time.get_ticks() - self.last_hit) > hit_cooldown:
                self.hit = False
        
        # check what action the ploayer is performing
        if self.running == True:
            self.update_action(1) # 1:run
        else:
            self.update_action(0) # 0:idle
        animation_cooldown = 70
        # handle animation
        # update image
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed to update the frame
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
           
            # reset frame index if it exceeds the length of the animation list
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0
            # self.image = self.animation_list[self.frame_index]
    
    def update_action(self, new_action):
        # check if the new action is diffrent to the previous one
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
         
    def draw(self, surface):
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        
        if self.char_type == 0:
            surface.blit(flipped_image,(self.rect.x, self.rect.y - constants.SCALE * constants.OFFSET))
        else:
            surface.blit(flipped_image, self.rect)