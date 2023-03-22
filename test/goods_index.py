import threading
from threading import Thread
import requests
import queue
import time
a = 0
countryCode = [
    ("us", "en"),
    ("ca", "en"),
    ("au", "en"),
    ("gb", "en"),
    ("fr", "fr"),
    ("mx", "es"),
    ("es", "es"),
    ("de", "de")
]


def index_work(goods, que):
    for i in range(100):
        count_data = que.get()
        url = f"https://api-t-3.azazie.com/1.0/build-index/increment?debug=true&goods_ids[]={goods}"
        headers = {"Content-Type": "application/json", "x-app": "pc", "x-token": "", "x-languageCode": count_data[1],
                   "x-project": "azazie", "x-countryCode": count_data[0], "cache-action": "flush"}
        requests.get(url=url, headers=headers)
        print(count_data[0], '完成',threading.enumerate())


if __name__ == '__main__':
    que = queue.Queue()

    # 把国家传入队列
    for i in countryCode:
        que.put(i)
    thread_obj = []

    # 创建线程数
    for i in countryCode:
        obj = Thread(target=index_work, args=('1055824', que))
        thread_obj.append(obj)

    for i in thread_obj:
        i.start()

    for i in thread_obj:
        i.join()
