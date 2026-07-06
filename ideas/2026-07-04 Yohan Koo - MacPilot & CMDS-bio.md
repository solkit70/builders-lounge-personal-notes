---
title: "구요한 (Yohan Koo) — MacPilot 개선 & CMDS-bio Builder 프로필"
created: 2026-07-04
status: 관찰 중
tags:
  - builders-lounge
  - builder-profile
  - cmds
  - product-candidate
links:
  - "[2026-07-04 Park Jun - Mark](<2026-07-04 Park Jun - Mark.md>)"
external:
  - "https://bio.cmdspace.work"
  - "https://github.com/johnfkoo951/cmds-bio"
  - "https://www.instagram.com/reel/DaUsYl0BjhP/?utm_source=ig_web_copy_link&igsh=NTc4MTIwNjQ2YQ=="
---

## 관련 문서

- [2026-07-04 Park Jun - Mark](<2026-07-04 Park Jun - Mark.md>)

## 인물 정보

| 항목 | 내용 |
|------|------|
| 이름 | 구요한 (Yohan Koo) |
| 소속 | CMDSPACE 대표 |
| 웹사이트 | cmdspace.work |
| 전문 분야 | AI 강의 · 임원코칭 · 지식관리 · LLM |
| Builders Lounge / Bila 멤버 | ❌ 아직 아님 (CMDS 커뮤니티 리더) |
| 첫 발견 | 2026-07-04, CMDS 커뮤니티 공유 |
| 연락 상태 | 미접촉 |

---

## Product 1 — MacPilot 개선 (원작: 박준)

> **"이동 중에 맥북을 쓸 일이 많다 — 운전, 강의, 소파에서 오케스트레이션까지"**

| 항목 | 내용 |
|------|------|
| 원작자 | 박준님 → [2026-07-04 Park Jun - Mark](<2026-07-04 Park Jun - Mark.md>) |
| 개선자 | 구요한 |
| Instagram Reel | https://www.instagram.com/reel/DaUsYl0BjhP/?utm_source=ig_web_copy_link&igsh=NTc4MTIwNjQ2YQ== |
| 플랫폼 | macOS |
| 상태 | 개인 개선 버전 (공개 여부 미확인) |

### 해결하려는 문제

맥북을 이동 중이나 비전통적 환경(운전, 강의, 소파)에서 사용할 때, 기본 키보드·트랙패드 조작만으로는 AI 에이전트 오케스트레이션 워크플로우를 유지하기 어렵다는 문제를 해결한다.

### 개선 내용

- **STT 모델 실행** — 음성 입력으로 맥북 제어
- **Raycast / Obsidian 실행** — 원터치 앱 전환
- **Cmux 윈도우/워크스페이스/탭 모니터링 관리** — 복잡한 멀티윈도우 상황 정리
- **통신 반응속도 개선** — 기존 앱 대비 빠른 응답
- **사용성 업그레이드** — 스트림덱 수준의 제어를 소프트웨어로 구현

### 주요 인사이트

스트림덱(하드웨어 입력 장치)을 별도로 구매하지 않고, 소프트웨어만으로 유사한 기능을 맥북에서 구현했다. AI 에이전트 오케스트레이션을 키보드 없이 진행하려는 워크플로우의 실용적 해법이다.

---

## Product 2 — CMDS-bio

> **"litt.ly 대신 index.html 한 장"**

| 항목 | 내용 |
|------|------|
| Product 이름 | CMDS-bio |
| 라이브 URL | https://bio.cmdspace.work |
| GitHub | https://github.com/johnfkoo951/cmds-bio (공개, 포크 가능) |
| 상태 | 본인 사용 중 + 오픈소스 공개 |
| 라이선스 | 공개 (포크 후 본인 것으로 교체 가능) |

### 해결하려는 문제

litt.ly 같은 외부 Link-in-bio 서비스에 의존하지 않고, **직접 호스팅하는 index.html 한 장**으로 모든 링크를 관리한다. 외부 서비스 종속성 제거 + 팔로워 수 자동 집계.

### 핵심 기능

- **팔로워 수 합계 자동 집계** — 여러 플랫폼의 17,000+ 팔로워를 스크립트로 자동 계산·표시
- **cmdspace.work와 상시 동기화** — 이력 정보가 메인 사이트와 항상 최신 상태 유지
- **오픈소스 + 포크 가능** — GitHub 코드 전체 공개, 본인 정보로 교체하면 바로 사용 가능

### 차별화 포인트

외부 서비스(litt.ly, linktree 등) 없이 자체 호스팅, 팔로워 수 자동 집계 스크립트가 내장되어 있어 관리 비용이 거의 없다. 오픈소스 공개로 커뮤니티 멤버들이 바로 활용 가능하다는 점에서 Builder 정신에 부합한다.

---

## Builders Lounge 연결 포인트

| BL 구상 | 구요한님의 상황 |
|---------|----------------|
| Builder가 실용 도구를 직접 만드는 공간 | MacPilot 개선 + CMDS-bio 모두 실제 본인이 쓰는 도구를 직접 개발 |
| 오픈소스 공유 문화 | CMDS-bio GitHub 공개, 누구나 포크 가능 |
| AI 에이전트 오케스트레이션 실험 | MacPilot 개선이 정확히 이 방향 |
| Bila AI 소개 연결 | CMDS 리더로서 Bila 소개 → 협력 시너지 가능 |

**주목 포인트**: 구요한님은 CMDS 리더로서 AI 강의·코칭을 하면서 동시에 본인이 직접 쓰는 도구를 만드는 "Builder + Teacher" 조합이다. Catch Up AI와 방향이 매우 가깝다.

---

## 다음 액션

- [ ] CMDS-bio GitHub 코드 검토 — 우리 용도로 활용 가능한지 파악
- [ ] bio.cmdspace.work 직접 방문 → 구조·디자인 참고
- [ ] MacPilot 개선판 Instagram reel 시청 → 실제 워크플로우 파악
- [ ] 구요한님에게 Bila / Builders Lounge 소개 기회 탐색 (CMDS 협력 각도)

---

*2026-07-04 기록. CMDS 커뮤니티 공유 내용 기반. 🤖 [Claude Code](https://claude.ai/code)로 작성.*
