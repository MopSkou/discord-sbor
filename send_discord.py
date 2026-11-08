import os
import time
import json
import urllib.request

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]
TEXT = "@everyone Сбор на турнир"

for i in range(1, 4):
    payload = {
        "content": f"{TEXT} ({i}/3)",
        "allowed_mentions": {"parse": ["everyone"]},
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(WEBHOOK_URL, data=data, headers={"Content-Type": "application/json"})
    try:
        urllib.request.urlopen(req)
        print(f"Сообщение {i}/3 отправлено.")
    except Exception as e:
        print(f"Ошибка при отправке {i}/3: {e}")
    if i < 3:
        time.sleep(2)
