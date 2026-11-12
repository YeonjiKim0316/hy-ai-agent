"""app/thermo.py 테스트. SPEC.md 예시표 한 줄 = 테스트 한 줄."""

import pytest

from app.thermo import is_mismatch, to_label, to_temperature

LABEL_CASES = [  # SPEC.md 예시표 to_label: (score, 기대 결과)
    pytest.param(0.9, "positive", id="0.9"),
    pytest.param(0.5, "positive", id="0.5_boundary"),
    pytest.param(0.4999, "negative", id="0.4999"),
    pytest.param(0.1, "negative", id="0.1"),
]

TEMPERATURE_CASES = [  # SPEC.md 예시표 to_temperature: (score, 기대 결과)
    pytest.param(0.8732, 87.3, id="0.8732"),
    pytest.param(0.5, 50.0, id="0.5"),
    pytest.param(0.0, 0.0, id="0.0"),
    pytest.param(1.0, 100.0, id="1.0"),
]

MISMATCH_CASES = [  # SPEC.md 예시표 is_mismatch: (rating, label, 기대 결과)
    pytest.param(5, "negative", True, id="rating5_negative"),
    pytest.param(4, "negative", True, id="rating4_negative"),
    pytest.param(2, "positive", True, id="rating2_positive"),
    pytest.param(1, "positive", True, id="rating1_positive"),
    pytest.param(3, "negative", False, id="rating3_negative"),
    pytest.param(5, "positive", False, id="rating5_positive"),
    pytest.param(1, "negative", False, id="rating1_negative"),
]


@pytest.mark.parametrize("score, expected", LABEL_CASES)
def test_to_label(score, expected):
    # Given: 예시표 한 줄의 점수(score)와 기대 결과(expected)
    # When: 점수를 라벨로 바꾼다
    label = to_label(score)
    # Then: 기대한 라벨과 같다
    assert label == expected


@pytest.mark.parametrize("score, expected", TEMPERATURE_CASES)
def test_to_temperature(score, expected):
    # Given: 예시표 한 줄의 점수(score)와 기대 결과(expected)
    # When: 점수를 온도로 바꾼다
    temperature = to_temperature(score)
    # Then: 기대한 온도와 같다
    assert temperature == expected


@pytest.mark.parametrize("rating, label, expected", MISMATCH_CASES)
def test_is_mismatch(rating, label, expected):
    # Given: 예시표 한 줄의 별점(rating), 라벨(label), 기대 결과(expected)
    # When: 별점과 라벨이 반대인지 확인한다
    mismatch = is_mismatch(rating, label)
    # Then: 기대한 결과와 같다
    assert mismatch == expected


# © 2026 김연지. All rights reserved. 수강생 개인 학습용 · 무단 강의·복제·배포·수정 금지 (LICENSE.md)
