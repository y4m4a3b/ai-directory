#!/bin/bash
set -e  # エラーが出たら即停止

# === 設定 ===

REPO_DIR="$HOME/Downloads/ai-directory-scaffold"
LOG_FILE="$REPO_DIR/pipeline.log"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "=============================" >> "$LOG_FILE"
echo "🚀 パイプライン実行開始: $DATE" >> "$LOG_FILE"
echo "=============================" >> "$LOG_FILE"

cd "$REPO_DIR" || { echo "❌ ディレクトリが見つかりません"; exit 1; }

# === ステップ1: RSS収集 ===

echo "📡 ステップ1: RSS収集中..." | tee -a "$LOG_FILE"
python3 scripts/scraper.py >> "$LOG_FILE" 2>&1

# === ステップ2: 要約生成 ===

echo "🧠 ステップ2: 要約生成中..." | tee -a "$LOG_FILE"
python3 scripts/summarizer.py >> "$LOG_FILE" 2>&1

# === ステップ3: HTML出力 ===

echo "🖋️ ステップ3: HTML生成中..." | tee -a "$LOG_FILE"
python3 scripts/generate_static.py >> "$LOG_FILE" 2>&1

# === ステップ4: GitHub に自動コミット & プッシュ ===

echo "📤 ステップ4: GitHubに自動プッシュ..." | tee -a "$LOG_FILE"

git add .
git commit -m "auto update: $DATE" >> "$LOG_FILE" 2>&1 || echo "（変更なし）" >> "$LOG_FILE"
git push origin main >> "$LOG_FILE" 2>&1

echo "✅ すべて完了: $DATE" | tee -a "$LOG_FILE"
echo "=============================" >> "$LOG_FILE"


