#利用__iter__()和__next__()重写迭代器本身
#以斐波那契数列为例:
class Fibs:
    def __init__(self,n = 20):
        self.a = 0
        self.b = 1
        self.n = n
        self.num = 0
    def __iter__(self):
        print('创建自身的迭代器')
        return self
    def __next__(self):
        self.num = self.num + 1
        self.a,self.b = self.b,self.a + self.b
        if self.num > self.n:
            raise StopIteration
        else :
            return self.a
fibs = Fibs(10)
for each in fibs:   #最开始调用__iter__(),再不断调用__next__()知道发出StopIteration
    print(each)