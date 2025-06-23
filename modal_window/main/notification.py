import asyncio
from aiogram import Bot

TOKEN = "BOT TOKEN"

CHAT_ID = 0 #YOUR CHAT ID

bot = Bot(token=TOKEN)

async def send_telegram_notification(message):
    await bot.send_message(chat_id=CHAT_ID, text=message)
