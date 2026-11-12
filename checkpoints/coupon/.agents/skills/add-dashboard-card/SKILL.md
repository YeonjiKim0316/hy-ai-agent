---
name: add-dashboard-card
description: 대시보드에 카드 하나를 더할 때 쓴다. DASHBOARD.md의 카드 한 줄을 명세로 보고, 테스트 먼저, 그다음 쿼리 순서로 한다.
---

# 대시보드 카드 하나 더하기

1. 사용자가 고른 카드 줄을 DASHBOARD.md 3장 표에서 찾는다. 없으면 어떤 줄인지 묻는다.
2. 그 줄로 tests/test_dashboard.py 맨 아래에 테스트를 하나 더한다(Given / When / Then 주석). 열 이름과 순서, 행이 1개 이상인지만 본다.
3. 테스트가 빨강인지 확인하고 사용자에게 알린다.
4. review-logs로 SQL을 실행해 결과를 보여 준다.
5. 결과가 맞으면 app/dashboard.py의 QUERIES에 새 키로 넣고, 테스트가 모두 초록인지 확인한다.

## 규칙
- 기존 테스트와 DASHBOARD.md는 고치지 않는다.
- DB는 읽기만 한다.
- 끝나면 테스트 결과 한 줄, 바뀐 파일, 커밋 메시지 한 줄을 제안한다.

<!-- © 2026 김연지. All rights reserved. 수강생 개인 학습용 · 무단 강의·복제·배포·수정 금지 (LICENSE.md) -->
