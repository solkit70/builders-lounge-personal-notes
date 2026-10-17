# CTS 부스 홍보 페이지 — 파일 안내

| 파일 | 역할 |
|---|---|
| `page.html` | **게시 원본** (2026-10-05 Version 8). https://claude.ai/artifact/Vs9GEkCtEXsyRdT5kvyF7s 에 그대로 게시한다. 이미지(QR 2장)가 들어 있어 바로 게시 가능 |
| `index.html` | `page.html` 과 같은 내용 (예전 경로 호환) |
| `intersection-draft.html` | 「Builders Lounge 교집합 시안」 https://claude.ai/artifact/2rHb8aedHbtbUJVuYt5TWz (비공개). 맨 아래에 부스 페이지에서 옮긴 **Gobi Space 가입 안내(컴퓨터 · 휴대폰 단계, 스크린샷 14장)** 보관 |
| `qr_builders_lounge_artifact.png` | 홍보 페이지 QR |
| `qr_newsletter_form.png` | 뉴스레터 신청 Google Form QR (forms.gle/942wiycPttG2CSDx8) |
| `page.template.html` · `build.py` | 9/29 까지 쓰던 빌드 방식 (스크린샷 15장 채우기). 10/5 부터는 쓰지 않는다 — 가입 안내가 교집합 시안으로 옮겨 갔기 때문 |
| `_backup_20261005/` | 10/5 수정 전 원본 |

## 2026-10-05 변경

- 04 절: 온라인 공간 두 곳 — ① Gobi Space Builders Lounge 채널(기존 카드 그대로) ② **창발 Slack #club-sg-ai** (초대 링크 버튼) + **뉴스레터 신청**(Google Form 버튼 · QR). 안내 문구 두 곳 수정(두 공간 소개 · 「아래에서 기기를 고르세요」 삭제)
- 04 아래 가입 안내(기기 탭 · Part 1~3 단계 · General/Catch up 참고 · 창발 소개 인용 · 마무리 링크)를 교집합 시안 페이지 아래로 옮기고 부스 페이지에서는 지움
- 페이지 자체의 doctype/html/head/body 태그를 빼서 게시 규격에 맞춤
