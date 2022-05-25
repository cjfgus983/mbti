from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect

from pybo.models import Question

import os
from flask import send_from_directory

bp = Blueprint('main',__name__,url_prefix='/')
@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return render_template('mainpage/mainpage.html')

@bp.route('/introduce')
def introduce():
    return render_template('category/introduce.html')