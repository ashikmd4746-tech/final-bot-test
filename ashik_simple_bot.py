from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import string, os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_NAME = "Ashik"
BOT_WEBSITE = "https://en.wikipedia.org/wiki/Pro_Tools"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! আমি আপনার simple chatbot। প্রশ্ন জিজ্ঞেস করুন।")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.strip().lower()
    msg_clean = msg.translate(str.maketrans('', '', string.punctuation))
    if "আপনার নাম কি" in msg_clean:
        reply = f"আমার নাম {BOT_NAME}"
    elif "আপনার website" in msg_clean:
        reply = f"My website URL: {BOT_WEBSITE}"
    elif any(greet in msg_clean for greet in ["hi","hello","hey","হাই","হ্যালো"]):
        reply = "Hello! কেমন আছেন?"
    else:
        reply = "দুঃখিত, আমি শুধু basic প্রশ্নের উত্তর দিতে পারি। 😅"
    await update.message.reply_text(reply)

if name == "main":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    print("Bot is running...")
    app.run_polling()
