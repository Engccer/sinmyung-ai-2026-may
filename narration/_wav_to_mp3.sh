#!/bin/bash
# wav -> mp3 64kbps 모노 변환 (음성용)
cd "$(dirname "$0")"
for wav in slide-*_gemini_tts.wav; do
  mp3="${wav%.wav}.mp3"
  if [ -f "$mp3" ]; then
    echo "[skip] $mp3"
    continue
  fi
  echo "[conv] $wav -> $mp3"
  ffmpeg -y -i "$wav" -acodec libmp3lame -ab 64k -ac 1 -ar 24000 "$mp3" 2>&1 | tail -1
done
echo ""
echo "=== Result ==="
du -sh slide-*.mp3 2>/dev/null | head -20
