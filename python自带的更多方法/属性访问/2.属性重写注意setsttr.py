#注意重写setsttr或者调用其他方法时,避免重复调用的错误:比如:
#delsttr中写del self.value
#getattr中写return self.value
#setsttr中写self.value = x
class Right():
    def __init__(self):
        self.x = 1
        self.y = 2#这种赋值操作调用了__setattr__()
    def __setattr__(self, key, value):
        try:
            self.key = value
        except:
            print('不能在setsttr中写=赋值操作')
        super().__setattr__(key,value)
    def __getattribute__(self, item):
        try:
            value = self.item
            return value
        except:
            print('不能直接return')
            return super().__getattribute__(item)
p = Right()
print(p.x)