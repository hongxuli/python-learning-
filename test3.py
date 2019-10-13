

# # def start(url):
# #     print(url + ' start crawl')
# #     r = request(url, callback=pares)
# #     yield r


# # def request(url, callback=None):
# #     response = ' this is response'
# #     url = url + ' after request'
# #     print('test')
# #     yield  pares(response) 




# def gen1(url):
#     print('this is gen1')
#     for i in range (6):
#         yield gen2(url)


# def gen2(url, callback=None):
#     response = 'this is response'
#     url = url + 'after request'
#     # print('test')
#     for i in range (6):
#         yield pares(response)


# def pares(response):
#     print(response+' after pares')


# if __name__ == "__main__":
    
#     for i in range(3):
#         s = gen1('www.baidu.com')
#         for d in s:
#             next(d)
        
def fun():
    a = list([1, 2, 3, 4])
    print(type(a))
    yield a
ab= fun()
print(type(ab))
for i in ab:
    for d in i:
        print(d)
