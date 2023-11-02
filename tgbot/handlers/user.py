import asyncio
from typing import Any
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hlink

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply("Вітаю, звичайний користувач!")


@user_router.message(F.new_chat_members)
async def welcome(message: Message):
    msg = await message.reply(
        f"{message.from_user.full_name}, вітаємо тебе у нашому телеграм-чаті з пошуку попутників!\n\nДля початку користування чатом - ознайомся з {hlink('ПРАВИЛАМИ', 'https://t.me/poputnyky_ua/1713/1715')}\n\nТакож, рекомендуємо підписатись на нашого партнера - телеграм-канал {hlink('ПЕРШИЙ ЕЛЕКТРОМОБІЛЬНИЙ', 'https://t.me/+B9CLRxWVEpdmYmQy')}")
    await asyncio.sleep(10)
    await msg.delete()
