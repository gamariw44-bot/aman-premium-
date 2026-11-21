import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("💎 Join Premium Channel", url="https://t.me/+HbD5SkqQFUgzNzE0")]]
    await update.message.reply_text(
        "💎 Welcome to Aman Premium\n\n"
        "ሰላም! ወደ Aman Premium በደህና መጡ። 🎉\n\n"
        "ልዩ ይዘቶችን ለማግኘት ከታች ያለውን ቁልፍ ይጫኑ።",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
