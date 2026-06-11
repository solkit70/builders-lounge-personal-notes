---
title: "Builders Lounge 2차 모임 정리"
source: "C:/Users/dougg/Videos/Youtube/2026/Builders_Lounge/20260608_secondMeeting/full_Transcript.txt"
created: 2026-06-11 04:34:10
event_date: 2026-06-08
location: "Bellevue City Hall Room 1E-108"
attendees_offline:
  - "Sung-Jin Kim"
  - "Minsuk Kang"
  - "Dokyu Lee"
  - "Changsoo Park"
  - "Sung Soo Kim"
attendees_online:
  - "박세진"
  - "손민수"
  - "김진영"
tags:
  - builders-lounge
  - meeting
  - transcript
  - product-demo
  - gobi-space
sources:
  - "../README.md"
  - "../notices/2026-06-08 Builders Lounge 2차 모임 안내.md"
---

## 요약

2026년 6월 8일 Builders Lounge 2차 모임은 “각자 만든 것을 보여주고, 서로가 첫 번째 사용자로 피드백을 주는 모임”이라는 방향이 실제로 작동한 자리였다. 오프라인으로는 Sung-Jin Kim, Minsuk Kang, Dokyu Lee, Changsoo Park, Sung Soo Kim 다섯 명이 참석했고, 온라인으로는 박세진, 손민수, 김진영 세 명이 참석했다. 모임은 Sung-Jin Kim의 Brain Training Science 데모로 시작해, Changsoo Park의 Builders Lounge 기록 저장소와 Gobi Space 연동 비전, Minsuk Kang의 Gobi Space 제품 데모, 김진영의 워싱턴 놀거리/트레일 맵, 손민수의 시스템 장애 대응 에이전트 아이디어로 이어졌다.

> "코드를 안 보고 실제로 그 프롬프트에다 넣어 가지고 해 달라고 하고 결과를 보고 또 프롬프트를 넣고 이렇게 계속 돌려서 만들어진 거거든요."  
> — Sung-Jin Kim, 00:02:50~00:03:07

이날의 핵심은 단순한 제품 발표가 아니라, AI 시대의 제품 개발 방식 자체를 함께 비교한 데 있었다. 개발자가 기존 방식대로 구조를 먼저 잡고 고치려는 접근, 비개발자가 말과 스크린샷으로 계속 수정하는 접근, 사용 중 발생한 문제를 다시 프롬프트에 넣어 처음부터 재생성하는 접근이 한 자리에서 비교되었다. → **관련 맥락**: [2회 준비 브레인덤프](../ideas/2026-05-24%20Builders%20Lounge%202%ED%9A%8C%20%EC%A4%80%EB%B9%84%20%EB%B8%8C%EB%A0%88%EC%9D%B8%EB%8D%A4%ED%94%84.md)

## 참석자

| 구분 | 참석자 |
| --- | --- |
| 오프라인 | Sung-Jin Kim, Minsuk Kang, Dokyu Lee, Changsoo Park, Sung Soo Kim |
| 온라인 | 박세진, 손민수, 김진영 |

## 주요 흐름

| 시간대 | 주제 | 핵심 내용 |
| --- | --- | --- |
| 00:01~00:45 | Brain Training Science 데모 | Sung-Jin Kim이 AI로 만든 보드게임 컬렉션과 vibe coding 과정을 소개 |
| 00:45~00:53 | Builders Lounge 기록 저장소 | Changsoo Park이 GitHub 기록 저장소, Q&A, Product monitoring, 모임 코디네이터 비전을 소개 |
| 00:53~01:12 | Gobi Space 데모 | Minsuk Kang이 AI-native social space, Space Agent, GitHub/Drive/Slack 연동 구조를 설명 |
| 01:12~01:44 | 에이전트 운영 방법론 | 기록, prompt, context, harness engineering, command/skill 활용 방식 논의 |
| 01:44~01:59 | 워싱턴 놀거리 맵 | 김진영이 WTA trail status, campground, golf course 정보를 모은 지도 앱을 소개 |
| 01:59~02:11 | 시스템 장애 대응 에이전트 | 손민수가 로그/리소스/UI 에이전트로 장애를 분석하는 MVP 아이디어를 소개 |

## 발표 Product 링크

| 발표자 | Product | 링크 |
| --- | --- | --- |
| Sung-Jin Kim | Brain Training Board Games | http://braintraining-boardgames-319297116860.s3-website-us-west-2.amazonaws.com/landing-page/ |
| Changsoo Park | Builders Lounge 기록 저장소 | https://github.com/solkit70/builders-lounge-personal-notes |
| Minsuk Kang | Gobi Space | https://www.gobispace.com/ |
| 김진영 | Washington State Leisure Map / Trails | https://trails.aiforbetter.me/ |

## Sung-Jin Kim — Brain Training Science

Sung-Jin Kim은 AI 에이전트가 사람의 일을 대신하면서 오히려 인간의 두뇌 사용량이 줄어들 수 있다는 문제의식에서 출발해, “헬스클럽처럼 두뇌를 훈련하는” 게임 아이디어를 소개했다. 대학생 한 명과 함께 보드게임을 웹앱으로 만들었고, Sung-Jin Kim은 tic-tac-toe 예시와 퍼블리시 과정, 서버 업로드 등을 도왔다. 중요한 점은 코드를 직접 보며 만든 것이 아니라, Gemini/Gemini CLI 계열 도구에 말로 요청하고 결과를 보며 프롬프트를 반복하는 방식으로 만들었다는 점이다.

→ **Product**: [Brain Training Board Games](http://braintraining-boardgames-319297116860.s3-website-us-west-2.amazonaws.com/landing-page/)

> "헬스클럽에 대해서 우리가 훈련하듯이 에이전트를 이용해서 내 두뇌를 훈련시킬 방법이 없을까 고민하다가 보드 게임을 한번 만들어 보는 걸로 했습니다."  
> — 00:01:34~00:01:49

데모에서는 two-player, one-player AI 모드, 여러 보드게임 컬렉션, AI가 규칙과 UI를 구성해 주는 흐름이 논의되었다. 참석자들은 강화학습이나 파인튜닝이 필요한지, AI가 이미 알고 있는 게임 규칙을 활용하는 것이 충분한지, 코딩 경험이 거의 없는 사람이 어떻게 완성도 있는 앱을 만들 수 있었는지 질문했다. 이 대화는 Builders Lounge의 핵심 방향인 “실제로 만든 것을 보여주고, 그 사용 경험을 바탕으로 피드백하는 구조”를 잘 보여준다.

## Vibe Coding 논의

Brain Training Science 데모 이후에는 vibe coding의 접근법 자체가 주요 논의가 되었다. Changsoo Park은 spec-driven development와 prompt-driven development를 비교했고, Minsuk Kang은 실제 사용 중 생기는 문제를 캡처해 AI에게 바로 보내는 use-driven development 관점도 제안했다. Sung Soo Kim은 비개발자 입장에서 “문제가 생기면 코드를 파고들기보다 바깥에서 다시 설명하고 다시 만들어 달라고 하는 방식”이 오히려 더 자연스럽다고 설명했다.

> "코딩 하지 프로그램 하시던 분들은 ... 문제가 생기면 거기에 딱 들어가서 해결을 본인이 해 보려고 애를 쓰고 있더라고요. 나는 그런 식으로 접근 안 하거든요."  
> — Sung Soo Kim, 00:39:40~00:40:01

이 대화에서 나온 중요한 인사이트는 “아는 게 병”이라는 표현이었다. 기존 개발자는 구조와 구현을 직접 통제하려는 습관이 있지만, AI를 처음부터 도구로 접한 사람은 자신이 원하는 결과와 불편함을 설명하는 데 더 집중한다. 다음 모임에서는 Sung Soo Kim이 이런 비개발자 관점의 AI 사용 방식을 더 자세히 발표하기로 했다.

## Changsoo Park — 기록 저장소와 Builders Lounge AI

Changsoo Park은 Builders Lounge 관련 Slack, 공지, 아이디어, 모임 기록이 `AI/Initiatives/Builders Lounge/` 아래에 정리되어 있고, 이 기록을 AI에게 읽히면 모임의 맥락을 질문할 수 있다고 설명했다. 핵심은 모임의 일회성 대화를 transcript와 Markdown 기록으로 바꾸고, 그 기록을 GitHub와 Gobi Space에 연결해 커뮤니티 AI가 참조할 수 있게 하는 것이다.

→ **기록 저장소**: [solkit70/builders-lounge-personal-notes](https://github.com/solkit70/builders-lounge-personal-notes)

> "AI를 주로 잘 이용하기 위해서는 기록이 중요하다라고 생각을 하고요. 여기에서 ... 빌더스 라운지 관련된 기록들을 여기가 지금 다 모으고 있어요."  
> — 00:46:13~00:46:29

Builders Lounge AI의 발전 방향은 세 단계로 제시되었다. Phase 1은 기록 기반 Q&A이고, Phase 2는 멤버들의 Product repository나 활동 기록을 모니터링해 서로 연결해 주는 자동 매칭이며, Phase 3는 안건 생성, 발표자 추천, 모임 후 정리까지 담당하는 커뮤니티 코디네이터다. → **관련 문서**: [AI 코디네이터 구상](../ideas/2026-05-30%20Builders%20Lounge%20AI%20%EC%BD%94%EB%94%94%EB%84%A4%EC%9D%B4%ED%84%B0%20%EA%B5%AC%EC%83%81.md)

## Minsuk Kang — Gobi Space 데모

Minsuk Kang은 Gobi Space를 “AI-native social product”로 소개했다. Space는 멤버들이 글을 올리고 댓글을 달며 소통하는 커뮤니티 공간이고, 여기에 Space Agent를 붙여 커뮤니티가 올린 글과 제공한 문서를 기반으로 질문에 답하게 할 수 있다. Gobi Space 안에서는 AI를 태그해 공개 질문을 던질 수 있고, 별도 채팅에서는 개인적으로 질문할 수도 있다.

→ **Product**: [Gobi Space](https://www.gobispace.com/)

> "각 스페이스에 AI 에이전트를 하나 만들어서 서로가 올렸던 글들이나 ... 다큐먼트들을 제공을 하면 얘가 그런 것들로 학습을 해서 ... 한 커뮤니티가 키워가는 AI."  
> — Minsuk Kang, 00:54:05~00:54:29

데모에서는 Changbal Space의 포스트, 댓글, AI 답변, 개인 채팅, knowledge graph, saved posts, admin 설정, agent system prompt, GitHub/Google Drive/Slack 연동 구조가 소개되었다. 이 흐름은 Builders Lounge가 단순 모임이 아니라 “기록이 쌓이고, 그 기록을 AI가 다시 활용하는 커뮤니티”로 발전할 수 있음을 보여준다. → **관련 문서**: [GOBI Mika 기술 검토](../slack/2026-06-05%20Builders%20Lounge%20AI%20%EC%BD%94%EB%94%94%EB%84%A4%EC%9D%B4%ED%84%B0%20GOBI%20Mika%20%ED%94%BC%EB%93%9C%EB%B0%B1%20Slack.md)

## 기록, PKM, Harness Engineering

중반부에는 Gobi Desktop, 개인 기록, PKM, Markdown, prompt/context/harness engineering에 대한 긴 논의가 이어졌다. Changsoo Park은 AI가 나를 위해 일하게 하려면 나에 대한 기록이 많아야 한다고 설명했고, Minsuk Kang은 Gobi Desktop이 로컬 데이터를 관리하고 Gobi Space로 포스팅하거나 댓글을 달 수 있는 구조를 설명했다. 참석자들은 반복 작업을 prompt, skill, command로 고정하는 방법과, AI가 어디서 멈춰야 하는지 결정하는 Definition of Done의 중요성을 논의했다.

> "AI를 진짜 나를 위해서 일을 하게끔 잘 활용을 하려면 나에 대해서 AI가 잘 알게끔 만들어져야 되는데 AI에게 나를 알려주는 방법은 지금은 텍스트."  
> — 01:25:39~01:26:03

이 논의는 Builders Lounge의 `Collective Intelligence` 방향성과 직접 연결된다. 개인 기록이 개인 AI의 context가 되듯, 커뮤니티 기록은 커뮤니티 AI의 context가 된다. 따라서 transcript, product demo, Q&A, feedback을 Markdown으로 남기는 일은 단순 문서화가 아니라, 이후 AI가 커뮤니티를 도울 수 있게 하는 기반 작업이다.

## 김진영 — 워싱턴 놀거리 맵

김진영은 워싱턴주 trail, campground, golf course 정보를 지도 위에 모은 개인 프로젝트를 소개했다. 특히 WTA(Washington Trails Association)의 trail report를 매일 크롤링해 open, snow gear, closed 같은 상태를 지도에 표시하고, campground와 golf course까지 레이어로 추가했다. 이 프로젝트는 “일하기 싫을 때 토큰을 쓰며 만든” 사이드 프로젝트로 소개되었지만, 참석자들은 산과 야외활동을 좋아하는 사람들에게 실질적 가치가 크다고 평가했다.

→ **Product**: [Washington State Leisure Map / Trails](https://trails.aiforbetter.me/)

김진영이 Slack에 올린 소개 글에 따르면, 이 프로젝트의 목표는 워싱턴주 레저에 대한 최신 정보를 담은 종합 데이터베이스를 만드는 것이다. 현재 범위는 `wta.org` 기반 상태 정보를 포함한 워싱턴주 모든 트레일, 예약 정보를 포함한 워싱턴주 모든 골프장, 예약 정보를 포함한 워싱턴주 모든 캠핑장이다. 김진영은 URL이 조만간 바뀔 예정이므로 email update 등록을 권했다.

> "이 정보들이 다 WTA라는 웹사이트가 있어요... 이 정보를 다 매일 일일이 가 보지 않고 한 곳에서 볼 수 있게."  
> — 01:47:17~01:47:46

피드백으로는 사용자의 위치 기준 driving time, 다녀온 trail history 기반 다음 trail 추천, 회원가입과 trip save 기능, 100명 정도의 무료 베타 사용자 모집, 야외활동 커뮤니티와의 연결 가능성이 나왔다. 김진영은 trail 정보를 API로 제공하고, Claude Skill을 만들어 2박 3일 road trip planning을 생성하는 실험도 진행 중이라고 설명했다.

## 손민수 — 시스템 장애 대응 에이전트

손민수는 새벽 시간대 시스템 장애에 사람이 즉시 대응하지 못해 문제가 몇 시간 지속된 경험에서 출발해, AI 에이전트가 시스템 상태를 감시하고 장애 원인을 분석하는 MVP 아이디어를 공유했다. resource agent, log scraper, vision agent, oracle agent처럼 역할을 나눈 에이전트가 CPU, memory, log, UI screenshot을 수집하고, evidence card와 timeline을 바탕으로 판단을 내리는 구조다.

> "문제가 생겼을 때 스스로 분석을 하고 문제를 해결을 하려는 목적으로."  
> — 손민수, 02:05:10~02:05:18

참석자들은 이 아이디어가 기존 on-call monitoring과 escalation process를 AI가 보조하거나 일부 대체하는 방향으로 볼 수 있다고 해석했다. 다만 실제 운영에서는 어떤 상태를 문제로 볼지, 누구에게 연락할지, 어떤 remediation을 자동으로 실행할지에 대한 decision criteria가 중요하다는 피드백이 나왔다. 다음 모임에서는 손민수가 이 프로젝트를 더 자세히 발표하고, Sung Soo Kim은 비개발자 관점에서 AI를 사용하는 방식을 발표하는 흐름으로 이어질 수 있다.

## AI 이름과 커뮤니티 운영

이날 AI 코디네이터 이름은 최종 확정하지 못했다. **Bila**는 후보이자 가칭으로 남겨 두고, 실제 커뮤니티 AI의 역할과 사용 맥락이 더 분명해진 뒤 이름을 확정하는 편이 자연스럽다. 이름 논의보다 더 중요한 것은 커뮤니티 AI가 실제로 무엇을 도와야 하는지였다. 기록 기반 Q&A, product matching, 모임 코디네이션, 후속 정리 자동화가 이날 확인된 핵심 후보 기능이다.

## 결정 및 후속 액션

| 항목 | 상태 | 후속 조치 |
| --- | --- | --- |
| Builders Lounge 2차 모임 | 완료 | 본 정리본을 공유 가능한 기록으로 보관 |
| AI 이름 | 보류 | Bila는 가칭으로 유지 |
| Brain Training Science | 피드백 완료 | 측정 지표, 학생/NGO 활용, 사용자 모집 가능성 검토 |
| Gobi Space 연동 | 진행 | GitHub/Drive/Slack 자료를 Space Agent가 참조하는 구조 실험 |
| Builders Lounge AI | 구상 유지 | Phase 1 Q&A부터 Product matching, 모임 코디네이터로 확장 |
| 워싱턴 놀거리 맵 | 피드백 완료 | 개인화 추천, trip save, beta user 모집 검토 |
| 시스템 장애 대응 에이전트 | 다음 발표 후보 | decision criteria, evidence card, escalation 기준 구체화 |
| 다음 모임 발표 | 후보 정리 | Sung Soo Kim, 손민수 발표 가능성 |

## Source Notes

- 원본 transcript: `C:/Users/dougg/Videos/Youtube/2026/Builders_Lounge/20260608_secondMeeting/full_Transcript.txt`
- Sung-Jin Kim product: http://braintraining-boardgames-319297116860.s3-website-us-west-2.amazonaws.com/landing-page/
- Changsoo Park Builders Lounge 기록 저장소: https://github.com/solkit70/builders-lounge-personal-notes
- Gobi Space: https://www.gobispace.com/
- 김진영 product: https://trails.aiforbetter.me/
- 김진영 Slack 캡처: 워싱턴주 트레일, 골프장, 캠핑장 최신 정보 데이터베이스 소개 및 email update 등록 안내
- Slack 당일 공지 및 후속 댓글: [2026-06-08 Builders Lounge 2차 모임 당일 및 후속 Slack](../slack/2026-06-08%20Builders%20Lounge%202%EC%B0%A8%20%EB%AA%A8%EC%9E%84%20%EB%8B%B9%EC%9D%BC%20%EB%B0%8F%20%ED%9B%84%EC%86%8D%20Slack.md)
- 관련 안내: [2026-06-08 Builders Lounge 2차 모임 안내](../notices/2026-06-08%20Builders%20Lounge%202%EC%B0%A8%20%EB%AA%A8%EC%9E%84%20%EC%95%88%EB%82%B4.md)
- AI 코디네이터 구상: [2026-05-30 Builders Lounge AI 코디네이터 구상](../ideas/2026-05-30%20Builders%20Lounge%20AI%20%EC%BD%94%EB%94%94%EB%84%A4%EC%9D%B4%ED%84%B0%20%EA%B5%AC%EC%83%81.md)
