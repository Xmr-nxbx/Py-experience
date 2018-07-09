import random as r
class Fish(object):
    def __init__(self):
        self.x = r.randrange(1,11)
        self.y = r.randrange(1,11)
    def move(self):
        print('这条鱼的位置是',self.x,self.y)
