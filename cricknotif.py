import requests
from bs4 import BeautifulSoup
from gi.repository import Notify
from time import sleep
def sendmessage(title, message):
    Notify.init("Test")
    notice = Notify.Notification.new(message)
    notice.show()
    return
url = "http://static.cricinfo.com/rss/livescores.xml"
while True:
    r = requests.get(url)
    while r.status_code is not 200:
            r = requests.get(url)
    soup = BeautifulSoup(r.text)
    data = soup.find_all("description")
    score = data[3].text
    sendmessage("Score", score)
    sleep(60)
