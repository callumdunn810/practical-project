from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:Grg170dx@34.105.231.190:3306/gendb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


from application import routes 
