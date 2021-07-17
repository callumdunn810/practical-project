from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from application import app, db 

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

class Character(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   skill = db.Column(db.String(50), nullable=True)
   alliance = db.Column(db.String(50), nullable=True)
   race = db.Column(db.String(50), nullable=True)