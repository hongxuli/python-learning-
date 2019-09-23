import urllib.request as ur

ret = ur.urlopen('https://edu.csdn.net/').read()
print(ret)

with open('edu.html','wb') as f:
    f.write(ret)