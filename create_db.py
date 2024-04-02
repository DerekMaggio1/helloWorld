from app import app, db
from models import Product, ProductCategory, Messages, Size

with app.app_context():
    db.drop_all()
    db.create_all()

    # Initial loading of product categories
    product_categories = [
        {'category_id': 1, 'category_name': 'Hats', 'size_metric': 'Circumference(in)'},
        {'category_id': 2, 'category_name': 'Shirts', 'size_metric': 'Chest'},
        {'category_id': 3, 'category_name': 'Pants', 'size_metric': 'Waist'},
    ]

    for each_product_category in product_categories:
        print(f'{each_product_category["category_name"]} inserted into product_category')
        a_product_category = ProductCategory(category_id=each_product_category['category_id'],
                                             category_name=each_product_category['category_name'],
                                             size_metric=each_product_category['size_metric'])
        db.session.add(a_product_category)
        db.session.commit()

    # Initial loading of products
    products = [
        {'product_name':'Red Hat', 'product_code':'PROD-0555', 'product_description':'Show your Terp spirit by wearing this stylish Red hat.',
            'product_image':'PROD-0555-hat_red.jpg', 'product_price':12.95, 'category_id': 1},
        {'product_name': 'Black Hat', 'product_code': 'PROD-0777',
         'product_description': 'Don\'t let a bad hair day hold you back from cheering on the Terps! This hat is your cap-tain solution for stylish team spirit.',
         'product_image': 'PROD-0777-hat_black.jpg', 'product_price': 14.99, 'category_id': 1},
        {'product_name': 'Men\'s Terrapin Shirt', 'product_code': 'PROD-0123', 'product_description': 'This Men\'s Maryland Terrapin shirt is your shell-ter for spontaneous beach weekend getaways!',
            'product_image': 'PROD-0123-shirt.jpg', 'product_price':39.99, 'category_id': 2},
        {'product_name': 'Boracay Shorts', 'product_code': 'PROD-0987', 'product_description': 'Skip the chips and dips, and rock your beach trips! These shorts are perfect for cheering on the team!',
            'product_image': 'PROD-0987-shorts.png', 'product_price':25.49, 'category_id': 3},
    ]

    for each_product in products:
        print(f'{each_product["product_name"]} inserted into product')
        a_product = Product(product_name=each_product['product_name'], product_code=each_product['product_code'],
                            product_description=each_product['product_description'], product_image=each_product['product_image'],
                            product_price=each_product['product_price'], category_id=each_product['category_id'])
        db.session.add(a_product)
        db.session.commit()

    category_sizes = [
        {'category_id': 1, 'size': 'S/M', 'value': '20.8 - 21.5'},
        {'category_id': 1, 'size': 'M/L', 'value': '22 - 23'},
        {'category_id': 1, 'size': 'L/XL', 'value': '23 - 24.2'},
        {'category_id': 2, 'size': 'S', 'value': '34.5 - 36'},
        {'category_id': 2, 'size': 'M', 'value': '36.5 - 40'},
        {'category_id': 2, 'size': 'L', 'value': '40.5 - 44'},
        {'category_id': 2, 'size': 'XL', 'value': '44.5 - 48'},
        {'category_id': 3, 'size': 'S', 'value': '28-30'},
        {'category_id': 3, 'size': 'M', 'value': '31-33'},
        {'category_id': 3, 'size': 'L', 'value': '34-36'},
    ]

    for each_category_size in category_sizes:
        print(f'{each_category_size["size"]} for Category {each_category_size["category_id"]} inserted into size')
        a_size = Size(size=each_category_size['size'], value=each_category_size['value']
                            , category_id=each_category_size['category_id'])
        db.session.add(a_size)
        db.session.commit()