#!/bin/bash
# 17개 slide txt → Gemini TTS wav (v3)
cd "$(dirname "$0")"
VOICE="${1:-Callirrhoe}"
STYLE="${2:-따뜻하고 차분하게, 동료 교사에게 부담을 주지 않는 합니다체로}"

for i in $(seq -f "%02g" 1 17); do
  txt="slide-${i}.txt"
  wav="slide-${i}_gemini_tts.wav"
  if [ -f "$wav" ]; then
    echo "[skip] $wav already exists"
    continue
  fi
  if [ ! -f "$txt" ]; then
    echo "[miss] $txt"
    continue
  fi
  echo "[gen ] $wav ..."
  python "C:/Users/pc/Windows-Projects/tools/converters/TTS/gemini_tts.py" "$txt" \
    --voice "$VOICE" \
    --style "$STYLE" \
    --language-code ko-KR \
    2>&1 | tail -3
done

echo ""
echo "=== Result ==="
ls -la slide-*.wav 2>/dev/null
