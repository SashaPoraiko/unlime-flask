from sqlalchemy.orm import relationship
from core.app import db


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    asin = db.Column(db.String(255), unique=True)

    reviews = relationship('Review')


class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    review = db.Column(db.Text())

    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
