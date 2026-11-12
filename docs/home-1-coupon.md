# 집에서 하는 과제 ① 쿠폰 발급 (3차 요청)

> © 2026 김연지. All rights reserved. 수강생 개인 학습용 · 무단 강의·복제·배포·수정 금지 · [LICENSE.md](../LICENSE.md)

수업이 끝난 뒤 집에서 합니다. 수업에서 한 순서(명세 → 테스트 먼저 → 구현)를 한 번 더 해 봅니다.
Copilot Chat을 Agent 모드로 두고, 서버를 켠 터미널은 그대로 둡니다.

안전 규칙: API 키·비밀번호·실제 고객 정보는 AI 채팅과 파일에 넣지 않습니다.

핵심 한 줄: 같은 요청을 몇 번 보내도 결과가 같은 것을 멱등성(같은 일을 여러 번 해도 결과가 한 번 한 것과 같은 성질)이라고 합니다. 쿠폰이 두 번 나가지 않습니다.

## 테스트 명령

Windows PowerShell:

```powershell
.venv\Scripts\python -m pytest -q
```

macOS:

```bash
.venv/bin/python -m pytest -q
```

## 1. 요청 읽기

`REQUEST.md`의 3차 요청을 읽습니다. 브라우저 http://localhost:8000 에서 리뷰를 분석한 뒤 쿠폰 버튼을 누르면 "쿠폰 API가 아직 없어요"가 보입니다. 정상입니다.

## 2. 명세 쓰기

Agent에게 인터뷰를 시켜 명세 초안을 만듭니다.

```text
나를 인터뷰해 줘. REQUEST.md의 3차 요청(쿠폰)을 읽고, 쿠폰 API 명세를 정하는 질문을 하나씩 최대 7개 해 줘 (주소 · 요청 필드 · 쿠폰 종류와 금액 · 쿠폰 코드 · 같은 요청을 두 번 보냈을 때 · 잘못된 입력). 끝나면 SPEC_COUPON.md 초안을 보여 줘. 규칙마다 예시표를 붙이고 경계 행을 넣어 줘. 내가 "승인"이라고 하면 저장해.
```

질문에 내 생각대로 답하고, 초안을 읽은 뒤 `승인`이라고 합니다.

## 3. 공식 명세와 비교

```text
SPEC_COUPON.md와 checkpoints/coupon/SPEC_COUPON_OFFICIAL.md를 비교해서 다른 점을 표로 보여 줘. 파일은 고치지 마.
```

그다음 공식 명세를 내 폴더로 복사합니다.

Windows PowerShell:

```powershell
Copy-Item checkpoints\coupon\SPEC_COUPON_OFFICIAL.md .
```

macOS:

```bash
cp checkpoints/coupon/SPEC_COUPON_OFFICIAL.md .
```

화면이 공식 약속대로 요청을 보내므로 구현은 공식 명세를 따릅니다. 내 명세는 비교용으로 남깁니다.

## 4. 테스트 먼저 (Red)

```text
SPEC_COUPON_OFFICIAL.md의 예시표를 tests/test_coupon.py의 pytest 테스트로 옮겨 줘. 표에 없는 행은 넣지 마. 테스트마다 Given / When / Then 주석을 붙여 줘. 구현은 아직 하지 마. 바뀔 내용을 보여 주고 내가 "승인"이라고 하면 저장해.
```

테스트 명령을 실행하면 `No module named 'app.coupon'` 오류가 나옵니다. 아직 `app/coupon.py`가 없어서입니다. 빨강(Red)이고 정상입니다. 다른 테스트까지 보려면 명령 끝에 `--continue-on-collection-errors`를 붙입니다.

## 5. 구현 (Green)

```text
SPEC_COUPON_OFFICIAL.md대로 POST /v1/coupons/issue를 만들어 줘. app/coupon.py를 새로 만들고 app/main.py와 app/schemas.py에는 쿠폰에 필요한 것만 더해. tests/와 SPEC 파일은 고치지 마. pytest가 모두 통과할 때까지 고쳐.
```

테스트가 모두 passed이면 브라우저에서 쿠폰 버튼을 눌러 봅니다. 바뀐 내용을 읽고 `승인`하면 커밋됩니다.

## 6. 공식 API 테스트로 확인

공식 API 테스트를 복사해서 돌립니다.

Windows PowerShell:

```powershell
Copy-Item checkpoints\coupon\tests\test_api_coupon.py tests\
```

macOS:

```bash
cp checkpoints/coupon/tests/test_api_coupon.py tests/
```

테스트 명령을 실행해 모두 passed이면 성공입니다. 완성본(`checkpoints/coupon`)은 `41 passed`입니다. 내 테스트가 있으면 개수는 조금 다를 수 있습니다. failed가 없으면 됩니다.

## 성공 기준

화면에서 같은 리뷰로 쿠폰 버튼을 두 번 눌러도 같은 쿠폰 코드가 나옵니다.
