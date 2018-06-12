# -*- coding:utf-8 -*-
import time
import requests

def saveResAsHtml(response):
    '''
    保存response正文
    '''
    file_path = "./response" + str(time.time()) + ".html"
    f = open(file_path, "w")
    f.write(response.text.encode("utf-8"))
    f.close()


if "__main__" == __name__:

    url = "https://www.baidu.com/s"

    # headers 模拟浏览器发送请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }

    # GET 请求参数，baidu搜索hello
    params = {
        "wd": "hello"
    }

    r = requests.get(url, params=params, headers=headers)

    print("request url with params is : {url_with_param}".format(url_with_param = r.url))

    saveResAsHtml(r)

