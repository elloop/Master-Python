# -*- coding:utf-8 -*-
import requests

if "__main__" == __name__:
    url = "https://www.baidu.com"
    r = requests.get(url)
    print("status: ", r.status_code)
    print(r.text)


