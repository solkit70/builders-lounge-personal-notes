---
title: "Bila AI Context 데이터 관리 문제와 GitHub 제안 구상"
author:
  - "Changsoo Park"
created: 2026-07-29 00:00:00
tags:
  - builders-lounge
  - bila-ai
  - github
  - idea
  - proposal
links:
  - "[[Initiatives/Builders Lounge/ideas/2026-07-29 Builders Lounge 멤버 간 1대1 교류 활성화 - Bila AI 매칭 전 실천]]"
  - "[[Initiatives/Builders Lounge/README]]"
---

## 계기

2026-07-29 저녁 Startup425 AI Accelerator Demo Day에서 박세진(David Sejin Park)님과 이야기를 나누고 돌아오는 차 안에서 정리한 생각. 세진님과도 비슷한 문제의식을 나눴다.

## 지금 Bila AI가 자료를 참조하는 방식

사용자가 기록한 내용을 GitHub Repository(`github.com/solkit70/builders-lounge-personal-notes`)에 올리면, Gobi Space 서버가 이 Repository를 다운로드해 로컬에 저장하고, 거기서 AI가 참조하는 구조다.

## 문제: 멤버 매칭 기능으로 확장하면 데이터 관리가 깨진다

Bila AI의 목표 중 하나는 멤버 간 매칭 기능이다 (→ [[Initiatives/Builders Lounge/ideas/2026-07-29 Builders Lounge 멤버 간 1대1 교류 활성화 - Bila AI 매칭 전 실천|1:1 교류 활성화 아이디어]]). 이걸 하려면 각 멤버에 대한 정보가 필요하고, Product 정보는 대부분 멤버 각자의 GitHub Repository에 있다. 멤버가 공개를 허락한다면 이론적으로는 그 정보를 쓸 수 있다.

그런데 지금 방식대로라면, 그 데이터를 전부 Gobi Space 서버에 다운로드해야 사용할 수 있다. Repository가 1개일 때는 괜찮지만, 멤버 수만큼 늘어나면:

- Gobi Space 서버의 저장 용량을 많이 차지한다
- 매 동기화마다 workload(다운로드·인덱싱)가 증가한다

AI에게는 풍부하고 양질의 Context를 잘 전달하는 것이 핵심인데, 정작 그 Context가 될 데이터를 **어떻게 관리할 것인가**가 병목이 된다.

## 아이디어: GitHub에 직접 제안

이 문제를 GitHub 측에 개발 제안으로 만들어 보는 것도 괜찮을 것 같다. 두 가지 방향이 있다.

1. **소비자 의견 제안** — "이런 기능이 있으면 좋겠다"는 사용자 의견을 전달하는 형태
2. **공동 개발 제안** — Bila AI 개발팀(강민석님 등)과 함께 개발하자는 제안서 형태

## 제안의 핵심 아이디어

GitHub이 자체적으로 **멤버 매칭을 돕는 AI Agent**를 GitHub 시스템 내에서 제공하고, 이를 API로 누구나 사용할 수 있게 하면:

- Bila AI 같은 서비스가 Repository를 통째로 다운로드하지 않고도, GitHub이 이미 인덱싱한 Context에 API로 접근해 매칭 기능을 만들 수 있다
- GitHub 입장에서도 단순 소스 저장소를 넘어, **AI 시대 새로운 Builder들의 Network의 장**이 될 수 있다 — 코드를 저장하는 곳에서 Builder들이 서로를 발견하는 곳으로 확장되는 것

## Next

- [ ] 제안서 초안 작성 여부 결정 — 소비자 의견 vs 공동 개발 제안, 둘 중 어느 형태로 쓸지
- [ ] 세진님과 나눈 문제의식 구체적으로 재확인 (필요하면 후속 대화)
- [ ] GitHub에 제안하기 전, 강민석님과 이 아이디어를 먼저 공유해 Bila AI 개발 방향과 맞는지 확인
