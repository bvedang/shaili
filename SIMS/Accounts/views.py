from flask import Blueprint,redirect,url_for,request,render_template
from flask_login import login_required
from SIMS.Accounts.forms import Amount_add,Genral_query
from SIMS.models import Accounts
from SIMS import db
from SIMS.Accounts.table import Miscellaneous_table
import datetime
import calendar
from SIMS.Accounts.required import getvalues,get_month,account_value
accounts_home = Blueprint('accounts_home',__name__,template_folder='templates/Accounts')

## HOME
@login_required
@accounts_home.route('/home',methods=['GET','POST'])
def home():
    month = get_month()
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
    return render_template('accounts_home.html',legend=legend,labels=labels,colors=colors,form=form,values=values,table_values=table_values,month=month)

## MISCELLANEOUS
@login_required
@accounts_home.route('/home/Miscellaneous',methods=['GET','POST'])
def miscellaneous():
    form = Genral_query()
    amount,date,message=account_value('Miscellaneous')
    colors = ['#666547','#fb2e01','#21bf73','#ffcc00','#ffe28a','#f65c78']
    if form.validate_on_submit():
        miscellaneous_entries = Accounts.query.filter(Accounts.date >= form.starting_date.data,Accounts.date <=form.ending_date.data).filter(Accounts.category=='Miscellaneous').order_by(Accounts.date).limit(10).all()
        miscellaneous_table = Miscellaneous_table(miscellaneous_entries,classes=['table','table-hover'])
        return render_template('accounts_miscellaneous.html',values = zip(message,amount,date),date=date,amount=amount,colors=colors,form=form,miscellaneous_table=miscellaneous_table)
    return render_template('accounts_miscellaneous.html',values = zip(message,amount,date),date=date,amount=amount,
    colors=colors,form=form)

## CASH
@login_required
@accounts_home.route('/home/Cash',methods=['GET','POST'])
def cash():
    form = Genral_query()
    amount,date,message=account_value('Cash')
    colors = ['#666547','#fb2e01','#21bf73','#ffcc00','#ffe28a','#f65c78']
    if form.validate_on_submit():
        cash_entries = Accounts.query.filter(Accounts.date >= form.starting_date.data,Accounts.date <=form.ending_date.data).filter(Accounts.category=='Cash').order_by(Accounts.date).limit(10).all()
        cash_table = Miscellaneous_table(cash_entries,classes=['table','table-hover'])
        return render_template('accounts_cash.html',values = zip(message,amount,date),date=date,amount=amount,colors=colors,form=form,cash_table=cash_table)
    return render_template('accounts_cash.html',values = zip(message,amount,date),date=date,amount=amount,colors=colors,form=form)

## Income
@login_required
@accounts_home.route('/home/income',methods=['GET','POST'])
def income():
    form = Genral_query()
    amount,date,message=account_value('Income')
    colors = ['#666547','#fb2e01','#21bf73','#ffcc00','#ffe28a','#f65c78']
    if form.validate_on_submit():
        income_entries = Accounts.query.filter(Accounts.date >= form.starting_date.data,Accounts.date <=form.ending_date.data).filter(Accounts.category=='Income').order_by(Accounts.date).limit(10).all()
        income_table = Miscellaneous_table(income_entries,classes=['table','table-hover'])
        return render_template('accounts_income.html',values = zip(message,amount,date),date=date,amount=amount,colors=colors,form=form,income_table=income_table)
    return render_template('accounts_income.html',values = zip(message,amount,date),date=date,amount=amount,colors=colors,form=form)


## Project Payment
@login_required
@accounts_home.route('/home/Project_Payment',methods=['GET','POST'])
def project_payment():
    form = Genral_query()
    amount,date,message=account_value('Project Payment')
    colors = ['#666547','#fb2e01','#21bf73','#ffcc00','#ffe28a','#f65c78']
    if form.validate_on_submit():
        project_payment = Accounts.query.filter(Accounts.date >= form.starting_date.data,Accounts.date <=form.ending_date.data).filter(Accounts.category=='Project Payment').order_by(Accounts.date).limit(10).all()
        project_payment_table = Miscellaneous_table(project_payment,classes=['table','table-hover'])
        return render_template('accounts_project_payment.html',values = zip(message,amount,date),date=date,amount=amount,colors=colors,form=form,project_payment_table=project_payment_table)
    return render_template('accounts_project_payment.html',values = zip(message,amount,date),date=date,amount=amount,colors=colors,form=form)

## Fixed Payment
@login_required
@accounts_home.route('/home/Fixed_Payment',methods=['GET','POST'])
def fixed_payment():
    form = Genral_query()
    amount,date,message=account_value('Fixed Payment')
    colors = ['#666547','#fb2e01','#21bf73','#ffcc00','#ffe28a','#f65c78']
    if form.validate_on_submit():
        fixed_payment = Accounts.query.filter(Accounts.date >= form.starting_date.data,Accounts.date <=form.ending_date.data).filter(Accounts.category=='Fixed Payment').order_by(Accounts.date).limit(10).all()
        fixed_payment_table = Miscellaneous_table(fixed_payment,classes=['table','table-hover'])
        return render_template('accounts_fixed_payment.html',values = zip(message,amount,date),date=date,amount=amount,colors=colors,form=form,fixed_payment_table=fixed_payment_table)
    return render_template('accounts_fixed_payment.html',values = zip(message,amount,date),date=date,amount=amount,colors=colors,form=form)

## Fixed Payment
@login_required
@accounts_home.route('/home/Raw_Material',methods=['GET','POST'])
def raw_material():
    form = Genral_query()
    amount,date,message=account_value('Raw Material')
    colors = ['#666547','#fb2e01','#21bf73','#ffcc00','#ffe28a','#f65c78']
    if form.validate_on_submit():
        raw_material = Accounts.query.filter(Accounts.date >= form.starting_date.data,Accounts.date <=form.ending_date.data).filter(Accounts.category=='Raw Material').order_by(Accounts.date).limit(10).all()
        raw_material_table = Miscellaneous_table(raw_material,classes=['table','table-hover'])
        return render_template('accounts_raw_material.html',values = zip(message,amount,date),date=date,amount=amount,colors=colors,form=form,raw_material_table=raw_material_table)
    return render_template('accounts_raw_material.html',values = zip(message,amount,date),date=date,amount=amount,colors=colors,form=form)