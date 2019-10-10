import urllib.parse as ul
import urllib.request as ur
#kw target name 
# kw='英雄联盟'
data = {
    'kw':'英雄联盟',
    'ie':'utf-8',
    'pn':'100'        #page number  50 per page 
}
# encode CN string 
data_url = ul.urlencode(data)

print(data_url)

#反编码
ret = ul.unquote(data_url)


request = ur.Request('https://tieba.baidu.com/f?'+data_url)
response = ur.urlopen(request).read()
print(response)

#wb   write binary 
# with open ('英雄联盟','wb') as f:
#     f.write(response)