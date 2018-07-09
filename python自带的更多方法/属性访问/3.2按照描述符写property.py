class Myproperty():
    def __init__(self,fget = None,fset = None,fdel = None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, owner):
        print('输出值')
        return self.fget(instance)
    def __set__(self, instance, value):
        print('设置值')
        self.fset(instance,value)
    def __delete__(self, instance):
        print('删除值')
        self.fdel(instance)
    def __del__(self):      #del 与delete 区别:delete删除的是属性,del删除的是实例对象的所有引用属性
        print('这个类被删除了!')
class Example():
    def toget(self):
        return self.name
    def toset(self,value):
        self.name = value
    def todel(self):
        del self.name
    x = Myproperty(toget,toset,todel)
p = Example()
p.x = 5
print(p.x)
del p.x
del p