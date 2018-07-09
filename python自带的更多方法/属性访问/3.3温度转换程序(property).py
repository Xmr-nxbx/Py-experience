class SheShiDu():
    def __set__(self, instance, value):
        self.name = value
    def __get__(self, instance, owner):
        return self.name
    def __delete__(self, instance):
        del self.name
        print('原记录已删除')
class HuaShiDu():
    def __get__(self, instance, owner):
        return instance.she * 1.8 + 32
    def __set__(self, instance, value):
        instance.she = (value - 32) / 1.8
    def __delete__(self, instance):
        del instance.she
class ZhuanHuanQi():
    she = SheShiDu()
    hua = HuaShiDu()
start = ZhuanHuanQi()
start.she = int(input('请输入摄氏度:'))
print('华氏度为%d°'%start.hua)
print('摄氏度为%d°'%start.she)
start.hua = int(input('请输入华氏度:'))
print('华氏度为%d°'%start.hua)
print('摄氏度为%d°'%start.she)
del start.hua