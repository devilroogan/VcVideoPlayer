from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from player.videoplayer import app
from player.videoplayer import call_py
bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="player"),
)

async def huehue():
    await bot.start()
    await app.start()
    await call_py.start()
    await idle()
