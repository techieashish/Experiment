__author__ = 'ASHISH'

import requests
import bs4
import time
import esse


def extract(url, choice=None):
    while True:
        try:
            headers = {'USER-AGENT': 'Mozilla/5.0'}
            res = requests.get(url, headers=headers)
        except (Exception, requests.RequestException, ConnectionError, TimeoutError) as e:
            print(e)
            time.sleep(30)
        else:
            break
    if choice == "res":
        return res
    else:
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        return soup


def zomato():
    u = 441
    while u > 0:
        url = "https://www.zomato.com/ncr/restaurants?page=%s" % u
        data = extract(url)
        for div in data.findAll('div', class_="ui cards"):
            articles = div.findAll('div', class_="content")
            for article in articles:
                everything = article.find('div', class_="col-s-12").findAll('a')
                for i in everything:
                    print(i.text)
        u -= 1
