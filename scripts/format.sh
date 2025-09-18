#!/bin/bash
set -e

# スクリプトが置かれているディレクトリに移動
cd "$(dirname "$0")/.."

# ruffがインストールされていなければ、開発依存関係をインストールする
if [ ! -f ".venv/bin/ruff" ]; then
    echo "--- ruffが見つかりません。開発依存関係をインストールします... ---"
    # .venv がなければ作成
    if [ ! -d ".venv" ]; then
        uv venv
    fi
    uv pip install -e ".[dev]"
    echo "--- インストールが完了しました ---"
fi


echo "--- フォーマットとリントを実行中... ---"

echo "1/2: インポート整理と自動修正..."
uv run ruff check . --fix

echo "2/2: コードフォーマット..."
uv run ruff format .

echo "フォーマットが完了しました。"
