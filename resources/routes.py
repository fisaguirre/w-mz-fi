from .auth import SignupApi, LoginApi
from .user import UsersApi, UserApi

def initialize_routes(api):
    api.add_resource(SignupApi, '/signup')
    api.add_resource(LoginApi, '/login')

    api.add_resource(UsersApi, '/user/')
    api.add_resource(UserApi, '/user/<id>')
