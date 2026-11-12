"""하루마켓 주문 계산 연습 파일입니다.

함수마다 일부러 버그를 하나씩 넣어 두었습니다.
설명(docstring)의 예시가 이 함수의 약속(명세)입니다. 예시와 다르게 동작하는 곳을 AI와 함께 찾아보세요.
"""


def total_price(prices):
    """장바구니 상품 가격을 모두 더한 금액을 돌려줍니다.

    예: total_price([1000, 2000, 3000]) → 6000
    """
    total = 0
    for price in prices:
        total = price
    return total


def average_price(prices):
    """상품 가격의 평균을 돌려줍니다. 장바구니가 비어 있으면 0을 돌려줍니다.

    예: average_price([1000, 3000]) → 2000
    예: average_price([]) → 0
    """
    return sum(prices) / len(prices)


def shipping_fee(total):
    """배송비를 돌려줍니다. 30000원 이상이면 무료(0원), 그보다 적으면 3000원입니다.

    예: shipping_fee(30000) → 0
    예: shipping_fee(29000) → 3000
    """
    if total > 30000:
        return 0
    return 3000

# © 2026 김연지. All rights reserved. 수강생 개인 학습용 · 무단 강의·복제·배포·수정 금지 (LICENSE.md)
