#property(特性/属性)描述符:descriptor
#指的是某种特殊类型的类的实例指派给另一个类的属性
#特殊类型的类指的是含有__set__().__get__(),__delete__()三个特殊方法的任一个
class MyDescriptor():
    def __get__(self, instance, owner):
        print('正在访问',self,instance,owner)   ###self指的是描述符自身的实例,instance是描述符拥有者所在类的实例,owner描述符拥有者所在类的本身
    def __set__(self, instance, value):
        print('正在设值',self,instance,value)
    def __delete__(self, instance):
        print('正在删除:',self,instance)
class Example():
    x = MyDescriptor()
p = Example()
p.x = 0
p.x
del p.x