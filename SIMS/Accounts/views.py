from flask import Blueprint,redirect,url_for,request,render_template
from flask_login import login_required
from SIMS.Accounts.forms import Amount_add,Miscellaneous
from SIMS.models import Accounts
from SIMS import db
from SIMS.Accounts.table import Miscellaneous_table
import datetime
import calendar


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


def miscellaneous_value():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    days = calendar.monthrange(year,month)[1]
    start_date = datetime.date(year,month,1)
    end_date = datetime.date(year,month,days)
    miscellaneous_values = Accounts.query.filter(Accounts.date >= start_date,Accounts.date <=end_date).filter(Accounts.category=='Miscellaneous').order_by(Accounts.date).all()
    expense_message = []
    expense_date = []
    expense_amount = []
    for i in miscellaneous_values:
        expense_message.append(i.message)
        expense_amount.append(i.amount)
        expense_date.append(i.date)
    return expense_amount,expense_date,expense_message


@login_required
@accounts_home.route('/home/Miscellaneous',methods=['GET','POST'])
def miscellaneous():
    form = Miscellaneous()
    amount,date,message=miscellaneous_value()
    colors = ['#666547','#fb2e01','#21bf73','#ffcc00','#ffe28a','#f65c78']
    if form.validate_on_submit():
        miscellaneous_entries = Accounts.query.filter(Accounts.date >= form.starting_date.data,Accounts.date <=form.ending_date.data).filter(Accounts.category=='Miscellaneous').order_by(Accounts.date).limit(10).all()
        miscellaneous_table = Miscellaneous_table(miscellaneous_entries,classes=['table','table-hover'])
        return render_template('accounts_miscellaneous.html',values = zip(message,amount,date),date=date,amount=amount,colors=colors,form=form,miscellaneous_table=miscellaneous_table)
    return render_template('accounts_miscellaneous.html',values = zip(message,amount,date),date=date,amount=amount,
    colors=colors,form=form)


def cash_value():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    days = calendar.monthrange(year,month)[1]
    start_date = datetime.date(year,month,1)
    end_date = datetime.date(year,month,days)
    miscellaneous_values = Accounts.query.filter(Accounts.date >= start_date,Accounts.date <=end_date).filter(Accounts.category=='Cash').order_by(Accounts.date).all()
    expense_message = []
    expense_date = []
    expense_amount = []
    for i in miscellaneous_values:
        expense_message.append(i.message)
        expense_amount.append(i.amount)
        expense_date.append(i.date)
    return expense_amount,expense_date,expense_message

@login_required
@accounts_home.route('/home/Cash',methods=['GET','POST'])
def cash():
    amount,date,message=cash_value()
    colors = ['#666547','#fb2e01','#21bf73','#ffcc00','#ffe28a','#f65c78']
    return render_template('accounts_cash.html',values = zip(message,amount,date),date=date,amount=amount,colors=colors)