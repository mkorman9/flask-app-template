from webapp.base import create_base_app

app = create_base_app()



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
