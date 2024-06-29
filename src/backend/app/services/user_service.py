from app.models.user_model import User
from app.db import db

class UserService:
    @staticmethod
    def get_all_users():
        return [user.to_dict() for user in User.query.all()]

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.get(user_id)
        return user.to_dict() if user else None

    @staticmethod
    def create_user(data):
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict()
