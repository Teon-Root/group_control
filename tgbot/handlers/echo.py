import asyncio
from aiogram import types, Router, F
from aiogram.filters import StateFilter, Text
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hcode


echo_router = Router()

@echo_router.message(~Text(contains='#'))
async def bot_echo(message: types.Message):
    text_test2 = ['Публікуйте ваше повідомлення використовуючи хештег\n#водій / #пасажир']
    msg = await message.reply("\n".join(text_test2))
    await asyncio.sleep(5)
    await msg.delete()