from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from src.config import Config
import src.commands as commands
import src.handlers as handlers


if __name__ == "__main__":
    print("Starting bot...")

    app = Application.builder().token(Config.TOKEN).build()

    # Comamands
    app.add_handler(CommandHandler("start", commands.start_command))
    app.add_handler(CommandHandler("help", commands.help_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handlers.handle_message))

    # Error Handler
    app.add_error_handler(handlers.error_handler)

    # Start polling
    print("Bot is running...")
    app.run_polling(poll_interval=3)
