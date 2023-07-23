from pyrogram import Client

phone = 6283866335220

api_id = 10103155
api_hash = "13bddab82f9a0f7188686ee7b5558663"

app = Client("my_account", api_id=api_id, api_hash=api_hash)

# passar o numero do telefone
app.run()
