#!/bin/bash

# 実行ディレクトリへ移動
cd ~/Downloads/ai-directory-scaffold

echo "🚀 Starting AI Directory pipeline at $(date)"

# ステップ1：RSS収集
python3 scripts/scraper.py

# ステップ2：要約生成
python3 scripts/summarizer.py

# ステップ3：HTML出力
python3 scripts/generate_static.py

echo "✅ All tasks completed successfully at $(date)"

