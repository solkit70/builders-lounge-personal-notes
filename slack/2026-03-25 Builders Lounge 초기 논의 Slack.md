---
title: "Builders Lounge 초기 논의 Slack"
source: "Changbal Slack thread screenshots, 2026-03-25"
author:
  - "Sung-Jin Kim"
  - "James H Kim"
  - "Changsoo Park"
created: 2026-05-24 12:57:31
tags:
  - builders-lounge
  - changbal
  - slack
  - community
  - brain-training
---

## 요약

2026년 3월 25일 수요일 Slack 대화에서 Builders Lounge로 이어지는 초기 흐름이 시작되었습니다.

- 출발점: 성진님의 **Brain Training Board Games** 소개
- 확장 주제: AI coding agent 활용, documentation 중심 개발, 앱 개발 방식
- 후속 흐름: 관심 있는 분들이 오프라인으로 만나 이야기해 보자는 제안
- Builders Lounge 연결: 각자 만든 Product를 소개하고 서로 첫 사용자로 feedback을 드리는 모임 방향

성진님이 소개한 웹사이트:
http://braintraining-boardgames-319297116860.s3-website-us-west-2.amazonaws.com/landing-page/

## Slack Thread 원문

### Sung-Jin Kim — 2026-03-25 07:08

> 뇌와 두뇌 건강은 저도 관심이 많은데 이걸 위해 지인분과 brain training 온라인 게임들을 만들어보고 있습니다. 개인적으로 해보는데 생각보다 재미가 있는거 같아 공부하시는대 참고겸 링크를 올려봅니다. 주변에 나이가 90이 넘은 분들이 계시는데 두뇌 건강을 유지하는 분들은 나름 어려운 문제나 과제를 풀고 계시는거 같아요. 백살까지 팔팔하기 위하여!
>
> http://braintraining-boardgames-319297116860.s3-website-us-west-2.amazonaws.com/landing-page/

링크 미리보기:

> **Brain Training Board Games**
>
> Train memory, logic, and strategy with a curated collection of browser-based board games and learning tools.

### Sung-Jin Kim — 2026-03-25 07:11

> 혼자하면 재미가 없을거 같아 인공지능과 대결을 하게 만들었습니다. 어떤 보드게임은 사람에게는 어렵진 않지만 믹맥스로 풀때에는 속도가 중요하네요. 그래서 JS에서 WASM으로 엔진을 업그레이드 한 게임도 포함하게 되었습니다.
>
> 게임만 하면 시간낭비라는 생각이 들거 같아 대학 수준의 기초 지식도 다루는 에듀게임도 포함했습니다. 향후 분자들의 구조에 대해 설명하는 앱입니다.
>
> 여유가 될때마다 하나씩 더 포함하고 있어요. 혹시 더 포함되면 좋겠다는 보드게임이나 에듀게임이 있으면 추천도 부탁드릴께요.

### James H Kim — 2026-03-25 19:41

> dual-n-back은 Brain Training중 아마 가장 과학적으로 증명이 많이 된걸로 알고요. The settlers of catan도 머리에 좋다는 얘기를 많이 들은것 같아요.

### Sung-Jin Kim — 2026-03-25 20:12

> 난이도가 있을거 같아 보이는데 그래도 한번 개발이 가능할지 살펴봐야 될 거 같네요. 고마워요.

### Sung-Jin Kim — 2026-03-25 20:16

> Coding agent 만능시대에 살다보니 그간 착각을 했던 거 같아요. LLM은 사실 코드를 체계적으로 구현하는 게 아니라, 그림을 그리고 직감적으로 표현하는 방식으로 동작하는데 그걸 잊고 있었네요. 그래서 이성적으로 작성하는 게 아니라 감각이나 직감으로 짜기 때문에 제대로 된 코드를 작성하는 데에는 본질적인 한계가 있다는 걸 코딩 에이전트들의 홍수 속에서 미처 인식하지 못하고 있었습니다.
>
> 이제는 그간의 경험을 바탕으로 coding agent를 전체적인 코드를 작성하는 단계에서는 가능하면 배제시키고 있습니다. 그러고 나니 오히려 효율도 늘고 내 역량이나 발전에도 크게 저해되지는 않는 거 같아요. 대신에 시간도 많이 들고 힘들기도 한 디버깅이나 컨설팅 쪽으로 활용하는 방향으로 다시 잡았어요.
>
> Coding agent가 스스로 뭔가 해줄 거 같아서 기다리고 또 기다리다가 토큰은 토큰대로 다 태우고 건강도 나빠지는 경우도 자주 보게 됩니다. 여러분은 coding agent 사용해 보니 어떠신가요?

### Changsoo Park — 2026-03-25 21:21

> 흥미롭네요. 조만간 만나서 자세히 이야기 들어 보고 싶습니다. 저는 요즘 Coding 보다는 Documenting 에 AI를 더 많이 사용하고 있어서 그 부분은 아주 많이 도움이 됩니다. 코딩은 Claude Skills로 만들 수 있을 정도의 단편적인 기능을 구현하는 것에는 사용해서 크게 문제의식 없이 잘 사용하고 있습니다. 성진님이 이야기 하신 건 좀 규모가 있는 앱 개발일 것 같고 그런 규모가 있는 앱 개발에서는 전체적인 코드 작성보다 task 들 작은 규모로 나눠서 Agent에게 코딩을 시키는 방식이 더 효율적이라는 인사이트를 공유해 주신 것 같은데요. 조만간 제가 벨뷰쪽으로 갈일 있을 때 연락 드릴께요. 한번 뵙고 그런 얘기 자세히 해 보죠. 😉

### Sung-Jin Kim — 2026-03-25 21:29

> 도큐멘트는 사실 코딩과 달리 더 수학적인 분야라 오히려 도움이 많이 되는거 같아요. 조만간 뵙고 이야기 많이 나누면 좋겠네요. 그때 관심 있는 다른 분들도 모여서 토론해도 좋을 거 같아요. 주제는 대충 "코딩 에이전트의 활용 이대로 좋은가"가 될 수 있지 않을까 싶네요.

### Changsoo Park — 2026-03-25 21:36

> 좋습니다. 그러면 오랜만에 오프모임 한번 주최 해 보겠습니다.

### Sung-Jin Kim — 2026-03-25 21:37

> 네 그러면 좋을 거 같습니다. 시대적으로 딱 필요한 토론 주제 같거든요.

### Changsoo Park — 2026-03-25 21:41

> 위에 성진님과 이야기 하다가 오랜만에 Off 모임 한번 하자고 이야기가 됐습니다.
>
> 그동안 많은 분들이 각자의 자리에서 AI 에 대한 연구도 많이 하셨고 나눌 이야기도 많을 것 같은데요. 성진님은 '코딩 에이전트의 활용 이대로 좋은지'에 대해 들려줄 좋은 경험과 인사이트가 있으신 것 같습니다. 이번주는 좀 힘들고 4월 중으로 한번 모임을 가져 볼까 하는데요.
>
> 여러분들 의견도 좀 들어 보고 싶습니다.
>
> 여기에 의견 주셔도 되고 저에게 DM 보내 주셔도 됩니다.
>
> 다른 분들 의견도 들어보고 나서 Off 모임 날짜와 형식을 정하겠습니다.
>
> 봄도 됐으니까 오랜만에 함 보죠. 😉

## 의미와 연결 포인트

이 thread는 Builders Lounge의 시작점으로 볼 수 있다. 처음에는 성진님의 Brain Training Board Games 소개와 AI 대결 기능, WASM 엔진 업그레이드, 에듀게임 방향이 공유되었다. 그러나 대화가 이어지면서 "AI coding agent를 어떻게 활용해야 하는가", "대규모 앱 개발에서 전체 코드를 맡기기보다 작은 task로 나눠야 하는가", "AI를 documenting에 더 잘 활용할 수 있는가" 같은 Builder 관점의 실전 문제가 드러났다.

특히 Changsoo Park의 "오프모임 한번 주최" 제안은 이후 Builders Lounge의 오프라인 모임으로 이어지는 직접적인 씨앗이다. 성진님의 Product는 이후 2회 모임의 Product Demo 후보로도 연결될 수 있으며, 이 thread는 Builders Lounge가 단순 친목 모임이 아니라 각자의 실제 제품과 AI 활용 경험을 바탕으로 배우고 피드백하는 모임이 되어야 한다는 방향을 잘 보여준다.

## Builders Lounge 관점의 핵심 포인트

| 포인트 | Slack 대화에서 나온 근거 | Builders Lounge로의 연결 |
| ------ | ----------------------- | ------------------------ |
| 실제 Product 중심 | 성진님의 Brain Training Board Games 소개 | Product Showcase와 Demo Day의 출발점 |
| 첫 사용자 피드백 | 보드게임/에듀게임 추천 요청 | 멤버들이 실제 사용 후 피드백 제공 |
| AI 개발 경험 공유 | coding agent 활용 방식 논의 | Builder 경험과 시행착오 공유 |
| 오프라인 모임 제안 | Changsoo Park의 오프모임 주최 제안 | Builders Lounge 1회 모임으로 이어진 흐름 |
| 기록의 중요성 | Slack thread 자체가 초기 맥락 자료 | 향후 홈페이지와 공동 기록 저장소에 보존 필요 |

## 후속 액션

- [ ] Brain Training Board Games를 Builders Lounge Product Showcase 첫 사례 후보로 정리한다.
- [ ] 성진님 Product Demo 요청 시 이 thread를 배경 자료로 연결한다.
- [ ] "코딩 에이전트의 활용 이대로 좋은가"를 Builders Lounge 토론 주제 후보로 남긴다.
- [ ] 이 Slack thread를 Builders Lounge 공동 기록 저장소 설계의 초기 샘플로 사용한다.
- [ ] [공동 기록 저장소 아이디어](<../ideas/2026-05-24 Builders Lounge 2회 준비 브레인덤프.md#공동 기록 저장소 아이디어>)와 연결해 기록 대상 예시로 반영한다.
