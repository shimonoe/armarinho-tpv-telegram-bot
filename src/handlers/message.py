import re

from telegram import Update
from telegram.ext import ContextTypes

from src.config import Config
from src.helpers.qr_code import generate_qr_code

from loguru import logger


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    if message_type == "group" and Config.BOT_USERNAME in text:
        text_: str = text.replace(Config.BOT_USERNAME, "").strip()
        qr_code = handle_user_text(text_)
        await update.message.reply_photo(photo=qr_code)
    else:
        qr_code = handle_user_text(text)
        await update.message.reply_photo(photo=qr_code)


def handle_user_text(text: str) -> str:
    code: str = ""
    text_ = text.strip()
    if len(text_) == 6:
        code = text_
    elif "👉🏼" in text_:
        code = "".join(re.findall(r"\w", text_.split("👉🏼")[-1]))

    if not code.isalnum():
        raise ValueError(f"Invalid code format: {code}")

    logger.info(f"Generating QR Code for code: {code.upper()}")
    qr_code = generate_qr_code(code.upper())
    return qr_code
