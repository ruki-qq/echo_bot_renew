from os import getenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from dotenv import load_dotenv

from echo_bot.handlers import ContentMsgHandler

load_dotenv()

BOT_TOKEN: str = getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_cmd(msg: Message) -> None:
    await msg.answer("Hi!\nMy name is EchoBot!\nSend me something!")


@dp.message(Command(commands=["help"]))
async def process_help_cmd(msg: Message) -> None:
    await msg.answer("Send me any message and I will send you the same message!")


@dp.message(F.photo)
async def send_photo_echo(msg: Message) -> None:
    await msg.answer_photo(photo=msg.photo[-1].file_id)


@dp.message(F.sticker)
async def send_sticker_echo(msg: Message) -> None:
    await msg.answer_sticker(sticker=msg.sticker.file_id)


dp.message.register(ContentMsgHandler)


def run_polling() -> None:
    print("Starting polling...")
    dp.run_polling(bot)
