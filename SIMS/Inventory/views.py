from flask import Blueprint,render_template,redirect,url_for,flash,request
from SIMS import db
from datetime import date
import datetime
from SIMS.Inventory.table import LS_Stage_1_Table,LS_Stage_2_Table,Livo_Ester
from SIMS.models import LS_Stage1,LS_Stage2,LS_Stage3
from flask_login import login_required

inventory = Blueprint('inventory',__name__,template_folder='templates/inventory')

@inventory.route('/inventory-home')
@login_required
def home():
    return render_template("inventory_home.html")

@inventory.route('/LS_Stage_1',methods=['GET','POST'])
@login_required
def ls_stage_1():
    entries = LS_Stage1.query.filter(LS_Stage1.is_complete==True).order_by(LS_Stage1.starting_date).limit(10).all()
    table=LS_Stage_1_Table(entries,classes=['table'])
    start_date = request.args.get('starting_date')
    end_date = request.args.get('ending_date')
    if start_date and end_date is not None:
        start_date = datetime.datetime.strptime(request.args.get('starting_date'),"%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(request.args.get('ending_date'),"%Y-%m-%d").date()
        between_date = LS_Stage1.query.filter(LS_Stage1.starting_date <= end_date, LS_Stage1.starting_date >= start_date).filter(LS_Stage1.is_complete==True).all()
        between_table = LS_Stage_1_Table(between_date,classes=['table'])
        return render_template('ls_stage_1_query.html',between_table=between_table,table=table)
    return render_template('ls_stage_1.html',table=table)

@inventory.route('/LS_Stage_2',methods=['GET','POST'])
@login_required
def ls_stage_2():
    entries = LS_Stage2.query.filter(LS_Stage2.is_complete==True).order_by(LS_Stage2.starting_date).limit(10).all()
    table=LS_Stage_2_Table(entries,classes=['table'])
    start_date = request.args.get('starting_date')
    end_date = request.args.get('ending_date')
    if start_date and end_date is not None:
        start_date = datetime.datetime.strptime(request.args.get('starting_date'),"%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(request.args.get('ending_date'),"%Y-%m-%d").date()
        between_date = LS_Stage1.query.filter(LS_Stage2.starting_date <= end_date, LS_Stage2.starting_date >= start_date).filter(LS_Stage2.is_complete==True).all()
        between_table = LS_Stage_2_Table(between_date,classes=['table'])
        return render_template('ls_stage_2_query.html',between_table=between_table,table=table)
    return render_template('ls_stage_2.html',table=table)


@inventory.route('/Livo_Ester',methods=['GET','POST'])
@login_required
def livo_ester():
    entries = LS_Stage3.query.filter(LS_Stage3.is_complete==True).order_by(LS_Stage3.starting_date).limit(10).all()
    table=Livo_Ester(entries,classes=['table'])
    start_date = request.args.get('starting_date')
    end_date = request.args.get('ending_date')
    if start_date and end_date is not None:
        start_date = datetime.datetime.strptime(request.args.get('starting_date'),"%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(request.args.get('ending_date'),"%Y-%m-%d").date()
        between_date = LS_Stage3.query.filter(LS_Stage3.starting_date <= end_date, LS_Stage3.starting_date >= start_date).filter(LS_Stage2.is_complete==True).all()
        between_table = Livo_Ester(between_date,classes=['table'])
        return render_template('livo_ester_query.html',between_table=between_table,table=table)
    return render_template('livo_ester.html',table=table)

@inventory.route('/bill_demo',methods=['GET','POST'])
def bill():
    return render_template('bill.html')