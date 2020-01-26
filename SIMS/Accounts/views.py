from flask import Blueprint,redirect,url_for,request,render_template
from flask_login import login_required
from SIMS.Accounts.forms import Amount_add
from SIMS.models import Accounts
from SIMS import db


accounts_home = Blueprint('accounts_home',__name__,template_folder='templates/Accounts')

def getvalues():
    mis_value = Accounts.query.filter_by(category='Miscellaneous').all()
    cash_value = Accounts.query.filter_by(category='Cash').all()
    prof_value = Accounts.query.filter_by(category='Profit').all()
    proj_value = Accounts.query.filter_by(category='Project Payment').all()
    fixed_value = Accounts.query.filter_by(category='Fixed Payment').all()
    raw_value = Accounts.query.filter_by(category='Raw Material').all()
    mis = 0
    for i in mis_value:
        mis = mis+i.amount
    cash = 0
    for i in cash_value:
        cash = cash+i.amount
    prof = 0
    for i in prof_value:
        prof = prof+i.amount
    proj = 0
    for i in proj_value:
        proj = proj+i.amount
    fixed = 0
    for i in fixed_value:
        fixed = fixed+i.amount
    raw = 0
    for i in raw_value:
        raw = raw+i.amount
    values = [mis,cash,prof,proj,fixed,raw]
    table_values = {'Miscellaneous':mis,'Cash':cash,'Profit':prof,'Project Payment':proj,'Fixed Payment':fixed,'Raw Material':raw}
    return values,table_values

@login_required
@accounts_home.route('/home',methods=['GET','POST'])
def home():
    values,table_values = getvalues()
    form = Amount_add()
    legend = 'Monthly Data'
    colors = ['#666547','#fb2e01','#21bf73','#ffcc00','#ffe28a','#f65c78']
    labels = ["Miscellaneous", "Cash", "Profit", "Project Payment", "Fixed Payment", "Raw Material"]
    if form.validate_on_submit():
        expense = Accounts(amount=form.amount.data,message=form.expense_message.data,category=form.category.data,date=form.date.data)
        db.session.add(expense)
        db.session.commit()
        #date = form.date.data
        #print(type(date))
        
        return redirect(url_for('accounts_home.home'))
    return render_template('accounts_home.html',legend=legend,labels=labels,colors=colors,form=form,values=values,table_values=table_values)

@login_required
@accounts_home.route('/home/Miscellaneous',methods=['GET','POST'])
def miscellaneous():
    pass