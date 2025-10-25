#!/bin/bash
# ======================================
# AI Directory 自動更新パイプライン
# RSS収集 → 要約 → HTML生成 → GitHub反映
# ======================================

set -e  # エラーが出たら停止

echo "🚀 パイプライン開始：$(date)"

# Python仮想環境を有効化（venv が同階層にある想定）
if [ -d "venv" ]; then
  source venv/bin/activate
  echo "✅ 仮想環境を有効化しました。"
else
  echo "⚠️ venv が見つかりません。'python3 -m venv venv' で作成してください。"
  exit 1
fi

# ステップ1：RSS収集
echo "📡 RSS収集中..."
python3 scripts/scraper.py

# ステップ2：要約処理
echo "🧠 要約処理中..."
python3 scripts/summarizer.py

# ステップ3：HTML生成
echo "📝 静的HTMLを生成中..."
python3 scripts/generate_static.py

# ステップ4：GitHub反映
echo "🌐 GitHub Pagesに反映中..."
git add .
git commit -m "Auto update: $(date '+%Y-%m-%d %H:%M:%S')" || echo "⚠️ 変更なしのためコミットスキップ"
git push origin main

echo "✅ パイプライン完了：$(date)"

