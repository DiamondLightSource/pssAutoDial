import os

from aioca import FORMAT_CTRL, camonitor, run
from twilio.rest import Client

# Alarm Details -----------------------------------------------------------
# alarm_dict stores ov names and associated details for the message
alarm_dict = {
    "SR04C-PS-FANC-01:STA": "Fan tray alarm in SR04. Located in the CIA rack.",
    "SR02C-PS-FANC-01:STA": "Fan tray alarm in SR02. Located in the CIA rack.",
}

pvs = list(alarm_dict.keys())
messages = list(alarm_dict.values())


# Key Functions  -----------------------------------------------------------
def make_call(message):
    # Twilio Details -----------------------------------------------------------
    # Twilio credentials from https://www.twilio.com/console
    account_sid = os.environ["ACCOUNT_SID"]
    auth_token = os.environ["AUTH_TOKEN"]
    # friendly_name = "Emergency"
    client = Client(account_sid, auth_token)

    # Your Twilio number and recipient number (E.164 format)
    twilio_number = os.environ["TWILIO_NUMBER"]
    to_number = os.environ["TO_NUMBER"]

    # URL with TwiML instructions for the call
    # twiml_url = "http://demo.twilio.com/docs/voice.xml"

    twilio_message = (
        "<Response><Say>Hello. There is a "
        + message
        + " I repeat. "
        + message
        + "</Say></Response>"
    )

    call = client.calls.create(
        to=to_number,
        from_=twilio_number,
        call_reason="PSS Alarm",
        twiml=twilio_message,
        method="GET",
    )

    print(f"Call initiated. SID: {call.sid}")


async def monitor_alarm():
    # print("Monitoring the alarm")

    async def about_once_a_second(value, pv_ref):
        print(f"new value of {pvs[pv_ref]} is {value.severity}")
        if value.severity == 2:
            message = messages[pv_ref]
            print("Making call")
            make_call(message)

        # If we are monitoring a binary status:

        # print(f"new value of {pvs[pv_ref]} is {value}")
        # if value == 0:
        #     message = messages[pv_ref]
        #     print("Making call")
        #     make_call(message)

    print("Running camonitor now:")
    camonitor(pvs, callback=about_once_a_second, format=FORMAT_CTRL)


def run_application():
    print("Monitoring!")
    run(monitor_alarm(), forever=True)
