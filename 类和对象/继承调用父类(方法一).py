###再一次运行一遍父类的函数
from MoBan import Fish
class NormalFish(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        ###为了可以调用父类,可以在此处使用  父类名.函数名  再运行一次
        Fish.__init__(self)
        self.hungry = True
    def isHungry(self):
        if self.hungry == True:
            print('鲨鱼很饿')
            self.hungry = False
        else :
            print('鲨鱼不饿')
one = NormalFish()
two = Shark()
one.move()
two.isHungry()
two.isHungry()
two.move()