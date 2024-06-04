from flask import Flask
from flask_migrate import Migrate
from core.db import db
from core.v1.views import product_reviews

app = Flask(__name__)
app.register_blueprint(product_reviews)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@db:5432'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
