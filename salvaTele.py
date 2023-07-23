from telethon import TelegramClient

phone = 6283866335220

api_id = 10103155
api_hash = "13bddab82f9a0f7188686ee7b5558663"

client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
client.start()
