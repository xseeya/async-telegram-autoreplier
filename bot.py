from aiogram import Bot, Dispatcher

import asyncio


import user
import config as cfg
   
    
async def main():
    bot = Bot(token=f'{cfg.token}')
    dp = Dispatcher()
    dp.include_router(user.router)
    await dp.start_polling(bot)
    
asyncio.run(main())
