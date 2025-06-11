# 構築マニュアル: 2Dダンジョンクローラーゲーム

## 前提条件
- Python 3.10以上がインストールされていること。
- `pip`が使用可能であること。

---

## 手順

### 1. 必要なライブラリのインストール
以下のコマンドを実行して、Pygameをインストールします。

```bash
pip install pygame

/
├── [main.py](http://_vscodecontentref_/6)
├── [character.py](http://_vscodecontentref_/7)
├── [weapon.py](http://_vscodecontentref_/8)
├── [items.py](http://_vscodecontentref_/9)
├── [constants.py](http://_vscodecontentref_/10)
├── [world.py](http://_vscodecontentref_/11)
├── assets/
│   ├── audio/
│   ├── fonts/
│   ├── images/
│       ├── buttons/
│       ├── characters/
│       ├── items/
│       ├── tiles/
│       ├── weapons/
├── levels/

3. 必要なファイルの作成
以下のファイルを作成し、それぞれのコードを記述します。

main.py
ゲームのメインロジックを記述します。

character.py
キャラクターのクラスを記述します。

weapon.py
武器のクラスを記述します。

items.py
アイテムのクラスを記述します。

constants.py
ゲーム内で使用する定数を記述します。

world.py
ワールド（タイルマップ）の生成ロジックを記述します。

4. アセットの準備
assetsフォルダに以下のファイルを配置します。

audio:
arrow_hit.wav
arrow_shot.mp3
coin.wav
heal.wav
music.wav
fonts:
AtariClassic.ttf
images:
必要なボタン、キャラクター、アイテム、タイル、武器の画像。
5. レベルデータの作成
levelsフォルダにCSV形式でレベルデータを作成します。

例: level1_data.csv

0,0,0,0,0,0,0,0,0,0
0,0,7,0,0,0,0,8,0,0
0,0,0,0,0,0,0,0,0,0


6. ゲームの実行
main.pyを実行してゲームを開始します。


トラブルシューティング
Pygameがインストールされていないエラー:

pip install pygameを再実行してください。
画像や音声が読み込まれない:

assetsフォルダ内のファイルパスを確認してください。
ゲームがクラッシュする:

エラーメッセージを確認し、該当するコードを修正してください。