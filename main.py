import asyncio

from aiogram import Bot, Dispatcher

from config import TOKEN
from app.handlers import router

from app.database.models import async_main

bot = Bot(token=TOKEN) # Токен бота
dp = Dispatcher()

async def main():
    await async_main()
    dp.include_router(router)
    await dp.start_polling(bot)

# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())
