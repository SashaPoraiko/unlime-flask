import csv
from core.app import db, app
from core.models import Product, Review


def fill_the_products(file_path):
    with app.app_context():
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                title = row['Title']
                asin = row['Asin']
                product = Product(title=title, asin=asin)

                db.session.add(product)

        db.session.commit()


def fill_the_reviews(file_path):
    with app.app_context():
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)

            for row in csv_reader:
                title = row['Title']
                asin = row['Asin']
                review = row['Review']

                product = Product.query.filter_by(asin=asin).first()
                if not product:
                    continue

                review = Review(title=title, product_id=product.id, review=review)
                db.session.add(review)

        db.session.commit()


if __name__ == "__main__":
    products_csv = "Products.csv"
    fill_the_products(products_csv)

    reviews_csv = 'Reviews.csv'
    fill_the_reviews(reviews_csv)
