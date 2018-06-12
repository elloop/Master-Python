# -*- coding:utf-8 -*-
import time
import requests

if "__main__" == __name__:

    url = "https://www.baidu.com"

    # headers 模拟浏览器发送请求
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }

    r = requests.get(url, headers=head)

    # 遍历服务器返回response里面的cookies
    for (k, v) in r.cookies.items():
        print("cookies: {key} = {value}".format(key = k, value = v))


    # cookies: BAIDUID = CBA89DD98C1F4F78C2B49971A431D12C:FG=1
    # cookies: BIDUPSID = CBA89DD98C1F4F78C2B49971A431D12C
    # cookies: H_PS_PSSID = 1444_21096_26350_26577_20718
    # cookies: PSTM = 1528820415
    # cookies: BDSVRTM = 0
    # cookies: BD_HOME = 0

    # 客户端请求中添加cookie
    url2 = "http://httpbin.org/cookies"
    client_cookie = dict(my_cookie_key="hahahaha")
    r2 = requests.get(url2, cookies=client_cookie)
    print("\n")
    print(r2.text)

    # 客户端可指定cookie的所生效的访问url路径
    jar = requests.cookies.RequestsCookieJar()
    jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
    jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
    url3 = 'http://httpbin.org/cookies'
    r3 = requests.get(url3, cookies=jar)
    print("\n")
    print(r3.text)  # 访问路径为/cookies, 只有'tasty_cookie'生效。




