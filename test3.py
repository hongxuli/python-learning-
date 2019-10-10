def foo():
    a = 1  # (1)
    b = yield a  # (2)
    c = yield b  # (3)
    d = yield b + c  # (4)
    print("end with {}".format(d))


f = foo()
# 预激协程，一直执行到第一个yield左边的等号处暂停(先执行a=1，再执行#(2)行等号右边的yield a，输出1，然后暂停，变量b等待后续赋值)
print(next(f))
print(next(f))  # send(3)将3赋值给#(2)行的b，并继续往下执行，执行#(3)行的yield b，输出 3，c等待后续赋值
print(f.send(5))  # send(5)将5赋值给#(3)行的c，并继续往下执行，执行#(4)行的yield b+c，输出8，d等待后续赋值
print(f.send(7))  # send(7)将7赋值给#(4)行

