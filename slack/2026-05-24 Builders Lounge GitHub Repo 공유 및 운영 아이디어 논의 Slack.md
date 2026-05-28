---
title: "Builders Lounge GitHub Repo 공유 및 운영 아이디어 논의 Slack"
source: "Changbal Slack, 2026-05-24~2026-05-25"
author:
  - "Changsoo Park"
  - "Sung-Jin Kim"
  - "MinSuk Kang"
created: 2026-05-28 03:00:00
tags:
  - builders-lounge
  - changbal
  - slack
  - github
  - gobi-space
  - autoresearch
---

## 요약

2026년 5월 24일(일) Changsoo Park이 Builders Lounge GitHub 개인 기록 저장소를 Slack 채널에 공유했다. 이후 Sung-Jin Kim의 autoresearch/HPO 트렌드 공유, Changsoo의 5/24 온라인 미팅(성진님) 후속 업데이트, MinSuk Kang의 Gobi Space Agent Dreaming 개발 현황 공유, Slack 대화 자동 MD 변환 아이디어가 이어졌다.

- GitHub repo 공유: https://github.com/solkit70/builders-lounge-personal-notes
- Builders Lounge 기록을 AI로 활용하는 방향 멤버 공유
- 5/24 성진님 온라인 미팅 내용 GitHub 업로드 완료
- MinSuk Kang: Gobi Space Agent "Dreaming" 프로세스 개발 중
- 슬랙 대화 자동 md 변환 기능 아이디어 제안

→ **GobiSpace 안내 글**: [[AI/Initiatives/Builders Lounge/notices/2026-05-25 Builders Lounge GobiSpace Changbal 안내 글|Changbal Space 안내 글]], [[AI/Initiatives/Builders Lounge/notices/2026-05-25 Builders Lounge GobiSpace Global 안내 글|Global 안내 글]]

## 관련 링크

| 링크 | 설명 |
| ---- | ---- |
| https://github.com/solkit70/builders-lounge-personal-notes | Builders Lounge 개인 기록 GitHub repo |
| https://github.com/karpathy/autoresearch | Andrej Karpathy autoresearch 프로젝트 |
| https://venturebeat.com/orchestration/your-ai-agents-need-a-terminal-not-just-a-vector-database | RAG의 한계와 AI Agent 아키텍처 (VentureBeat) |
| https://link.springer.com/article/10.1186/s13321-026-01220-7 | HPO 기반 약물 물성 예측 논문 (Springer Cheminformatics) |

## 5월 24일: GitHub Repo 공유 공지

### Changsoo Park — 2026-05-24 14:03

> 안녕하세요. Builders Lounge 관련해서 제가 개인적으로 정리하고 있던 기록들을 GitHub repo로 만들어 공유드립니다.
>
> https://github.com/solkit70/builders-lounge-personal-notes
>
> Builders Lounge 방향성 중 하나가 모임 과정에서 나오는 대화, 발표, 피드백, 아이디어를 잘 기록해 두고, 나중에 이 기록들을 바탕으로 AI를 활용해 새로운 시도나 결과물을 만들어 보는 것이라고 생각합니다.
>
> 일단은 제가 개인적으로 Slack 대화, 모임 준비 과정, 첫 모임 내용, GOBI Hands-on 영상 transcript, Custom Homepage 아이디어 등을 정리해 두었습니다. 아직 공식 기록 저장소라기보다는 개인 기록에 가깝습니다. 앞으로 모임 차원에서 더 효율적이고 좋은 기록 방식이 있으면 함께 찾아보면 좋겠습니다.
>
> 관심 있으신 분들은 이 repo를 로컬에 clone해서 AI 도구에 읽혀 보셔도 좋을 것 같습니다. 예를 들어 "Builders Lounge가 어떻게 시작됐는지 요약해줘", "다음 모임 agenda를 제안해줘", "Product feedback board에 필요한 기능을 정리해줘" 같은 식으로 활용할 수 있습니다. 기록을 보시고 추가 의견이나 새로운 제안이 있으시면 편하게 공유해 주세요.
>
> 조만간 Builders Lounge 2회 모임 일정도 정해서 다시 공유드리겠습니다.

## 5월 24일: autoresearch 및 AI 트렌드 공유

### Sung-Jin Kim — 2026-05-24 16:05

> 바이브코딩도 트렌드이지만 스킬.md를 잘 활용하는 것도 큰 트렌드 같아요. 그 주에서 요즘 관심을 많이 받고 있는 autoresearch가 참 흥미롭네요. 한때 Hyper-parameter optimization (HPO)이라는 기술이 Deeplearning에서는 중요하게 떠올랐는데 Autoresearch는 ML 모델을 학습 시키는 방법을 스스로 찾아간다는 점에서 HPO 이후의 방식이라고들 하네요. 이 방법이 요즘 ML 모델 만들기 외에 다른 분야의 최적화에도 적용되고 있다는데 같이 디스커션해보면 좋을거 같아요.
>
> https://github.com/karpathy/autoresearch

### Sung-Jin Kim — 2026-05-24 16:14 (thread reply)

> Autoresearch를 보다보니 HPO로 Quantum Chemistry 분야에서 논문 쓴 것이 생각나네요. 특히, 한국으로 나가서 성균관대 교수를 하던 기간에 공동으로 가르치던 학생이 쓴 첨부의 HPO 기반 인공지능 물질 예측 관련된 기술의 논문이 최근에 출판이 되어서 더욱 관심이 가는 분야이네요.
>
> https://link.springer.com/article/10.1186/s13321-026-01220-7
>
> **Prediction of intrinsic solubility for drug-like organic compounds using automated network optimizer (ANO) for physicochemical feature and hyperparameter optimization**
> — Journal of Cheminformatics

### Sung-Jin Kim — 2026-05-25 06:27

> RAG의 한계를 극복하는 방식에 대한 내용이 링크 공유해요. 잘활용하면 개인 지식 관리에도 도움이 될 것 같아요.
>
> https://venturebeat.com/orchestration/your-ai-agents-need-a-terminal-not-just-a-vector-database

## 5월 25일: 5/24 미팅 결과 업데이트 (May 24 글의 thread reply)

### Changsoo Park — 2026-05-25 07:04

> 가끔 성진님이랑 온라인으로 연결해서 안부도 묻고 그동안 관심있게 지켜본 AI 분야에 대해서도 의견 교환하고 하는 시간을 갖습니다.
>
> 어제 온라인 미팅에서는 Builders Lounge 모임 관련된 이야기도 해서 그 부분을 정리한 후 GitHub 에 올렸습니다.
>
> Builders Lounge 운영 방향과 다음 모임 등에 대해 의견을 나눴습니다.
>
> @MinSuk Kang 성진님이 GOBI 에 애정을 갖고 GOBI 에 대한 고견도 이야기 하셔서 문서 마지막에 정리 했습니다. 도움이 되시길 바랍니다. 😉
>
> builders-lounge-personal-notes/ideas/2026-05-25 Builders Lounge 공유용 아이디어 메모 - 김성진님 미팅.md

→ [[AI/Initiatives/Builders Lounge/ideas/2026-05-25 Builders Lounge 공유용 아이디어 메모 - 김성진님 미팅|2026-05-25 Builders Lounge 공유용 아이디어 메모 - 김성진님 미팅]]

### MinSuk Kang — 2026-05-25 14:54

> 의견 감사합니다! 안그래도 지금 Space Agent의 Dreaming 프로세스를 제작중에 있습니다. 말씀하신 쌓인다는 것을 기능으로 구현해 보려고 하는데요. Gobi Space의 내용은 물론 Github이나 Google Drive로의 연결도 가능할것 같습니다.
>
> 말씀하신대로 소셜 에이전트가 언제 무엇을 공유할지 알아내서 유저의 승인을 위해 드래프트를 만드는 기능이 있습니다만 아직 첫 버전이라 테스트가 필요한 상황입니다 ㅎㅎ
>
> @lifidea 테스트중이신 소셜 에이전트 프롬프트 공유해주실수있으세요?

### MinSuk Kang — 2026-05-25 17:11

> @Changsoo Park Builder's Lounge의 에이전트가 보여주신 깃헙을 참조하는것도 좋은 방법일것 같습니다.

### Changsoo Park — 2026-05-25 17:33

> @MinSuk Kang 그것도 좋은 아이디어네요. 여기 저기 흩어져 있는 정보를 AI 가 관리 하도록 할 수도 있겠네요. 그리고 이 슬랙 채널에서 오고 가는 내용을 정기적으로 그리고 자동으로 md 파일로 만들어서 정리 하는 기능도 있으면 좋겠습니다.

## 주요 인사이트

| 포인트 | 내용 |
| --- | --- |
| Gobi Space Agent "Dreaming" | MinSuk Kang 개발 중. 정보 누적 + GitHub/Google Drive 연결 + 소셜 에이전트 드래프트 기능 |
| Slack → MD 자동 변환 | Changsoo 아이디어: 슬랙 대화를 정기적·자동으로 md 파일화 |
| autoresearch | Karpathy의 autoresearch: ML 학습 방법 자동화, HPO 이후 방향. 다른 분야 최적화에도 적용 가능 |
| GOBI agentic knowledge network | 로컬 파일 AI 도구 → 개인 지식과 커뮤니티 공간을 연결하는 agentic network로 발전 가능성 |
| Builders Lounge agent | GitHub repo를 참조하는 Builders Lounge 전용 AI Agent 구성 가능성 |

## 후속 액션

- [ ] Gobi Space Agent Dreaming 프로세스 완성 시 Builders Lounge에 적용 검토
- [ ] Slack → md 자동 변환 기능 구현 가능성 탐색 (@MinSuk Kang 또는 GOBI CLI 활용)
- [ ] autoresearch 접근법의 product feedback 분석 응용 가능성 검토
- [ ] 2회 모임에서 autoresearch / RAG 한계 주제를 Builders 관점으로 다루는 방안 고려
