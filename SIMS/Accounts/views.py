from flask import Blueprint,redirect,url_for,request,render_template
from flask_login import login_required
import matplotlib.pyplot as plt,mpld3


accounts = Blueprint('accounts',__name__,template_folder='templates/Accounts')

@login_required
@accounts.route('/home',methods=['GET','POST'])
def home():
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)
    fig1, ax1 = plt.subplots(figsize=(6,4))
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90,textprops={'fontsize':16})
    ax1.axis('equal')
    ax1.legend(labels,title="Animals",loc="upper right")
    ax1.set_title('Expense Chart')
    plot = mpld3.fig_to_html(fig1,template_type='general')
    plt.close('all')
    return render_template('accounts_home.html',plot=plot)