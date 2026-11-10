import os
import json
import urllib.request

# Ссылка на НОВЫЙ (третий) канал
WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_THIRD"]

# Текст сообщения (можете поменять на свой)
TEXT = "@everyone Просьба отписаться в чат до 19:00 по МСК, так как будут формироваться отряды!"

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

payload = {
    "content": TEXT,
    "allowed_mentions": {"parse": ["everyone"]},
}

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(WEBHOOK_URL, data=data, headers=HEADERS)

try:
    urllib.request.urlopen(req)
    print("Сообщение в третий канал успешно отправлено.")
except Exception as e:
    print(f"Ошибка при отправке: {e}")
