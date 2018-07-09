#每一次迭代结果作为下次开始的初始值
#关于迭代python有两个Built-in function:iter()和next()
#对iter()的调用就是得到他的迭代器,next()返回下一个值,如果迭代器没有值可以调用,抛出StopIteration
#关于操作如下
def diedai(*args):
    it = iter(args)
    while True:
        try:
            each = next(it)
            print(each)
        except:
            break;
list = [1,2,3,4,5,6,7]
set = {1,2,3,4,5,6,7}
dict = {'5':3,'6':4}
string = '1234567'
diedai(*list)
diedai(*set)
diedai(*dict)#字典迭代出的是key
diedai(*string)