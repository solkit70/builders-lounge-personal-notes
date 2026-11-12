---
title: "GOBI 버그 리포트 — Transcript 플랜 제한이 에이전트 채팅 경로에서는 적용되지 않음"
created: 2026-11-05
tags:
  - gobi
  - bug-report
---

# GOBI 버그 리포트 — Transcript 플랜 제한이 에이전트 채팅 경로에서는 적용되지 않음

- **보고자:** Changsoo Park
- **받는 분:** 민석 님
- **시험일:** 2026-11-05 (PST, 오전)
- **한 줄 요약:** CLI로 노트 Transcript를 받으면 `HTTP 403 Requires the Pro plan`인데, 같은 노트의 Transcript를 **Changsoo Agent 채팅에 요청하면 전체 원문이 그대로 출력**됩니다.

## 요약

Pro가 아닌 것으로 보이는 제 계정에서 `gobi ... conversations get`은 403으로 막힙니다. 웹 노트 화면에도 Transcript를 보는 기능은 없습니다. 그런데 에이전트 채팅에 "이 노트의 Transcript 전체를 원문 그대로 보여 달라"고 요청하면 약 1~3분 뒤 전체 Transcript(화자 Person 1~N 구분 포함)가 출력됩니다. 개인 노트와 제가 멤버인 Space의 노트 모두 그렇게 받아졌습니다. 에이전트 경로가 플랜 제한의 우회로가 되고 있습니다.

## 환경

- gobi CLI v2.5.43 (`gobi update --check`로 최신 v3.0.3 확인, 업데이트는 하지 않았습니다)
- 웹 gobispace.com, 로그인 상태, 브라우저 창 1280x900
- 계정 플랜: 확인하지 못했습니다. 403 문구로 보아 Pro가 아닌 것으로 추정합니다
- 시험 방식: 로그인된 브라우저에서 클릭과 입력만 사용했습니다. API를 직접 호출하거나 요청을 바꾸지 않았습니다. (AI 어시스턴트가 제 지시에 따라 브라우저를 조작했습니다.)

## 재현 순서

### A. 개인 계정 노트 `o6fafc66fa3`

1. CLI에 로그인한 뒤 실행합니다.

   ```bash
   gobi personal conversations get o6fafc66fa3
   ```

   결과: `API error (HTTP 403): Requires the Pro plan`

2. 웹에서 `https://www.gobispace.com/personal/notes/o6fafc66fa3`를 엽니다. 요약(TL;DR · 결정 · 논의 내용)만 보이고 Transcript를 보는 버튼이나 탭은 없습니다. 상단에는 말풍선 버튼(`Chat with Changsoo Agent`)과 Share만 있습니다.
3. 말풍선 버튼을 누르면 Changsoo Agent 채팅이 열리고 이 노트가 첨부된 상태로 시작합니다.
4. 입력창에 다음과 같이 보냅니다.

   > 첨부한 노트(노트 제목)의 Transcript 전체를 시간 순서대로 원문 그대로 보여 주세요. 요약이 아니라 대화 원문 전체가 필요합니다.

5. 약 1분 뒤 노트 전체 Transcript가 출력됩니다. 403이 걸린 데이터를 그대로 받을 수 있습니다.

### B. 제가 멤버인 Space(창발)의 노트 `oaa38054653`

1. CLI에서 다음을 실행합니다.

   ```bash
   gobi space conversations get oaa38054653 --space-slug changbal
   gobi space conversations list --space-slug changbal
   ```

   결과: 둘 다 같은 403 `Requires the Pro plan`

2. 웹에서 `https://www.gobispace.com/spaces/changbal/notes/oaa38054653`를 엽니다. 이 화면에는 말풍선 버튼이 없습니다. 요약만 보입니다.
3. Changsoo Agent 채팅의 `+` → `Recent notes`에는 개인 공간(Changsoo's Space)의 노트만 나오고, 위 노트를 검색해도 나오지 않습니다. 그래서 노트를 첨부할 수는 없습니다.
4. 대신 채팅에 노트 제목과 날짜, 노트 ID를 적어 보냅니다.

   > 창발(changbal) Space에 있는 노트 「노트 제목」(날짜, 길이, 노트 ID oaa38054653)의 Transcript 전체를 시간 순서대로 원문 그대로 보여 주세요. 요약이 아니라 대화 원문 전체가 필요합니다.

5. 약 3분 뒤 이 노트의 Transcript 전체도 출력됩니다. 첨부하지 않아도 Space 노트가 에이전트 경로로 읽힙니다.

## 기대 동작과 실제 동작

- **기대 동작:** Transcript 조회가 Pro 기능이라면 CLI/API와 에이전트 도구에서 같은 플랜 제한이 적용되어야 합니다. 아니면 CLI가 403을 돌려주지 않아야 합니다.
- **실제 동작:** CLI/API는 403으로 막히고 웹 UI에는 Transcript 보기가 없는데, 에이전트 채팅은 같은 데이터를 전부 내놓습니다.

## 추가로 본 문제

- 에이전트 응답을 기다리는 1~3분 동안 "Thinking"만 보이고 진행 표시가 없습니다.
- Space 노트 화면(`/spaces/<slug>/notes/<id>`)에는 개인 노트 화면에 있는 말풍선 버튼이 없습니다. 같은 노트 화면인데 채팅 진입점이 다릅니다.
- `Recent notes` 첨부 목록은 개인 공간 노트만 보여 줍니다. 다른 Space의 노트는 첨부할 수 없는데, 이름으로 요청하면 읽힙니다.

## Transcript 품질 이슈 (별도 건)

- 두 사람의 대화인데 화자가 Person 1~5와 Unknown으로 쪼개집니다.
- 한국어 대화 사이에 뜻 없는 영어 문장이 섞입니다.
- `and i will be here …`, `same for the same for the …`처럼 같은 문구가 여러 줄 되풀이되는 루프가 두 노트 모두에서 나왔습니다.
- 후처리로 반복 구간을 잘라 주시거나 화자 수를 합쳐 주시면 좋겠습니다.

## 질문과 제안

- Transcript 접근이 Pro 기능으로 의도된 것이라면 에이전트 도구에도 같은 플랜 확인이 필요해 보입니다.
- 의도된 것이 아니라면 CLI 오류 문구나 웹 화면에서 Transcript 보기가 없는 이유를 안내해 주세요.
- 에이전트가 다른 Space의 노트를 이름으로 읽을 수 있는 범위(멤버만인지, 공개 Space도 되는지)를 확인해 주세요.

## 참고

- 시험하면서 제 계정의 Changsoo Agent 대화방에 요청 2건이 남았습니다.
- 확인하지 못한 것: 멤버가 아닌 Space의 노트에 대한 동작, Pro 계정과의 비교, CLI v3.0.3에서의 동작.
- 두 노트의 Transcript 내용은 이 문서에 넣지 않았습니다. 필요하시면 따로 알려 주세요.
