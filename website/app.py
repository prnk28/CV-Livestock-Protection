import twilio_sms
import fire_detect
import bgsb
import os

#Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/sms/")
def twilio_fcn():
    twilio_sms.send_text('Warning: possible wildfire near you!')
    return render_template('index.html')

@app.route("/fire", methods=['GET', 'POST'])
def fire_msg():
    print("Running. . .")
    os.system("python ../yolo_video.py -i='../videos/fox_chicken_cropped.mp4' -o='../output/chicken-1.avi' -y=yolo-coco")
    return render_template('index.html')

@app.route("/agreement/")
def docusign_agree():  
    import docusign_tools.sig_request
    return "Check your email for fire-monitoring subscription agreement."

   
@app.route("/")
def home():
    return render_template('index.html')





if __name__ == "__main__":
    app.run(debug=True)
