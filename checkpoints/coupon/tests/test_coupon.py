"""app/coupon.py 테스트. SPEC_COUPON_OFFICIAL.md 예시표 한 줄 = 테스트 한 줄."""

import pytest

from app.coupon import decide_coupon

# r7의 글: "배송도 빠르고 포장도 꼼꼼해서 정말 만족합니다 또 살게요" (공백 포함 30자 이상)
PRAISE = "배송도 빠르고 포장도 꼼꼼해서 정말 만족합니다 또 살게요"
# 경계: 공백 포함 정확히 30자 / 29자
EXACT_30 = "배송이 빠르고 포장도 꼼꼼해서 정말 만족해요 또 살게요"
EXACT_29 = "배송이 빠르고 포장도 꼼꼼해서 정말 만족해요 또살게요"

NOT_ISSUED = {"issued": False, "coupon_type": None, "amount": None, "code": None}

COUPON_CASES = [  # SPEC_COUPON_OFFICIAL.md 예시표: (review_id, text, label, 기대 결과)
    pytest.param(
        "r2", "한쪽이 안 들려요", "negative",
        {"issued": True, "coupon_type": "APOLOGY", "amount": 3000, "code": "HARU-APL-R2"},
        id="r2_negative_apology",
    ),
    pytest.param(
        "r7", PRAISE, "positive",
        {"issued": True, "coupon_type": "THANKS", "amount": 1000, "code": "HARU-THX-R7"},
        id="r7_long_praise_thanks",
    ),
    pytest.param("r9", "좋아요", "positive", NOT_ISSUED, id="r9_short_praise_none"),
    pytest.param(
        "r4", EXACT_30, "positive",
        {"issued": True, "coupon_type": "THANKS", "amount": 1000, "code": "HARU-THX-R4"},
        id="r4_exactly_30_thanks",
    ),
    pytest.param("r5", EXACT_29, "positive", NOT_ISSUED, id="r5_29_chars_none"),
]


def test_boundary_texts_have_exact_length():
    """경계 행의 글이 정말 30자 / 29자인지 확인."""
    # Given: 경계 행에 쓰는 두 글(EXACT_30, EXACT_29)
    # When: 앞뒤 공백을 뺀 글자 수를 센다
    length_30 = len(EXACT_30.strip())
    length_29 = len(EXACT_29.strip())
    # Then: 각각 30자, 29자다
    assert length_30 == 30
    assert length_29 == 29


@pytest.mark.parametrize("review_id, text, label, expected", COUPON_CASES)
def test_decide_coupon(review_id, text, label, expected):
    # Given: 예시표 한 줄의 리뷰 번호, 글, 라벨과 기대 결과
    # When: 쿠폰을 정한다
    result = decide_coupon(review_id, text, label)
    # Then: 기대한 결과와 같다
    assert result == expected


def test_decide_coupon_same_request_twice():
    """같은 요청을 두 번 보내도 같은 결과 (예시표의 마지막 행)."""
    # Given: 같은 리뷰 번호, 글, 라벨
    # When: 쿠폰을 두 번 정한다
    first = decide_coupon("r2", "한쪽이 안 들려요", "negative")
    second = decide_coupon("r2", "한쪽이 안 들려요", "negative")
    # Then: 두 결과가 같고 코드는 HARU-APL-R2다
    assert first == second
    assert first["code"] == "HARU-APL-R2"


# © 2026 김연지. All rights reserved. 수강생 개인 학습용 · 무단 강의·복제·배포·수정 금지 (LICENSE.md)
