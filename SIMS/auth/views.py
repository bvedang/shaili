from flask import Blueprint, redirect, url_for, render_template, request, flash
from SIMS import db
from SIMS.models import Employee
from SIMS.auth.forms import RegisterForm,LoginForm
from flask_login import login_required,login_user,current_user,logout_user

auth = Blueprint('auth',__name__,)

#Register

@auth.route('/Register', methods=['GET','POST'])
def register():
    registerform = RegisterForm()
    if registerform.validate_on_submit():
        employee = Employee(email=registerform.email.data,
                            first_name=registerform.first_name.data,
                            last_name=registerform.last_name.data,
                            password=registerform.password.data)
        db.session.add(employee)
        db.session.commit()
        flash('You have Sucessfully Registered!')
        return redirect(url_for('auth.login'))
    return render_template('register.html',registerform=registerform)
#LOGIN

@auth.route('/Login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        employee = Employee.query.filter_by(email=form.email.data).first()

        if employee.check_password(form.password.data) and employee is not None:
            login_user(employee)
            flash('Logged In Sucessfully')
            return redirect(url_for('core.dashboard'))
        else:
            return redirect(url_for('core.error'))
    return render_template('login.html',form=form)

#logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index'))

@auth.route('/index')
def index():
    return render_template('bill1 bvc.html')