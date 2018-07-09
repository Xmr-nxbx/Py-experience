###格式 class 类名(被继承类的名字)
class Parent:
    def func(self):
        print('这是父类的方法')
class Child1(Parent):
    pass
class Child2(Parent):
    def func(self):
        print('这是Child2覆盖父类的方法')
one = Child1()
two = Child2()
print('继承调用父类,调用子类覆盖父类:')
one.func()
two.func()