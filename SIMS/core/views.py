from flask import render_template,Blueprint
from flask_login import login_required

core = Blueprint('core',__name__)

@core.route('/')
def index():
    return render_template('index.html')

@core.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')