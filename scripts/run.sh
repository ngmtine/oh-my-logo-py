#!/bin/bash
set -e

# スクリプトが置かれているディレクトリに移動
cd "$(dirname "$0")/.."

# oh-my-logo-pyがインストールされていなければ、依存関係をインストールする
if [ ! -f ".venv/bin/oh-my-logo-py" ]; then
    echo "--- oh-my-logo-pyが見つかりません。依存関係をインストールします... ---"
    # .venv がなければ作成
    if [ ! -d ".venv" ]; then
        uv venv
    fi
    uv pip install -e ".[dev]"
    echo "--- インストールが完了しました ---"
fi

# このスクリプトに渡されたすべての引数（"$@"）を oh-my-logo-py に渡す
uv run oh-my-logo-py "$@"
