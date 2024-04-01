from typing import Any

from aiogram.enums import ContentType
from aiogram.handlers import MessageHandler


class ContentMsgHandler(MessageHandler):
    async def handle(self) -> Any:
        msg = self.event
        if msg.content_type == ContentType.TEXT and msg.text.startswith("/"):
            return msg.answer(
                text="Wrong command.\nSupported commands:\n\n/start\n/help"
            )
        try:
            ans = await msg.send_copy(chat_id=msg.chat.id)
        except TypeError:
            ans = await msg.reply(text="This update type is not supported by send_copy")
        return ans
