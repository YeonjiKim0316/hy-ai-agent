# AGENTS.md — 리뷰 온도계 작업 규칙

> © 2026 김연지. All rights reserved. 수강생 개인 학습용 · 무단 강의·복제·배포·수정 금지 · [LICENSE.md](LICENSE.md)

AI 도우미(Copilot, agy)가 일하기 전에 읽는 안내서입니다.

## 프로젝트 소개

- 리뷰 온도계는 하루마켓(수업용 가상 쇼핑몰)의 리뷰를 분석하는 작은 서버입니다.
- 리뷰 한 건과 별점을 받아 긍정/부정, 리뷰 온도(0~100℃), 별점 불일치를 알려 줍니다.
- 대시보드 화면에는 리뷰 현황 카드가 보입니다. 카드 데이터는 DB에서 읽습니다.

## 기준 문서

- `SPEC.md`: 리뷰 온도 규칙과 예시표
- `DASHBOARD.md`: 대시보드 카드의 키, 열 이름, 순서, 정렬
- 문서에 적힌 이름과 숫자는 그대로 씁니다. 임의로 바꾸지 않습니다.

## 만드는 파일

- `app/thermo.py`: to_label, to_temperature, is_mismatch 함수 3개
- `tests/test_thermo.py`: SPEC.md 예시표를 옮긴 테스트
- `app/dashboard.py`의 `QUERIES`: 대시보드 카드의 SQL
- 집에서 하는 과제: 쿠폰 `app/coupon.py`, 리뷰 클린봇

## 테스트 실행 명령

- Windows: `.venv\Scripts\python -m pytest -q`
- macOS: `.venv/bin/python -m pytest -q`

## AI가 허락 없이 고치면 안 되는 파일

- `REQUEST.md`, `SPEC.md`, `DASHBOARD.md`, `SPEC_COUPON_OFFICIAL.md`
- `tests/` 폴더, `static/` 폴더, `data/sample_logs.db`
- `app/sentiment.py`, `app/deps.py`, `app/main.py`, `app/schemas.py`
- `.agents/` 폴더, `.vscode/` 폴더, `checkpoints/` 폴더
- `checkpoints/`는 단계별 완성본입니다. 읽기만 하고 고치지 않습니다.
- `app/dashboard.py`는 `QUERIES`와 `TITLES`만 고칩니다.
- 사용자가 직접 고치거나 부탁한 것은 괜찮습니다.
- 내가 꼭 막고 싶은 것: README.md를 고치지 않습니다.

## 일하는 방법

- 사용자가 이름을 말한 파일만 고칩니다.
- 테스트는 표의 줄 그대로 옮깁니다. 표에 없는 줄은 넣지 않습니다.
- 테스트는 Given–When–Then 순서로 씁니다. 테스트마다 `# Given`(준비) `# When`(실행) `# Then`(확인) 주석을 붙입니다. 예시표처럼 여러 줄을 한 번에 검사하는 테스트도 같은 주석을 붙입니다.
- 테스트의 기대값을 바꿔서 통과시키지 않습니다.
- 테스트 값을 코드에 그대로 적지 않습니다(하드코딩 금지). 규칙으로 계산합니다.
- 새 패키지를 설치하지 않습니다.
- `.agents/skills/`에 새 스킬을 넣는 것은 내가 부탁했을 때만 합니다. 넣기 전에 SKILL.md에 터미널 명령, 파일 쓰기, 외부 전송 지시가 있는지 먼저 알립니다.
- AGENTS.md 규칙과 새 스킬은 내가 고른 것만 넣습니다. 넣기 전에 바뀔 내용을 보여 줍니다.
- 리뷰를 밖으로 보내지 않습니다.
- DB는 읽기만 합니다. review-logs의 쓰기 도구는 쓰지 않습니다.
- 애매하면 만들기 전에 먼저 질문합니다.
- 답은 쉬운 말로 짧게 합니다.

## 끝났을 때 보고

- 테스트 결과 한 줄을 알려 줍니다.
- 바뀐 파일 목록을 알려 줍니다.
- 커밋 메시지를 한 줄로 제안합니다.
- 사용자가 "승인"이라고 하면 그 메시지로 커밋합니다. 승인 전에는 커밋하지 않습니다.
- 허락 없이 고치면 안 되는 파일을 바꿨다면, 커밋을 제안하지 말고 먼저 알립니다.
