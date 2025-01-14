import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import my_router
from app.admhandlers import adm_router

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router=my_router)
    dp.include_router(router=adm_router) # можно добавить доп. роутеры
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print('Бот запущен')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот завершен')
