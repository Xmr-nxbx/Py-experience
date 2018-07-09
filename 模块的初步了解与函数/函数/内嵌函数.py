#在函数内部更改全局变量:global关键字:
def test1():
    global key1
    key1 = 5
key1 = 3
test1()
print (key1)
#内嵌函数只能通过内部进行访问
def test2():
    print ('test2正在被访问')
    def test3():
        print('test3正在被访问')
    test3()
test2()
#test3()
