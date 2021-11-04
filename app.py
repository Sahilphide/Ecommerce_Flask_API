from typing import AnyStr
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import *
from modal import *
from flask import jsonify, request, Response


@app.route('/home')
def home():
    return "hello, you are on home route choose product, order or user rout to know more about this and their apis"

# ----product route------------


@app.route('/product', methods=['GET'])
def get_product():
    '''Function to get all the movies in the database'''
    return jsonify({'Product': Product.get_all_product()})


@app.route('/product/<int:productid>', methods=['GET'])
def get_product_by_id(productid):
    return_value = Product.get_product(productid)
    return jsonify(return_value)


@app.route('/product', methods=['POST'])
def add_product():
    '''Function to add new movie to our database'''
    request_data = request.get_json()  # getting data from client(in this case from postman)
    Product.add_product(request_data["product_name"], request_data["price"],
                        request_data["quantity"])
    response = Response("Product added", 201, mimetype='application/json')
    return response


@app.route('/product/<int:productid>', methods=['PUT'])
def update_product(productid):
    '''Function to edit movie in our database using movie id'''
    request_data = request.get_json()
    Product.update_product(
        productid, request_data['product_name'], request_data['price'], request_data['quantity'])
    response = Response("Product Updated", status=200,
                        mimetype='application/json')
    return response


@app.route('/product/<int:productid>', methods=['DELETE'])
def remove_product(productid):
    Product.delete_product(productid)
    response = Response("Product Deleted", status=200,
                        mimetype='application/json')
    return response


# -----------user route-----------


@app.route('/user', methods=['GET'])
def get_user():
    '''Function to get all the movies in the database'''
    return jsonify({'User': User.get_all_user()})


@app.route('/user/<int:userid>', methods=['GET'])
def get_user_by_id(userid):
    return_value = User.get_user(userid)
    return jsonify(return_value)


@app.route('/user', methods=['POST'])
def add_user():
    '''Function to add new movie to our database'''
    request_data = request.get_json()  # getting data from client(in this case from postman)
    User.add_user(request_data["user_name"], request_data["email"],
                  request_data["password"])
    response = Response("user added", 201, mimetype='application/json')
    return response


@app.route('/user/<int:userid>', methods=['PUT'])
def update_user(userid):
    '''Function to edit movie in our database using movie id'''
    request_data = request.get_json()
    User.update_user(
        userid, request_data['user_name'], request_data['email'], request_data['password'])
    response = Response("User Updated", status=200,
                        mimetype='application/json')
    return response


@app.route('/user/<int:userid>', methods=['DELETE'])
def remove_user(userid):
    User.delete_user(userid)
    response = Response("User Deleted", status=200,
                        mimetype='application/json')
    return response


# ---------order routes------------


@app.route('/order', methods=['GET'])
def get_order():
    '''Function to get all the movies in the database'''
    return jsonify({'Order': Order.get_all_order()})


@app.route('/order/<int:orderid>', methods=['GET'])
def get_order_by_id(orderid):
    return_value = Order.get_order(orderid)
    return jsonify(return_value)


@app.route('/order', methods=['POST'])
def add_order():
    '''Function to add new movie to our database'''
    request_data = request.get_json()  # getting data from client(in this case from postman)
    Order.add_order(request_data["product_name"], request_data["product_price"],
                    request_data["ordered_on"])
    response = Response("order placed", 201, mimetype='application/json')
    return response


@app.route('/order/<int:orderid>', methods=['PUT'])
def update_order(orderid):
    '''Function to edit movie in our database using movie id'''
    request_data = request.get_json()
    Order.update_order(
        orderid, request_data['product_name'], request_data['product_price'], request_data['ordered_on'])
    response = Response("order Updated", status=200,
                        mimetype='application/json')
    return response


@app.route('/order/<int:orderid>', methods=['DELETE'])
def remove_order(orderid):
    Order.delete_order(orderid)
    response = Response("order Deleted", status=200,
                        mimetype='application/json')
    return response


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
