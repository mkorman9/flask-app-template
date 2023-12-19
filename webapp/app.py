from webapp.base import create_app_base

app = create_app_base(__name__)


# register app endpoints


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
