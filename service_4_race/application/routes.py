from flask import Flask, request
import random
from application import app

@app.route('/get_race', methods=['POST'])
def get_race():
    alliance = request.data.decode('utf-8')
    if alliance == "Aldmeri Dominion":
        return 'High Elf' or 'Wood Elf' or 'Khajiit'
    elif alliance == "Daggerfall Covenant":
        return 'Orc' or 'Breton' or 'Redguard'
    elif alliance == "Ebonheart Pact":
        return 'Dark Elf' or 'Nord' or 'Argonian'
    else:
        return 'Error, please try again'
