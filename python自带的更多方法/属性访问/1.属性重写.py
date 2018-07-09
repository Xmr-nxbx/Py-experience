#与__del(set)attr__(self,item)有关,在进行get时,有两种方式都会执行getattribute(),如果不存在才会执行__getattr__
class A(object):
    def __getattribute__(self, item):#访问类的属性: 对象.value
        print('执行getattribute')
        return super().__getattribute__(item)
    def __getattr__(self, item):#获取一个不存在的类的属性
        print('执行getattr')
    def __setattr__(self, key, value):
        print('执行setattr,key = %s,value = %s'%(key,value))
        super().__setattr__(key,value)
    def __delattr__(self, item):
        print('执行delattr:删除%s'%item)
        super().__delattr__(item)
a = A()
a.sum
a.sum = 0
print(a.sum)
del a.sum