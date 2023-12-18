import atexit
import os

from gevent import get_hub

from webapp.base import create_app_base

get_hub().exception_stream = None

app = create_app_base(__name__)


# register app endpoints


def on_startup():
    print(f'✅ Worker is ready (PID={os.getpid()})')


def on_shutdown():
    print(f'⛔ Worker is shutting down (PID={os.getpid()})')


on_startup()
atexit.register(on_shutdown)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
