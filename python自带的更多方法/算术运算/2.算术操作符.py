#对原油的方法进行重写
class caozuoint(int):
    def __add__(self,n):
        return int.__add__(self,n)
    def __sub__(self,n):
        return int.__sub__(self,n)
    def __mul__(self,n):
        return int.__mul__(self,n)
    def __truediv__(self,n):
        return int.__truediv__(self,n)
    def __floordiv__(self,n):         #与truediv不一样的是,floordiv是整数除法没有四舍五入
        return int.__floordiv__(self,n)
    def __mod__(self,n):
        return int.__mod__(self,n)
    def __pow__(self,n):
        return int.__pow__(self,n)
a = caozuoint(7)
b = caozuoint(5)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a ** b)
class cuow(int):
    def __sub__(self, other):
        return int(self) - other       #如果不加形式限制,就会不断地访问self的同一种函数
c = cuow(3)
d = cuow(4)
print(d - c)