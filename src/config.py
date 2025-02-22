import os
from dataclasses import dataclass
from typing import Final

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    """Configuration dataclass for the bot"""

    TOKEN: Final[str] = os.getenv("BOTFATHER_TOKEN")
    BOT_USERNAME: Final[str] = os.getenv("BOT_USERNAME")
