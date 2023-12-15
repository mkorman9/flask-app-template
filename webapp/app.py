import atexit
import os

from webapp.flask_base import create_base_app

app = create_base_app()


def on_startup():
    print(f'✅ Worker #{os.getpid()} is ready')


def on_shutdown():
    print(f'⛔ Worker #{os.getpid()} is shutting down')


# register app endpoints


on_startup()
atexit.register(on_shutdown)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
