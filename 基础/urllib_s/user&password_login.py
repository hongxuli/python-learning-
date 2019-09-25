import urllib.request as ur
import urllib.parse as ul

url = 'http'
userName = 'hongxu'
passWord = 'password'

pwdmgr = ur.HTTPPasswordMgrWithDefaultRealm()
pwdmgr.add_password(None,url,user,passWord)

auth_handler = ur.HTTPBasicAuthHandler(pwdmgr)
opener = ur.build_opener(auth_handler)

response = opener.open(url)
print(response.read().decode('utf-8'))

# ur.Request(
#     url = url,
#     headers={
#         'User-Agent':xxxxx(),
#         'Cookie':'xxxxxxx',
#     }
# )