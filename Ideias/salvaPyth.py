from telethon.sync import TelegramClient
from ppadb.client import Client
import pyautogui
import asyncio
import time
import re
import clipboard

# Credenciais da API do Telegram
phone = "281222157406"
api_id = 10103155
api_hash = "13bddab82f9a0f7188686ee7b5558663"

client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
client.start()