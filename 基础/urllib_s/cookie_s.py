import urllib.request as ur


#moudle  that contain random userAgents
import user_agent


import lxml.etree as le




request = ur.Request(
    url='http.....',
    headers={
        # user agent 大写
        'User-Agent':user_agent.get_usr_agent_pc(),
        # 在浏览器network里  request headers  cookie   
        'Cookie':'.......'
    }
)

response = ur.urlopen(request).read().decode('utf-8')
with open('xxxxx.html','w',encoding='utf-8') as f:
    f.write(response)

html_x = le.HTML(response)
title_s = html_x.xpath('')
print(title_s)