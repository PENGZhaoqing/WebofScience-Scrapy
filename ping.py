# coding=utf-8
import requests
import json
import time

is_login = False


def login():
    global is_login
    try:
        loginUrl = "http://210.77.16.21/eportal/InterFace.do?method=login&userId=%25E5%25BD%25AD%25E5%2585%2586%25E5%258D%25BF%255C201628008629001&password=asd456zxc123&service=&queryString=wlanuserip%253D0bc386d9e643d188b011a0d00c9b5c40%2526wlanacname%253D5fcbc245a7ffdfa4%2526ssid%253D%2526nasip%253D2c0716b583c8ac3cbd7567a84cfde5a8%2526mac%253D53ba540bde596b811a6d5617a86fa028%2526t%253Dwireless-v2%2526url%253D2c0328164651e2b4f13b933ddf36628bea622dedcc302b30&operatorPwd=&operatorUserId=&validcode=&passwordEncrypt=false"
        c = requests.get(url=loginUrl)
        res = json.loads(c.content)
        if res["result"] == "success":
            print "login success"
            is_login = True
        else:
            print res
            print "login failed"
    except Exception as e:
        print e
        print "login failed"


while True:
    try:
        a = requests.get(url="http://www.bilibili.com")
        if not a.headers["Connection"] == "close":
            is_login = True
            print "online"
        else:
            is_login = False
            print "offline, try to connect"
    except Exception as e:
        print e
        is_login = False

    time.sleep(1)

    while not is_login:
        login()
        time.sleep(1)
