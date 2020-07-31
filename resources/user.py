from flask import Response, request
from database.models import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

class UsersApi(Resource):
    @jwt_required
    def get(self):
        users = User.objects().to_json()
        return Response(users, mimetype="application/json", status=200)
    
class UserApi(Resource):
    @jwt_required
    def delete(self, id):
        user = User.objects(id=id)
        if user.delete():
            return '', 200

    @jwt_required
    def get(self, id):
        user = User.objects.get(id=id).to_json()
        if user:
            return Response(user, mimetype="application/json", status=200)

