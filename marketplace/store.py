from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
import os
from werkzeug.utils import secure_filename

from marketplace.auth import login_required, seller_only
from marketplace.db import get_db
bp = Blueprint('store', __name__)
print(os.path.dirname(os.path.realpath(__file__)), __file__)
dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = dir_path + '/static/img'

@bp.route('/')
def index():
    if not g.user:
        return redirect(url_for('auth.login'))
    db = get_db()
    items = db.execute(
        'SELECT i.id, i.item_name, i.item_description, i.item_image, i.price'
        ' FROM item i'
    ).fetchall()
    return render_template('index.html', items=items)


@bp.route('/shop-detail', methods=['GET', 'POST'])
def shop_details():
    if request.method() == 'POST':
        db = get_db()
        db.execute(
            'INSERT INTO cart (user_id, item_id)'
            ' VALUES (?, ?)',
            (g.user['id'], item_id)
        )
        db.commit()
        flash("Item successfully added to cart", 'success')
    return render_template('shop-detail.html')


@bp.route('/shop')
def shop():
    return render_template('shop.html')

@bp.route('/cart')
def cart():
    return render_template('cart.html')


@bp.route('/create', methods=('GET', 'POST'))
@login_required
@seller_only
def create():
    if request.method == 'POST':
        item_name = request.form["name"]
        item_description = request.form["description"]
        item_image = request.files["image"]
        price = request.form["price"]

        if item_image:
            secure_filename(item_image.filename)
            item_image.save(os.path.join(UPLOAD_FOLDER, item_image.filename))

        if not item_name:
            error = 'Title is required.'
            flash(error)
        else :
            db = get_db()
            db.execute(
                'INSERT INTO item (item_name, item_description, item_image, price)'
                ' VALUES (?, ?, ?, ?)',
                (item_name, item_description, item_image.filename, price)
            )
            db.commit()
            flash(item_name + ' was added to the store', 'success')

    return render_template('create.html')


"""
@bp.route('/delete_cart_item/<int:item_id>', methods=['POST'])
@login_required
@seller_only
def delete(item_id):
    db = get_db()
    db.execute('DELETE FROM item WHERE id = ?', [item_id])
    db.commit()
    return redirect(url_for('store.index'))"""