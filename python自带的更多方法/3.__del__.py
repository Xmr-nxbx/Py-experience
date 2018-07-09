###对象销毁的时候,这个函数就会执行
#这个函数是在对象都被 销毁 后进行的一种垃圾回收机制
class exam:
    def __del__(self):
        print('执行垃圾回收')
a = exam()
b = a
c = b
del a
del b   #由于ab销毁了c引用的实例对象没有销毁,就不会执行__del__
del c