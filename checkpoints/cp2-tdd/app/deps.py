"""강사 제공 파일: 라우터가 분류기를 받는 의존성.

테스트에서는 `app.dependency_overrides[get_predict]` 로 가짜 함수로 바꿔 끼운다.
대시보드가 읽는 DB 파일의 경로(`get_dashboard_db`)도 같은 방법으로 바꿔 끼울 수 있다.
"""

from collections.abc import Callable
from pathlib import Path

from app import sentiment


def get_predict() -> Callable[[list[str]], list[float]]:
    return sentiment.predict


def get_dashboard_db() -> str:
    """대시보드가 읽는 샘플 DB의 경로 (data/sample_logs.db). 읽기 전용으로만 연다."""
    return str(Path(__file__).resolve().parent.parent / "data" / "sample_logs.db")

# © 2026 김연지. All rights reserved. 수강생 개인 학습용 · 무단 강의·복제·배포·수정 금지 (LICENSE.md)
