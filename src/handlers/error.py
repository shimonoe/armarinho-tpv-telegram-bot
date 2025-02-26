from telegram import Update
from telegram.ext import ContextTypes
from loguru import logger


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"An error occurred: {context.error}")
    await update.message.reply_text(
        "Ops! Parece que algo deu errado. 😅\n\n"
        "Verifique se a mensagem que você copiou está no formato "
        "correto ou o código tem 6 caracteres. 📦"
    )
