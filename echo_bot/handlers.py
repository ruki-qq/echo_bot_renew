from typing import Any

from aiogram.handlers import MessageHandler


class ContentMsgHandler(MessageHandler):
    async def handle(self) -> Any:
        msg = self.event
        try:
            ans = await msg.send_copy(chat_id=msg.chat.id)
        except TypeError:
            ans = await msg.reply(text="This update type is not supported by send_copy")
        return ans
