#像self中的例子,如果在创建对象时,自动就创建好一些对象的属性,可以用到__init__
class Drink():
    def __init__(self,name):
        self.name = name
    def saySomething(self):
        print('对象中name的值为%s'%self.name)
drink = Drink('果汁')
drink.saySomething()