from SIMS import db,admin,login_manager
from flask_login import UserMixin
from datetime import date
from werkzeug.security import generate_password_hash,check_password_hash
from flask_admin.contrib.sqla import ModelView

@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(user_id)


class Employee(db.Model,UserMixin):
    __tablename__ = 'Employee'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(128),unique=True,index=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    admin = db.Column(db.Boolean,default=False)
    password_hash = db.Column(db.String(128))

    def __init__(self,email,first_name,last_name,password):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password_hash = generate_password_hash(password)
    def __repr__(self):
        return f"Name : {self.first_name} \n Email : {self.email}"
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

class LS_Stage1(db.Model):
    __tablename__ = 'LS Ester RM Stock Stage 1'

    id = db.Column(db.Integer,primary_key=True)
    fda_batch_no = db.Column(db.Integer,nullable=False,unique=True)
    starting_date = db.Column(db.Date,default=date.today,nullable=False)
    salicylic_acid = db.Column(db.Float)
    dms = db.Column(db.Float)
    caustic_soda_flakes = db.Column(db.Float)
    hcl = db.Column(db.Float)
    water = db.Column(db.Float)
    wet_cake = db.Column(db.Float)
    dry_output = db.Column(db.Float)
    p_yeild = db.Column(db.Float)
    complete_date = db.Column(db.Date,default=date.today,nullable=False)
    is_complete = db.Column(db.Boolean, unique=False, default=False)
    utilized = db.Column(db.Boolean, unique=False, default=False)
    
    def __repr__(self):
        f"Batch number{self.fda_batch_no}"

    def ls1_factor(self,dry_output,sa):
        self.p_yeild = (dry_output/sa)

class LS_stage_1_view(ModelView):
    create_modal=True
    can_export = True
    can_view_details = True



class LS_Stage2(db.Model):
    __tablename__ = 'LS Ester RM Stock Stage 2'

    id = db.Column(db.Integer,primary_key=True)
    fdb_batch_no = db.Column(db.String(128),nullable=False)
    starting_date = db.Column(db.Date,nullable=False,default=date.today())
    fda = db.Column(db.Float)
    fda_batch_no = db.Column(db.String(128),nullable=False)
    chlorosulphonic_acid = db.Column(db.Float)
    thionyl_cholride = db.Column(db.Float)
    liq_amonia = db.Column(db.Float)
    sulphuric_acid = db.Column(db.Float)
    wet_cake_after_csa_reaction = db.Column(db.Float)
    wet_cake = db.Column(db.Float)
    dry_output = db.Column(db.Float)
    factor = db.Column(db.Float)
    complete_date = db.Column(db.Date,default=date.today,nullable=False)
    is_complete = db.Column(db.Boolean, unique=False, default=False)
    utilized = db.Column(db.Boolean, unique=False, default=False)

    def __repr__(self):
        f"Batch number{self.fdb_batch_no}"

    def ls2_factor(self,fda,dry_output):
        self.factor = (dry_output/fda)

class LS_stage_2_view(ModelView):
    create_modal=True
    can_export = True
    can_view_details = True

class LS_Stage3(db.Model):
    __tablename__ = 'LS Ester RM Stock Stage 3'

    id = db.Column(db.Integer,primary_key=True)
    fdc_batch_no = db.Column(db.String(128),nullable=False)
    starting_date = db.Column(db.Date,nullable=False,default=date.today())
    fdb = db.Column(db.Float)
    fdb_batch_no = db.Column(db.String(128),nullable=False)
    ok_fresh = db.Column(db.Float)
    ok_recovered = db.Column(db.Float)
    ok_cf_ml = db.Column(db.Float)
    sulphuric_acid = db.Column(db.Float)
    part_A_wet_cake = db.Column(db.Float)
    dmf_fresh = db.Column(db.Float)
    dmf_recovered = db.Column(db.Float)
    cmf_ml_dmf = db.Column(db.Float)
    soda_ash = db.Column(db.Float)
    charcoal = db.Column(db.Float)
    final_wet_cake = db.Column(db.Float)
    dry_output = db.Column(db.Float)
    factor = db.Column(db.Float)
    remarks = db.Column(db.String(128))
    complete_date = db.Column(db.Date,default=date.today,nullable=False)
    is_complete = db.Column(db.Boolean, unique=False, default=False)

    def __repr__(self):
        f"Batch number{self.fdc_batch_no}"

    def ls3_factor(self,fdb,dry_output):
        self.factor = (dry_output/fdb)

class LS_stage_3_view(ModelView):
    create_modal=True
    can_export = True
    can_view_details = True

class BillsPDF(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(300),nullable=False)
    bill_pdf = db.Column(db.LargeBinary,nullable=False)
    date = db.Column(db.Date,default=date.today,nullable=False)
    grand_total = db.Column(db.Float,nullable=False)
    reminder_given = db.Column(db.Boolean,default=False)

class BillsPDF_view(ModelView):
    column_exclude_list = ('bill_pdf')
    can_export = True
    can_view_details = True

admin.add_views(LS_stage_1_view(LS_Stage1,db.session,endpoint='ls_stage1'))
admin.add_views(LS_stage_2_view(LS_Stage2,db.session,endpoint='ls_stage2'))
admin.add_views(LS_stage_3_view(LS_Stage3,db.session,endpoint='livo_ester'))
admin.add_view(BillsPDF_view(BillsPDF,db.session))