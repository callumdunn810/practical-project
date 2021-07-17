from flask import Flask, request
import random
from application import app

@app.route('/get_alliance', methods=['GET'])
def get_alliance():
    return random.choice(['Aldmeri Dominion','Daggerfall Covenant','Ebonheart Pact'])
