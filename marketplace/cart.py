from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from marketplace.db import get_db
from marketplace.auth import login_required

bp = Blueprint('cart', __name__)

@bp.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    if request.method == 'POST':
        print("Hi")
        fnm = request.form['firstName']
        lnm = request.form['lastName']
        unm = request.form['username']
        eml = request.form['email']
        ad1 = request.form['address']
        ad2 = request.form['address2']
        cnt = request.form['country']
        stt = request.form['state']
        zip = request.form['zip']
        sad = request.form.get('same-address')
        pay = request.form.get('paymentMethod')
        db = get_db()
        db.execute(
            'INSERT INTO orders (fnm, lnm, unm, eml, ad1, ad2, cnt, stt, zip, sad, pay) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (fnm, lnm, unm, eml, ad1, ad2, cnt, stt, zip, sad, pay)
        )
        db.commit()
    return render_template('checkout.html')
