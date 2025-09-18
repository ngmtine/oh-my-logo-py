# oh-my-logo-py

[oh-my-logo](https://github.com/shinshin86/oh-my-logo) の Python 移植版です

## 開発手順 (Development Workflow)

このプロジェクトは `uv` と `scripts` ディレクトリ内のシェルスクリプトを使って管理されています

### 1. 依存関係のインストール

最初に、以下のコマンドを実行して、仮想環境の作成とすべての依存関係のインストールを行います

```bash
./scripts/install.sh
```

### 2. CLI ツールの実行

`run.sh` スクリプトを使って `oh-my-logo-py` を実行します

**基本的な使い方**

```bash
./scripts/run.sh "Hello World"
```

**オプションを指定**

```bash
./scripts/run.sh "hello, world!" -p sunset --filled
./scripts/run.sh "lazy fox" -p purple-red --filled -f slick
./scripts/run.sh "lorem ipsum" --filled --gallery
```

### 3. 開発時のコマンド

開発用のタスクは `scripts` ディレクトリ内のスクリプトを実行します

**コードのフォーマットとインポート整理**

```bash
./scripts/format.sh
```

**静的解析と Linter**

```bash
./scripts/check.sh
```

**型チェック**

```bash
./scripts/typecheck.sh
```

## ライブラリとして使用する場合

このプロジェクトは、他の Python プロジェクトからライブラリとして利用することもできます

### 使用例

以下のように `oh_my_logo` 関数をインポートして使用します

```python
from oh_my_logo_py import oh_my_logo

# テキストとデフォルトのスタイルでロゴを表示
oh_my_logo("Hello World")

# パレットを指定して表示
oh_my_logo("Pythonista", palette_name="grad-purple")

# フォントや塗りつぶしオプションも指定可能
oh_my_logo("FILLED", palette_name="mono", font="block", filled=True)
```

`oh_my_logo` 関数は以下の引数を取ります

-   `text` (str): 表示するテキスト
-   `palette_name` (str): カラーパレット名 (デフォルト: `"grad-blue"`)
-   `font` (str): `pyfiglet` または `cfonts` で使用するフォント名 (デフォルト: `"standard"`)
-   `filled` (bool): `cfonts` を使った塗りつぶしモードを有効にするか (デフォルト: `False`)

## `uv` を直接使用した開発手順

シェルスクリプトを使用しない場合は、`uv` を使って直接開発コマンドを実行できます

### 1. 仮想環境の作成と依存関係のインストール

```bash
# 仮想環境の作成
uv venv

# 仮想環境のアクティベート (uv run を使う場合は任意)
source .venv/bin/activate

# 依存関係のインストール
uv pip install -e ".[dev]"
```

### 2. CLI ツールの実行

```bash
uv run oh-my-logo-py "Hello World" -p sunset
```

### 3. 開発時のコマンド

-   **フォーマットとリント (自動修正あり):**

```bash
uv run ruff check . --fix
uv run ruff format .
```

-   **型チェック:**

```bash
uv run pyright
```
