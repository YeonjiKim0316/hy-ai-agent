"""리뷰 대시보드의 데이터 (강사 제공 뼈대). 세션 4에서 AI와 함께 QUERIES를 채웁니다.

화면(static/dashboard.html)은 카드마다 여기서 돌려준 결과를 보여 줍니다.
카드마다 무슨 열을 어떤 순서로 돌려줄지는 DASHBOARD.md에 적혀 있습니다.
고치는 곳은 아래 QUERIES(와 카드를 더할 때 TITLES)뿐입니다. 다른 부분은 고치지 않습니다.
"""

import sqlite3
from pathlib import Path
from urllib.parse import quote

# 카드 키 -> SQL 한 문장 (SELECT 또는 WITH로 시작). 비어 있으면 화면에 "쿼리를 채워 주세요"가 보입니다.
# 열 이름·순서·정렬은 DASHBOARD.md를 따릅니다. 데이터는 data/sample_logs.db 입니다.
QUERIES: dict[str, str] = {
    # 총 리뷰 수 -> 열: count
    "total": "SELECT COUNT(*) AS count FROM analysis_logs",
    # 내 카드는 아래에 새 키로 더합니다
    # 내 카드 예시 (세션 4)
    "by_rating": "SELECT rating, COUNT(*) AS count FROM analysis_logs GROUP BY rating ORDER BY rating",
}

# 화면에 보이는 카드 제목. 새 카드를 추가해도 제목이 없으면 키가 그대로 제목으로 보입니다.
TITLES: dict[str, str] = {
    "total": "총 리뷰 수",
    "by_label": "긍정·부정 수",
    "keyword_counts": "키워드별 리뷰 수",
    "by_rating": "별점별 리뷰 수",
}


def check_sql(sql: str) -> str:
    """SELECT 또는 WITH로 시작하는 문장 한 개만 허락한다. 아니면 ValueError."""
    text = sql.strip().rstrip(";").strip()
    if ";" in text:
        raise ValueError("문장은 한 개만 쓸 수 있습니다 (세미콜론 금지)")
    if text.split(None, 1)[0].upper() not in ("SELECT", "WITH"):
        raise ValueError("SELECT 또는 WITH로 시작하는 쿼리만 쓸 수 있습니다")
    return text


def open_readonly(db_path: str) -> sqlite3.Connection:
    """DB를 읽기 전용으로 연다. 쓰려고 하면 SQLite가 오류를 낸다."""
    uri = "file:" + quote(Path(db_path).resolve().as_posix()) + "?mode=ro"
    return sqlite3.connect(uri, uri=True)


def run_dashboard(db_path: str) -> dict[str, dict]:
    """카드마다 결과를 돌려준다.

    빈 쿼리   -> {"title", "todo": True}
    채운 쿼리 -> {"title", "columns": [...], "rows": [[...], ...]}
    오류      -> {"title", "error": "메시지"}
    """
    results: dict[str, dict] = {}
    with open_readonly(db_path) as conn:
        for key, sql in QUERIES.items():
            title = TITLES.get(key, key)
            if not sql.strip():
                results[key] = {"title": title, "todo": True}
                continue
            try:
                cursor = conn.execute(check_sql(sql))
                results[key] = {
                    "title": title,
                    "columns": [c[0] for c in cursor.description],
                    "rows": [list(r) for r in cursor.fetchall()],
                }
            except (ValueError, sqlite3.Error) as exc:
                results[key] = {"title": title, "error": str(exc)}
    return results

# © 2026 김연지. All rights reserved. 수강생 개인 학습용 · 무단 강의·복제·배포·수정 금지 (LICENSE.md)
