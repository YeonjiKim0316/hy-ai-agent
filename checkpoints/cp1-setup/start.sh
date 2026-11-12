#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
if [ ! -x .venv/bin/python ]; then
  echo "[1/3] 가상환경을 만듭니다..."
  python3 -m venv .venv
fi
echo "[2/3] 패키지를 설치합니다. 처음에는 몇 분 걸립니다..."
if ! .venv/bin/python -m pip install -q -r requirements.txt; then
  echo "설치에 실패했습니다. 빨간 줄을 복사해 Copilot에게 물어보세요."
  exit 1
fi
echo "[3/3] 서버를 켭니다. 브라우저에서 http://localhost:8000 을 여세요. 끌 때는 Ctrl+C"
.venv/bin/python -m uvicorn app.main:app --reload

# © 2026 김연지. All rights reserved. 수강생 개인 학습용 · 무단 강의·복제·배포·수정 금지 (LICENSE.md)
