###使用super函数
from MoBan import Fish as f
class NormalFish(f):
    pass
class Shark (f):
    def __init__(self):
        super().__init__()
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