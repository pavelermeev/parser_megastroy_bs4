import logging
import asyncio
from os import getenv

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, FSInputFile
from dotenv import load_dotenv

from main import parse

load_dotenv()

TELEGRAM_BOT_TOKEN = getenv('BOT_TOKEN')

form_router = Router()


@form_router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        '''Привет! Я бот-парсер товаров магазина Мегастрой.
        Просто пришлите мне ссылку с нужной тебе категорией товаров,
        а я пришлю Вам файл.'''
    )


@form_router.message(Command(commands=['help']))
async def help(message: Message):
    await message.answer(
        'Для корректной работы бота, нужна ссылка формата:'
        'https://<город>.megastroy.com/catalog/<категория>'
        'Пример: https://cheboksary.megastroy.com/catalog/cement'
    )


@form_router.message(
        lambda message: message.text.startswith(
            'https') and message.text.count('megastroy.com/catalog/') == 1)
async def recive_url(message: Message):
    url = message.text
    parse(url)
    file = FSInputFile('megastroy.csv')
    await message.answer_document(file, caption='Вот ваш файл с данными.')
    await message.answer('Если нужно ещё, то отправьте ещё ссылку.')


@form_router.message()
async def wrong_answer(message: Message):
    await message.answer(
        '''Я не умею отвечать на сообщения, но за то умею парсить ссылки!
        Пришлите ссылку, пожалуйста.'''
    )


async def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(form_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
