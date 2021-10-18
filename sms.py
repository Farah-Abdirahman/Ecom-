import africastalking
africastalking.initialize(
    username='mwasika',
    api_key='e006d3d5bfb275e24057295b181c4b669f3dec17f7ab306b99c3285e1723c171'
)
sms = africastalking.SMS
def sending(phone,fname):
    # TODO: Send message
    recipients = [phone]
    message = "Hi {}, Welcome to Nike Shop, For all your shopping experience".format(fname)
    sender = 'AFRICASTKNG' # Place your SenderID here
    try:
        response = sms.send(message, recipients)
        print(response)
    except Exception as e:
        print(f'Houston, something went wrong: ${e}')