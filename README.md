# Builders Lounge 개인 기록 저장소

이 저장소는 Changsoo가 개인적으로 정리하고 있는 Builders Lounge 기록 공간입니다. 공식 Builders Lounge repository는 아니지만, 멤버분들이 모임의 시작 배경과 현재 논의 흐름을 빠르게 파악하실 수 있도록 공개 가능한 자료만 모아 두었습니다.

이 문서들과 저장소 구조는 Changsoo가 정리한 Slack 대화, 모임 기록, 운영 아이디어를 바탕으로 **VS Code + Codex**를 사용해 작성했습니다.

## 한눈에 보기

- **목적**: Builders Lounge의 시작 배경, 논의 흐름, 모임 기록, 운영 아이디어 정리
- **현재 상태**: 1회 공식 모임 완료, 2차 모임 완료 (2026-06-08 월, 벨뷰 시청 온/오프 하이브리드)
- **핵심 방향**: Product demo, 첫 사용자 feedback, 기록 기반 collective intelligence
- **활용 방법**: 이 repo를 clone한 뒤 AI에게 폴더 전체를 읽히고 질문
- **주의 사항**: 개인 기록 저장소이며, 공식 결정사항은 별도 공지 기준으로 확인

## Builders Lounge 개요

Builders Lounge는 AI를 활용해 Product, app, agent, workflow를 만드는 분들이 서로의 작업을 소개하고, 직접 사용해 보고, 피드백을 주고받으며 함께 성장하는 builder community입니다.

> "모두가 Builder이고, 동시에 서로의 사용자다" — Catch Up AI · Builders Lounge 비전 *(AI in Action Live #12, 2026-05-31)*

핵심은 단순 발표가 아니라 **서로의 첫 번째 사용자가 되어 드리는 것**입니다. 제품을 직접 써보고, 첫 화면이 이해되는지, 실제로 사용할 이유가 있는지, 어디서 막히는지, 다음에 무엇을 개선하면 좋을지 구체적으로 나누는 흐름을 지향합니다.

## 5가지 방향성

| 방향성                         | 의미                                                                              |
| --------------------------- | ------------------------------------------------------------------------------- |
| **Practical Build**         | 개발 경험 유무와 관계없이 누구나 참여할 수 있으며, 이론 학습에 머무르지 않고 AI를 활용해 실제 Product를 만들고 실험한 경험을 공유 |
| **Builder for Builders**    | 서로의 첫 번째 고객이 되어 피드백과 경험을 나누고, 필요할 때 협업하며 함께 성장                                  |
| **Workflow Sharing**        | AI와 협업하며 얻은 workflow, 시행착오, 도구 활용법 공유                                           |
| **Collective Intelligence** | Slack, Gobi Space, meeting, demo, pitch 기록을 AI가 활용 가능한 지식 자산으로 축적하고, AI Agent를 통해 누구나 언제든 활용할 수 있도록 지원 |
| **Open Ecosystem**          | Bellevue에서 시작해 지역과 소속의 경계를 넘어 어디서든 함께할 수 있는 열린 커뮤니티 지향                          |

## 현재 상태

- 2026년 5월 7일 첫 공식 오프라인 모임을 진행했습니다.
- 첫 모임에서는 GOBI Space / Desktop hands-on을 진행했습니다.
- 2026년 6월 8일 2차 모임을 Bellevue City Hall에서 온/오프 하이브리드로 진행했습니다.
- 모임 이름은 **Builders Lounge**로 확정했습니다.
- 별도 Gobi Space를 바로 만들기보다 기존 **Changbal Space**를 함께 활용하는 방향을 논의했습니다.
- 다음 단계는 Product 소개, feedback 요청, review 기록을 구조화하는 운영 방식 마련입니다.

## 멤버분들이 도와주실 수 있는 일

- 🛠️ 자신의 Product, app, agent, workflow 소개
- 👀 다른 멤버의 Product를 실제로 사용해 보고 feedback 작성
- 📝 Slack, Gobi Space, 온라인/오프라인 meeting, pitch, demo 기록 정리
- 💡 Gobi Space Custom Homepage 기능 아이디어 제안
- 🧩 Review template, feedback board, product showcase, demo day 운영 방식 제안
- 📚 GitHub repo 또는 Gobi Space 기반 공동 기록 방식 제안

## Product 소개 형식

```text
나의 Product: [Product 이름]
Product 위치: [GitHub / URL]
Demo 방법: Online / Offline
Product 설명: 어떤 문제를 해결하는가, 어떻게 만들었는가
Demo 계획: 무엇을 보여주고 싶은가 (예상 시간)
지금 가장 받고 싶은 Feedback: [예: 첫 화면, onboarding, 가격, AI 기능, VC perspective 등]
```

## 기록 대상

| 기록 대상 | 예시 | 활용 가능성 |
| --- | --- | --- |
| Slack 대화 | 모임 공지, 댓글, Product 소개, feedback 요청 | 모임 history, decision log |
| Gobi Space 글 | Changbal Space post, 댓글, AI 요약 | 공동 지식 축적, member knowledge base |
| Product Demo | 발표 자료, 영상, Q&A | Product showcase, feedback archive |
| 온라인/오프라인 회의 | transcript, 요약, action item | 다음 모임 준비, AI 기반 회고 |
| Custom Homepage 아이디어 | 기능 목록, UI 제안, 구현 제약 | Gobi Space homepage / future app design |

## 폴더 구조

```text
builders-lounge-personal-notes/
├─ README.md
├─ slack/      Slack 대화와 논의 흐름
├─ notices/    멤버 공지와 진행 상황 공유
├─ videos/     공식 모임 영상 정리와 transcript
├─ ideas/      운영 아이디어와 다음 모임 준비
├─ feedback/   멤버 Product review와 방향성 feedback
└─ assets/     이미지 자료
```

| 폴더 | 설명 |
| --- | --- |
| `README.md` | 저장소 목적, 현재 상태, 참여 방법, 주요 문서 링크 |
| `slack/` | Builders Lounge가 논의되고 준비되는 과정의 Slack 기록 |
| `notices/` | 멤버분들께 공유한 진행 상황 공지와 운영 안내 |
| `videos/` | 공식 모임 녹화 영상 정리와 transcript |
| `ideas/` | 2회 모임 준비, Custom Homepage, 공동 기록 저장소 아이디어 |
| `feedback/` | 멤버들이 서로의 Product, app, agent, workflow에 대해 남긴 review와 방향성 feedback |
| `assets/` | README나 문서에서 사용할 이미지 자료 |

## 주요 문서

| 문서 | 내용 |
| --- | --- |
| [2026-03-25 Builders Lounge 초기 논의 Slack.md](slack/2026-03-25%20Builders%20Lounge%20%EC%B4%88%EA%B8%B0%20%EB%85%BC%EC%9D%98%20Slack.md) | Brain Training Board Games 소개와 coding agent 활용 논의에서 오프모임 아이디어가 시작된 기록 |
| [2026-04-09 Builders Lounge 모임 준비 Slack.md](slack/2026-04-09%20Builders%20Lounge%20%EB%AA%A8%EC%9E%84%20%EC%A4%80%EB%B9%84%20Slack.md) | 4월 오프모임 준비, Gobi Desktop, VibeLearn AI, Harness Engineering 논의 |
| [2026-04-11 Builders Lounge 준비 모임과 첫 오프라인 모임 Slack.md](slack/2026-04-11%20Builders%20Lounge%20%EC%A4%80%EB%B9%84%20%EB%AA%A8%EC%9E%84%EA%B3%BC%20%EC%B2%AB%20%EC%98%A4%ED%94%84%EB%9D%BC%EC%9D%B8%20%EB%AA%A8%EC%9E%84%20Slack.md) | 온라인 준비 미팅, 4/23 Dote Coffee Bar 모임, 장소 섭외, 이름 공모, 공동 지식 축적 논의 |
| [2026-05-07 Builders Lounge 첫 정식 모임 Slack.md](slack/2026-05-07%20Builders%20Lounge%20%EC%B2%AB%20%EC%A0%95%EC%8B%9D%20%EB%AA%A8%EC%9E%84%20Slack.md) | Bellevue City Hall 첫 정식 모임 안내, 5가지 방향성, Gobi 링크 공유 |
| [2026-05-09 Builders Lounge 1회 후속 Slack.md](slack/2026-05-09%20Builders%20Lounge%201%ED%9A%8C%20%ED%9B%84%EC%86%8D%20Slack.md) | 1회 모임 결과, Builders Lounge 이름 확정, 문턱 낮추기 논의 |
| [2026-05-15 Builders Lounge 1 GOBI Hands-on 영상 정리.md](videos/2026-05-15%20Builders%20Lounge%201%20GOBI%20Hands-on%20%EC%98%81%EC%83%81%20%EC%A0%95%EB%A6%AC.md) | 첫 모임 GOBI Space / Desktop hands-on 영상 요약 |
| [2026-06-08 Builders Lounge 2차 모임 정리.md](videos/2026-06-08%20Builders%20Lounge%202%EC%B0%A8%20%EB%AA%A8%EC%9E%84%20%EC%A0%95%EB%A6%AC.md) | 2차 모임 transcript 기반 요약 — Brain Training Science, Gobi Space, Builders Lounge AI, Product demo 피드백 |
| [2026-06-08 Builders Lounge 2차 모임 당일 및 후속 Slack.md](slack/2026-06-08%20Builders%20Lounge%202%EC%B0%A8%20%EB%AA%A8%EC%9E%84%20%EB%8B%B9%EC%9D%BC%20%EB%B0%8F%20%ED%9B%84%EC%86%8D%20Slack.md) | 6/8 당일 Slack 공지, 6/9 기록 공유 계획, 6/10 Podcast와 SkillOpt 후속 자료 |
| [2026-05-15 Builders Lounge 운영 방향과 Custom Homepage 논의 Slack.md](slack/2026-05-15%20Builders%20Lounge%20%EC%9A%B4%EC%98%81%20%EB%B0%A9%ED%96%A5%EA%B3%BC%20Custom%20Homepage%20%EB%85%BC%EC%9D%98%20Slack.md) | 창발 빌라, Product 소개 템플릿, VC perspective 리뷰 요청, Custom Homepage 논의 |
| [2026-05-18 Builders Lounge 진행 상황 공지.md](notices/2026-05-18%20Builders%20Lounge%20%EC%A7%84%ED%96%89%20%EC%83%81%ED%99%A9%20%EA%B3%B5%EC%A7%80.md) | Builders Lounge 진행 상황 공지 정리본 |
| [2026-05-24 Builders Lounge 2회 준비 브레인덤프.md](ideas/2026-05-24%20Builders%20Lounge%202%ED%9A%8C%20%EC%A4%80%EB%B9%84%20%EB%B8%8C%EB%A0%88%EC%9D%B8%EB%8D%A4%ED%94%84.md) | 2회 모임 준비 아이디어, 홈페이지와 공동 기록 저장소 구상 |
| [2026-05-24 Builders Lounge Custom Homepage 기능 구상 - ChatGPT.md](ideas/2026-05-24%20Builders%20Lounge%20Custom%20Homepage%20%EA%B8%B0%EB%8A%A5%20%EA%B5%AC%EC%83%81%20-%20ChatGPT.md) | Product Showcase, Feedback Request, Review Template 등 홈페이지 기능 구상 |
| [2026-06-18 GOBI B2B SI 방향 피드백 - 김성진님.md](feedback/2026-06-18%20GOBI%20B2B%20SI%20%EB%B0%A9%ED%96%A5%20%ED%94%BC%EB%93%9C%EB%B0%B1%20-%20%EA%B9%80%EC%84%B1%EC%A7%84%EB%8B%98.md) | GOBI의 데이터 수집-관리-활용 흐름과 B2B/SI Knowledge Management 가능성에 대한 멤버 피드백 |
| [2026-06-18 GOBI Space Open Harness 제안 - Changsoo.md](feedback/2026-06-18%20GOBI%20Space%20Open%20Harness%20%EC%A0%9C%EC%95%88%20-%20Changsoo.md) | Space admin과 멤버가 Agent prompt, Skill, MCP를 함께 관리하는 Open Harness 제안 |
| [2026-07-02 Nate Cho - Job Search Co-pilot.md](ideas/2026-07-02%20Nate%20Cho%20-%20Job%20Search%20Co-pilot.md) | 창발 멤버 Nate Cho님의 취업 준비 도구 프로필 — Claude Cowork Plugin 기반, "don't make hiring teams connect the dots for you" 철학, 오픈소스·초기 테스트 중 |
| [2026-07-05 AI4PKM Vault 활용 피드백 - Changsoo.md](feedback/2026-07-05%20AI4PKM%20Vault%20%ED%99%9C%EC%9A%A9%20%ED%94%BC%EB%93%9C%EB%B0%B1%20-%20Changsoo.md) | 김진영님의 ai4pkm-vault를 5개월 실사용한 데이터 기반 피드백과 원저자에게 드리는 질문 12개 |
| [2026-07-06 Builders Lounge KACC Coffee Chat 결과 공유 - Codex 요약.md](notices/2026-07-06%20Builders%20Lounge%20KACC%20Coffee%20Chat%20%EA%B2%B0%EA%B3%BC%20%EA%B3%B5%EC%9C%A0%20-%20Codex%20%EC%9A%94%EC%95%BD.md) | KACC Coffee Chat 결과 요약 — 11월 프로그램, 제품 사용 피드백, 한인 스타트업 네트워크, 환대 키워드 |
| [2026-05-24 Builders Lounge GitHub Repo 공유 및 운영 아이디어 논의 Slack.md](slack/2026-05-24%20Builders%20Lounge%20GitHub%20Repo%20%EA%B3%B5%EC%9C%A0%20%EB%B0%8F%20%EC%9A%B4%EC%98%81%20%EC%95%84%EC%9D%B4%EB%94%94%EC%96%B4%20%EB%85%BC%EC%9D%98%20Slack.md) | GitHub repo Slack 공유, autoresearch/HPO 논의, Gobi Space Agent Dreaming, Slack→MD 자동 변환 아이디어 |
| [2026-05-25 Builders Lounge 2회 모임 준비 및 GitHub 공유 Slack.md](slack/2026-05-25%20Builders%20Lounge%202%ED%9A%8C%20%EB%AA%A8%EC%9E%84%20%EC%A4%80%EB%B9%84%20%EB%B0%8F%20GitHub%20%EA%B3%B5%EC%9C%A0%20Slack.md) | @Paul Kim에게 2회 모임 준비 현황 공지, GitHub 기록 저장소 공유 및 GobiSpace 안내 |
| [2026-05-25 Builders Lounge GobiSpace Changbal 안내 글.md](notices/2026-05-25%20Builders%20Lounge%20GobiSpace%20Changbal%20%EC%95%88%EB%82%B4%20%EA%B8%80.md) | [창발 빌라] Changbal Space 게시 글 — GitHub repo 공유, 성진님 운영 아이디어, GOBI agentic network 관점 |
| [2026-05-25 Builders Lounge GobiSpace Global 안내 글.md](notices/2026-05-25%20Builders%20Lounge%20GobiSpace%20Global%20%EC%95%88%EB%82%B4%20%EA%B8%80.md) | GobiSpace Global 게시 글 — 커뮤니티 소개, AI 기록 활용, Changbal Space 참여 안내 |
| [2026-05-26 Builders Lounge 스페이스 이름 및 AI 이름 논의 Slack.md](slack/2026-05-26%20Builders%20Lounge%20%EC%8A%A4%ED%8E%98%EC%9D%B4%EC%8A%A4%20%EC%9D%B4%EB%A6%84%20%EB%B0%8F%20AI%20%EC%9D%B4%EB%A6%84%20%EB%85%BC%EC%9D%98%20Slack.md) | MinSuk Kang과 DM — 창발 Space 이름 변경, Builders Lounge 독립성, 커뮤니티 AI 이름(Bila 후보), Dreaming 프로세스 |
| [2026-06-05 Builders Lounge AI 코디네이터 GOBI Mika 피드백 Slack.md](slack/2026-06-05%20Builders%20Lounge%20AI%20%EC%BD%94%EB%94%94%EB%84%A4%EC%9D%B4%ED%84%B0%20GOBI%20Mika%20%ED%94%BC%EB%93%9C%EB%B0%B1%20Slack.md) | GOBI 개발자 Mika — Phase 1~3 기술 검토: QnA 즉시 가능, Phase 3는 웹훅 트리거 구조, Phase 2는 Cron 방식 |

## Custom Homepage 아이디어

첫 버전에서 중요한 기능은 아래 세 가지입니다.

1. **Product Showcase**: 멤버분들이 자신의 Product를 등록하고 설명하는 공간
2. **Feedback Request**: 지금 받고 싶은 feedback을 명확하게 요청하는 공간
3. **Review Template**: 일정한 품질의 피드백을 남기도록 돕는 구조

추가 후보:

- Demo Day page
- Member Profile
- Product Journey Log
- Review Credit System
- Dashboard

## 공동 기록 저장소 아이디어

Builders Lounge 기록은 개인 컴퓨터에만 남기기보다 멤버분들이 함께 접근할 수 있는 공간에 쌓이는 것이 좋습니다. GitHub repo는 그 첫 단계로 사용할 수 있습니다.

AI로 활용할 수 있는 예시는 아래와 같습니다.

- 모임 history 요약
- Product별 feedback 요약
- Demo Day 준비 자료 생성
- Review template 개선
- Member/Product map 생성
- Builders Lounge 소개 페이지 또는 newsletter 생성
- Gobi Space Custom Homepage 요구사항 정리

## 현재 논의 질문

- Product 소개와 feedback 요청을 Gobi Space post/comment만으로 운영할 수 있을까요?
- Custom Homepage에서 Product Showcase와 Review Board를 어느 정도까지 구현할 수 있을까요?
- Tag, dashboard, score 같은 기능이 없을 때 MVP를 어떻게 설계하면 좋을까요?
- 기록 담당 멤버를 정할까요, 아니면 모임마다 rotation할까요?
- 공개 가능한 기록과 멤버 전용 기록을 어떻게 구분하면 좋을까요?
- Builders Lounge를 지역 기반 커뮤니티로 둘까요, 온라인으로 더 넓게 열까요?

## 멤버 목록

| 멤버 | 이메일 | Product | URL | 상태 | 비고 |
| --- | --- | --- | --- | --- | --- |
| Minsuk Kang (강민석) | `gpminsuk@gmail.com` | Gobi Space | [gobispace.com](https://www.gobispace.com/) | 서비스 중 | AI-native social space, Bila 플랫폼 |
| Sung-Jin Kim (김성진) | `jamessungjin.kim@gmail.com` | Brain Training Board Games | [링크](http://braintraining-boardgames-319297116860.s3-website-us-west-2.amazonaws.com/landing-page/) | 배포 완료 | AI 시대 두뇌 훈련 보드게임 웹앱 |
| 김진영 | `myleo.jerry@gmail.com` | AI4PKM | [jykim/ai4pkm-vault](https://github.com/jykim/ai4pkm-vault) | 개발 중 | Beyond LLM Wiki 발표자 (CMDS, 7/2), 사이드: Washington State Leisure Map |
| Daniel Kang | `fromdj2k@gmail.com` | AllStay.ai | [allstay.ai](https://allstay.ai/) | GTM 중 | AI 기반 Short-Term Rental 운영 자동화 |
| Sung Soo Kim (김성수) | `hebronplatform@gmail.com` | HebronGuide | [hebronguide.com](https://www.hebronguide.com/) | 운영 중 | 재외 한인 75개 도시 정착 커뮤니티 플랫폼 |
| Changsoo Park (박창수) | `solkit70@gmail.com` | CatchUp AI | [catchupai.net](https://catchupai.net) | 운영 중 | AI 활용법 콘텐츠·커뮤니티, 운영자 |
| Nate Cho | `nate.cho.nyc@gmail.com` | Job Search Co-pilot | [GitHub](https://github.com/nathanscho/jobsearch-copilot) | 초기 테스트 중 | Claude Cowork Plugin 기반 취업 준비 도구, MIT 오픈소스 |
| 송재희 | `jsong@seattlepartners.us` | Build with AI | [buildwithai.clearlyreqs.com/ko](https://buildwithai.clearlyreqs.com/ko) | 공개 완료 | 비개발자를 위한 무료 12부작 AI Builder 가이드 |
| Dokyu Lee (이도규) | `mickeyfromsd@gmail.com` | — | — | — | 2차 모임 오프라인 참석 |
| 박세진 | `davidsejinpark@gmail.com` | — | — | — | 2차 모임 온라인 참석 |
| 손민수 | `commercial209@gmail.com` | 시스템 장애 대응 에이전트 | — | 아이디어/MVP | 2차 모임 온라인 참석, 샌프란시스코 거주 |
| Eunsil Ha | `haysil@naver.com` | — | — | — | Bila 멤버, 2차 모임 일정 착오로 불참 |
| 여상호 | `sangho.yeo@gmail.com` | — | — | — | 참석 시도, 일정 불일치로 불참 |

> Daniel Kang — 2026-06-04 Slack 소개: "AI를 활용한 Short-Term Rental 운영 플랫폼 AllStay를 만들고 있습니다. 플랫폼 개발은 상당 부분 진행된 상태입니다. 이제 가장 중요한 고객 확보와 Go-to-Market 단계에 집중하고 있어, Sales/Business Development에 관심 있는 분을 찾고 있습니다." — 벨뷰 지역 활동

## 관련 링크

- Gobi Space: https://www.gobispace.com/
- Changbal Space: https://www.gobispace.com/spaces/changbal
- Gobi CLI: https://github.com/gobi-ai/gobi-cli
- Builders Lounge personal notes GitHub repo: https://github.com/solkit70/builders-lounge-personal-notes
- Builders Lounge #1 GOBI Hands-on video: https://youtu.be/AoOhKZ4LoKs
- Brain Training Board Games: http://braintraining-boardgames-319297116860.s3-website-us-west-2.amazonaws.com/landing-page/
- AllStay.ai (Daniel Kang): https://allstay.ai/
- Washington State Leisure Map / Trails: https://trails.aiforbetter.me/
- The Washington State Hiking Podcast: https://podcasts.apple.com/us/podcast/the-washington-state-hiking-podcast/id1734650082
- SkillOpt Explained: https://medium.com/@linafaik/skillopt-explained-from-prompt-engineering-to-skill-training-7ca8439cef73

## 활용 방법

이 repository를 clone하거나 zip으로 내려받은 뒤, AI 도구에 폴더 전체를 읽히면 됩니다. 예시는 아래와 같습니다.

- "Builders Lounge가 어떻게 시작됐는지 요약해 주세요."
- "2회 모임에서 논의할 agenda를 만들어 주세요."
- "Product feedback board의 MVP 요구사항을 뽑아 주세요."

추가 기록 파일명은 아래 형식을 권장드립니다.

```text
YYYY-MM-DD Builders Lounge [주제].md
```

예:

```text
2026-05-31 Builders Lounge 2회 모임 준비 회의.md
2026-06-07 Builders Lounge Product Demo Feedback.md
```

## 현재 기준 안내

- 이 저장소는 공식 Builders Lounge repository가 아니라 Changsoo의 개인 기록입니다.
- 멤버분들이 참고하고 기여하실 수 있도록 공개 가능한 형태로 정리하고 있습니다.
- 추후 공식 repository나 Gobi Space 내 전용 기능이 생기면 이 기록을 그쪽으로 옮기거나 연결할 수 있습니다.
