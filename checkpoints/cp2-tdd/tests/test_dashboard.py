"""대시보드 테스트 (강사 제공). DASHBOARD.md의 카드가 맞는 열 이름·값을 돌려주는지 확인합니다.

기대값은 data/sample_logs.db 를 직접 세어서 정한 값입니다. 쿼리를 아직 안 채운 카드는 건너뜁니다(skipped).
채운 쿼리가 틀리면 실패(FAILED)합니다.
내 카드 테스트는 맨 아래에 더합니다. 그 밖의 부분은 고치지 않습니다. 실패하면 app/dashboard.py 의 QUERIES 쿼리를 고칩니다.
"""

import pytest

from app import dashboard
from app.deps import get_dashboard_db

# 카드 키 -> (열 이름, 기대하는 행)
EXPECTED = {
    "total": (["count"], [[462]]),
}


@pytest.fixture
def cards(make_client):
    """/v1/dashboard 가 돌려준 카드들."""
    r = make_client(0.5).get("/v1/dashboard")
    assert r.status_code == 200
    return r.json()


@pytest.mark.parametrize("key", list(EXPECTED))
def test_card(cards, key):
    """쿼리를 채운 카드는 열 이름과 값이 DASHBOARD.md대로다. 빈 카드는 건너뛴다."""
    card = cards[key]
    if card.get("todo"):
        pytest.skip(f"쿼리를 채우면 검사합니다 (app/dashboard.py · {key})")
    assert "error" not in card, f'QUERIES["{key}"] 오류: {card.get("error")}'
    columns, rows = EXPECTED[key]
    assert card["columns"] == columns
    assert card["rows"] == rows


def test_write_query_is_rejected(monkeypatch):
    """INSERT·UPDATE·DELETE 같은 쓰기 쿼리는 실행되지 않고 오류로 돌아온다."""
    monkeypatch.setattr(dashboard, "QUERIES", {"bad": "DELETE FROM analysis_logs"})
    card = dashboard.run_dashboard(get_dashboard_db())["bad"]
    assert "error" in card


def test_only_one_statement(monkeypatch):
    """문장이 두 개 이상이면 오류로 돌아온다."""
    monkeypatch.setattr(dashboard, "QUERIES", {"two": "SELECT 1; SELECT 2"})
    card = dashboard.run_dashboard(get_dashboard_db())["two"]
    assert "error" in card

# © 2026 김연지. All rights reserved. 수강생 개인 학습용 · 무단 강의·복제·배포·수정 금지 (LICENSE.md)
