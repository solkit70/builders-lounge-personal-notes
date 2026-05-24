# Builders Lounge 개인 기록 저장소

이 폴더는 Changsoo가 개인적으로 정리하고 있는 Builders Lounge 기록 저장소입니다. Builders Lounge 멤버들이 모임의 시작 배경, 진행 과정, 현재 논의 중인 방향, 앞으로 도울 수 있는 지점을 빠르게 파악할 수 있도록 Slack 대화, 모임 공지, 영상 transcript, 운영 아이디어를 모아 두었습니다.

지금은 개인 기록이지만, 멤버들이 참고하거나 이 폴더를 GitHub repository로 clone해서 AI와 함께 모임의 맥락을 탐색하는 용도로 사용할 수 있습니다. 필요하다면 멤버들이 추가 기록을 정리해 올릴 수도 있습니다. 나중에는 공식 Builders Lounge GitHub repository를 따로 만들거나, Gobi Space 안에 이 기능이 구현되면 그쪽으로 옮겨갈 수 있습니다.

## 작성 정보

이 문서들과 저장소 구조는 Changsoo가 정리한 Slack 대화, 모임 기록, 아이디어를 바탕으로 VS Code와 Codex를 사용해 작성했습니다. 현재 기준으로 공식 Builders Lounge repository가 아니라 Changsoo의 개인 기록 저장소이며, 멤버들이 참고하거나 추가 기록을 제안할 수 있도록 공개 가능한 형태로 정리하고 있습니다.

## Builders Lounge란?

Builders Lounge는 AI를 활용해 Product, app, agent, workflow를 만드는 사람들이 서로의 작업을 소개하고, 직접 사용해 보고, 피드백을 주고받으며 함께 성장하는 builder community입니다.

핵심은 단순 발표가 아니라 서로의 첫 번째 사용자가 되는 것입니다. 누군가 만든 제품을 다른 멤버가 실제로 써보고, 첫 화면이 이해되는지, 실제로 쓸 이유가 있는지, 어떤 부분이 막히는지, 다음에 무엇을 개선하면 좋을지 알려주는 것이 모임의 중심입니다.

## 5가지 방향성

1. **Practical Build**: 이론 공부를 넘어 각자가 개발 중인 AI 애플리케이션과 실험 결과물을 직접 공유합니다.
2. **Builder for Builders**: 우리는 서로의 첫 번째 고객이 되어 실질적인 사용 경험과 피드백을 제공합니다.
3. **Workflow Sharing**: 도구 개발뿐 아니라 AI와 협업하며 얻은 효율적인 workflow와 시행착오를 공유합니다.
4. **Collective Intelligence**: Slack, Gobi Space, meeting, demo, pitch 기록을 축적해 나중에 AI가 활용할 수 있는 지식 자산으로 만듭니다.
5. **Open Ecosystem**: Bellevue 지역과 그 밖의 다양한 builder, startup, creator에게 열린 커뮤니티를 지향합니다.

## 현재 상태

현재 Builders Lounge는 첫 오프라인 모임을 마쳤고, 두 번째 모임을 준비하는 단계입니다. 첫 모임에서는 GOBI Space / Desktop hands-on을 진행했고, 모임 이름을 Builders Lounge로 확정했습니다. 이후에는 별도 Gobi Space를 새로 만들기보다 기존 Changbal Space를 함께 활용하고, 내부 별칭으로 `창발 빌라`를 사용하자는 방향이 논의되었습니다.

다음 단계는 각자의 Product를 소개하고, 서로 사용해 보고, 구조화된 feedback을 남기는 운영 방식을 만드는 것입니다. 이를 위해 Gobi Space Custom Homepage, post/comment 기반 feedback, 향후 tag/dashboard 기능, GitHub 기반 기록 저장소 같은 여러 가능성을 검토하고 있습니다.

## 멤버가 도울 수 있는 일

- 자신의 Product, app, agent, workflow를 아래 형식으로 소개해 주세요.
- 다른 멤버의 Product를 실제로 써보고 첫 번째 사용자 관점에서 feedback을 남겨 주세요.
- Slack, Gobi Space, 온라인/오프라인 meeting, pitch, demo 내용을 기록으로 남기는 데 참여해 주세요.
- Gobi Space Custom Homepage에 필요한 기능 아이디어를 제안해 주세요.
- Review template, feedback board, product showcase, demo day 운영 방식에 의견을 주세요.
- GitHub repo나 Gobi Space 기반 공동 기록 관리 방식에 대한 제안을 주세요.

## Product 소개 형식

```text
나의 Product: [Product 이름]
Product 위치: [GitHub / URL]
Demo 방법: Online / Offline
Product 설명: 어떤 문제를 해결하는가, 어떻게 만들었는가
Demo 계획: 무엇을 보여주고 싶은가 (예상 시간)
지금 가장 받고 싶은 Feedback: [예: 첫 화면, onboarding, 가격, AI 기능, VC perspective 등]
```

## 기록으로 남기고 싶은 것

| 기록 대상 | 예시 | 활용 가능성 |
| --- | --- | --- |
| Slack 대화 | 모임 공지, 댓글, product 소개, feedback 요청 | 모임 history, decision log |
| Gobi Space 글 | Changbal Space post, 댓글, AI 요약 | 공동 지식 축적, member knowledge base |
| Product Demo | 발표 자료, 영상, Q&A | Product showcase, feedback archive |
| 오프라인/온라인 회의 | transcript, 요약, action item | 다음 모임 준비, AI 기반 회고 |
| Custom Homepage 아이디어 | 기능 목록, UI 제안, 구현 제약 | Gobi Space homepage / future app design |

## 폴더 구조

GitHub 첫 화면에서는 이 README를 먼저 보고, 세부 기록은 아래 폴더에서 확인하면 됩니다. 루트에는 README만 두고, 기록의 성격에 따라 하위 폴더로 나누었습니다.

```text
builders-lounge-personal-notes/
├─ README.md
├─ slack/      Slack 대화와 논의 흐름
├─ notices/    멤버 공지와 진행 상황 공유
├─ videos/     모임 영상 정리와 transcript
├─ ideas/      운영 아이디어와 다음 모임 준비
└─ assets/     이미지 자료
```

| 폴더 | 내용 |
| --- | --- |
| `README.md` | 저장소의 목적, 현재 상태, 참여 방법, 주요 문서 링크를 정리한 첫 화면 문서 |
| `slack/` | Builders Lounge가 논의되고 준비되고 운영되는 과정에서 나온 Slack 대화 기록 |
| `notices/` | 멤버들에게 공유한 진행 상황 공지와 운영 안내 |
| `videos/` | 모임 녹화 영상 정리와 transcript |
| `ideas/` | 2회 모임 준비, Custom Homepage, 기록 저장소 같은 운영 아이디어 |
| `assets/` | README나 문서에서 사용할 수 있는 이미지 자료 |

## 주요 문서

| 문서 | 내용 |
| --- | --- |
| [2026-03-25 Builders Lounge 초기 논의 Slack.md](slack/2026-03-25%20Builders%20Lounge%20%EC%B4%88%EA%B8%B0%20%EB%85%BC%EC%9D%98%20Slack.md) | Brain Training Board Games 소개와 coding agent 활용 논의에서 오프모임 아이디어가 시작된 기록 |
| [2026-04-09 Builders Lounge 모임 준비 Slack.md](slack/2026-04-09%20Builders%20Lounge%20%EB%AA%A8%EC%9E%84%20%EC%A4%80%EB%B9%84%20Slack.md) | 4월 오프모임 준비, Gobi Desktop, VibeLearn AI, Harness Engineering 논의 |
| [2026-04-11 Builders Lounge 준비 모임과 첫 오프라인 모임 Slack.md](slack/2026-04-11%20Builders%20Lounge%20%EC%A4%80%EB%B9%84%20%EB%AA%A8%EC%9E%84%EA%B3%BC%20%EC%B2%AB%20%EC%98%A4%ED%94%84%EB%9D%BC%EC%9D%B8%20%EB%AA%A8%EC%9E%84%20Slack.md) | 온라인 준비 미팅, 4/23 Dote Coffee Bar 모임, 장소 섭외, 이름 공모, 공동 지식 축적 논의 |
| [2026-05-07 Builders Lounge 첫 정식 모임 Slack.md](slack/2026-05-07%20Builders%20Lounge%20%EC%B2%AB%20%EC%A0%95%EC%8B%9D%20%EB%AA%A8%EC%9E%84%20Slack.md) | Bellevue City Hall 첫 정식 모임 안내, 5가지 방향성, Gobi 링크 공유 |
| [2026-05-09 Builders Lounge 1회 후속 Slack.md](slack/2026-05-09%20Builders%20Lounge%201%ED%9A%8C%20%ED%9B%84%EC%86%8D%20Slack.md) | 1회 모임 결과, Builders Lounge 이름 확정, Gobi Space 개설 예정, 문턱 낮추기 논의 |
| [2026-05-15 Builders Lounge 1 GOBI Hands-on 영상 정리.md](videos/2026-05-15%20Builders%20Lounge%201%20GOBI%20Hands-on%20%EC%98%81%EC%83%81%20%EC%A0%95%EB%A6%AC.md) | 첫 모임 GOBI Space / Desktop hands-on 영상 요약 |
| [2026-05-15 Builders Lounge 1 GOBI Hands-on Transcript.md](videos/2026-05-15%20Builders%20Lounge%201%20GOBI%20Hands-on%20Transcript.md) | YouTube 자동 생성 transcript |
| [2026-05-15 Builders Lounge 운영 방향과 Custom Homepage 논의 Slack.md](slack/2026-05-15%20Builders%20Lounge%20%EC%9A%B4%EC%98%81%20%EB%B0%A9%ED%96%A5%EA%B3%BC%20Custom%20Homepage%20%EB%85%BC%EC%9D%98%20Slack.md) | 창발 빌라, Product 소개 템플릿, VC perspective 리뷰 요청, Custom Homepage 구현 가능성 논의 |
| [2026-05-18 Builders Lounge 진행 상황 공지.md](notices/2026-05-18%20Builders%20Lounge%20%EC%A7%84%ED%96%89%20%EC%83%81%ED%99%A9%20%EA%B3%B5%EC%A7%80.md) | Builders Lounge 진행 상황 공지 정리본 |
| [2026-05-24 Builders Lounge 2회 준비 브레인덤프.md](ideas/2026-05-24%20Builders%20Lounge%202%ED%9A%8C%20%EC%A4%80%EB%B9%84%20%EB%B8%8C%EB%A0%88%EC%9D%B8%EB%8D%A4%ED%94%84.md) | 2회 모임 준비 아이디어, 홈페이지와 공동 기록 저장소 구상 |
| [2026-05-24 Builders Lounge Custom Homepage 기능 구상 - ChatGPT.md](ideas/2026-05-24%20Builders%20Lounge%20Custom%20Homepage%20%EA%B8%B0%EB%8A%A5%20%EA%B5%AC%EC%83%81%20-%20ChatGPT.md) | Product Showcase, Feedback Request, Review Template 등 홈페이지 기능 구상 |

## Custom Homepage 아이디어

Gobi Space Custom Homepage는 Builders Lounge 운영의 실험 공간이 될 수 있습니다. 첫 버전에서 가장 중요한 기능은 세 가지입니다.

1. **Product Showcase**: 멤버가 자신의 Product를 등록하고 설명하는 공간
2. **Feedback Request**: 지금 어떤 feedback을 받고 싶은지 명확하게 요청하는 공간
3. **Review Template**: 자유 댓글이 아니라 일정 품질 이상의 피드백을 남기도록 돕는 구조

이후에는 Demo Day page, Member Profile, Product Journey Log, Review Credit System, dashboard 같은 기능을 단계적으로 검토할 수 있습니다. Vibe Coding 시대에는 하나의 홈페이지만 정답일 필요가 없습니다. 여러 멤버가 각자 homepage prototype을 만들어 보고, 더 좋은 기능은 main homepage에 흡수하는 방식도 가능합니다.

## 공동 기록 저장소 아이디어

Builders Lounge 기록은 개인 컴퓨터에만 남기기보다 멤버들이 함께 접근할 수 있는 공간에 쌓이는 것이 좋습니다. GitHub repo는 그 첫 단계가 될 수 있습니다. Slack과 Gobi Space에서 오간 대화, 온라인/오프라인 모임 transcript, Product Demo, pitch, feedback 기록을 모아두면 나중에 AI로 다음과 같은 작업을 할 수 있습니다.

- 모임 history 요약
- Product별 feedback 요약
- Demo Day 준비 자료 생성
- Review template 개선
- Member/Product map 생성
- Builders Lounge 소개 페이지 또는 newsletter 생성
- Gobi Space Custom Homepage 요구사항 정리

## 현재 고민 중인 질문

- Product 소개와 feedback 요청을 Gobi Space post/comment만으로 충분히 운영할 수 있을까?
- Custom Homepage에서 Product Showcase와 Review Board를 어느 정도까지 구현할 수 있을까?
- Tag, dashboard, score 같은 기능이 없을 때 MVP를 어떻게 설계해야 할까?
- 기록 담당 멤버를 정할 것인가, 아니면 모임마다 rotation할 것인가?
- 공개 가능한 기록과 멤버 전용 기록을 어떻게 구분할 것인가?
- Builders Lounge를 지역 기반 커뮤니티로 둘 것인가, 온라인으로 더 넓게 열 것인가?

## 관련 링크

- Gobi Space: https://www.gobispace.com/
- Changbal Space: https://www.gobispace.com/spaces/changbal
- Gobi CLI: https://github.com/gobi-ai/gobi-cli
- Builders Lounge #1 GOBI Hands-on video: https://youtu.be/AoOhKZ4LoKs
- Brain Training Board Games: http://braintraining-boardgames-319297116860.s3-website-us-west-2.amazonaws.com/landing-page/

## 사용 방법

GitHub에 올라간 뒤에는 이 repository를 clone하거나 zip으로 내려받아 AI 도구에 폴더 전체를 읽히면 됩니다. 예를 들어 "Builders Lounge가 어떻게 시작됐는지 요약해줘", "2회 모임에서 논의할 agenda를 만들어줘", "Product feedback board의 MVP 요구사항을 뽑아줘"처럼 질문할 수 있습니다.

추가 기록을 올릴 때는 날짜와 주제를 파일명에 넣어 주세요.

```text
YYYY-MM-DD Builders Lounge [주제].md
```

예:

```text
2026-05-31 Builders Lounge 2회 모임 준비 회의.md
2026-06-07 Builders Lounge Product Demo Feedback.md
```

## 현재 기준

이 저장소는 공식 Builders Lounge repository가 아니라 Changsoo의 개인 기록입니다. 다만 멤버들이 참고하고 기여할 수 있도록 공개 가능한 형태로 정리하고 있습니다. 추후 공식 repository나 Gobi Space 내 전용 기능이 생기면 이 기록은 그쪽으로 옮기거나 연결할 수 있습니다.
