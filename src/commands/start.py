from telegram import Update
from telegram.ext import ContextTypes


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Olá! Eu sou o bot do Armarinho TPV.\n\n"
        "Para gerar um QRcode, basta colar a mensagem que você recebeu da portaria "
        "ou o código diretamente neste chat, e eu cuidarei do resto! #️⃣"
    )
