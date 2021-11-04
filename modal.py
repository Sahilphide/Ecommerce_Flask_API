from settings import *
import json
from datetime import datetime

# Initializing database
db = SQLAlchemy(app)


class Product(db.Model):
    __tablename__ = 'product'
    productid = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.DECIMAL)
    quantity = db.Column(db.Integer, nullable=False)

    def json(self):
        return {'productid': self.productid, 'product_name': self.product_name,
                'price': self.price, 'quantity': self.quantity}

    def add_product(_product_name, _price, _quantity):

        new_product = Product(product_name=_product_name,
                              price=_price, quantity=_quantity)
        db.session.add(new_product)
        db.session.commit()

    def get_all_product():
        return [Product.json(product) for product in Product.query.all()]

    def get_product(_productid):

        return [Product.json(Product.query.filter_by(productid=_productid).first())]

    def update_product(_productid, _product_name, _price, _quantity):

        product_to_update = Product.query.filter_by(
            productid=_productid).first()
        product_to_update.product_name = _product_name
        product_to_update.price = _price
        product_to_update.quantity = _quantity
        db.session.commit()

    def delete_product(_productid):

        Product.query.filter_by(productid=_productid).delete()
        db.session.commit()


class User(db.Model):
    __tablename__ = 'user'
    userid = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def json(self):
        return {'userid': self.userid, 'user_name': self.user_name,
                'email': self.email, 'password': self.password}

    def add_user(_user_name, _email, _password):

        new_user = User(user_name=_user_name,
                        email=_email, password=_password)
        db.session.add(new_user)
        db.session.commit()

    def get_all_user():
        return [User.json(user) for user in User.query.all()]

    def get_user(_userid):

        return [User.json(User.query.filter_by(userid=_userid).first())]

    def update_user(_userid, _user_name, _email, _password):

        user_to_update = User.query.filter_by(
            userid=_userid).first()
        user_to_update.user_name = _user_name
        user_to_update.email = _email
        user_to_update.password = _password
        db.session.commit()

    def delete_user(_userid):

        User.query.filter_by(userid=_userid).delete()
        db.session.commit()


class Order(db.Model):
    __tablename__ = 'order'
    orderid = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    product_price = db.Column(db.Integer, nullable=False)
    ordered_on = db.Column(db.String(100), nullable=False,
                           default=datetime.utcnow)

    def json(self):
        return {'orderid': self.orderid, 'product_name': self.product_name,
                'product_price': self.product_price, 'order_on': self.ordered_on}

    def add_order(_product_name, _product_price, _ordered_on):

        new_order = Order(product_name=_product_name,
                          product_price=_product_price, ordered_on=_ordered_on)
        db.session.add(new_order)
        print(new_order)
        db.session.commit()

    def get_all_order():
        return [Order.json(order) for order in Order.query.all()]

    def get_order(_orderid):

        return [Order.json(Order.query.filter_by(orderid=_orderid).first())]

    def update_order(_orderid, _product_name, _product_price, _ordered_on):

        order_to_update = Order.query.filter_by(
            orderid=_orderid).first()
        order_to_update.product_name = _product_name
        order_to_update.product_price = _product_price
        order_to_update.order_on = _ordered_on
        db.session.commit()

    def delete_order(_orderid):

        Order.query.filter_by(orderid=_orderid).delete()
        db.session.commit()
