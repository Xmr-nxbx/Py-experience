#基本上都是算术操作符函数英文名称前加上r
#反运算就是第一个为数或者其他(此时不支持__add__()函数),就会执行__radd__()函数
#所以在做减法,除法之类讲究先后顺序的计算时,rsub rdiv return的数据与算术操作的位置相反
class Toint(int):
    def __radd__(self, other):
        print('radd')
        return int.__add__(other,self)
    def __rtruediv__(self, other):
        print('rtruediv')
        return int.__truediv__(other,self)
    def __rsub__(self, other):
        print('rsub')
        return int.__sub__(other,self)
    def __rmul__(self, other):
        print('rmul')
        return int.__mul__(other,self)
a = Toint(6)
print(3 + a)
print(16 - a)
print(10 * a)
print(18 / a)