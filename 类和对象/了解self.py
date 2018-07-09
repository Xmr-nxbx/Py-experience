#每一个self对应的是每一个创建好的对象的本身,这样,创建多个对象时,就不会发生对象对应的错误
class Drink():
    def setName(self,name):
        self.name = name
    def putSomething(self):
        print('我输入的是%s饮料'%self.name)
if __name__ == '__main__':
    drink1 = Drink()
    drink2 = Drink()
    drink1.setName('果汁')
    drink2.setName('可乐')
    drink1.putSomething()
    drink2.putSomething()
    #在这里,将会输出两个不同的结果