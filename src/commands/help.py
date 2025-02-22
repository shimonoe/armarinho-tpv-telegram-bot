from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Precisa de ajuda? 😉\n\n"
        "É simples! Envie o código que você recebeu (ou a mensagem completa da portaria) "
        "e eu gero o QR Code para você usar no armário. 📦\n\n"
        "Tudo feito com segurança e sem guardar seus dados! 🔒"
    )
