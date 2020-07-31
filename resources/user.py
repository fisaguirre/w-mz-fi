from flask import Response, request
from database.models import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

class UsersApi(Resource):
    def get(self):
        query = User.objects()
        users = User.objects().to_json()
        print ("el id es: ")
        print (get_jwt_identity())
        return Response(users, mimetype="application/json", status=200)
    
class UserApi(Resource):
    """@jwt_required"""
    def delete(self, id):
        user_jwt = get_jwt_identity()
        """con get_jwt_identity obtengo el JWT del endpoint"""
        user = User.objects(id=id).delete()
        user = User.objects(id=id).delete()
        return '', 200

    """@jwt_required"""
    def get(self, id):
        user = User.objects.get(id=id).to_json()
        return Response(user, mimetype="application/json", status=200)


