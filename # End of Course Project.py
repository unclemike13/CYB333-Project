# End of Course Project
# Michael FElton
# CYB333
# Charles Heinen


import os
import smtplib
import requests

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

def notify_user():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        
        subject = 'Your website is down'
        body = 'Ensure you restart your server and that it is operating normal'
        msg = f'Subject: {subject}\n\n{body}'
        
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)

def reboot_server():
    # client = LinodeClient(LINODE_TOKEN)
    # my_server = client.linode(Instance, XXXXX)
    # my_server.reboot()
    # for linode in client.linode.instances():
    #     print(f'{linode.lable}:  {linode.id}')

try:
    r = requests.get('https://www.google.com', timeout=10)
    
    if r.status_code !=200:
        notify_user()
        reboot_server()
    
except Exception as e:
    raise e




        




