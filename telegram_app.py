from telegram import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import CommandHandler, ContextTypes
from config import BOT_TOKEN
from telegram.ext import ApplicationBuilder

WEBAPP_URL = "https://yourdomain.com/app"

async def app_entry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Открыть приложение 🥊", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Запусти наше Telegram-приложение:", reply_markup=reply_markup)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("app", app_entry))
    print("Telegram App бот запущен.")
    app.run_polling()