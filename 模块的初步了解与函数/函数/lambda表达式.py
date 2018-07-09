#用关键词lambda创建函数->匿名函数
def addfunc(x,y):
    return x+y
print (addfunc(1,5))
#可以表示为:
g = lambda a,b : a + b
print (g(1,5))
#lambda函数作用:代码简洁;不需要考虑命名的问题;简化代码可读性