import asyncio
from aiogram import types, Router, F
from aiogram.filters import StateFilter, Text
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hcode


echo_router = Router()

@echo_router.message(~Text(contains='#'))
async def bot_echo(message: types.Message):
    if message.chat.id != -1001971714044:
        msg = await message.reply('Публікуйте ваше повідомлення використовуючи хештег\n#водій / #пасажир')
        await asyncio.sleep(5)
        await msg.delete()

