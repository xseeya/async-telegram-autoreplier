from pyrogram import Client, filters

import datetime

import config as cfg


app = Client("my_account", api_id=cfg.api_id, api_hash=cfg.api_hash)


@app.on_message(filters.incoming & ~filters.group & ~filters.bot)
async def hello(client, message) -> None:
    async for message in app.get_chat_history(message.chat.id, limit=1, offset=1):
        info = await app.get_messages(message.chat.id, message.id)
    
    if datetime.datetime.now().timestamp() - info.date.timestamp() > cfg.delay:
        await message.reply(f"{cfg.text}")

