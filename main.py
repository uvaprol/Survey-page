from flask import Flask, render_template, request
from datetime import date
import pandas as pd

df = pd.read_csv('offer.csv')


app = Flask(__name__)

@app.route('/')
def display_chat():
    return render_template('index.html')


@app.route('/sendOffer')
def sendOffer():
    global df
    orgName         = request.args['orgName']
    shortOrgName    = request.args['shortOrgName']
    userType        = request.args['userType']
    bossPost        = request.args['bossPost']
    bossName        = request.args['bossName']
    responsiblePost = request.args['responsiblePost']
    responsibleName = request.args['responsibleName']
    tel             = request.args['tel']
    mail            = request.args['mail']
    new_offer = {
        'orgName'        : orgName,
        'shortOrgName'   : shortOrgName,
        'userType'       : userType,
        'bossPost'       : bossPost,
        'bossName'       : bossName,
        'responsiblePost': responsiblePost,
        'responsibleName': responsibleName,
        'tel'            : tel,
        'mail'           : mail,
        'date-time'      : date.today()
    }
    send_key = True
    for k, v in new_offer.items():
        if v == '':
            send_key = False
    if send_key:
        df = df._append(new_offer, ignore_index=True)
        df.to_csv('offer.csv', index=False, header=True)
    return True


app.run(host='0.0.0.0', port=80)
