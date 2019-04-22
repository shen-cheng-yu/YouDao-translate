import requests
import os
import json
import random
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
#这里的问号前面有一个 _o 要删掉

word = input("请输入要翻译的文字：")
agent_list = [
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0 Safari/537.36 OPR/15.0",
     "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Safari/535.1 Chrome/14.0.835.202 360EE"
]
user_agent = random.choice(agent_list)
#这个爬虫用不到 header ，但可以加深练习，而且这里的 referer 放第 4 行那个 url 也行好像
header = {
    "User-Agent": user_agent,
    "Referer": "http://fanyi.youdao.com/?keyfrom=fanyi.logo"  # 从这个 url 请求过来的
}
# 最基本的只需要保留 i 和 doctype 就行了
formData = {
    'i': word,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15552145285567',
    'sign': '1bb13722dda908dda3d8738eb30fc844',
    'ts': '1555214528556',
    'bv': 'd6c3cd962e29b66abe48fcb8f4dd7f7d',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
    'doctype': 'json'
}
response = requests.post(url,formData,header)

# print(type(response))        <class 'requests.models.Response'>
# print(type(response.text))   <class 'str'>
# print(response.text)

content = response.text
result = json.loads(content)  #将字符串转换成一个字典对象

# print(type(result))   <class 'dict'>
# print(result['translateResult'])

result = result.get('translateResult')[0]
# result = result[0]  或者另起一行提取第0个元素

for i in result:
    #file_name = "翻译结果"+i['src'][0]+".txt"
    print("原文：%s"%i['src'])
    print("译文：%s"%i['tgt'])
    #with open(file_name,"wb") as f:
       # f.write(i['tgt'])   # TypeError: a bytes-like object is required, not 'str'
       # f.write(i['tgt'].content)     # AttributeError: 'str' object has no attribute 'content'
    print("---------------------------------分割线----------------------------------")

os.system("pause")