import urllib.request as ur

#.strip  去掉代理地址分隔符
proxy_adress = ur.urlopen('代理借口地址 http.....').read().decode('utf-8').strip()


#创建proxyHandler
proxy_handler = ur.ProxyHandler(
    {
        'http':proxy_adress
    }
)

#新建opener对象
proxy_opener = ur.build_opener(proxy_handler)


request = ur.Request(url='https:....')
response = proxy_opener.open(request).read()
