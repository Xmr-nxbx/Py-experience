#容器类型包括:序列类型(列表,元组,字符串),映射类型(字典)
#定制容器,就要了解有关的协议:
#不可变容器:__len__()与__getitem__()
#可变容器在不可变容器基础上有__setitem__()与__delitem__()
class MyList():
    def __init__(self,*args):
        self.value = [x for x in args]  #建立列表,列表推导式:见3.8
        self.count = {}.fromkeys(range(len(args)),0)#以字典形式访问元素被访问次数,计数初始值设置为10
        print(type(self.value))
    def __len__(self):
        return len(self.value)
    def __getitem__(self, item):
        self.count[item] += 1
        return self.value[item]
li1 = MyList(1,3,5,7,9)
li2 = MyList(2,4,6,8,10)
print(li1[1],li2[3],li1[4]+li2[0])
print(li1.count)
print(li2.count)
print(len(li1))