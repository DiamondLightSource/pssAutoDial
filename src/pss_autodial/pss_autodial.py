import os

from aioca import FORMAT_CTRL, camonitor, run
from twilio.rest import Client

# Alarm Details -----------------------------------------------------------
# This is the PV name of the alarm you wish to monitor
pv = "SR04C-PS-FANC-01:STA"  # Fan alarm in SR04


# Key Functions  -----------------------------------------------------------
def make_call():
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

    message = (
        "<Response><Say>Hello. There is an incident on Beamline B L 10 E. "
        "The P S S has detected an oxygen depletion event. Please attend the "
        "site. </Say><Play>http://demo.twilio.com/docs/classic.mp3</Play></Response>"
    )

    call = client.calls.create(
        to=to_number,
        from_=twilio_number,
        call_reason="Emergency",
        twiml=message,
        method="GET",
    )

    print(f"Call initiated. SID: {call.sid}")


async def monitor_alarm():
    async def about_once_a_second(value):
        print(f"new value is {value}")
        print(value.__dict__)

        if value.severity == 2:
            make_call()

    camonitor(pv, callback=about_once_a_second, format=FORMAT_CTRL)


def run_application():
    # print("Monitoring!")
    run(monitor_alarm(), forever=True)
