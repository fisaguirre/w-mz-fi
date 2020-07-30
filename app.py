from flask import Flask, app


default_config = {'MONGODB_SETTINGS': {
    'db': 'w_mz_fi',
    'host': 'localhost',
    'port': 27017,
    'username': 'admin',
    'password': 'password',
    'authentication_source': 'admin'}}


def get_flask_app(config: dict = None) -> app.Flask:
    flask_app = Flask(__name__)

    config = default_config if config is None else config
    flask_app.config.update(config)

    return flask_app

if __name__ == '__main__':
    app = get_flask_app()
    app.run(debug=True)