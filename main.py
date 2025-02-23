from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from src.config import Config
import src.commands as commands
import src.handlers as handlers

from loguru import logger
logger.add("./logs/file_{time}.log", rotation="1 MB", retention="10 days", level="DEBUG")


if __name__ == "__main__":
    print("Starting bot...")

    app = ApplicationBuilder()\
        .token(Config.TOKEN)\
        .connect_timeout(30)\
        .connection_pool_size(8)\
        .read_timeout(30)\
        .write_timeout(30)\
        .get_updates_read_timeout(30)\
        .get_updates_write_timeout(30)\
        .media_write_timeout(30)\
        .build()

    # Comamands
    app.add_handler(CommandHandler("start", commands.start_command))
    app.add_handler(CommandHandler("help", commands.help_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handlers.handle_message))

    # Error Handler
    app.add_error_handler(handlers.error_handler)

    # Start polling
    print("Bot is running...")
    app.run_polling(poll_interval=3, timeout=30)
