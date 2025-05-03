from flask import Blueprint, request, jsonify
from app.models import db, Product

api_products_bp = Blueprint('api_products', __name__, url_prefix='/api/products')

@api_products_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = [product_to_dict(p) for p in products]
    return jsonify(products=product_list)

@api_products_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product=product_to_dict(product))

@api_products_bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product(
        name=data['name'],
        description=data['description'],
        image=data['image'],
        price=data['price'],
        stock=data['stock'],
        category=data['category'],
        sub_category=data['sub_category']
    )
    db.session.add(product)
    db.session.commit()
    return jsonify(message='Product created', product=product_to_dict(product)), 201

@api_products_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.stock = data.get('stock', product.stock)
    db.session.commit()
    return jsonify(message='Product updated', product=product_to_dict(product))

@api_products_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify(message='Product deleted')

def product_to_dict(product):
    return {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'image': product.image,
        'price': product.price,
        'stock': product.stock,
        'category': product.category,
        'sub_category': product.sub_category
    }
