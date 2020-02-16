import datetime
import calendar
from flask import request
from SIMS.models import Accounts

def getvalues():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    days = calendar.monthrange(year,month)[1]
    start_date = datetime.date(year,month,1)
    end_date = datetime.date(year,month,days)
    mis_value = Accounts.query.filter(Accounts.date >= start_date,Accounts.date <=end_date).filter(Accounts.category=='Miscellaneous').all()
    cash_value = Accounts.query.filter(Accounts.date >= start_date,Accounts.date <=end_date).filter(Accounts.category=='Cash').all()
    income_value = Accounts.query.filter(Accounts.date >= start_date,Accounts.date <=end_date).filter(Accounts.category=='Income').all()
    proj_value = Accounts.query.filter(Accounts.date >= start_date,Accounts.date <=end_date).filter(Accounts.category=='Project Payment').all()
    fixed_value = Accounts.query.filter(Accounts.date >= start_date,Accounts.date <=end_date).filter(Accounts.category=='Fixed Payment').all()
    raw_value = Accounts.query.filter(Accounts.date >= start_date,Accounts.date <=end_date).filter(Accounts.category=='Raw Material').all()
    mis = 0
    for i in mis_value:
        mis = mis+i.amount
    cash = 0
    for i in cash_value:
        cash = cash+i.amount
    income = 0
    for i in income_value:
        income = income+i.amount
    proj = 0
    for i in proj_value:
        proj = proj+i.amount
    fixed = 0
    for i in fixed_value:
        fixed = fixed+i.amount
    raw = 0
    for i in raw_value:
        raw = raw+i.amount
    values = [mis,cash,income,proj,fixed,raw]
    table_values = {'Miscellaneous':mis,'Cash':cash,'Income':income,'Project Payment':proj,'Fixed Payment':fixed,'Raw Material':raw}
    return values,table_values


def get_month():
    now  = datetime.datetime.now()
    month = now.month
    month = calendar.month_name[month]
    return month


#####    ACCOUNT VALUES
def account_value(category):
    page = request.args.get('page',1,type=int)
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    days = calendar.monthrange(year,month)[1]
    start_date = datetime.date(year,month,1)
    end_date = datetime.date(year,month,days)
    account_values = Accounts.query.filter(Accounts.date >= start_date,Accounts.date <=end_date).filter(Accounts.category==category).order_by(Accounts.date.desc()).paginate(page=page,per_page=5)
    return account_values