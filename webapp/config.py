import logging
import os
import sys
from typing import Optional

from dotenv import load_dotenv
from pydantic import ValidationError, BaseModel


class ConfigModel(BaseModel):
    pass


_config: Optional[ConfigModel] = None


def get_config():
    global _config

    if not _config:
        try:
            load_dotenv()
            _config = ConfigModel(**os.environ)
        except ValidationError as e:
            logging.error('🚫 Failed to load configuration', exc_info=e)
            sys.exit(4)

    return _config
