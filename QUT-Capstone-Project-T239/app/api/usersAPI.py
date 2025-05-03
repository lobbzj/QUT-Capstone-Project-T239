from flask import Blueprint, jsonify, request
from app.models import db, User

api_users_bp = Blueprint('api_users', __name__, url_prefix='/api/users')

# Get all users
@api_users_bp.route('/', methods=['GET'])
def get_users():
    users = db.session.scalars(db.select(User)).all()
    return jsonify([{
        'id': u.id,
        'name': u.name,
        'email': u.email,
        'mobile': u.mobile,
        'member_type': u.member_type,
        'address': u.address
    } for u in users])

# Create a new user
@api_users_bp.route('/', methods=['POST'])
def create_user():
    json_data = request.get_json()
    if not json_data:
        return jsonify(message='No input data provided'), 400
    
    user = User(
        name=json_data['name'],
        email=json_data['email'],
        password_hash=json_data['password'],
        mobile=json_data.get('mobile'),
        member_type=json_data.get('member_type', 'regular'),
        address=json_data.get('address')
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(message='User created', user_id=user.id), 201

# Update an existing user
@api_users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = db.session.get(User, user_id)
    if not user:
        return jsonify(message='User not found'), 404
    
    json_data = request.get_json()
    user.name = json_data.get('name', user.name)
    user.email = json_data.get('email', user.email)
    user.mobile = json_data.get('mobile', user.mobile)
    user.address = json_data.get('address', user.address)
    user.member_type = json_data.get('member_type', user.member_type)

    db.session.commit()
    return jsonify(message='User updated'), 200

# Delete a user
@api_users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = db.session.get(User, user_id)
    if not user:
        return jsonify(message='User not found'), 404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify(message='User deleted'), 200

def user_to_dict(user):
    return {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'mobile': user.mobile,
        'member_type': user.member_type,
        'address': user.address
    }
