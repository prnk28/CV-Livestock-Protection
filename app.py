from flask import Flask, jsonify, request
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACfb78325b02e06e7a48e6b7e9508d00fa'
auth_token = '1cd511db84d6950525e1fb22b38ebb03'
client = Client(account_sid, auth_token)

app = Flask(__name__)

# Paramaters Include: phone, hazardName, and animalCount
@app.route('/alert', methods=['POST'])
def sendMessage():
    message = client.messages \
                    .create(
                        body='Your ' + str(request.args.get('animalCount', default = 0, type = int)) +
                        ' animal(s) are facing a threat from '
                        + request.args.get('hazardName', default = 'None', type = str) + '.',
                        from_='+12403496055',
                        to=str(request.args.get('phone', default = +17033216471, type = int))
                    )
    return "The Message was sent"

if __name__ == '__main__':
    app.run(debug=True)
