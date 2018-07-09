###组合有点像是在类里创建其它类的对象,再进行操作
class Turtle:
    def __init__(self,x):
        self.x = x
class Fish:
    def __init__(self,y):
        self.y = y
class Pool:             ###在这个类中创建其它类的对象
    def __init__(self,x,y):
        self.fish = Fish(y)         ###创建的对象是self.对象名 = 对象([元素])
        self.turtle = Turtle(x)
    def OutPut(self):
        print ('池子中有鱼%d条,乌龟%d只'%(self.fish.y,self.turtle.x))
pool = Pool(5,7)
pool.OutPut()
###有关Mixin使用:http://bbs.fishc.com/thread-48888-1-1.html   (在Python3.x不能运行)