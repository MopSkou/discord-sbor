import os
import time
import json
import urllib.request

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]
TEXT = "@everyone Сбор на турнир/потасы"

# Добавляем заголовок User-Agent, чтобы Discord не блокировал запрос
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

for i in range(1, 4):
    payload = {
        "content": f"{TEXT} ({i}/3)",
        "allowed_mentions": {"parse": ["everyone"]},
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(WEBHOOK_URL, data=data, headers=HEADERS)
    try:
        urllib.request.urlopen(req)
        print(f"Сообщение {i}/3 отправлено.")
    except Exception as e:
        print(f"Ошибка при отправке {i}/3: {e}")
    if i < 3:
        time.sleep(2)
