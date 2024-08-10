import functools, os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from marketplace.db import get_db

bp = Blueprint('extra', __name__, url_prefix='/')
dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = dir_path + '/static'


@bp.route('about')
def about():
    return render_template('about.html')


@bp.route('my-account')
def my_acc():
    return render_template('my-account.html')


@bp.route('contact-us')
def contact_us():
    return render_template('contact-us.html')