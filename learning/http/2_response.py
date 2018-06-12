# -*- coding:utf-8 -*-
import requests

def dumpResonpse(r):
    '''
    打印出response的字段
    url	请求的URL
    status_code	状态码
    encoding	响应编码，这个值可以改变，改变之后text属性也会根据编码而变化
    text	HTTP字符
    content	未编码的二进制数据
    json()	返回JSON数据
    raw	结果的原始字节流
    headers	请求头字典
    cookies	cookies字典
    history     如果发生重定向，所有请求对象都会保存到这里
    '''
    print("status_code: ", r.status_code)
    print("\n")

    print("url: ", r.url)
    print("\n")

    print("encoding: ", r.encoding)
    print("\n")

    print("headers: ", r.headers)
    print("\n")

    print("cookies: ", r.cookies)
    print("\n")

    print("history: ", r.history)
    print("\n")

    print("text: ", r.text)
    print("\n")

    print("content: ", r.content)
    print("\n")

    try:
        print("json: ", r.json())
    except:
        print("no json")
    print("\n")

    print("raw: ", r.raw)
    print("\n")


if "__main__" == __name__:
    url = "https://www.baidu.com"
    response = requests.get(url)
    dumpResonpse(response)


