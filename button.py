import pygame

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        # check if the mouse is over the button
        if self.rect.collidepoint(pos):
            # check for mouse click
            if pygame.mouse.get_pressed()[0]:
                action = True

        surface.blit(self.image, self.rect)
        
        return action