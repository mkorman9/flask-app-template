import atexit
import os

import gevent

from webapp.base import create_app_base
from webapp.logger import log

gevent.get_hub().exception_stream = None

app = create_app_base(__name__)


# register app endpoints


def on_startup():
    log.info('✅ Worker is ready (PID=%d)', os.getpid())


def on_shutdown():
    log.info('⛔ Worker is shutting down (PID=%d)', os.getpid())


on_startup()
atexit.register(on_shutdown)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
