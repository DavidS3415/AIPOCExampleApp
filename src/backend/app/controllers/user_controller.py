from flask import jsonify, request
from app.services.user_service import UserService

class UserController:
    @staticmethod
    def get_all_users():
        users = UserService.get_all_users()
        return jsonify(users)

    @staticmethod
    def get_user(user_id):
        user = UserService.get_user_by_id(user_id)
        if user:
            return jsonify(user)
        else:
            return jsonify({'message': 'User not found'}), 404

    @staticmethod
    def create_user():
        data = request.get_json()
        user = UserService.create_user(data)
        return jsonify(user), 201
