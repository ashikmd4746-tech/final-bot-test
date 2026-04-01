from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import string, os

# Environment variable থেকে token নাও
BOT_TOKEN = os.environ.get("BOT_TOKEN")

BOT_NAME = "Ashik"
BOT_WEBSITE = "https://en.wikipedia.org/wiki/Pro_Tools"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! আমি আপনার simple chatbot 🤖\nআপনি আমাকে প্রশ্ন করতে পারেন!"
    )

# message handler
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.strip().lower()
    msg_clean = msg.translate(str.maketrans('', '', string.punctuation))

    if "আপনার নাম কি" in msg_clean:
        reply = f"আমার নাম {BOT_NAME} 🤖"

    elif "website" in msg_clean:
        reply = f"My website URL:\n{BOT_WEBSITE}"

    elif any(greet in msg_clean for greet in ["hi", "hello", "hey", "হাই", "হ্যালো"]):
        reply = "Hello! 😊 কেমন আছেন?"

    elif "কেমন আছ" in msg_clean:
        reply = "আমি ভালো আছি 😄 আপনি কেমন আছেন?"

    else:
        reply = "দুঃখিত 😅 আমি এখনো limited chatbot। সহজ প্রশ্ন করুন।"

    await update.message.reply_text(reply)

# main run
if __name__ == "__main__":
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN not found! Render environment-এ add করো")
        exit()

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("✅ Bot is running...")
    app.run_polling()
