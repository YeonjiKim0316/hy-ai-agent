# 리뷰 온도계

> © 2026 김연지. All rights reserved. 수강생 개인 학습용 · 무단 강의·복제·배포·수정 금지 · [LICENSE.md](LICENSE.md)

가상 쇼핑몰 하루마켓의 리뷰 한 건과 별점을 넣으면 긍정인지 부정인지 알려 주는 서버를 만듭니다.
리뷰가 얼마나 좋은지 0~100℃ '리뷰 온도'로 보여 주고, 별점과 내용이 반대인 리뷰도 찾아 줍니다.
AI 에이전트(스스로 파일을 읽고 고치는 AI)와 함께, 명세(만들 것을 적은 글)에서 시작해 테스트와 코드를 만듭니다.

붙여 넣을 문장은 실습 카드에 있습니다: https://claude.ai/artifact/NHdo2gwBRpBs129C44VoNo

## 처음 켜기

Python 3.11 ~ 3.13이 필요합니다. `python --version`(macOS `python3 --version`)으로 확인합니다.

### 1. 저장소 받기(git clone)

`git clone`은 인터넷에 있는 저장소를 내 PC로 복사해 오는 명령입니다.

터미널을 엽니다. (Windows: 시작 메뉴에서 PowerShell, macOS: 터미널 앱) 아래 세 줄을 한 줄씩 칩니다. 마지막 줄은 받은 폴더를 VS Code로 엽니다.

Windows PowerShell:

```powershell
cd $HOME\Documents
git clone https://github.com/YeonjiKim0316/hy-ai-agent.git
code hy-ai-agent
```

macOS:

```bash
cd ~/Documents
git clone https://github.com/YeonjiKim0316/hy-ai-agent.git
code hy-ai-agent
```

`cd $HOME\Documents`에서 경로가 없다고 나오면 문서 폴더가 OneDrive로 옮겨진 PC입니다. `cd $HOME\OneDrive\Documents`(또는 `cd $HOME\OneDrive\문서`)로 바꿉니다.

VS Code가 열리면 "신뢰합니까?" 창에서 Yes를 누릅니다. `code` 명령이 없다고 나오면 VS Code → File → Open Folder → 문서 폴더의 `hy-ai-agent`를 엽니다.

clone이 안 되면 수업에서 받은 예비 zip 파일을 풉니다. (Windows: 오른쪽 클릭 → 모두 압축 풀기) 그다음 VS Code에서 File → Open Folder → `hy-ai-agent`를 엽니다.

### 2. 가상환경 만들고 패키지 설치 (세 줄)

Terminal → New Terminal을 엽니다. 아래 세 줄을 한 줄씩 칩니다. 가상환경을 켜는(activate) 명령은 치지 않아도 됩니다.

① 가상환경(이 프로젝트만의 파이썬 상자)을 만듭니다 ② 필요한 패키지를 넣습니다(처음에는 몇 분 걸립니다. 멈춘 듯 보여도 기다립니다) ③ 서버를 켭니다

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m uvicorn app.main:app --reload
```

macOS:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m uvicorn app.main:app --reload
```

막히면 `.\start.bat`(macOS `bash start.sh`)으로 한 번에 할 수 있습니다.

### 3. 서버 켜기

세 번째 줄이 서버를 켭니다. 터미널에 `Uvicorn running on http://127.0.0.1:8000`이 보이면 서버가 켜진 것입니다. 이 터미널은 그대로 둡니다.

처음 분석하면 AI 모델을 내려받느라 "AI 부품이 아직 준비 중"이 먼저 나올 수 있습니다. 잠시 뒤 다시 누릅니다.

브라우저에서 아래 주소를 엽니다.

- http://localhost:8000 : 리뷰 분석 화면
- http://localhost:8000/dashboard.html : 대시보드 화면
- http://localhost:8000/docs : API 설명서

서버를 끌 때는 터미널에서 `Ctrl+C`를 누릅니다.

## 테스트

- VS Code 왼쪽의 테스트 창(비커 아이콘)에서 ▷를 누릅니다.
- 또는 터미널에서 아래 명령을 칩니다. (서버가 켜진 터미널과는 다른 터미널입니다)

Windows PowerShell:

```powershell
.venv\Scripts\python -m pytest -q
```

macOS:

```bash
.venv/bin/python -m pytest -q
```

빨강(Red)은 테스트가 실패한 것이고, 초록(Green)은 통과한 것입니다.

## 오늘 순서

| 세션 | 하는 일 | 끝에 보이는 것 |
|---|---|---|
| 1. AI와 처음 일해 보기 | 저장소 받기, 서버 켜기, Copilot에게 부탁하기, AGENTS.md 쓰기, 첫 커밋 | 서버가 켜지고, 커밋이 2개 보입니다 |
| 2. 명세 = 예시표 | 예시표 빈칸 채우기, 테스트 먼저, 구현 | 리뷰 분석에서 온도가 나옵니다 |
| 3. AI에 도구 붙이기 | MCP로 DB에 질문하기, 스킬 써 보기 | 리뷰 수를 AI가 DB에서 세어 알려 줍니다 |
| 4. 나만의 카드 + agy | 대시보드 카드 만들기, agy 설치와 시연, 규칙·스킬 남기기 | 대시보드에 총 리뷰 수와 내 카드가 보입니다 |

## 실습 카드

붙여 넣을 문장은 실습 카드에 있습니다. 카드 번호는 세션 번호와 순서입니다. 예를 들어 2-3은 세션 2의 세 번째 카드입니다.

## 안전 규칙

- API 키·비밀번호·실제 고객 정보는 AI 채팅과 파일에 넣지 않습니다.
- 결제 수단은 어디에도 등록하지 않습니다.
- MCP 신뢰 창에서는 내가 넣은 것만 허락합니다. 처음 보는 것은 허락하지 않습니다.
- DB는 읽기만 합니다. 쓰기 도구는 거절합니다.

## git

git 명령은 AI가 대신 치고, 나는 바뀐 내용을 읽고 '승인'합니다. commit은 내 PC에만 남습니다.

마음에 들지 않는 변경은 이렇게 되돌립니다. Copilot Agent에게 부탁합니다. `<파일>을 마지막 커밋 상태로 되돌려 줘.`(고친 파일 되돌리기) · `방금 한 커밋을 되돌려 줘.`(커밋 되돌리기)

## 막혔을 때

[docs/troubleshooting.md](docs/troubleshooting.md)에서 증상을 찾습니다. 낱말이 어려우면 [docs/glossary.md](docs/glossary.md)를 봅니다. 그래도 안 되면 손을 듭니다.

## 집에서 하는 과제

수업이 끝난 뒤 집에서 합니다.

1. 쿠폰 발급: [docs/home-1-coupon.md](docs/home-1-coupon.md)
2. 리뷰 클린봇: [docs/home-2-cleanbot.md](docs/home-2-cleanbot.md)

socratic-tutor로 오늘 배운 것을 제대로 복습해 보세요(질문 수 제한 없이).

## 폴더 안내

- `hy-ai-agent`: 내가 일하는 저장소입니다.
- `checkpoints/cp1-setup`, `checkpoints/cp2-tdd`, `checkpoints/final`, `checkpoints/coupon`: 저장소 안에 있는 단계별 완성본입니다. 비교·참고용입니다. 읽기만 합니다.
- `docs/my-prompts.md`: 내 부탁 기록표입니다.
- `warmup/orders.py`: 연습용 파일입니다. 함수 세 개에 일부러 버그를 하나씩 넣어 두었습니다. 설명의 예시와 다르게 동작하는 곳을 AI와 함께 찾아봅니다.

문서 목록: [REQUEST.md](REQUEST.md)(개발요청서), [SPEC.md](SPEC.md)(리뷰 온도 명세), [DASHBOARD.md](DASHBOARD.md)(대시보드 명세), [AGENTS.md](AGENTS.md)(AI 작업 규칙)
