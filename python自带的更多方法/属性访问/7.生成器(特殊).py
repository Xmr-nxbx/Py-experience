#生成器摆脱了类和对象,只需要在普通函数里加上yield实现
#生成器是迭代器中的一种实现,运行到yield处暂停或者是被挂起,第二次调用函数时,就在后面继续或者重新开始
#以斐波那契数列为例:
def fibs(n = 20):
    a = 0
    b = 1
    i = 0
    while i <= n:
        a,b = b,a + b
        yield a
        i = i + 1
for each in fibs():
    print(each)