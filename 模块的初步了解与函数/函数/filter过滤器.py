#filter有两种方法:
def odd(a):
    return a%2
print (list(filter(odd,range(11))))
#或者filter(None,可迭代对象) 返回可迭代对象里的True
print (list(filter(None,[1,0,2,True,False])))