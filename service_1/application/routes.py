from flask import Flask, render_template
import requests
from application import app, db
from application.models import Character
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/generate')
def gen():
    skill = requests.get('http://service_2_skill:5000/get_skill')
    alliance = requests.get('http://service_3_alliance:5000/get_alliance')
    race = requests.post('http://service_4_race:5000/get_race',data=alliance.text)

    last_five_characters = Character.query.order_by(Character.id.desc()).limit(1).all()
    db.session.add(
        Character(
            skill=skill.text,
            alliance=alliance.text,
            race=race.text
        )
    )
    db.session.commit()



    return render_template('gen.html',skill=skill.text,alliance=alliance.text,race=race.text,last_five_characters=last_five_characters)