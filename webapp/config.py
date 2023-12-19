import logging
import os
import sys

from dotenv import load_dotenv
from pydantic import ValidationError, BaseModel

from webapp import logger


class ConfigModel(BaseModel):
    pass


try:
    load_dotenv()
    logger.configure_logger(os.getenv('LOG_LEVEL', 'INFO'))
    config = ConfigModel(**os.environ)
except ValidationError as e:
    logging.error('🚫 Failed to load configuration', exc_info=e)
    sys.exit(4)
