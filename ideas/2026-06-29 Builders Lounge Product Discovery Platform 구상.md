---
title: "Builders Lounge Product Discovery Platform 구상"
created: 2026-06-29 03:13:53
tags:
  - builders-lounge
  - initiative
  - idea
  - product-discovery
  - community
  - bila-ai-agent
source: "사용자 아이디어, 2026-06-29"
links:
  - "[README](<../README.md>)"
  - "[2026-05-24 Builders Lounge Custom Homepage 기능 구상 - ChatGPT](<2026-05-24 Builders Lounge Custom Homepage 기능 구상 - ChatGPT.md>)"
  - "[2026-05-30 Builders Lounge AI 코디네이터 구상](<2026-05-30 Builders Lounge AI 코디네이터 구상.md>)"
  - "[2026-06-29 - Weekly Progress and Planning](<../../../Roundup/2026-06-29 - Weekly Progress and Planning.md>)"
  - "[2026-06-29 - Live17 Weekly Rundown](<../../../Roundup/2026-06-29 - Live17 Weekly Rundown.md>)"
  - "[2026-06-29 - Weekly Dashboard.canvas](<../../../Roundup/2026-06-29 - Weekly Dashboard.canvas>)"
  - "[2026-06-29 Build with AI source note](<../builders/Song-Jae-hee-Build-with-AI/2026-06-29 Build with AI source note.md>)"
  - "[20260628_M1_Bila-AI-Agent](<../../../../Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/vl_worklog/20260628_M1_Bila-AI-Agent.md>)"
external:
  - "https://buildwithai.clearlyreqs.com/ko/"
  - "https://github.com/revfactory/webtoon-harness"
---

## 요약

AI가 보급되면서 직접 product, app, agent, workflow를 만드는 Builder들이 빠르게 늘어나고 있습니다. 그런데 이들이 만든 product가 소개되고, 실제 사용자에게 소비되고, 피드백을 받고, 다른 Builder와 연결되는 플랫폼은 아직 부족합니다. 이 문서는 Catch Up AI, Builders Lounge, Bila AI Agent를 연결해 **Builder들이 만든 product를 발견하고 소비하고 피드백하는 플랫폼**으로 발전시키는 초기 구상입니다.

핵심은 세 축입니다. Catch Up AI YouTube 채널은 Builder와 product를 소개하고 인터뷰하는 미디어 채널이 됩니다. Builders Lounge는 Builder들이 서로의 product를 직접 사용해 보고 feedback을 주며 networking하는 커뮤니티가 됩니다. Bila AI Agent는 온라인에서 멤버들의 product를 모니터링하고, 서로 관계되는 Builder와 Product를 매칭하는 AI coordinator가 됩니다. → **관련 맥락**: [Builders Lounge Product 소개 형식](<../README.md#Product 소개 형식>), [Bila Phase 2 구상](<2026-05-30 Builders Lounge AI 코디네이터 구상.md#Phase 2 — 멤버 Product 모니터링 & 매칭>)

## 원문 아이디어

> "AI 가 보급되면서 사람들이 무엇인가 만드는 것들이 많아 졌습니다. 바로 Builder들이 많아 지고 있는거죠. 이런 사람들이 build 한 product들이 소개되고 소비되는 플랫폼이 부족하다는 것을 느꼈습니다. 그런 플랫폼을 만들면 어떨까? 하는 생각이 들었습니다."

> "저의 Catch Up AI 유투브 채널에서는 이런 Product 들을 소개하고 Builder 분들도 직접 인터뷰 하구요. Builders Lounge 에서도 Builder 분들이 자신의 Product 를 소개하고 상대방의 Product 들을 사용해보고 feedback 을 주면서 Networking 을 하구요. 그리고 온라인에서는 Bila AI Agent 가 Builders Rounge 멤버들의 Product 들을 모니터링 하면서 서로 관계되는 Builder 와 Product들을 매칭 시켜 주는 일을 하는 겁니다."

## 문제 인식

AI 도구가 널리 보급되면서 "무언가를 만드는 사람"의 수가 늘어나고 있습니다. 예전에는 개발자, 디자이너, 창업자처럼 특정 역량을 가진 사람이 product를 만들었다면, 지금은 AI를 활용해 혼자서도 app, agent, workflow, content tool, automation을 만들어 공개하는 사람이 늘고 있습니다. 즉 Builder의 수가 늘어나고 있고, Builders Lounge가 다루려는 대상도 점점 넓어지고 있습니다.

하지만 product를 만드는 속도에 비해, 그 product들이 제대로 소개되고 소비되는 경로는 부족합니다. SNS에는 개별 홍보 글이 흩어지고, Slack이나 GobiSpace에는 대화가 흘러가며, YouTube에는 개별 creator의 콘텐츠가 존재하지만, Builder와 Product를 지속적으로 발견하고 비교하고 사용해 보고 피드백하는 구조는 아직 약합니다. 그래서 Builders Lounge는 단순 모임을 넘어, AI 시대 Builder product discovery와 feedback platform으로 발전할 수 있습니다.

## 왜 "내 주변 Builder"인가 — AI 시대와 우리만의 정보

이 구상의 방향은 유튜브·SNS의 일반적인 AI 콘텐츠 흐름과 의도적으로 다릅니다. 대부분의 AI 콘텐츠는 OpenAI, Anthropic, MS, Google, Meta처럼 이미 Public하게 홍보된 대기업 기술이나 소식을 전달합니다. 이 구상은 그 반대 방향을 택합니다. 즉 **내 주변에서 실제로 벌어지고 있는 AI 관련 기술과 노력**을 주변 사람들, 나아가 더 넓은 곳에 알리는 것입니다.

> "저는 그렇지 않고 내 주변에서 벌어지는 AI 관련 기술을 내 주변사람들과 더 나아가서 좀 더 넓은 곳에 그 기술이나 노력들을 알리고 싶습니다. 그럼으로서 실제로 내 주변에 AI 에 관심이 많고 실제 무엇인가를 만드는 Builder 들이 실제로 도움을 주고 받고 더 나아가 자신들의 Product 들을 사용해 협업하거나 프로모션에 서로 도움이 되는 그런 활동을 하고 싶습니다."

이 방향이 단순한 취향이 아니라 **AI 시대에 더 적합한 전략**이라고 보는 이유는 정보의 가치 구조가 바뀌었기 때문입니다. Public한 정보를 AI에게 Context로 줘봤자, 다른 모든 사람도 동일한 정보로 동일한 답을 얻을 수 있으므로 차별화된 가치가 생기지 않습니다. 반면 **나만의 정보, 우리 그룹이나 회사만의 정보**가 Context가 되면, AI는 다른 누구에게도 주지 못했던 더 유니크하고 가치 있는 답을 줄 수 있습니다.

> "AI 시대에는 Public 한 정보 보다는 나만의 정보 혹은 우리 그룹이나 회사만의 정보가 더 가치 있어 질 것입니다. Public 정보를 AI 에게 Context 로 주어 봤자 다른 사람들도 다 얻는 그런 결과만 얻을 겁니다. 하지만 나만의 정보, 우리 그룹이나 우리 회사만의 정보가 Context 가 되면 AI 는 다른 사람들에게 답하지 않았던 더 유니크한 그래서 더 가치가 있는 대답을 줄 것입니다."

이 원칙은 개인 차원에만 머물지 않습니다. Builders Lounge가 하려는 일은 바로 이 원칙을 **그룹 차원**으로 확장하는 것입니다. 여기서 "주변"은 지역이나 직종으로 좁게 한정할 필요가 없습니다. 오프라인 지역 모임에서 시작했지만, 네트워킹으로 연결된 사람이라면 누구든 이 순환에 들어올 수 있습니다.

> "저는 개인적인 차원에서도 이런 작업을 하지만 제 주위의 사람들과 그룹 차원에서 이런 일을 하고 싶습니다. 주변이라고 하면 굳이 지역이나 직종 등에 국한 시킬 필요가 없다고 생각합니다. 같이 네트워킹을 맺게 된 사람들 사이의 AI Product Build 정보를 공유하면서 도움을 주고 받고 그런 과정과 내용이 기록 되고 그 기록이 다시 AI 에게로 가서 그룹 멤버와 그룹의 발전을 꾀하고 싶습니다."

정리하면 이 구상이 만들려는 것은 단순한 "Product 소개 채널"이 아니라, **공유 → 협업/피드백/프로모션 상호 지원 → 기록 → 그 기록이 다시 AI Context가 되어 그룹과 멤버 모두를 강하게 만드는 순환**입니다. 이 순환은 이번 주 발견한 Product Discovery Platform의 세 축(Catch Up AI·Builders Lounge·Bila AI Agent)과 정확히 맞물립니다. Catch Up AI는 이 "우리만의 정보"를 밖으로 알리는 확성기이고, Builders Lounge는 그 정보가 실제 협업·피드백으로 전환되는 현장이며, Bila AI Agent는 쌓인 기록을 Context로 삼아 그룹 차원의 유니크한 가치를 만들어내는 엔진입니다.

## 플랫폼 비전

이 구상에서 플랫폼은 하나의 웹사이트만을 의미하지 않습니다. YouTube, 오프라인/온라인 모임, GobiSpace, GitHub 기록 저장소, Bila AI Agent가 함께 작동하는 **분산형 product discovery network**에 가깝습니다. 각 채널은 역할이 다르고, 서로 보완됩니다.

| 축 | 역할 | 구체적 활동 |
| --- | --- | --- |
| Catch Up AI YouTube | Product 소개와 Builder 인터뷰 | Builder story, product demo, 사용 후기, launch story 영상화 |
| Builders Lounge | 실제 사용과 피드백 커뮤니티 | Product demo, hands-on, 첫 사용자 feedback, networking |
| GobiSpace / 기록 저장소 | Product 정보와 피드백 기록 | Product profile, feedback request, review, meeting transcript 축적 |
| Bila AI Agent | 온라인 매칭과 추천 | Product 모니터링, 관련 Builder 연결, 니즈 기반 product 추천 |

이 구조는 기존 Custom Homepage 아이디어의 확장입니다. 기존 구상은 Product Showcase, Feedback Request, Review Template을 중심으로 Builders Lounge 내부 운영 기능을 생각했습니다. 이번 아이디어는 거기에 **외부 소개 채널(Catch Up AI)**과 **AI 매칭 layer(Bila)**를 결합해, product가 커뮤니티 내부에서만 머물지 않고 더 넓게 발견되도록 만드는 방향입니다. → **관련 구상**: [Custom Homepage 요약](<2026-05-24 Builders Lounge Custom Homepage 기능 구상 - ChatGPT.md#요약>)

## 작동 시나리오

### 1. Builder가 Product를 등록합니다

Builder는 Builders Lounge에 자신의 product를 소개합니다. 최소 정보는 product 이름, URL, 해결하려는 문제, 현재 상태, 사용 방법, 받고 싶은 feedback입니다. 기존 README의 Product 소개 형식을 확장해 사용하면 됩니다. → **관련 형식**: [Product 소개 형식](<../README.md#Product 소개 형식>)

### 2. Catch Up AI가 Product와 Builder를 소개합니다

Catch Up AI YouTube 채널은 selected product를 소개하고, Builder를 직접 인터뷰합니다. 단순 홍보가 아니라 "무엇을 만들었는가", "왜 만들었는가", "AI를 어떻게 활용했는가", "지금 어떤 feedback이 필요한가"를 다룹니다. 이 영상은 product discovery 콘텐츠이자, Builder의 성장 기록이 됩니다.

### 3. Builders Lounge 멤버들이 실제로 사용하고 Feedback을 줍니다

멤버들은 제품을 직접 써보고 feedback을 남깁니다. 첫 화면이 이해되는지, 실제로 사용할 이유가 있는지, AI 기능이 차별화되어 보이는지, onboarding이 막히는지 같은 질문을 Review Template으로 구조화합니다. 이 단계에서 Builders Lounge는 "서로의 첫 사용자"가 됩니다.

### 4. Bila AI Agent가 Product와 Builder를 매칭합니다

Bila는 GobiSpace, GitHub 기록 저장소, Product profile, feedback 기록을 읽고 멤버들의 product와 니즈를 모니터링합니다. 예를 들어 어떤 Builder가 go-to-market feedback이 필요하면 sales/business development 경험이 있는 멤버를 연결하고, 어떤 product가 특정 AI agent workflow를 쓰고 있으면 유사한 문제를 해결한 멤버를 추천합니다. 이 구상은 기존 Bila Phase 2인 "멤버 Product 모니터링 & 매칭"과 직접 연결됩니다. → **관련 구상**: [Bila Product 모니터링 & 매칭](<2026-05-30 Builders Lounge AI 코디네이터 구상.md#Phase 2 — 멤버 Product 모니터링 & 매칭>)

## 핵심 구성 요소

### Product Profile

각 product의 기본 카드입니다. 이름, URL, 한 줄 소개, target user, 현재 상태, demo 방법, feedback 요청, Builder profile을 포함합니다. 이 정보가 있어야 YouTube 소개, 모임 demo, Bila matching이 모두 같은 source를 바라볼 수 있습니다.

### Builder Interview

Catch Up AI 콘텐츠로 발전시키기 위한 인터뷰 포맷입니다. Builder가 어떤 문제를 보았고, 왜 만들었고, AI를 어떻게 사용했고, 지금 누구의 feedback이 필요한지를 묻습니다. 인터뷰는 product 홍보뿐 아니라 AI 시대 Builder 문화 자체를 기록하는 역할을 합니다.

### Feedback Loop

Product를 소개하고 끝내는 것이 아니라, 다른 멤버가 써보고 feedback을 남기고, Builder가 수정하고, 그 변화가 다시 기록되는 loop입니다. 이 loop가 쌓이면 Product Journey Log가 되고, Builders Lounge의 collective intelligence가 됩니다.

### Bila Matching Layer

Bila는 Product Profile과 Feedback Loop 위에서 작동합니다. 수동 검색이나 우연한 만남에만 의존하지 않고, "이 Builder는 이 product를 써보면 좋겠습니다", "이 product는 이 멤버의 니즈와 맞습니다", "이 문제는 이전에 다른 멤버가 해결했습니다" 같은 연결을 제안합니다.

## 초기 MVP 아이디어

아직은 아이디어 단계이므로, 처음부터 별도 플랫폼을 크게 만들기보다 기존 자산을 연결해 작게 시작하는 것이 좋습니다.

| 단계 | MVP | 설명 |
| --- | --- | --- |
| M0 | Product 목록 정리 | README의 멤버 Product 목록을 확장해 Product Profile 초안 작성 |
| M1 | Product 소개 템플릿 | Builder가 직접 채울 수 있는 표준 Product Profile 템플릿 작성 |
| M2 | Catch Up AI 소개 코너 | 주 1개 또는 월 2개 product를 YouTube/Live에서 소개 |
| M3 | Feedback Request 운영 | Builders Lounge에서 "이번 주 feedback 요청 product"를 선정 |
| M4 | Bila 매칭 실험 | Bila가 Product Profile을 읽고 관련 멤버/니즈를 추천하는지 테스트 |

## 관찰 사례 Inbox

Product Discovery Platform 구상을 보강하는 관찰 사례와 실험 후보를 함께 관리합니다. Build with AI는 이번 주 Live #17 실험으로 전환했고, Webtoon Harness는 아직 구체 task가 아닌 외부 Product 관찰 사례로 유지합니다.

### 2026-07-02 Nate Cho — Job Search Co-pilot (창발 멤버, Bila 합류 후보)

Nate Cho는 창발 멤버로 Claude Cowork plugin 기반의 취업 준비 도구 **Job Search Co-pilot**을 직접 만들어 Slack에 공유했습니다. 핵심 원칙은 "don't make hiring teams connect the dots for you"입니다. 지원 수를 늘리는 것이 아니라, 역할 분석·포지셔닝 thesis 구성·인터뷰 prep·debrief까지 구조적으로 돕는 도구입니다. Free, MIT 오픈소스, 초기 테스트 단계입니다.

**왜 Bila과 맞는가**: Product를 만들어 실제 사용자에게 테스트시키길 원하는 상황이 Builders Lounge가 하려는 일과 정확히 일치합니다. Bila 멤버 중 구직 중인 분이 생기면 즉시 실제 사용 피드백을 줄 수 있는 첫 번째 사례가 될 수 있습니다.

→ **상세 프로필**: [2026-07-02 Nate Cho - Job Search Co-pilot](<2026-07-02 Nate Cho - Job Search Co-pilot.md>)
**GitHub**: https://github.com/nathanscho/jobsearch-copilot
**LinkedIn 글**: https://www.linkedin.com/posts/nathanscho_interviewing-communication-productmanagement-share-7478447354132525056-OR-g/

**관심 포인트**:
- 다음 Bila 모임 Product 소개 세션에 초대 검토
- Catch Up AI 인터뷰 후보: 취업 준비 + AI 도구 활용 각도
- Bila 내 구직 중인 멤버 생기면 바로 연결
- Bila가 구직 중 멤버에게 이 Product 추천하는 시나리오 검토

### 2026-06-28 송재희님 Build with AI 글

> "강의가 끝나고 한 달이 지나면, 거의 모든 프로젝트가 멈춥니다."

> "\"만든다\"와 \"서비스가 된다\" 사이에는 두꺼운 벽이 하나 있습니다. 이 벽은 코딩 실력으로 넘는 게 아닙니다."

송재희님의 글은 Product Discovery Platform의 "Builder가 만든 product를 발견한다"는 방향을 넘어, 데모 이후 실제 서비스로 넘어가지 못하는 병목을 다룹니다. 특히 비개발자 Builder가 먼저 배워야 할 것은 코딩 자체가 아니라 문제 구조화, 대상 사용자 정의, AI 판단과 사람 검증의 경계 설정, 서비스 기준 통과 여부라는 관점이 중요합니다. 이 인사이트는 이번 주 Live #17에서 Build with AI 자료를 공부하고 영상 콘텐츠 angle을 잡는 실험으로 전환합니다. → [2026-06-29 Build with AI source note](<../builders/Song-Jae-hee-Build-with-AI/2026-06-29 Build with AI source note.md>)

**관심 포인트**:
- 데모 이후 서비스화가 멈추는 이유를 Builder 교육과 Product Discovery 관점에서 공부
- Build with AI 12부작 가이드를 VibeLearn AI, Vibe Guiding, Builders Lounge Product Profile과 비교
- 필요하면 송재희님 인터뷰 또는 Builders Lounge 발표 요청 검토
- 이번 주 Live #17 실험으로 핵심 질문과 첫 영상 angle 정리

### Webtoon Harness 외부 Product 사례

> "웹툰 제작용 하네스를 무료 공개합니다."

> "27개의 AI 에이전트가 웹툰 소재 조사부터 시나리오 작성, 웹툰 제작, 검수까지 전 과정을 담당합니다."

Webtoon Harness는 모르는 분의 외부 product이지만, AI agent workflow를 product화하고 공개했다는 점에서 Product Discovery Platform의 좋은 관찰 사례입니다. 한 줄 prompt에서 조사, 시나리오, 제작, 검수까지 이어지는 구조는 VibeLearn AI의 학습 workflow와도 닮아 있어, 향후 "AI agent harness" 또는 "workflow product" 유형으로 분석할 가치가 있습니다.

**원문 링크**: https://github.com/revfactory/webtoon-harness

**이미지 자료**:
- ![WebtoonHarness01](<images/WebtoonHarness01.jpg>)
- ![WebtoonHarness02](<images/WebtoonHarness02.jpg>)
- ![WebtoonHarness03](<images/WebtoonHarness03.jpg>)
- ![WebtoonHarness04](<images/WebtoonHarness04.jpg>)

### 2026-07-03 김성수 — HebronGuide (Bila 멤버, 운영 중인 Product)

김성수님은 Bila 멤버로 재외 한인 이주자를 위한 커뮤니티 플랫폼 **HebronGuide**를 직접 개발·운영 중입니다. 현재 75개 도시 커버, 한인 교회·비즈니스 디렉토리 중심입니다. 이메일로 직접 공유해 왔습니다.

**왜 Bila과 맞는가**: 장기간 직접 개발·운영 중인 실제 Builder이며, 해외 한인 타겟 제품을 Bila 멤버들에게 소개하고 실제 피드백을 받아볼 수 있는 Product Discovery 첫 번째 실험 후보입니다.

→ **상세 프로필**: [2026-07-03 Sung Soo Kim - HebronGuide](<2026-07-03 Sung Soo Kim - HebronGuide.md>)
**웹사이트**: https://www.hebronguide.com

**관심 포인트**:
- Product 구조가 VibeLearn AI와 비슷한지 비교
- Catch Up AI에서 외부 Builder/Product 사례로 소개 가능성 검토
- Builders Lounge에서 "서로 모르는 Builder의 product도 발견하고 연결하는 플랫폼" 필요성을 보여주는 사례로 활용
- 단, 현재는 구체 task가 아니라 콘텐츠/학습 후보로만 보관

## Product 소개 템플릿 초안

```text
Product 이름:
Builder:
URL / GitHub:
현재 상태: idea / prototype / beta / live / GTM
한 줄 소개:
해결하려는 문제:
대상 사용자:
AI 활용 방식:
Demo 방법:
지금 가장 받고 싶은 feedback:
도움이 필요한 영역:
관련 멤버 / 관련 product:
Catch Up AI 소개 가능 여부:
공개 가능 범위:
```

## Bila에게 맡길 수 있는 일

| 역할 | 설명 |
| --- | --- |
| Product index 관리 | Builders Lounge 멤버 product 목록을 읽고 최신 상태 요약 |
| Feedback request 감지 | 누가 어떤 feedback을 요청하는지 찾아서 정리 |
| Builder matching | 비슷한 문제, 기술 stack, target user를 가진 멤버 연결 |
| Product recommendation | 특정 니즈를 가진 멤버에게 관련 product 추천 |
| Interview prep | Catch Up AI 인터뷰 질문 초안 작성 |
| Demo Day prep | 다음 모임에서 소개할 product와 순서 제안 |

## 아직 열려 있는 질문

- 이 플랫폼의 첫 사용자는 Builders Lounge 멤버인가, Catch Up AI 시청자인가, 아니면 둘 다인가?
- Product Profile은 GobiSpace post로 시작할 것인가, GitHub markdown으로 시작할 것인가, Custom Homepage로 바로 갈 것인가?
- Catch Up AI에서 소개할 product 선정 기준은 무엇인가?
- Builder가 공개를 원하지 않는 정보와 공개 가능한 정보를 어떻게 나눌 것인가?
- Bila AI Agent가 product matching을 하려면 어떤 데이터 필드가 반드시 필요한가?
- Feedback은 공개 댓글로 둘 것인가, 멤버 전용 기록으로 둘 것인가?
- "소비되는 플랫폼"이라는 표현에서 소비는 사용, 구매, 구독, feedback, partnership 중 어디까지 포함할 것인가?

## Weekly Reminder 연결

이 구상은 별도 아이디어로만 보관하지 않고 2026-06-29 주간 일정 관리에 상시 reminder로 연결합니다. Catch Up AI Product 소개, Builders Lounge Product demo/feedback, Bila AI Agent M2, 7/6 커피챗, Product Profile 작성 같은 관련 작업을 시작할 때마다 이 문서를 열고 새로운 인사이트를 보강합니다. → **Weekly 관리**: [상시 Reminder](<../../../Roundup/2026-06-29 - Weekly Progress and Planning.md#7. 상시 Reminder>), [Live #17 방송 소재](<../../../Roundup/2026-06-29 - Live17 Weekly Rundown.md#② Builders Lounge Product Discovery Platform 구상>), [Weekly Dashboard](<../../../Roundup/2026-06-29 - Weekly Dashboard.canvas>)

특히 Product 소개 후보, Builder 인터뷰 질문, Product Profile 필드, Bila가 모니터링해야 할 데이터, 실제 feedback loop 운영 방식은 작업이 진행될수록 계속 구체화합니다. Build with AI 실험에서 나온 "데모 → 서비스" 병목과 비개발자 Builder의 문제 구조화 관점도 이 구상에 반영합니다. Weekly Roundup을 작성할 때도 이번 주 관련 작업에서 이 문서에 반영할 내용이 있었는지 확인하고, 다음 주 일정으로 이어갈지 결정합니다.

## 다음 액션

- [ ] 기존 멤버 Product 목록을 Product Profile 초안으로 확장합니다.
- [ ] Product 소개 템플릿을 Builders Lounge README 또는 별도 template 문서로 분리할지 결정합니다.
- [ ] Catch Up AI에서 첫 번째로 소개할 Product 후보를 정합니다.
- [ ] Build with AI Live #17 실험 후 영상 콘텐츠 angle과 Product Discovery Platform 연결점을 정리합니다.
- [ ] Bila AI Agent M2에서 Product Profile을 데이터 소스로 읽을 수 있는지 확인합니다.
- [ ] 다음 Builders Lounge 모임 또는 7/6 커피챗에서 "Builder product discovery platform" 아이디어를 공유할지 검토합니다.
- [ ] Custom Homepage 구상과 이 문서를 비교해 겹치는 기능과 새로 추가된 기능을 정리합니다.

## 한 문장 비전

> Builders Lounge는 AI 시대에 늘어나는 Builder들의 product가 발견되고, 실제로 사용되고, 피드백을 받고, AI가 적절한 사람과 product를 연결해 주는 product discovery community로 발전할 수 있습니다.

## 인포그래픽 자료 (7/6 커피챗 공유용)

이 구상의 3축 구조(Catch Up AI · Builders Lounge · Bila AI Agent)를 여러 AI 도구로 인포그래픽화한 자료입니다. 7/6 한인 상공회의소 커피챗에서 말로 설명할 때 곁들이는 시각 보조 자료로 씁니다.

### 최초 버전 (OpenAI gpt-image-2)

![Builders Lounge Product Discovery 3축 구조 — Catch Up AI · Builders Lounge · Bila AI Agent](images/2026-07-06%20BL%20Product%20Discovery%20-%20KACC%20Coffeechat_01.png)

### ChatGPT 버전

![Builders Lounge Product Discovery 인포그래픽 - ChatGPT (1/2)](images/2026-07-06%20BL%20Product%20Discovery%20-%20KACC%20Coffeechat_ChatGPT01.png)

![Builders Lounge Product Discovery 인포그래픽 - ChatGPT (2/2)](images/2026-07-06%20BL%20Product%20Discovery%20-%20KACC%20Coffeechat_ChatGPT02.png)

### Claude Fable 5 버전

![Builders Lounge Product Discovery 인포그래픽 - Claude Fable 5 (1/2)](images/2026-07-06%20BL%20Product%20Discovery%20-%20KACC%20Coffeechat_Fable5_01.png)

![Builders Lounge Product Discovery 인포그래픽 - Claude Fable 5 (2/2)](images/2026-07-06%20BL%20Product%20Discovery%20-%20KACC%20Coffeechat_Fable5_02.png)

### Gemini 버전

![Builders Lounge Product Discovery 인포그래픽 - Gemini](images/2026-07-06%20BL%20Product%20Discovery%20-%20KACC%20Coffeechat_Gemini.png)
