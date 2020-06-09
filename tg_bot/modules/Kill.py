import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
      "🔥🔥",
      "⚡⚡",
      "⭐⭐",
 )
@run_async
def kill(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /Test  🔥
"""

__mod_name__ = "Killing Commands"

KILL_HANDLER = DisableAbleCommandHandler("kill", kill)

dispatcher.add_handler(KILL_HANDLER)
