import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

REACTIONS = ["👍", "❤️", "🔥", "🎉", "😮", "👏", "🥰", "💯"]

async def auto_react(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post
    if message:
        reaction = random.choice(REACTIONS)
        await context.bot.set_message_reaction(
            chat_id=message.chat_id,
            message_id=message.message_id,
            reaction=[{"type": "emoji", "emoji": reaction}]
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, auto_react))
app.run_polling()
