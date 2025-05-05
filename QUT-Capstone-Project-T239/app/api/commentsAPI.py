from flask import Blueprint, request, jsonify
from app.models import db, Comment

api_comments_bp = Blueprint('api_comments', __name__, url_prefix='/api/comments')

# Get all comments
@api_comments_bp.route('/', methods=['GET'])
def get_comments():
    comments = db.session.scalars(db.select(Comment)).all()
    return jsonify([{
        'id': c.id,
        'text': c.text,
        'created_at': c.created_at.isoformat(),
        'user_id': c.user_id,
        'product_id': c.product_id
    } for c in comments])

# Create a new comment
@api_comments_bp.route('/', methods=['POST'])
def create_comment():
    data = request.get_json()
    if not data:
        return jsonify(message='No input data provided'), 400
    
    # Optional: validate user/product exist
    comment = Comment(
        text=data['text'],
        user_id=data['user_id'],
        product_id=data['product_id']
    )
    db.session.add(comment)
    db.session.commit()
    return jsonify(message='Comment created', comment_id=comment.id), 201

# Update a comment
@api_comments_bp.route('/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    comment = db.session.get(Comment, comment_id)
    if not comment:
        return jsonify(message='Comment not found'), 404

    data = request.get_json()
    comment.text = data.get('text', comment.text)
    db.session.commit()
    return jsonify(message='Comment updated'), 200

# Delete a comment
@api_comments_bp.route('/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    comment = db.session.get(Comment, comment_id)
    if not comment:
        return jsonify(message='Comment not found'), 404

    db.session.delete(comment)
    db.session.commit()
    return jsonify(message='Comment deleted'), 200

def comment_to_dict(comment):
    return {
        'id': comment.id,
        'text': comment.text,
        'created_at': comment.created_at.isoformat(),
        'user_id': comment.user_id,
        'product_id': comment.product_id
    }
