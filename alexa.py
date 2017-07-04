from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/")

@ask.launch
def start_skill():
    red_val = requests.get("https://api.particle.io/v1/devices/3c0020000a47353137323334/red_val?access_token=79cecc0df866aeeabd18a68f2a7b32b33d54de03")
    green_val = requests.get("https://api.particle.io/v1/devices/3c0020000a47353137323334/green_val?access_token=79cecc0df866aeeabd18a68f2a7b32b33d54de03")
    yellow_val = requests.get("https://api.particle.io/v1/devices/3c0020000a47353137323334/yellow_val?access_token=79cecc0df866aeeabd18a68f2a7b32b33d54de03")

    r_d = red_val.json()
    g_d = green_val.json()
    y_d = yellow_val.json()

    if (y_d['result']) == 0 and (r_d['result'] == 0) and (g_d['result'] == 0):
        output_txt = "Entire library is yours to conquer..!!"
    elif (r_d['result']) == 0 and (g_d['result'] == 0):
        output_txt = "Ther are 2 spots, one on 1st Floor on Green Couches and one on 2nd Floor on Red Couches"
    elif (y_d['result']) == 0 and (g_d['result'] == 0):
        output_txt = "Ther are 2 spots, one on 1st Floor on Green Couches and one on 2st Floor on Yellow couches"
    elif (y_d['result']) == 0 and (r_d['result'] == 0):
        output_txt = "Ther are 2 spots, one on 2st Floor on Yellow couches on left and other on Red Couches at the right"
    elif r_d['result'] == 0:
        output_txt = "There is 1 spot on 2nd Floor on Red Couches at the right end side of entrance"
    elif g_d['result'] == 0:
        output_txt = "There is 1 spot on 1st Floor on Green Couches at the very end"
    elif y_d['result'] == 0:
        output_txt = "There is a spot on 2st Floor on Yellow couches on the left side"
    else:
        output_txt = "Sorry, I could not find anything on 1st and 2nd Floor but you may find something on 3rd or 4th floor"
    return statement(output_txt)

@ask.intent("ask_spotty")
def share_headlines():
    red_val = requests.get("https://api.particle.io/v1/devices/3c0020000a47353137323334/red_val?access_token=79cecc0df866aeeabd18a68f2a7b32b33d54de03")
    green_val = requests.get("https://api.particle.io/v1/devices/3c0020000a47353137323334/green_val?access_token=79cecc0df866aeeabd18a68f2a7b32b33d54de03")
    yellow_val = requests.get("https://api.particle.io/v1/devices/3c0020000a47353137323334/yellow_val?access_token=79cecc0df866aeeabd18a68f2a7b32b33d54de03")

    r_d = red_val.json()
    g_d = green_val.json()
    y_d = yellow_val.json()

    if (y_d['result']) == 0 and (r_d['result'] == 0) and (g_d['result'] == 0):
        output_txt = "Entire library is yours to conquer..!!"
    elif (r_d['result']) == 0 and (g_d['result'] == 0):
        output_txt = "Ther are 2 spots, one on 1st Floor on Green Couches and one on 2nd Floor on Red Couches"
    elif (y_d['result']) == 0 and (g_d['result'] == 0):
        output_txt = "Ther are 2 spots, one on 1st Floor on Green Couches and one on 2st Floor on Yellow couches"
    elif (y_d['result']) == 0 and (r_d['result'] == 0):
        output_txt = "Ther are 2 spots, one on 2st Floor on Yellow couches on left and other on Red Couches at the right"
    elif r_d['result'] == 0:
        output_txt = "There is 1 spot on 2nd Floor on Red Couches at the right end side of entrance"
    elif g_d['result'] == 0:
        output_txt = "There is 1 spot on 1st Floor on Green Couches at the very end"
    elif y_d['result'] == 0:
        output_txt = "There is a spot on 2st Floor on Yellow couches on the left side"
    else:
        output_txt = "Sorry, I could not find anything on 1st and 2nd Floor but you may find something on 3rd or 4th floor"
    return statement(output_txt)

if __name__ == '__main__':
    app.run(debug=True)

