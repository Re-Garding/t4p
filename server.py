"""Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db
from crud import * 
from pprint import pprint
from jinja2 import StrictUndefined
from inventory import get_inventory
from word2number import w2n
from singleItem import get_item_info

app = Flask(__name__)
app.secret_key = "dev"
# app.jinja_env.undefined = StrictUndefined



@app.route('/')
def home():
    items = get_items()

    return render_template('home.html', items=items)



@app.route('/contact')
def contact_owner():
    return


@app.route('/admin/view_inventory')
def view_inventory():
    
    return render_template('inventory.html')

@app.route('/admin/edit/<item_id>')
def edit_item(item_id):

    int_id = w2n.word_to_num(item_id)
    item = get_item_info(int_id)
    pprint(item)
    return render_template("/edit_item.html", item=item)


@app.route("/admin/add_items")
def add_items():
    return render_template("/add_items.html")




@app.route('/inventory')
def inventory():
    """pulls all inventory from db and sorts objects into a dictionary
    for rendering into json
    
    can be found in inventory.py -- separated for ease of reading server.py"""
    return jsonify(get_inventory())




if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
