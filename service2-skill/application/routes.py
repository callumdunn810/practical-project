from flask import Flask, request
import random
from application import app

@app.route('/get_skill', methods=['GET'])
def get_skill():
    return random.choice(['Necromancer','Nightblade','Sorcerer','Templar','Warden','Dragonknight'])

