# 대시보드 명세 — 리뷰 현황

> © 2026 김연지. All rights reserved. 수강생 개인 학습용 · 무단 강의·복제·배포·수정 금지 · [LICENSE.md](LICENSE.md)

> 주어진 명세입니다. 읽기만 합니다. 고치는 곳은 4-3 단계에서 3장 표 맨 아래에 내 카드 줄을 붙여 넣을 때뿐입니다. 화면은 `static/dashboard.html`, 데이터를 채울 곳은 `app/dashboard.py`의 `QUERIES`입니다.

## 1. 한 문장 요약

MD팀이 리뷰 현황을 한눈에 볼 수 있게, 분석 기록 DB(`data/sample_logs.db`)에서 숫자를 뽑아 카드 2개(총 리뷰 수 + 내 카드)로 보여 준다.

## 2. 규칙

| 번호 | 규칙 |
|---|---|
| D1 | 카드마다 키(`QUERIES`의 이름)가 있고, 쿼리는 SELECT 또는 WITH로 시작하는 문장 한 개다 |
| D2 | 카드가 돌려주는 열의 이름과 순서, 정렬은 아래 3장 표대로다 |
| D3 | DB는 읽기만 한다. INSERT·UPDATE·DELETE 같은 쓰기는 하지 않는다 |
| D4 | 쿼리가 비어 있는 카드는 화면에 "쿼리를 채워 주세요"가 보인다 |

## 3. 카드

| 키 | 뜻 | 돌려줄 열 (순서대로) | 정렬 |
|---|---|---|---|
| `total` | 총 리뷰 수 | `count` | 한 줄 |
| `by_rating` | 별점별 리뷰 수 | `rating`, `count` | `rating` 순 |

## 4. 내 카드 후보 — 하나를 골라 3장 표 맨 아래에 그대로 붙여 넣습니다

| 키 | 뜻 | 돌려줄 열 (순서대로) | 정렬 |
|---|---|---|---|
| `by_label` | 긍정·부정 수 | `label`, `count` | `label` 순 |
| `keyword_counts` | 키워드가 들어간 리뷰 글의 수 | `keyword`, `review_count` | `review_count` 많은 순, 같으면 `keyword` 순 |
| `by_rating` | 별점별 리뷰 수 | `rating`, `count` | `rating` 순 |

- `keyword_counts`의 키워드는 이 10개로 고정입니다: 배송, 포장, 가격, 품질, 소리, 배터리, 사이즈, 색상, 환불, 재구매. 글에 그 단어가 들어 있으면 센다(한 리뷰는 키워드마다 한 번만).

## 5. 데이터 (`data/sample_logs.db`)

수업용으로 만든 가상 데이터입니다.

`analysis_logs` (분석 기록 한 줄이 리뷰 한 건)

| 열 | 뜻 |
|---|---|
| `id` | 번호 |
| `created_at` | 분석한 시각 (`2026-10-12T08:44:46` 꼴 글자) |
| `rating` | 별점 1~5 |
| `text_length` | 리뷰 글자 수 |
| `label` | AI가 본 결과 (`positive` / `negative`) |
| `score` | AI 점수 0~1 |
| `temperature` | 리뷰 온도 0~100 (정수) |
| `mismatch` | 별점과 내용이 반대인가 (1 = 그렇다, 0 = 아니다) |
| `review_text` | 리뷰 글 (가상) |

## 6. 돌려주는 모양 예시 (`by_label`)

| label | count |
|---|---|
| (첫째 label) | (숫자) |
| (둘째 label) | (숫자) |

열 이름은 `label`, `count` 그대로, 순서도 이 순서입니다. 행은 `label` 순입니다.
