from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'product'
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_id = db.Column(db.Integer, db.ForeignKey('product_category.category_id'))
    product_name = db.Column(db.String(100), nullable=False)
    product_code = db.Column(db.String(30), nullable=False)
    product_description = db.Column(db.Text)
    product_image = db.Column(db.String(100))
    product_price = db.Column(db.Float, nullable=False)

    def __init__(self, product_name, product_code, product_description, product_image, product_price, category_id):
        self.product_name = product_name
        self.product_code = product_code
        self.product_description = product_description
        self.product_image = product_image
        self.product_price = product_price
        self.category_id = category_id

    def __repr__(self):
        return f"{self.product_name}"


class ProductCategory(db.Model):
    __tablename__ = 'product_category'

    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(30), nullable=False)
    size_metric = db.Column(db.String(30), nullable=False)
    products = db.relationship('Product', backref='products')

    def __init__(self, category_id, category_name, size_metric):
        self.category_id = category_id
        self.category_name = category_name
        self.size_metric=size_metric

    def __repr__(self):
        return f"{self.category_id} - {self.category_name}"

class Size(db.Model):
    __tablename__ = 'category_size'

    size_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_id = db.Column(db.Integer, db.ForeignKey('product_category.category_id'))
    size = db.Column(db.String(20))
    value = db.Column(db.String(30))


    def __init__(self, category_id, size, value):
        self.category_id = category_id
        self.size = size
        self.value = value

    def __repr__(self):
        return f"{self.size} - {self.value}"

class Messages(db.Model):
    __tablename__ = 'message'
    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100))
    message = db.Column(db.String(512))

    def __init__(self, email, message):
        self.email = email
        self.message = message

    def __repr__(self):
        return f"{self.email}"