#!/bin/bash
set -e

# スクリプトが置かれているディレクトリに移動
cd "$(dirname "$0")/.."

echo "--- 仮想環境の作成と依存関係のインストール ---"

# .venv がなければ作成
if [ ! -d ".venv" ]; then
    echo "仮想環境を作成します..."
    uv venv
fi

# 依存関係をインストール
echo "依存関係をインストールします..."
uv pip install -e ".[dev]"

echo "インストールが完了しました。"
