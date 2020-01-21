from flask import Blueprint,redirect,url_for,request,render_template
from flask_login import login_required


accounts = Blueprint('accounts',__name__,template_folder='templates/Accounts')

@login_required
@accounts.route('/home',methods=['GET','POST'])
def home():
    return render_template('accounts_home.html')