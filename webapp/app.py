import atexit
import os

from webapp.flask_base import create_base_app

app = create_base_app()


def on_startup():
    print(f'✅ Worker is ready (PID={os.getpid()})')


def on_shutdown():
    print(f'⛔ Worker is shutting down (PID={os.getpid()})')


# register app endpoints


on_startup()
atexit.register(on_shutdown)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
