#!/bin/bash
set -e

# スクリプトが置かれているディレクトリに移動
cd "$(dirname "$0")/.."

# pyrightがインストールされていなければ、開発依存関係をインストールする
if [ ! -f ".venv/bin/pyright" ]; then
    echo "--- pyrightが見つかりません。開発依存関係をインストールします... ---"
    # .venv がなければ作成
    if [ ! -d ".venv" ]; then
        uv venv
    fi
    uv pip install -e ".[dev]"
    echo "--- インストールが完了しました ---"
fi

echo "--- pyrightで型チェックを実行中... ---"
uv run pyright

echo "型チェックが完了しました。"
