---
title: "2026-11-10 송이 채취 영상 썸네일 프롬프트"
created: 2026-11-10 14:25:00
author:
  - "Claude Code"
tags:
  - builders-lounge
  - youtube
  - thumbnail
related:
  - "[[Initiatives/Builders Lounge/videos/2026-11-10 송이 채취 영상 유튜브 업로드 자료 by Claude Code]]"
  - "[[Tasks/items/송이버섯 채취 동영상 편집 · 유튜브 업로드]]"
---

## 방향

지금 썸네일은 집에서 찍은 사진이라 현장감이 약하다. 산속에서 송이를 손에 든 장면을 주인공으로 바꾸고, 「시애틀 레이니어산」 배지와 숫자 두 개(61개 · $5,000)로 호기심을 만든다. 김진영 님 대담 썸네일이 잘 된 이유는 큰 한 줄 카피, 숫자 강조 배지, 진짜 사람과 현장, 높은 대비였다. 이번에도 같은 공식을 쓴다. 제목은 「송이 61개 따며 세운 2027 계획 — 은퇴 후 AI로 한 달 $5,000 만들기」이므로, 썸네일은 제목을 반복하지 않고 **숫자와 장면**으로 클릭을 부른다.

## AI 에게 함께 줄 이미지

모두 `C:\Users\dougg\Videos\Youtube\2026\Builders_Lounge\20261104_Songyi\materials\thumbnail_refs\` 에 모아 두었다.

| 파일 | 장면 | 쓰임 |
|---|---|---|
| `ref2_hand_holding_songyi.png` | 숲 한가운데서 손에 든 큰 송이 (본편 13:25) | **주인공** — 전경 왼쪽에 크게 |
| `ref1_cluster_in_forest.png` | 한 자리에 모여 난 송이 무리 (박창수 캡처) | 「한 자리에서 우르르」 현장감 · 바닥 질감 |
| `ref4_harvest_61.png` | 차 트렁크의 오늘 채취분 61개 (31:10) | 오른쪽 작은 인셋 「오늘 61개」 증거 컷 |
| `ref3_old_growth_forest.png` | 거대한 고목이 선 원시림 (5:50) | 배경 분위기 · 색감 |
| `ref5_catchupai_character.png` | Catch Up AI 캐릭터 | 선택 — 오른쪽 아래 작게 (채널 표지) |

최소 구성은 ref2 + ref4 + ref3 세 장이다. 챗봇이 이미지를 여러 장 받으면 섞어 버리는 경우가 있어, 처음엔 세 장으로 시작하고 결과가 단조로우면 ref1 · ref5 를 더한다.

## 프롬프트 A — 손에 든 송이 + 61개 인셋 (추천)

```
Create a YouTube thumbnail, 16:9, 1280x720, photorealistic, high contrast, bright and punchy like a top Korean YouTube thumbnail.

Use the attached photos as the real source material. Keep the mushrooms looking exactly like the real matsutake (songi) in the photos — white caps with brown flecks and soil — do not turn them into generic cartoon mushrooms.

COMPOSITION
- Left 55%: hero shot from ref2 — a hand holding one large fresh matsutake mushroom close to the camera, in a lush Pacific Northwest old-growth forest (ferns, moss, tall fir trunks from ref3). Sharp mushroom, slightly blurred forest background with soft morning light rays.
- Far background, top right: a faint, majestic snow-capped Mount Rainier peak seen through a gap in the trees, misty, subtle — it should read as "Mt. Rainier, Washington" without dominating.
- Right side lower: a tilted polaroid-style inset photo with white border showing the day's harvest pile from ref4 (a box full of matsutake). Small yellow sticker on it: "오늘 61개".
- Optional bottom-right corner: small cute blue robot mascot from ref5 waving (about 12% of height), as a channel signature.

TEXT (Korean, render exactly, bold rounded Korean sans-serif, thick dark outline + drop shadow, very legible on a phone):
1. Top-left small badge, red pill with white location pin icon: "시애틀 레이니어산"
2. Main headline, huge, 2 lines, left-center over the forest, white text with black outline, the number in bright yellow:
   "하루에 송이"
   "61개!"
3. Bottom banner, dark green rounded bar across the lower left, white text, with "$5,000" in a bright orange/yellow pill:
   "은퇴 후 AI로 월 $5,000?"

STYLE
- Vivid but natural forest greens, warm golden light, crisp focus on the mushroom and the text.
- Clean layout, no more than these three text elements, no extra English words, no watermark, no fake YouTube UI.
- Leave the bottom-right 15% free of text (YouTube timestamp area).
```

## 프롬프트 B — 숲속 송이 무리 와이드 (대안)

```
Create a YouTube thumbnail, 16:9, 1280x720, photorealistic, cinematic, high contrast.

Use the attached photos as real reference. Main image: the cluster of wild matsutake (songi) mushrooms growing together on the forest floor from ref1, seen from a low angle so the mushrooms feel big and abundant, with the tall old-growth trees of ref3 rising behind them. Through the trees in the far background, a soft misty snow-capped Mount Rainier. Golden morning light, ferns and moss in the foreground.

Small inset in the top-right corner, tilted polaroid with white border: the harvest box from ref4, with a small yellow sticker "오늘 61개".

TEXT (Korean, render exactly, bold rounded sans-serif, thick black outline, legible on mobile):
- Top-left red pill badge with location pin: "시애틀 레이니어산"
- Huge headline across the left/middle: "송이밭 발견!" in white, and below it "하루 61개" with "61" in bright yellow
- Bottom dark-green bar: "숲에서 세운 2027 계획 — AI로 월 $5,000" with "$5,000" highlighted in an orange pill

No extra text, no watermark, no YouTube UI. Keep the bottom-right corner clear for the timestamp.
```

## 카피 후보 (결과를 보고 바꿔 끼울 것)

| 자리 | 1안 | 2안 | 3안 |
|---|---|---|---|
| 메인 | 하루에 송이 61개! | 송이밭 발견! 하루 61개 | 2020년 이후 하루 기록 3위, 61개 |
| 아래 띠 | 은퇴 후 AI로 월 $5,000? | 숲에서 세운 2027 계획 | AI로 월 $5,000 도전 |
| 배지 | 시애틀 레이니어산 | 워싱턴 레이니어산 | 📍 Mt. Rainier |

숫자는 두 개까지만 쓴다(61 · $5,000). 세 개가 넘으면 휴대폰 화면에서 읽히지 않는다.

## 만든 뒤 확인할 것

- **한글 오타**: 이미지 모델은 한글을 자주 틀린다. 「레이니어산」「송이」「$5,000」을 한 글자씩 확인하고, 틀리면 같은 대화에서 "Fix the Korean text exactly to: …"로 다시 요청한다. 계속 틀리면 글자 없는 버전을 받아 Remotion·Canva 에서 글자만 얹는 방법도 있다(요청하면 Claude Code 가 얹어 준다).
- **송이 모양**: 일반 버섯 그림처럼 바뀌지 않았는지(흰 갓 · 갈색 점 · 흙).
- **레이니어산**: 너무 크거나 다른 산 모양이면 "make Mount Rainier smaller and fainter"로 줄인다. 실제 채취지는 레이니어산 남쪽 Gifford Pinchot National Forest 라 산은 배경의 상징으로만 둔다.
- **휴대폰 크기 테스트**: 결과를 320px 폭으로 줄여 봐도 메인 카피가 읽히는지.
- 저장: `public/songyi-1110/images/thumbnail.png` 를 새 결과로 바꾸면 업로드 자료의 썸네일 경로를 그대로 쓸 수 있다.

## 결과 (11/10)

박창수가 프롬프트 B 계열로 만든 안을 최종 선택했다 → `public/songyi-1110/images/ThumbNail_Selected.png` (다른 후보 `ThumbNailImg.png`). 숲속 송이 무리 · 뒤편 레이니어산 · 오른쪽 위 「오늘 61개」 폴라로이드, 문구는 「시애틀 레이니어산」 「송이밭 발견! 하루 61개」 「숲에서 세운 2027 계획 — AI로 월 $5,000」. 한글 오타는 없다. 원본이 2.9MB 라 유튜브 2MB 제한에 맞춰 1280×720 JPG(`thumbnail_upload.jpg`, 434KB)를 만들었다.
