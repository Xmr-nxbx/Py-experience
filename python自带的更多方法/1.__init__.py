###__init__也就是构造函数,一般用于初始化对象的属性,函数的返回值一定是None否则抛出tryerror
class exam(object):
    def __init__(self,n):
        self.num = n
        return
p = exam(5)
print(p.num)
###python没有重载函数