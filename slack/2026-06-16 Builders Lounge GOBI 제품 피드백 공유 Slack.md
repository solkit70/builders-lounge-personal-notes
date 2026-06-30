---
title: "Builders Lounge GOBI 제품 피드백 공유 Slack"
created: 2026-06-18 17:30:00
source: "Slack screenshots provided by Changsoo Park"
event_date: 2026-06-16
tags:
  - builders-lounge
  - slack
  - gobi
  - product-feedback
  - bila-ai
---

## 요약

2026년 6월 16일, Changsoo Park이 전날(6/15) Sung-Jin Kim(@lifidea)과 가졌던 온라인 미팅에서 나온 GOBI 제품 피드백을 정리해 GitHub builders-lounge-personal-notes 저장소에 업로드했다. 이 Slack 대화는 그 공유 이후 이어진 세 명의 짧지만 밀도 높은 교환을 담고 있다. Sung-Jin Kim은 AI가 개인적인 이야기를 잘 걸러냈다고 확인했고, MinSuk Kang은 피드백 문서에 담긴 12개 질문에 GOBI 팀의 입장으로 일일이 답했다. 이후 Changsoo Park은 답변 내용을 해당 문서에 반영했고, MinSuk Kang과 귀국 후 만나 Bila AI Agent 작업과 운영 방식을 자세히 논의하기로 일정을 조율했다. 이 기록은 Changbal Space의 Bila AI가 참조하는 데이터로 활용될 예정이다.

## 2026-06-16 Tuesday

### Changsoo Park — 17:12

Changsoo Park은 전날 Sung-Jin Kim과 오랜만에 온라인으로 만나 안부를 나누다가 GOBI 제품 전반에 대한 피드백 성격의 대화가 이어졌고, 그 내용을 정리해 GitHub에 올렸다고 알렸다. MinSuk Kang과 Sung-Jin Kim 두 명을 태그하며 내용이 의도한 대로 전달되는지 확인을 요청했다.

> @MinSuk Kang @lifidea 어제 성진님이랑 오랜만에 온라인으로 만나서 서로 안부 인사를 나눴는데요. 이야기 하다가 GOBI product 에 대한 Feedback 성격의 대화가 있었습니다. 이 대화를 정리해서 GitHub 에 올렸습니다. 저와 성진님의 Feedback 파일이 아래에 있으니까 참조하세요.
> [builders-lounge-personal-notes/feedback at main · solkit70/builders-lounge-personal-notes](https://github.com/solkit70/builders-lounge-personal-notes)
> @Sung-Jin Kim 혹시 저와 Codex 가 정리한 파일 내용이 의도한 것과 다르게 전달되는게 있다면 알려 주세요.
> P.S. 여기에 기록되는 데이터들은 Changbal Space 내에서 Bila AI 라는 AI Agent 가 참조하는 데이터가 될 겁니다.

공개된 GitHub 링크는 Builders Lounge 멤버들이 개인 노트와 피드백을 공유하는 저장소다. 대화가 발생한 즉시 정리해서 공개 저장소에 올리는 이 방식은, 구두 대화가 검색·참조 가능한 기록으로 전환되는 Builders Lounge의 기록 workflow를 그대로 따른다.

### Sung-Jin Kim — 17:33

> AI는 참 잘 정리하네요. 척하면 착이라고 해야할까요. 하나를 말하면 10개를 정리하는데요. 여기에 개인적인 이야기들은 빼도록 프롬프팅을 하신건가요? 그런건 찾아봐도 잘 안보이네요.

Sung-Jin Kim은 AI가 대화 내용을 잘 구조화했다고 반응했다. 특히 "하나를 말하면 10개"라는 표현은 AI가 키워드 하나에서 관련 맥락과 후속 질문을 자동으로 확장해 정리하는 방식에 대한 인상을 담고 있다. 개인적인 이야기가 정리 문서에 보이지 않는다는 점도 확인했다.

### Changsoo Park — 17:36

> 예 그런건 빼도록 프롬프팅 한 겁니다.

피드백 대화를 정리할 때 "개인적인 이야기는 제외"라는 명시적인 조건을 프롬프트에 포함했음을 확인한 것이다. 공개 저장소에 올라가는 기록이므로, 업무·제품 관련 내용과 개인적 언급을 분리하는 작업을 프롬프팅 단계에서 처리한 것이다.

### MinSuk Kang — 17:39

MinSuk Kang은 피드백 방향이 GOBI 팀이 생각하는 방향과 많이 일치한다며 감사를 전하고, 피드백 문서에 담긴 질문들에 대해 현재 GOBI의 입장을 항목별로 답했다.

> 좋은 논의와 발전 방향에 대해해 말씀 나눠주셔서 감사드려요! 저희가 생각하는 방향과 많이 일치하는것 같습니다ㅎㅎ. 질문 주신것 답변 드립니다

#### Q&A — GOBI 제품 피드백

| 질문 | MinSuk Kang 답변 |
|------|-----------------|
| 현재 GOBI Space Agent의 system prompt와 운영 규칙은 누가 만들고 관리하는가? | 현재 Admin이 설정할 수 있고, 기본 가드레일·instructions는 저희가 관리합니다 |
| Space admin이 자신의 Agent prompt를 확인하거나 수정할 수 있는 기능을 고려하고 있는가? | 그 기능은 이미 있습니다 |
| GOBI가 반드시 통제해야 하는 공통 Guardrail과 Space가 자율적으로 관리해도 되는 영역은 어디까지인가? | 이부분은 기존 프롬프트를 놓고 논의해보면 좋겠습니다 |
| Prompt 변경을 versioning하고 test할 수 있는 가장 작은 MVP는 무엇인가? | 현재 구현되어있는 Settings → Agent에서 프롬프트 입력하시면 됩니다 |
| Space별 Agent Skills와 MCP 연결을 장기적으로 지원할 계획이 있는가? | 물론입니다! |
| 한 Space에서 잘 작동한 Harness를 다른 Space가 template으로 가져올 수 있게 할 수 있는가? | 이 기능도 좋긴 하겠지만 검증 된 후에 풀수있을것 같습니다 |
| Builders Lounge의 Bila AI를 이 구조의 첫 번째 실험 사례로 사용해 볼 수 있는가? | 저는 이미 그렇게 하는 것으로 알고 있었습니다 😊 |
| GOBI는 데이터 수집·관리·활용 중 어디에 가장 큰 전략적 우선순위를 두고 있는가? | 수집과 활용에 우선순위를 두고 있습니다 |
| Knowledge Management는 GOBI의 핵심 역량인가, 아니면 수집과 활용을 연결하는 supporting layer인가? | 핵심 역량은 아닙니다만 에이전트는 핵심에 있습니다 |
| 기업 고객에게 제공할 수 있는 첫 번째 Knowledge Management use case는 무엇인가? | 컨퍼런스/출장 등 현장 학습의 데이터를 가지고 리포트 작성 |
| Builders Lounge 기록 workflow를 GOBI의 작은 demo case로 만들 수 있는가? | 그럴수 있다면 좋은 실험이 될 것 같습니다 |
| B2C ambient AI와 B2B Knowledge Management는 서로 어떻게 연결될 수 있는가? | 저희는 ambient AI를 전체적인 end to end의 경험을 통칭하는 단어로 생각합니다. 웨어러블을 통한 수집의 혁신과 에이전트를 이용한 활용의 혁신으로 생각하시면 좋을것 같습니다. 그 사이의 knowledge management는 회사마다 사람마다 프로세스와 생각의 방식이 다른것 처럼 각각 다를것 같습니다. |

## 2026-06-19 Friday — 답변 반영과 후속 논의 요청

### Changsoo Park — 06:15

Changsoo Park은 MinSuk Kang의 답변을 해당 문서에 업데이트했다고 알렸다. 또한 한국에서 돌아오면 Bila AI Agent 작업과 관련해 자세히 의논하고 싶다고 요청했다. 이 메시지는 Slack Q&A가 단순 댓글로 끝나지 않고, GitHub 문서 업데이트와 실제 후속 미팅으로 이어지는 흐름을 보여준다.

> @MinSuk Kang 예 답변하신 내용은 해당 문서에 업데이트 해 놓았습니다.
> [builders-lounge-personal-notes/feedback at main · solkit70/builders-lounge-personal-notes](https://github.com/solkit70/builders-lounge-personal-notes)
>
> 한국에서 돌아 오시면 Bila AI Agent 작업과 관련해서 자세하게 의논 하고 싶은데요.
> 다음주에 한번 만나면 좋겠습니다.

### MinSuk Kang — 11:08

MinSuk Kang은 돌아왔다고 답하며 다음 주에 만나자고 했다. 이 답변으로 GOBI 제품 피드백, Bila AI 운영 prompt, Space Agent 실험을 별도 대화로 이어갈 실무 미팅이 열리게 되었다.

> 넵 돌아왔는데요 다음주에 뵙죠!

## 2026-06-21 Sunday — Bila AI Agent 논의 미팅 조율

### Changsoo Park — 10:08

Changsoo Park은 화요일 오전 11시 만남을 제안했다. 장소는 지난번처럼 Bellevue City Hall 1층을 제안했고, 이번에는 본인이 컴퓨터를 가져가서 Bila AI Agent를 어떻게 작업하고 셋업하는지 직접 배우겠다고 했다.

> @MinSuk Kang 화요일 오전에 어떠세요? 11시쯤에 만나면 좋을 것 같습니다. 장소는 지난 번 처럼 진영님 사무실 1층이 좋겠구요. 이번에는 제가 Bila AI Agent 를 어떻게 작업하면 좋은지 좀 배우고 싶습니다. 제 컴퓨터 가져 가서 직접 해 보면서 배우겠습니다.

### MinSuk Kang — 10:09

MinSuk Kang은 11시는 조금 이르지만 화요일 12시 이후는 괜찮다고 답했다.

> 넵 11시는 좀 일러서요 화요일 12시 이후에 괜찮습니다

### Changsoo Park — 10:10

Changsoo Park은 12시 30분을 제안했다.

> 예 그럼 12시 30분 괜찮나요?

### MinSuk Kang — 10:10

MinSuk Kang은 좋다고 답했다.

> 넵 그때 뵈어요!

## 2026-06-23 Tuesday — Bellevue City Hall 미팅 장소 확인

### Changsoo Park — 11:07

Changsoo Park은 MinSuk Kang이 시청에 주차할 예정인지 확인하고, 그렇다면 아예 Bellevue City Hall에서 만나는 것이 좋겠다고 제안했다. City Hall은 인터넷이 잘 되고 두 사람이 앉아 이야기할 공간도 충분하다는 이유였다.

> 시청에 주차하실거죠? 그럼 아예 시청에서 보는게 좋을것 같습니다. 인터넷도 잘 되고 둘 정도 앉기 공간도 많구요.

### MinSuk Kang — 11:07

MinSuk Kang은 좋다고 답했다.

> 넵 그럼 시청에서 뵈요

### MinSuk Kang — 12:33

MinSuk Kang은 시청 안에 도착해 있다고 알렸다.

> 시청 안에 있습니다~

## 의미

이 대화는 Builders Lounge의 기록 workflow가 실제로 어떻게 작동하는지 보여주는 사례다. 구두 대화가 AI로 정리되고, 개인 정보가 걸러지고, GitHub 저장소에 올라가고, 슬랙에서 공유되는 전 과정이 하루 안에 이뤄졌다.

MinSuk Kang의 Q&A는 몇 가지 중요한 방향을 확인해 준다. GOBI가 Knowledge Management를 핵심 역량이 아닌 supporting layer로 보는 대신 에이전트를 핵심에 두고 있다는 점, Builders Lounge Bila AI가 공식적으로 GOBI 팀이 인지하는 첫 번째 Space-specific agent 실험 사례라는 점, Space별 Harness template 공유 기능이 검증 후 제공될 계획이라는 점이 눈에 띈다.

또한 "컨퍼런스/출장 등 현장 학습의 데이터를 가지고 리포트 작성"이라는 첫 번째 KM use case 답변은, Catch Up AI가 시애틀·벨뷰 지역 AI 세미나를 녹화·정리해온 방식과 정확히 맞닿아 있다.

6월 19일부터 23일까지 이어진 후속 댓글은 이 기록 workflow가 실제 제품 실험으로 이어지는 방식을 보여준다. Slack에서 받은 답변은 GitHub 문서에 반영되고, 그 다음에는 MinSuk Kang과 직접 만나 Bila AI Agent를 설정하고 배우는 미팅으로 이어졌다. 특히 Bellevue City Hall에서 노트북을 들고 직접 해보며 배우겠다는 계획은 Builders Lounge의 방향이 단순 토론이 아니라 hands-on 실험과 커뮤니티 AI 운영으로 이동하고 있음을 보여준다.

## 연결되는 항목

| 항목 | 내용 |
|------|------|
| Builders Lounge personal notes GitHub | https://github.com/solkit70/builders-lounge-personal-notes |
| Bila AI (Changbal Space Agent) | Builders Lounge 기록을 참조하는 커뮤니티 AI |
| GOBI 제품 방향 | 수집·활용 우선 / 에이전트 핵심 / KM은 supporting layer |
| Bellevue City Hall 미팅 | MinSuk Kang과 Bila AI Agent 작업·셋업을 직접 배우기 위한 후속 미팅 장소 |
| [GOBI Space Open Harness 제안 — Changsoo](../feedback/2026-06-18%20GOBI%20Space%20Open%20Harness%20제안%20-%20Changsoo.md) | 이 Slack Q&A의 원본 제안 문서 (질문 1–7) |
| [GOBI B2B/SI 방향 피드백 — 김성진님](../feedback/2026-06-18%20GOBI%20B2B%20SI%20방향%20피드백%20-%20김성진님.md) | 이 Slack Q&A의 원본 피드백 문서 (나머지 질문) |

## 후속 액션

| 항목 | 액션 |
|------|------|
| GOBI Guardrail 경계 논의 | 기존 프롬프트를 기반으로 Changsoo ↔ MinSuk 간 별도 논의 진행 |
| Builders Lounge KM demo case | GitHub 기록 workflow를 GOBI demo로 구체화하는 방향 검토 |
| Space Harness template 기능 | 검증 완료 후 활용 가능 여부 확인 |
| Bila AI 운영 prompt | Space agent 역할과 guardrail 범위를 MinSuk Kang과 구체화 |
| Bila AI hands-on 미팅 | MinSuk Kang과 직접 만나 Agent 설정, prompt 관리, 운영 방식 학습 |
