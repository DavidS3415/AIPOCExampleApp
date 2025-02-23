from flask import Blueprint, render_template
from app.controllers.user_controller import UserController

user_bp = Blueprint('user', __name__)

user_bp.route('/users', methods=['GET'])(UserController.get_all_users)
user_bp.route('/users/<int:user_id>', methods=['GET'])(UserController.get_user)
user_bp.route('/users', methods=['POST'])(UserController.create_user)

@user_bp.route('/test', methods=['GET'])
def view_users():
    return render_template('users.html')
