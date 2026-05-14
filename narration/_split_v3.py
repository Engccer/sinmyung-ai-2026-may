#!/usr/bin/env python3
"""_gemini_response_v3.txt → slide-NN.txt 17개로 분할 (===SN=== 형식)."""
import re
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "_gemini_response_v3.txt"
text = SRC.read_text(encoding="utf-8", errors="replace")

# 헤더 노이즈 제거: 첫 ===S1=== 이전은 버림
m = re.search(r"^===S\d+===", text, flags=re.M)
if m:
    text = text[m.start():]

parts = re.split(r"^===S(\d+)===\s*$", text, flags=re.M)
intro = parts[0]
data = parts[1:]

count = 0
for i in range(0, len(data), 2):
    num = int(data[i])
    body = data[i + 1]
    # 마지막 슬라이드 본문에서 영어 스택 노이즈 차단
    body = re.split(r"\n(?:Warning:|Attempt\s+\d+ failed|_GaxiosError|at\s+\S+\.\S+|\{\s*$)", body, maxsplit=1)[0]
    body = body.strip()
    out = ROOT / f"slide-{num:02d}.txt"
    out.write_text(body + "\n", encoding="utf-8")
    print(f"slide-{num:02d}.txt: {len(body)} chars")
    count += 1

print(f"\nTotal: {count} files")
