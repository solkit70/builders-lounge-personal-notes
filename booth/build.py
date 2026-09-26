"""page.template.html + 원본 Artifact 의 이미지(base64) -> index.html

템플릿의 DATAURI 자리표시를 원본 페이지에 나오는 순서대로 채운다.
(QR 1장 + 컴퓨터 스크린샷 6장 + 휴대폰 스크린샷 8장 = 15장)

사용: python build.py [원본 HTML 경로]
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
DEFAULT_SRC = Path(
    r"C:\Users\dougg\.claude\projects\c--AI-study-2026-Changsoo-Vault"
    r"\d5e5fb65-a809-41fb-b956-22670ec6295e\tool-results"
    r"\artifact-e9c029bd-1788781014-cace.html"
)

src = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SRC
images = re.findall(r"data:image/[a-z]+;base64,[A-Za-z0-9+/=]+", src.read_text(encoding="utf-8"))
template = (HERE / "page.template.html").read_text(encoding="utf-8")

slots = template.count("DATAURI")
if slots != len(images):
    sys.exit(f"자리표시 {slots}개 != 원본 이미지 {len(images)}개 — 순서가 어긋났을 수 있다")

it = iter(images)
out = re.sub("DATAURI", lambda _: next(it), template)
(HERE / "index.html").write_text(out, encoding="utf-8")
print(f"index.html {len(out) / 1024:.0f} KB · 이미지 {len(images)}장")
