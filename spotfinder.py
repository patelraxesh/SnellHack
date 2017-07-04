from twilio import twiml
import nltk
from flask import Flask, request
import urllib2
from twilio.rest import TwilioRestClient
import requests
import pandas as pd
from collections import Counter
import smtplib
import requests

ACCOUNT_SID = "TWILIO_ACCOUNT_SID"
AUTH_TOKEN = "TWILIO_AUTH_TOKEN"
TWILIO_NUMBER = 'TWILIO_PH_NO'

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
app = Flask(__name__)

@app.route("/")
def hello():
	out_text = "Hi, How can i help you ?"
	response = twiml.Response()
	response.message(out_text)
	return str(response)

@app.route("/sms", methods=['POST'])
def nursechat():
	in_text = request.form["Body"]
	ph_number = request.form["From"]
	in_text = in_text.lower()
	out_text = get_response(in_text)
	response = twiml.Response()
	response.message(out_text)
	return str(response)

@app.route('/call', methods=['POST'])
def call():
    # Make an outbound call to the provided number from your Twilio number
    call = client.calls.create(to='+18574520056', from_=TWILIO_NUMBER,
                               url="http://demo.twilio.com/docs/voice.xml")

    # Return a message indicating the call is coming
    return 'Call coming in!'


def send_mail():
	msg = MIMEMultipart()
	msg['From'] = 'raxeshp1991@gmail.com'
	msg['To'] = 'raxesh4you@gmail.com'
	msg['Subject'] = "BENS REPORT"
	msg.attach(MIMEText(file("sample.pdf").read()))
	output_txt = "Bens latest data as on 03/27/2017 7:00 PM:\
        \nBP = 122\
        \nHR = 72\
        \nWeight = 187 lb\
        \nBlood Sugar = 130"
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login('raxeshp1991@gmail.com','sahajanand')
	s.sendmail('raxeshp1991@gmail.com',['raxesh4you@gmail.com'], output_txt)
	s.quit()

def find_seats(input_str):
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
    return output_txt

def get_response(input_st):
    '''
    Get the response output from input
    '''
    input_str = input_st.lower()
    input_words = input_str.split()
    red_val = requests.get("https://api.particle.io/v1/devices/3c0020000a47353137323334/red_val?access_token=79cecc0df866aeeabd18a68f2a7b32b33d54de03")
    green_val = requests.get("https://api.particle.io/v1/devices/3c0020000a47353137323334/green_val?access_token=79cecc0df866aeeabd18a68f2a7b32b33d54de03")
    yellow_val = requests.get("https://api.particle.io/v1/devices/3c0020000a47353137323334/yellow_val?access_token=79cecc0df866aeeabd18a68f2a7b32b33d54de03")

    r_d = red_val.json()
    g_d = green_val.json()
    y_d = yellow_val.json()
    # patients
    all_w = ['find','spot']
    greeting = ['hi']

    if all(x in input_str for x in all_w):
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
        return output_txt

    elif all(x in input_str for x in greeting):
        output_txt = "Hi, This is your SpotFinder." + find_seats(input_str)
        return output_txt
    else:
        output_txt = "You could try something like 'find me a spot' or 'spotfinder'"
        return output_txt

if __name__ == "__main__":
	app.run(debug=True)
