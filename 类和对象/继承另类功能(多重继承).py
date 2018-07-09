###由于多重继承很容易引起代码混乱,最好不要使用(*与方法解析顺序有关Method Resolution Order 也叫做MRO):
from pprint import pprint
class One():
    str1 = 'One类的数据'
class Two():
    str2 = 'Two类的数据'
class Main(One,Two):
    def OutPut(self):
        print('第三个类调用多重继承后结果:')
        print(self.str1)
        print(self.str2)
P = Main()
pprint(Main.mro())          ###查看运行顺序
P.OutPut()
P = None
###相关网页:https://www.jianshu.com/p/71c14e73c9d9
###在零基础学习书中,有调用父类方法和super方法一说:
###在多重继承中.调用父类会使每一次父类按顺序运行(同时会运行重复的父类),可能使代码数据重新赋值
###用super方法,在调用顺序中,会使后调用的类(一般是父类)先运行(避免同种父类再次调用),再接着运行前面调用的类(从后往前):
class Fir():
    def __init__(self):
        print('调用了一层父类')
class Sec(Fir):
    def __init__(self):
        super().__init__()
        print('调用了二层第一个子类')
class Thi(Fir):
    def __init__(self):
        super().__init__()
        print('调用了二层第二个子类')
class For(Sec,Thi):
    def __init__(self):
        super().__init__()
        print('调用了三层子类')
pprint(For.mro())
P = For()
