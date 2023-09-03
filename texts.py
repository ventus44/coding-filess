import requests
import schedule
import time

def send_message():
#we make a dictionary that has the url of the webpage we're going to use
    resp = requests.post("https://textbelt.com/text", {
        "phone": "+70250",
        "message": "Hey",
        "key": "textbelt", 
    })
    print(resp.json())
#this line sets the schedure for the time i want to send the message 
#schedule.every().day.at("18:32").do(send_message)
#this line sets the commant for every 10 seconds
#schedule.every(10).seconds.do(send_message)
#it's repeated through a while loop
#while True:
    schedule.run_pending()
    time.sleep(1)
exit