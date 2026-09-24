---
title: "Builders Lounge 5차 모임 정리"
source: "C:/Users/dougg/Videos/Youtube/2026/Builders_Lounge/20260922_BL_5th/0923_BL5th_SMS_SpeedUp.mp4"
created: 2026-09-24 14:45:00
event_date: 2026-09-16
location: "Bellevue City Hall Room 1E-109 (온/오프 하이브리드)"
attendees_offline:
  - "Minsuk Kang (강민석)"
  - "조윤상"
  - "Changsoo Park (박창수)"
attendees_online:
  - "손민수"
  - "김진영"
  - "김성진"
tags:
  - builders-lounge
  - meeting
  - multi-agent
  - agentic-ai
  - bila-ai
sources:
  - "../README.md"
  - "../newsletters/2026-09-07 Builders Lounge 뉴스레터 - 5차 모임 확정 안내.md"
---

## 요약

2026년 9월 16일 Builders Lounge 5차 모임은 **「만들면서 부딪힌 것들이 결국 업계가 말하는 구조와 같아지더라」** 는 이야기가 중심이었다. 메인 스피커 **손민수** 님은 4차에서 보여 준 시스템 장애 대응 에이전트를 **멀티 에이전트로 다시 구현하면서 겪은 시행착오**를 36분에 걸쳐 풀었고, 마지막에 실제로 돌아가는 시스템을 라이브로 시연했다.

발표의 힘은 성공담이 아니라 **실패의 순서**에 있었다. 중복 호출로 하루에 100만 토큰을 태우고, 회사 토큰은 물론 개인 토큰까지 날린 사고에서 AI Gateway 가 나왔다. 무한 반복에서 TimeoutWatcher 가, 상태가 꼬이는 문제에서 State Machine 이, 에이전트를 셀 수 없다는 문제에서 객체화가 나왔다. 그렇게 하나씩 고쳐 놓고 보니 **Anthropic 이 권하는 Agentic 아키텍처와 거의 같았다.**

> "결국은 이게 업계에서 말하는 것도 얘네들이 무슨 막 Scientist가 딱 개발하는 게 아니라 다들 비슷하게 이렇게 시행착오를 거치면서 필요한 애들을 다 적용시키다보니까 그래서 결국은 이제 업계에서 말하는 그런 것처럼 되더라."
> — 손민수, [[Ingest/Transcripts/Builders_Lounge/2026-09-16 Builders Lounge 5th Meeting - 손민수 Multi-Agent AI - transcript#Transcript|#194~195]]

또 하나 이날의 소득은 **AI와 어디까지 함께 갈 수 있는가**에 대한 현장 감각이었다. 손민수 님은 아키텍처를 미리 설계하지 않고 AI와 대화하면서 키웠다고 했지만, 동시에 선을 그었다.

> "2026년 현재는 AI들이 이런 아키텍처까지 결정할 정도로 똑똑하지는 않다… 그냥 사용자의 수준에 맞춰가지고 주는 것 같습니다. 그래가지고 제가 느끼는 게 야 그래도 아직은 사람이 필요하구나. 이 사람이 계속 조율을 해야지 AI에게 모든 것을 맡겨 놓으면 절대 안 된다."
> — 손민수, [[Ingest/Transcripts/Builders_Lounge/2026-09-16 Builders Lounge 5th Meeting - 손민수 Multi-Agent AI - transcript#Transcript|#132~136]]

## 모임 정보

| 항목 | 내용 |
|---|---|
| 일시 | **2026년 9월 16일 (수) 19:00** |
| 장소 | **Bellevue City Hall Room 1E-109** · 온/오프 하이브리드 |
| 참석 | **총 6명** — 오프라인 3, 온라인 3 |
| 오프라인 | **강민석 · 조윤상 · 박창수** |
| 온라인 | **손민수 · 김진영 · 김성진** |
| 발표 자료 | [손민수 님 슬라이드 34장 (HTML)](../assets/presentations/2026-09-16%20손민수%20-%20Multi-Agent%20AI%20시스템%20(5차%20모임%20발표자료).html) |
| 전사본 | [[Ingest/Transcripts/Builders_Lounge/2026-09-16 Builders Lounge 5th Meeting - 손민수 Multi-Agent AI - transcript\|한국어·영어 279문장]] |

> 📌 **조윤상 님은 이날이 첫 참석**이었다. 9/11 KSC·총영사관 분기 모임에서 박창수와 처음 만나 *"말씀하신 모임에도 참석하고 싶구요"* 라고 한 지 닷새 만이고, 9/15 바이브 코딩 1:1 온보딩 바로 다음 날이다. 30여 분 자리를 지키다 바쁜 일로 먼저 가셨고, 이튿날 GOBI Space 의 Builders Lounge 채널에 가입해 인사글을 남겼다 → [[Initiatives/VibeCoding-Onboarding/participants/조윤상님 (Shoreline)/README\|조윤상 님 기록]]

## 순서

| | 발표 | 상태 |
|---|---|---|
| **[Main Speaker]** | **손민수 — Multi-Agent AI 시스템: 시스템 장애 대응 자동화를 위한 아키텍처 심층 분석** (36:51) | ✅ 영상 자막 작업 완료 (영어 자막) |
| **[발표]** | **김진영** | ⏳ **영상 편집 대기** — 손민수 님 영상 작업이 끝난 뒤 진행 |
| **[10분 발표]** | **박창수 — AI와 함께 몰락해 가는 유튜브 채널을 살린 과정** | 데이터 분석 파이프라인과 회생 전략 공유 |

## 손민수 발표 — 무엇을 다뤘나

발표는 10개 절로 구성됐다. 슬라이드 34장.

| # | 주제 | 핵심 |
|---|---|---|
| 1 | 왜 Multi-Agent인가 | 단일 LLM 은 컨텍스트가 터지고, 툴이 과하게 붙고, 검증이 안 된다 |
| 2 | 핵심 아키텍처 | Brain(오케스트레이터) · Judge · Investigation · Specialist · Airman(UI), 그리고 **Agent Bus** |
| 3 | Agent 구현 | ReAct 루프 — Thought → Action → Observation → Loop. Confidence 가 0 에서 0.92 로 올라가면 조사 완료 |
| 4 | Tool Use | SSH · Kubernetes · GitHub · newrelic. **동적 디스커버리** — 하드코딩이 아니라 등록 방식이라 Agent 를 추가해도 Judge 코드를 안 고친다 |
| 5 | 비용 최적화 | **AI Gateway** · 시그니처 기반 인시던트 중복 제거 |
| 6 | Stateful/Stateless 분리 | **100 TargetAgents(가벼운 상태 객체) + 7 LLM Workers(공유 compute) = 107개** (기존 200개) |
| 7 | Harness Engineering | State Machine · Timeout · Rate Limit · CoolDown · **Kill Switch** · State History |
| 8 | AgentGroup 객체화 | 정확한 에이전트 수 추적 · 부모 단위 제어 · 스케일 판단 |
| 9 | 시행착오 | Python → Go 전환, 업계 패턴으로의 자연 수렴 |
| 10 | 라이브 데모 & Q&A | 스트레스 테스트로 메모리를 올리고 실제 탐지·조치까지 시연 |

### 기억에 남는 숫자와 장면

- **하루 100만 토큰 소진** — 시뮬레이션으로 같은 장애를 반복시키자 에이전트들이 매번 LLM 을 때렸다. 이미 조사 중인 인시던트를 스킵하게 하자 **토큰 사용량이 20배 이상 감소**했다 (#86~91)
- **200개 → 107개** — 타겟마다 에이전트를 하나씩 붙이자 응답이 느려졌다. Stateful 100개 + Stateless Worker 7개로 나누니 **타겟이 1,000개로 늘어도 Pool 은 안 늘어난다** (#107~123)
- **ChatGPT Mini 로 충분했다** — 고도의 추론이 아니라 오퍼레이션 추론이라 미니 모델로 되고, 값도 쌌다 (#198~199)
- **Python 으로는 안 된다** — 에이전트가 100·1,000·10,000 개로 가면 Python 은 프로세스마다 Redis 가 필요하다. Go 는 **goroutine** 으로 Redis 없이 수백 개를 동시에 돌린다 (#183~188)
- **라이브 데모** — 메모리를 97% 까지 올리자 AI 가 60% 확률로 원인을 지목했고, 심어 둔 프로세스를 정확히 찾아냈다. Approve → Execute 로 조치하자 메모리가 내려갔다 (#225~231)

### 구글 검색을 2년째 안 쓴다

Qdrant 를 어떻게 골랐느냐는 김진영 님의 질문에 나온 답이 이날 가장 많이 회자될 대목이다.

> "제가 구글 서치를 사용 안 한 지가 지금 거의 한 2년이 돼가고 있거든요… 그 대신에 이제 어떻게 물어보냐면은 이 AI가 과거에 학습된 모델일 수도 있잖아요 그래서 항상 검색을 하고 알려달라 이렇게 물어보거든요."
> — 손민수, [[Ingest/Transcripts/Builders_Lounge/2026-09-16 Builders Lounge 5th Meeting - 손민수 Multi-Agent AI - transcript#Transcript|#76~78]]

여기에 **AI 교차 검증**이 붙는다. KIRO(AWS)·Claude·ChatGPT 를 오가며 *"야 Claude 가 Qdrant 쓰려는데 맞냐"* 하고 되묻는 방식이다 (#79~83).

## Q&A — 레드팀으로 써볼 수 있나

발표 뒤 토론은 **이 시스템을 공격 쪽으로 돌릴 수 있는가**로 흘렀다. 강민석 님의 제안에서 시작했다.

> "되게 좋은 시스템을 하나 만드신 것 같은데 이걸로 Red Teaming 하는 쪽으로도 써볼 수 있을까요? 그러니까 해킹하는 쪽으로 써볼 수도 있을까요?"
> — 강민석, [[Ingest/Transcripts/Builders_Lounge/2026-09-16 Builders Lounge 5th Meeting - 손민수 Multi-Agent AI - transcript#Transcript|#238]]

손민수 님은 며칠 전 Bay Area 에서 받은 Security AI Cyber 교육을 들며 답했다 — *"AI 공격이 들어오기 때문에 어차피 공격을 막으려면 우리가 AI를 공부해야 되는 거는 100%다"* (#241). 그리고 스트레스 테스트로 일부러 망가뜨린 뒤 **블루팀 에이전트가 잡아내는지 보는 방식**으로 충분히 쓸 수 있다고 했다 (#243).

박창수는 방향을 뒤집었다.

> "공격하는 시스템도 방어하는 것보다 저는 더 중요할 것 같아요… 방어는 AI한테 아무리 물어보면 하는 데까지는 하고 어디까지 믿어야 될지를 모른단 말이죠. 그래서 공격을 해줬으면 좋겠다."
> — 박창수, [[Ingest/Transcripts/Builders_Lounge/2026-09-16 Builders Lounge 5th Meeting - 손민수 Multi-Agent AI - transcript#Transcript|#246~247]]

김진영 님은 **장애는 과거 패턴만 반복되지 않는다**는 점을 짚으며 Chaos Monkey 를 꺼냈고 (#259~261), 이 대화에서 **Evaluate 기능**(지금은 CPU·메모리·디스크 3종만 스트레스 테스트)을 Red Teaming 으로 얻은 패턴으로 넓히자는 아이디어가 나왔다 (#263~267).

마지막은 사이버 시큐리티 전망으로 닫혔다 — 강남언니 유출 사례, 젠슨 황의 *"AI 다음은 사이버 시큐리티"* 발언, 그리고 **블루팀 수요가 급증할 것이고 결국 AI 로 AI 를 막게 될 것**이라는 이야기 (#269~275).

## 이 프로젝트의 현재 상태

> "사실은 오늘이 어쨌든 제가 이 프로젝트는 마지막에 될 것 같고요. 왜냐하면 거의 MVP는 끝났고 이제 이걸 쓰냐 마느냐는 사실은 지금 이제 회사에서 논의 중입니다. 왜냐하면 사람들이 하도 그 뉴스에서 AI가 위험하다는 얘기를 확 돌아가지고."
> — 손민수, [[Ingest/Transcripts/Builders_Lounge/2026-09-16 Builders Lounge 5th Meeting - 손민수 Multi-Agent AI - transcript#Transcript|#235~236]]

**MVP 는 완료, 사내 도입 여부는 논의 중.** 향후 계획이던 자동 리메디에이션은 *"거의 Human In The Loop 선에서 끝날 것 같다"* 고 했다 (#208~209). 다음 모임에서는 **다른 프로젝트**를 소개하겠다고 예고했다 (#237).

## 후속

- [x] 손민수 발표 영상 — **영어 자막 작업 완료** (2026-09-24). 한국어·영어 SRT/VTT 포함
- [ ] **김진영 님 발표 영상 편집** — 손민수 님 영상 작업 완료 후 진행 (2026-09-24 사용자 결정)
- [ ] 편집 완료된 영상 공개 → 뉴스레터·채널 안내
- [ ] 다음 모임: **송재희 님 온라인 특강** (일정·주제 미정)

## 관련

- 모임 개요 → [[Initiatives/Builders Lounge/README\|Builders Lounge README]]
- 5차 모임 사전 안내 → [[Initiatives/Builders Lounge/newsletters/2026-09-07 Builders Lounge 뉴스레터 - 5차 모임 확정 안내\|9/7 뉴스레터]]
- 4차 모임(손민수 님 첫 발표 「AI들이 서로 대화하더니 서버를 고쳤습니다」) → [[Initiatives/Builders Lounge/videos/2026-08-06 Builders Lounge 4차 모임 정리\|4차 모임 정리]]
- 전체 FAQ → [[Initiatives/Builders Lounge/videos/Builders Lounge 모임 전체 FAQ (1~5차)\|모임 전체 FAQ]]
