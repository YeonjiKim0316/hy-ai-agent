"""쿠폰 API 계약 테스트 (강사 제공). SPEC_COUPON_OFFICIAL.md의 약속을 HTTP 요청과 응답만으로 확인합니다.

내부 함수 이름이나 파일 구조는 보지 않습니다. 그래서 어떻게 나눠 만들든 약속만 지키면 통과합니다.
"""

PRAISE = "배송도 빠르고 포장도 꼼꼼해서 정말 만족합니다 또 살게요"  # 30자 이상


def test_coupon_apology(make_client):
    """부정(점수 0.2) -> 사과 쿠폰 HARU-APL-R2."""
    # Given: 점수 0.2를 돌려주는 가짜 AI
    client = make_client(0.2)
    # When: 쿠폰을 요청한다
    r = client.post("/v1/coupons/issue", json={"review_id": "r2", "text": "한쪽이 안 들려요"})
    # Then: 사과 쿠폰이 나온다
    assert r.status_code == 200
    assert r.json() == {"issued": True, "coupon_type": "APOLOGY", "amount": 3000, "code": "HARU-APL-R2"}


def test_coupon_thanks(make_client):
    """긍정(점수 0.9) + 30자 이상 -> 감사 쿠폰."""
    # Given: 점수 0.9를 돌려주는 가짜 AI
    client = make_client(0.9)
    # When: 30자 이상의 좋은 리뷰로 쿠폰을 요청한다
    r = client.post("/v1/coupons/issue", json={"review_id": "r7", "text": PRAISE})
    # Then: 감사 쿠폰이 나온다
    assert r.status_code == 200
    assert r.json() == {"issued": True, "coupon_type": "THANKS", "amount": 1000, "code": "HARU-THX-R7"}


def test_coupon_short_praise(make_client):
    """긍정이어도 글이 짧으면 미발급 (그래도 200)."""
    # Given: 점수 0.9를 돌려주는 가짜 AI
    client = make_client(0.9)
    # When: 짧은 글로 쿠폰을 요청한다
    r = client.post("/v1/coupons/issue", json={"review_id": "r9", "text": "좋아요"})
    # Then: 쿠폰이 나가지 않는다
    assert r.status_code == 200
    assert r.json() == {"issued": False, "coupon_type": None, "amount": None, "code": None}


def test_coupon_same_request_same_code(make_client):
    """같은 요청을 두 번 보내도 같은 코드 (중복 발급 없음)."""
    # Given: 점수 0.2를 돌려주는 가짜 AI와 같은 요청 내용
    client = make_client(0.2)
    body = {"review_id": "r2", "text": "한쪽이 안 들려요"}
    # When: 같은 요청을 두 번 보낸다
    first = client.post("/v1/coupons/issue", json=body).json()
    second = client.post("/v1/coupons/issue", json=body).json()
    # Then: 코드가 같다
    assert first["code"] == second["code"] == "HARU-APL-R2"


def test_coupon_exactly_30_chars(make_client):
    """공백 포함 정확히 30자 -> 감사 쿠폰."""
    # Given: 점수 0.9를 돌려주는 가짜 AI와 정확히 30자인 글
    client = make_client(0.9)
    text = "배송이 빠르고 포장도 꼼꼼해서 정말 만족해요 또 살게요"
    assert len(text) == 30
    # When: 쿠폰을 요청한다
    r = client.post("/v1/coupons/issue", json={"review_id": "r4", "text": text})
    # Then: 감사 쿠폰이 나온다
    assert r.status_code == 200
    assert r.json() == {"issued": True, "coupon_type": "THANKS", "amount": 1000, "code": "HARU-THX-R4"}


def test_coupon_29_chars(make_client):
    """29자 -> 미발급 (그래도 200)."""
    # Given: 점수 0.9를 돌려주는 가짜 AI와 29자인 글
    client = make_client(0.9)
    text = "배송이 빠르고 포장도 꼼꼼해서 정말 만족해요 또살게요"
    assert len(text) == 29
    # When: 쿠폰을 요청한다
    r = client.post("/v1/coupons/issue", json={"review_id": "r5", "text": text})
    # Then: 쿠폰이 나가지 않는다
    assert r.status_code == 200
    assert r.json() == {"issued": False, "coupon_type": None, "amount": None, "code": None}


def test_coupon_invalid_input(make_client):
    """review_id 21자, 글 501자, 필드 없음은 422."""
    # Given: 점수 0.2를 돌려주는 가짜 AI
    client = make_client(0.2)
    # When: 잘못된 입력 네 가지를 보낸다
    too_long_id = client.post("/v1/coupons/issue", json={"review_id": "r" * 21, "text": "한쪽이 안 들려요"})
    too_long_text = client.post("/v1/coupons/issue", json={"review_id": "r2", "text": "가" * 501})
    no_text = client.post("/v1/coupons/issue", json={"review_id": "r2"})
    no_id = client.post("/v1/coupons/issue", json={"text": "한쪽이 안 들려요"})
    # Then: 모두 422다
    assert too_long_id.status_code == 422
    assert too_long_text.status_code == 422
    assert no_text.status_code == 422
    assert no_id.status_code == 422


def test_coupon_blank_text(make_client):
    """공백뿐인 글은 422."""
    # Given: 점수 0.2를 돌려주는 가짜 AI
    client = make_client(0.2)
    # When: 공백뿐인 글로 쿠폰을 요청한다
    r = client.post("/v1/coupons/issue", json={"review_id": "r2", "text": "  "})
    # Then: 422다
    assert r.status_code == 422


def test_coupon_ai_down(broken_client):
    """AI 부품이 고장 나면 503 (분석 API와 같은 방식)."""
    # Given: 고장 난 AI 부품(broken_client)
    # When: 쿠폰을 요청한다
    r = broken_client.post("/v1/coupons/issue", json={"review_id": "r2", "text": "한쪽이 안 들려요"})
    # Then: 503이다
    assert r.status_code == 503


# © 2026 김연지. All rights reserved. 수강생 개인 학습용 · 무단 강의·복제·배포·수정 금지 (LICENSE.md)
