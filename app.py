from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import time
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/w_mz_fi'
}
initialize_db(app)
initialize_routes(api)

app.run()