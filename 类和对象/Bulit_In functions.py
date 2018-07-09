class A(object):
    pass
class B(A):
    other = '特殊值'
    def getNum(self):
        return self.num
    def setNum(self,n):
        self.num = n
    def delNum(self):
        del self.num
    def spmething(self):
        pass
    x = property(getNum,setNum,delNum)         ###38排! 填入函数名,没有括号
p = B()
###issubclass判断第一个类是不是第二个类或者元组的子类
print(issubclass(B,(A,)))
###isinstance判断第一个元素是否是属于第二个类或者元祖的实例对象
print('判断建立的p对象是B的实例对象:%s\n判断建立的p对象是否是A的实例对象:%s'%(isinstance(p,B),isinstance(p,A)))
###hasattr(object,name)判断name这个属性是否在这个对象里  注意!!!name要用字符串表示出来
print('未建立属性时:',hasattr(p,'num'))
p.setNum(3)
print('建立属性后:',hasattr(p,'num'))
###geattr(object,name,[default])返回属性,如果在对象中不存在,抛出错误或者返回default位置处的值
print(getattr(p,'num','未找到'))
print(getattr(p,'o','未找到'))
###setattr(object,name,value)设置属性中的值,如果不存在,新建
setattr(p,'o',2)
print(getattr(p,'o','未找到'))
try:
    setattr(p,'something','重新设置')
except:
    print('不能覆盖类中的方法')
print(getattr(p,'something','something方法没有被覆盖'))
###delattr(object,name)删除对象中的值
print(p.other)
delattr(B,'other')          ###只能删除类对象
print(getattr(p,'other','不存在了'))
###property(fget,fset,fdel,doc)前三个是指的是对象中的方法,方便调用,返回一个设置的属性,通过输出,赋值'=',删除(del)快速操作
print(p.x)
p.x = 19
print(p.x)
del p.x
print(getattr(p,'num','num已经被删除'))