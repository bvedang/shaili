from flask import Blueprint,redirect,url_for,request,render_template
from flask_login import login_required
import matplotlib.pyplot as plt,mpld3
from mpld3 import plugins

accounts = Blueprint('accounts',__name__,template_folder='templates/Accounts')

@login_required
@accounts.route('/home',methods=['GET','POST'])
def home():
    labels1 = 'Raw material', 'Bills', 'Cash', 'Misilaneous','Unkown'
    sizes = [15, 30, 45, 10, 40]
    colors=['#003f5c','#58508d','#bc5090','#ff6361','#ffa600']
    fig1,ax1 = plt.subplots(figsize=(6,3.5))
    ax1.pie(sizes,labels=labels1,shadow=True,startangle=0,colors=colors,autopct='%1.2f%%',textprops={'fontsize': 16})
    centre_circle = plt.Circle((0,0),0.20,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    ax1.axis('equal')
    plt.tight_layout()
    plt.subplots_adjust(right=0.95)
    plt.legend(labels1,loc="upper right")
    pie_chart = mpld3.fig_to_html(fig1,template_type='general')
    return render_template('accounts_home.html',pie_chart=pie_chart)