from datetime import datetime, timedelta

import json,logging, requests



#Create and configure logger
logging.basicConfig(filename="records.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
#Creating an object
logger=logging.getLogger()
#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)



PIN = #<YOUR PIN CODE>      #type: int 
NUMBER_OF_DAYS = 7          #type: int
PHONE = #<YOUR PHONE NUMBER WITH COUNTRY CODE, eg: "+91.." for India>     #type: str

baseurl="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"

def my_function(name, capacity):
    """

    Alert my number,
    goto the cowin site and book the slot if possible,

    inputs -> site address, phone number , otp, pincode, name , address

    """
    from twilio.rest import Client

    # Your Account Sid and Auth Token from twilio account
    account_sid = #str
    auth_token = #str
    # instantiating the Client
    client = Client(account_sid, auth_token)
    # sending message
    message = client.messages.create(
        body=f"\nVaccination alert...\n{name} has {capacity} vaccines available",
        from_="+16105573820",
        to=PHONE,
    )
    call = client.calls.create(
        twiml="<Response><Say>Vaccines available!</Say></Response>",
        to=PHONE,
        from_=# twilio number # type: str,
    )
    # printing the sid after success
    print(message.sid)


def check(json_data):
    for x in range(len(json_data["centers"])):
        # filter for minimum age limit
        if json_data["centers"][x]["sessions"][0]["min_age_limit"] == 45:
            continue
        name = json_data["centers"][x]["name"]
        address = json_data["centers"][x]["address"]
        capacity = json_data["centers"][x]["sessions"][0]["available_capacity"]
        if capacity > 0:
            print(name)
            my_function(name, capacity)


for x in range(NUMBER_OF_DAYS):
    date_time = datetime.now() + timedelta(days=x)
    date=date_time.strftime("%d-%m-%Y")
    url = f"{baseurl}?pincode={PIN}&date={date}"
    print(url)
    res = requests.get(
        url,
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    })
    json_data = json.loads(res.text)
    check(json_data)
