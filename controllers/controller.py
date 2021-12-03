from app import app
from flask import render_template
from models.items_list import items
from models.item import *


@app.route('/items')
def index():
    return render_template('index.html', items=items)
