from flask import jsonify, request, Blueprint
from sqlalchemy.orm import joinedload

from core.db import db
from core.models import Product, Review
from core.v1.schemas import ReviewCreateModel, ProductGetModel

product_reviews = Blueprint('product_reviews', __name__)


@product_reviews.route('/products')
def get_product():
    page = request.args.get('page', 1, type=int)
    try:
        product_id = int(request.args.get('product_id'))
    except Exception:
        product_id = None

    if product_id:
        product = Product.query \
            .options(joinedload(Product.reviews)) \
            .get(product_id)

        if product is None:
            return jsonify({"error": f"Product with ID {product_id} not found"}), 404

        product_data = ProductGetModel.from_orm(product).dict()
        return jsonify(product_data)

    else:
        products = Product.query \
            .options(joinedload(Product.reviews)).paginate(page=page, per_page=4)

        products_data = [ProductGetModel.from_orm(product).dict() for product in products]
        return jsonify(products_data)


@product_reviews.route('/make-review', methods=['POST'])
def make_review():
    data = request.json
    ReviewCreateModel.validate(data)
    product = Product.query.get(data['product_id'])
    if not product:
        return jsonify({"error": f"Product with ID {data['product_id']} not found"}), 404

    review = Review(title=data['title'], product_id=data['product_id'], review=data['review'])
    db.session.add(review)
    db.session.commit()

    return jsonify({"review": "Object created"}), 201
