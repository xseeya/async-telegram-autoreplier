from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router, F

import nest_asyncio


import config as cfg
from run import app

nest_asyncio.apply()

router = Router()

state = {'status': 0}
# state['status'] = 0


kb_settings = [[
    KeyboardButton(text='Выключить'),
    KeyboardButton(text='Включить')
]]

keyboard_settings= ReplyKeyboardMarkup(keyboard=kb_settings, resize_keyboard=True)


@router.message((F.from_user.id == cfg.user_id) & (F.text =='Включить'))
async def cmd_on(message: Message):
    state['status'] = 1
    await app.start()
    await message.answer('Автоответчик включен', reply_markup=keyboard_settings)
    
@router.message((F.from_user.id == cfg.user_id) & (F.text =='Выключить'))
async def cmd_off(message: Message):
    state['status'] = 0
    await app.stop()
    await message.answer('Автоответчик выключен', reply_markup=keyboard_settings)



@router.message(F.from_user.id == cfg.user_id)
async def cmd_start(message: Message):
    if state['status'] == 0:
        await message.answer(f'Автоответчик выключен', reply_markup=keyboard_settings)
    else:
        await message.answer(f'Автоответчик включен', reply_markup=keyboard_settings)

  