from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

import sys
import os


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


resource_path('icon.ico')


def notifyTangi(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="E:\covidnotify\icon.ico",
        timeout=8
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    while True:
       # notifyTangi("Tangi", "Virus ki ma behen ek kar de !!")
        myHtmlData = getData('https://www.mohfw.gov.in/')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[1].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")

        states = ['Kerala', 'Maharashtra', 'Karnataka', 'Delhi', 'West Bengal']
        for item in itemList[0:23]:
            dataList = item.split("\n")
            if dataList[1] in states:
                print(dataList)
                nTitle = 'Cases of Covid-19'
                nText = f"{dataList[1]} \nIndian:{dataList[2]}<-->Foreign:{dataList[3]}\n Cured:{dataList[4]}Deaths:{dataList[5]}"
                notifyTangi(nTitle, nText)
                time.sleep(2)

        time.sleep(1800)
