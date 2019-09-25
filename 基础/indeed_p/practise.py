import urllib.request as ur


keyword = input('please input keyword')
city = input('please input city')
url = 'https://ca.indeed.com/jobs?q={}&l={}%2C+MB'.format(keyword,city)


request = ur.Request(
    url=url,
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
    }
    )

response = ur.urlopen(request).read().decode('utf-8')

with open('./indeed_p/indeed2.html','w') as f:
    f.write(response)











'''
使用代理
'''
# proxy_websit = '代理地址'

# def get_proxy():
#     proxy_address = ur.urlopen(proxy_websit).read().decode('utf-8').strip()
#     return proxy_address

# proxy_handler = ur.ProxyHandler({
#     'http':get_proxy()
# })

# proxy_opener = ur.build_opener(proxy_handler)
# response = proxy_opener.open(request).read()



# response = ur.build_opener(ur.ProxyHandler({'http':'xxxxx'})).open(requset).read()