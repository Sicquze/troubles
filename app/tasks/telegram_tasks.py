from app.helper import bot


async def send_message(chat_id, message):
    await bot.send_message(chat_id=chat_id, text=message)
