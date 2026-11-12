# 막혔을 때

> © 2026 김연지. All rights reserved. 수강생 개인 학습용 · 무단 강의·복제·배포·수정 금지 · [LICENSE.md](../LICENSE.md)

| 증상 | 이렇게 합니다 |
|---|---|
| `cd $HOME\Documents`에서 경로가 없다고 나옵니다 | 문서 폴더가 OneDrive로 옮겨진 PC입니다. `cd $HOME\OneDrive\Documents`(또는 `cd $HOME\OneDrive\문서`)로 바꿉니다. |
| `python`이 없다고 나오거나 Microsoft Store가 열립니다 | 터미널에서 `py --version`을 쳐 봅니다. 버전이 나오면 `python` 대신 `py`로 `py -m venv .venv`를 칩니다. 안 나오면 손을 듭니다. (macOS는 `python3 --version`) |
| 패키지 설치에서 빨간 줄이 나오며 실패합니다 | 빨간 줄을 복사해 Copilot에게 붙여 넣고 물어봅니다. |
| 서버를 켰는데 8000번 포트를 이미 쓰고 있다고 나옵니다 | 서버가 켜진 터미널이 하나 더 있는지 찾아 `Ctrl+C`로 끕니다. 그다음 다시 켭니다. |
| 화면에 "아직 구현되지 않았어요"가 나옵니다 | 세션 2 전에는 정상입니다. 카드 2-4를 마치면 사라집니다. |
| 화면에 503 또는 "AI 부품이 아직 준비 중"이 나옵니다 | 처음 분석하면 AI 모델을 내려받느라 "AI 부품이 아직 준비 중"이 먼저 나올 수 있습니다. 잠시 뒤 다시 누릅니다. |
| 화면에 "쿠폰 API가 아직 없어요"가 나옵니다 | 정상입니다. 집에서 하는 과제에서 만듭니다. |
| 테스트 창에 테스트가 안 보입니다 | 명령 팔레트(`Ctrl+Shift+P`, macOS는 `Cmd+Shift+P`)에서 `Python: Select Interpreter`를 고르고 `.venv`를 선택합니다. 그다음 테스트 창을 새로고침합니다. |
| `npx`가 안 됩니다 | Windows: `cmd /c npx -y -p mcp-sqlite@1.0.9 node -v`를 쳐 봅니다. Node.js를 설치했다면 VS Code를 닫았다가 다시 엽니다. |
| MCP를 Start했는데 도구가 안 보입니다 | Copilot 채팅의 모드가 Agent인지 확인합니다. Ask 모드에서는 도구를 쓰지 않습니다. |
| AI가 고치면 안 되는 파일을 바꿨습니다 | `<파일>을 마지막 커밋 상태로 되돌려 줘.`라고 부탁합니다. |
| 4-4에서 새 테스트가 빨강이 아니라 초록입니다 | 새 테스트가 빨강이 아니라 초록이면 AI가 쿼리까지 미리 만든 것입니다. `app/dashboard.py를 마지막 커밋 상태로 되돌려 줘.`라고 한 뒤 다시 확인합니다. |
| 커밋할 것이 없다고 나옵니다 | 이미 커밋했다는 뜻입니다. 정상입니다. |
| `agy` 명령이 없다고 나옵니다 | 터미널을 닫고 새 터미널을 엽니다. |
| `Activate.ps1`이나 "실행 정책" 오류가 나옵니다 | 가상환경을 켜는(activate) 명령은 치지 않아도 됩니다. README의 세 줄을 그대로 칩니다. |
| 커밋할 때 "Please tell me who you are"가 나옵니다 | 터미널에 `git config --global user.name "내 이름"`과 `git config --global user.email "내 메일"`을 칩니다. 메일은 GitHub에 쓰는 것입니다. |
| `code` 명령이 없다고 나옵니다 | VS Code → File → Open Folder → 문서 폴더의 `hy-ai-agent`를 엽니다. |
| git clone이 안 됩니다 | 주소를 다시 확인합니다. `git --version`이 나오는지도 봅니다. 그래도 안 되면 수업에서 받은 예비 zip 파일을 풀고 그 폴더를 엽니다. |
| Context7이 안 켜집니다 | `npx`가 되는지 확인합니다. 잠시 뒤 `.vscode/mcp.json`에서 context7을 다시 Start합니다. |
| 스킬과 대화가 너무 길어집니다 | 채팅에 `멈춰 줘`라고 씁니다. 처음부터 `질문은 3개만 하고 멈춰.`를 붙여도 됩니다. |

그래도 안 되면 손을 듭니다. 무엇을 했는지 말하면 더 빨리 도울 수 있습니다.
