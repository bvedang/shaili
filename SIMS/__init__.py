import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin

app = Flask(__name__,template_folder='templates')
app.config['SECRET_KEY'] = 'mysecret'

#dataBase Setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

#Admin

admin = Admin(app)

#login manager
# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='auth.login'

#Blueprints
from SIMS.core.views import core
from SIMS.auth.views import auth
from SIMS.Inventory.views import inventory
from SIMS.Bill.views import bills
from SIMS.Accounts.views import accounts
app.register_blueprint(core)
app.register_blueprint(auth,url_prefix='/auth')
app.register_blueprint(inventory,url_prefix='/inventory')
app.register_blueprint(bills,url_prefix='/bills')
app.register_blueprint(accounts,url_prefix='/accounts')