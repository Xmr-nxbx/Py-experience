#使用dict2 = dict1.copy()对一个字典重新赋值
dict1 = {'a':'apple','b':'banana','c':["c",'cd']}
dict2 = dict1.copy()       #这种方法在dict1父对象是处于'深拷贝',但是在数组部分(子对象)处于浅拷贝
dict3 = dict1              #这种方法在dict1改变的时候也会同时改变dict3:浅拷贝

del(dict1['b'])            #改变dict1的同时改变dict3
dict1['c'].remove('cd')    #改变dict1['c']的元素时同时改变dict2和dict3

print('结果如下:')
print('dict1结果是:',dict1)
print('dict2结果是:',dict2)
print('dict3结果是:',dict3)
del(dict1)
del(dict2)
del(dict3)
#深拷贝操作:import copy
import copy
dict1 = {'a': 'apple','b':{'g':'grape','b':'banana'}}
print('原来的dict1:',dict1)
dict2 = copy.deepcopy(dict1)    #深拷贝:copy.deepcopy()
dict3 = copy.copy(dict1)        #与dict1.copy()相同
del(dict1['b']['g'])
#dict1['b'].setdefault('o','orange')
dict1['b']['o'] = 'orange'
dict1['a'] = dict1['a'] + 'Watch'
print ('现在的dict1:',dict1)
print ('dict2(深拷贝)与dict3(浅拷贝)对比如下:')
print ('dict2:',dict2)
print ('dict3:',dict3)