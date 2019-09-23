import urllib.request as ur
import urllib.parse as up
import json


word = input('input word need to translate')
data = {
    'kw':word
}

data_url = up.urlencode(data)
#data 先进行编码

request = ur.Request(
    url='https://fanyi.baidu.com/sug',
    data=data_url.encode('utf-8')
   # data 转换成字节类型
)

response = ur.urlopen(request).read()
#print(response)
#b'{"errno":0,"data":[{"k":"python","v":"n. \\u87d2; \\u86ba\\u86c7;"},{"k":"pythons","v":"n. \\u87d2; \\u86ba\\u86c7;  python
#\\u7684\\u590d\\u6570;"}]}'
#response is a json file 

ret = json.loads(response)
#print(ret)

translate = ret['data'][0]['v']
print(translate)