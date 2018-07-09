###严格要求方法有实例才能被调用
class A():
    def func1():
        print('成功的输出了结果!')
    def func2(self):
        pass
a = A()
A.func1()
try:
    a.func1()
except TypeError:
    print('没有成功调用类中的函数')##这是因为Python的绑定机制,会把a对象作为(((第一个参数传入)))
###用'__dict__'查看对象所拥有的属性
print(a.__dict__)
print(A.__dict__)
###这个字典中只有实例对象的属性,键为属性名,值为数据值
###这其中的self相当于是代替了对象名字,传入参数例如 : 类中的self.value,其实就是 属性名字.value
##如果删除类示例,调用存在的属性的方法:
del A
a.func2()