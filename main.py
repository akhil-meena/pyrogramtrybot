from os import environ
from pyrogram import Client

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
bot_token = environ["BOT_TOKEN"]
info = "Greetings from **Heroku**!"

app = Client(":memory:",bot_token, api_id, api_hash)

#print(info)

@app.on_message()
async def work(client, message):
    await app.send_message(message.chat.id, info)

app.run()
