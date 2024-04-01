from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN: str = "7095961209:AAHhlUYeUln9hpQfEaCX0N8JZFRcFCAYkIg"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_cmd(message: Message) -> None:
    await message.answer("Hi!\nMy name is EchoBot!\nSend me something!")


@dp.message(Command(commands=["help"]))
async def process_help_cmd(message: Message) -> None:
    await message.answer("Send me any message and I will send you the same message!")


@dp.message(F.photo)
async def send_photo_echo(msg: Message) -> None:
    await msg.answer_photo(photo=msg.photo[-1].file_id)


@dp.message()
async def send_echo(message: Message) -> None:
    await message.answer(text=message.text)


def run_polling() -> None:
    print("Starting polling...")
    dp.run_polling(bot)
