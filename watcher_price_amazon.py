import requests
from bs4 import BeautifulSoup
import smtplib

url = 'YOUR PRODUCT LINK'

your_condition_amount = int('enter your amount here')
#NOTE:-search "my user agent on google, copy that and paste it below"

headers = {'User-Agent':'PASTE IT HERE'}
page = requests.get(url,headers=headers)
soup = BeautifulSoup(page.content,'html.parser')
title = soup.find(id='productTitle').get_text().strip()
price = float("".join(list(soup.find(id='priceblock_ourprice').get_text().strip())[2:]).replace(",",""))

#follow below instruction
'''
Log in to your Google account, and use these links:

Step 1 [Link of Disabling 2-step verification]:

https://myaccount.google.com/security?utm_source=OGB&utm_medium=act#signin
"==================disable it=================="
Step 2: [Link for Allowing less secure apps]

https://myaccount.google.com/u/1/lesssecureapps?pli=1&pageId=none
"==================make it allow==============="
'''
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('from@gmail.com','password')
    
    msg = "YOUR MSG"

    server.sendmail(
        'from@gmail.com',
        'to@gmail.com',
        msg
    )
    print("EMAIL SENT")
    server.quit()
if price < your_condition_amount:
    print (title)
    print(price)
    send_mail()
else:
    print("nothing happend")