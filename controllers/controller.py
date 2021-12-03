from app import app
from flask import render_template, request
from models.items_list import items, add_new_item
from models.item import *


@app.route('/items')
def index():
    return render_template('index.html', items=items)


@app.route('/items', methods=['POST'])
def add_item():
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']
    bought = True if 'bought' in request.form else False
    new_item = Item(name, price, quantity, bought)
    add_new_item(new_item)
    return render_template('index.html', items=items)
