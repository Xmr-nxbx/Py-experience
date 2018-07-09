#函数式编程的一种语法结构(内嵌函数):
def funx():
    x = 5
    def funy():
        y = 0
        y += x
        #x += x
        print (x)
    return funy
#内部可以访问这个变量,但是不能修改外部(不是全局)的变量
i = funx()
i()
#解决方法1:
def funx1():
    x = 5
    def funy1():
        nonlocal x
        x += x
        return x
    return funy1()
    #return funy1            ###千万注意没有(),不是funy1()
i = funx1()
#print(i())             ###若前者是funy1(),则i后面不需要()
print(i)
#解决方法2:
def funx2():
    x = [5]
    def funy2():
        x[0] += x[0]
        return x[0]
    return funy2
i = funx2()
print(i())