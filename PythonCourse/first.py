
import requests
from pyquery import PyQuery as pq
def WhatsUrName(*name):
    if not name:
        name = input("What's your name:")
    payload = {'ie':'utf-8','wd':name}
    r = requests.get("http://www.baidu.com/s", params=payload)
    return pq(r.text)
def ShowList():
    #doc = WhatsUrName("孔庆晓")
    doc = WhatsUrName()
    rlist = doc("h3.t").items()
    n = 0;
    for i in rlist:
        n = n + 1
        index = "%02d" % n
        print("======== "+ index + " ========\r\n\r\n" + "标题: " + i("a").text() + "\n" + "链接: " + i("a").attr("href") + "\r\n")
ShowList()