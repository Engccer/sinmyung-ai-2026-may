#!/usr/bin/env python3
"""_gemini_response.txt → slide-NN.txt 16개로 분할."""
import re
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "_gemini_response.txt"
text = SRC.read_text(encoding="utf-8")

# === slide-NN === 로 split
parts = re.split(r"^===\s*slide-(\d+)\s*===\s*$", text, flags=re.M)
# parts: [intro(빈)/잡문, '01', body1, '02', body2, ...]
intro = parts[0]
data = parts[1:]

count = 0
for i in range(0, len(data), 2):
    num = int(data[i])
    body = data[i+1].strip()
    out = ROOT / f"slide-{num:02d}.txt"
    out.write_text(body + "\n", encoding="utf-8")
    print(f"slide-{num:02d}.txt: {len(body)} chars")
    count += 1

print(f"\nTotal: {count} files")
