from typing import Any

from aiogram.handlers import MessageHandler


class ContentMsgHandler(MessageHandler):
    async def handle(self) -> Any:
        msg = self.event
        return msg.answer(text=msg.text)
