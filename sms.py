import requests 
import json

url = "https://www.fast2sms.com/dev/bulk"


# create a dictionary
my_data = {
     # Your default Sender ID
    'sender_id': '9168782220',

     # Put your message here!
    'message': 'An unidentified person tried to access your personal assistant',

    'language': 'english',
    'route': 'p',

    # You can send sms to multiple numbers
    # separated by comma.
    'numbers': '9588674523,9145783547,8605964402,8805624842'
}

headers = {
    'authorization': 'IxlGykWntDuz7BHeVZRjKfv2b5XPJN81Q0phmc4wUTYCErgoaAOZcCv68Sxkg4tIpPw01VbT7zrnJDNB',
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache"
}

def sendSms():
    response = requests.request("POST",
                            url,
                            data = my_data,
                            headers = headers)
    #load json data from source
    returned_msg = json.loads(response.text)
    
    # print the send message
    print(returned_msg['message'])
