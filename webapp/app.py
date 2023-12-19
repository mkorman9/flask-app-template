from webapp.flask_base_app import create_flask_base_app
from webapp.config import get_config
from webapp.logger import configure_logger

configure_logger()
_ = get_config()

app = create_flask_base_app(__name__)


# register app endpoints


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
