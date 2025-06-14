# Dungeon Crawler Game

## 概要
このプロジェクトは、PythonとPygameを使用して開発された2Dダンジョンクローラーゲームです。プレイヤーはキャラクターを操作し、敵を倒したり、アイテムを収集したりしながらダンジョンを探索します。ゲームにはスコアシステム、ライフシステム、武器システム、アニメーション、レベルデータの読み込み機能が含まれています。

---

## 特徴
- **プレイヤーキャラクター**: 上下左右に移動可能で、弓矢を使用して敵を攻撃。
- **敵キャラクター**: プレイヤーを追尾し、攻撃を仕掛けてくる。
- **アイテムシステム**: コインやポーションを収集してスコアを増加、ライフを回復。
- **レベルシステム**: CSVファイルからタイルマップを読み込み、複数のレベルを実装。
- **サウンド**: BGMや効果音を使用してゲーム体験を向上。
- **UI**: プレイヤーのライフやスコアを画面上部に表示。

---

## 必要条件
- Python 3.10以上
- Pygameライブラリ

---

## インストール方法

1. **リポジトリをクローン**
   ```bash
   git clone https://github.com/<your-username>/dungeon_crawler_game.git
   cd dungeon_crawler_game

2.必要なライブラリをインストール
  pip install pygame

3.アセットの確認
   assetsフォルダ内に必要な画像、音声、フォントファイルが揃っていることを確認してください。

実行方法
プロジェクトフォルダに移動します。
cd dungeon_crawler_game

ゲームを実行します。
python main.py

ディレクトリ構造
/
├── [main.py](http://_vscodecontentref_/0)               # メインゲームロジック
├── [character.py](http://_vscodecontentref_/1)          # キャラクタークラス
├── [weapon.py](http://_vscodecontentref_/2)             # 武器クラス
├── [items.py](http://_vscodecontentref_/3)              # アイテムクラス
├── [constants.py](http://_vscodecontentref_/4)          # 定数定義
├── [world.py](http://_vscodecontentref_/5)              # ワールド生成ロジック
├── assets/               # アセットフォルダ
│   ├── audio/            # サウンドファイル
│   ├── fonts/            # フォントファイル
│   ├── images/           # 画像ファイル
│       ├── buttons/      # ボタン画像
│       ├── characters/   # キャラクター画像
│       ├── items/        # アイテム画像
│       ├── tiles/        # タイル画像
│       ├── weapons/      # 武器画像
├── levels/               # レベルデータ
│   ├── level1_data.csv   # レベル1のタイルマップ
│   ├── level2_data.csv   # レベル2のタイルマップ
│   ├── ...
└── __pycache__/          # Pythonキャッシュ

操作方法
移動: W (上), A (左), S (下), D (右)
攻撃: マウス左クリック
ポーズ: ESC

今後の改善案
敵のAI強化:
敵がプレイヤーを追尾するロジックを追加。
新しいアイテムの追加:
攻撃力アップやスピードアップなどのアイテムを追加。
複数レベルの実装:
レベルクリア後に次のレベルへ進む機能を追加。
スコア保存機能:
ハイスコアを保存して表示する機能を追加。
ライセンス
このプロジェクトはMITライセンスの下で公開されています。詳細はLICENSEファイルを参照してください。
