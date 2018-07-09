#Python内部有一种name mangling名字改编技术,变量名或者函数名之前加上__就会变成私有
#如果要访问,可以用到_类名__变量名
class CeShi():
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

one = CeShi()
two = CeShi()
one.setName(input('输入一个变量:'))
two.setName(input('输入一个变量:'))
try:
    print('尝试访问内部私有变量:',one.__name,two.__name)
except:
    print('访问内部私有变量出错')
print(one.getName())
print(two.getName())
print('另一种方法访问之伪私有访问(_类名__变量名):',one._CeShi__name,two._CeShi__name)