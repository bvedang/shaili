from flask import Blueprint,redirect,url_for,request,render_template
from flask_login import login_required


accounts = Blueprint('accounts',__name__,template_folder='templates/Accounts')

@login_required
@accounts.route('/home',methods=['GET','POST'])
def home():
    legend = 'Monthly Data'
    colors = ['rgb(255, 99, 132,)','rgba(54, 162, 235)','rgba(255, 206, 86)','rgba(75, 192, 192)',
              'rgba(153, 102, 255)','rgba(255, 159, 64)','#fd5e53','#c9485b','#f0134d','#cc0066',
              '#3e206d','#2c786c']
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [100, 90, 80, 70, 60, 90, 70, 80]
    return render_template('accounts_home.html',values=values,legend=legend,labels=labels,colors=colors)