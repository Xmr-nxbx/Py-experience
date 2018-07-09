###__new__(cls[,...])是对象实例化调用的第一个方法,前面的cls指的是这个类,其他参数传递给__init__()
###__new__()需要返回一个 实 例 对 象,通常是这个类的实例对象,也可以返回其他对象
###一般在继承一个不可变的类型的时候需要重写
class CapStr(str):
    def __new__(cls,string):
        string = string.upper()
        return str.__new__(cls,string)
a = CapStr('yes,it is')
print(a)
##一般在继承中继承不可变类型就较为重要