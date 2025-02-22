from telegram import Update
from telegram.ext import ContextTypes


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"An error occurred: {context.error}")
    await update.message.reply_text(
        "Ops! Parece que algo deu errado. 😅\n\n"
        "Verifique se a mensagem que você copiou está no formato "
        "correto ou o código tem 6 caracteres. 📦"
    )
