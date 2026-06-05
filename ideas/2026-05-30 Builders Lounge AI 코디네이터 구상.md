---
title: "Builders Lounge AI 코디네이터 구상"
created: 2026-05-30 23:00:00
tags:
  - builders-lounge
  - gobi-space
  - ai-agent
  - community
  - idea
links:
  - "[[Initiatives/Builders Lounge/README]]"
  - "[[AI/Private Meetings/Gobi/2026-05-28 Gobi Weekly Sync]]"
---

## 개요

Builders Lounge를 GobiSpace 안에서 AI가 운영을 보조하는 커뮤니티로 만들고 싶다. CMDS x GOBI Cohort에서 이미 구현된 "기록 기반 Q&A" 모델에서 출발해, 더 나아가 멤버 간 협업을 자동으로 조율하는 **커뮤니티 코디네이터 AI**로 발전시키는 것이 목표다.

---

## 레퍼런스: CMDS x GOBI Cohort AI

GobiSpace의 CMDS Space에는 Cohort 기록이 담긴 GitHub 레포가 연결되어 있다.
멤버가 Cohort에 대해 질문하면 CMDS AI가 기록을 기반으로 답변한다.

- GobiSpace: https://www.gobispace.com/spaces/cmds-gobi-1
- BL 개인 기록 레포: https://github.com/solkit70/builders-lounge-personal-notes

**Builders Lounge도 이 구조에서 시작한다.** BL 기록 레포를 연결하면 "Builders Lounge AI"가 모임의 맥락을 이해하고 질문에 답할 수 있다.

---

## 단계별 발전 구상

### Phase 1 — 기록 기반 Q&A (출발점)

현재 CMDS AI와 동일한 구조. BL 기록 레포(GitHub)를 GobiSpace Brain에 연결하고, 멤버의 질문에 AI가 기록을 바탕으로 답한다.

- "지난 모임에서 어떤 안건이 있었나요?"
- "어떤 멤버가 랜딩 페이지 관련 Product를 만들고 있나요?"
- "다음 모임 일정은 언제인가요?"

### Phase 2 — 멤버 Product 모니터링 & 매칭

멤버들이 자신의 Product를 공유하면 (GitHub Repo, 프로젝트 문서 등) AI가 각 Product의 내용과 진행 상황을 파악한다.

**자동 매칭 시나리오:**
- 멤버 A가 "백엔드 API 연동이 막혔다"고 올리면 → 유사 경험을 가진 멤버 B에게 알림
- 멤버 C의 Product와 멤버 D의 니즈가 겹치면 → 둘을 직접 연결
- 특정 기술 스택이 겹치는 멤버끼리 → 자동 그룹핑 제안

**솔루션 전달 시나리오:**
- 이미 같은 문제를 해결한 멤버의 기록/코드가 있으면 → 그 해결책을 바로 전달

### Phase 3 — 모임 코디네이터

AI가 정기 모임의 전 과정을 자동으로 보조한다.

| 시점 | AI 역할 |
|------|---------|
| 모임 전 | 안건 정리, 참석 여부 설문, 장소/형식 공지 |
| 모임 중 | 실시간 transcript → 회의록 초안 생성 |
| 모임 후 | 회의록 배포, 결정사항 요약, 다음 모임 action item 추적 |
| 상시 | 멤버 Product 상태 모니터링, 도움 요청 감지, 매칭 제안 |

---

## 2차 모임 AI 이름 공모

2차 모임 안건에 포함됨. 후보 예시: **"Bila"** (강민석님 제안).
커뮤니티 AI 브랜딩의 시작 — 이름이 정해지면 GobiSpace Brain으로 공개 배포.

---

## 이번 주 2차 모임 준비 과정

| 날짜 | 작업 |
|------|------|
| 5/24 (일) | 김성진님 온라인 미팅 — 2차 모임 운영 방향 논의 |
| 5/24 (일) | BL 기록 저장소 정리 & GitHub push (`solkit70/builders-lounge-personal-notes`) |
| 5/28 (목) | 2차 모임 안건 확정 (아래 참조) |
| 5/28 (목) | Polly 설문 생성 → Slack #club-sg-ai 게시 |
| 5/28 (목) | GobiSpace Changbal + Global 공지 포스팅 |
| 5/30 (토) | 2차 모임 날짜 확정: 6월 9일(화) 오후 6:30, 온/오프 하이브리드 |
| 6/2 (화) | 벨뷰 시 회신: 6/9(화) City Council로 불가 → **6월 8일(월) 오후 6:30로 변경, 승인 대기** |
| 6/1 (월) | 벨뷰 시청 미팅룸 예약 예정 → 확정 후 정식 공지 |

### 확정된 2차 모임 안건

| 구분 | 담당 | 내용 |
|------|------|------|
| 발표 | 김성진님 | Brain Training Game — Vibe Coding 과정 및 인사이트 (온라인, 20~30분) |
| 발표 | 박창수 | BL GitHub 레포 소개 및 AI 활용 계획 |
| 논의 | 강민석님 제안 | GobiSpace 전용 Space 생성 여부, Builders Lounge AI 이름 공모, Agent 개발 현황 |
| 논의 | 모두 | 각자 Product 소개 및 피드백 |

---

## 핵심 비전 한 문장

> "Builders Lounge AI는 기록을 읽고 답하는 것에서 시작해, 멤버들이 서로의 성장을 가속시키는 연결 엔진이 된다."

*관련 문서: [[Initiatives/Builders Lounge/ideas/2026-05-24 Builders Lounge 2회 준비 브레인덤프]]*
*관련 문서: [[Initiatives/Builders Lounge/ideas/2026-05-24 Builders Lounge Custom Homepage 기능 구상 - ChatGPT]]*
