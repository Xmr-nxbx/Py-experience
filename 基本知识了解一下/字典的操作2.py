#方法:dict.keys(),dict.values()使用
dict = {'a':'apple','b':'banana','g':'grape','o':'orange'}
print (dict.keys())
print (dict.values())
#del(dict['a']) #如果是del(dict),则是完全删除dict
#dict.clear()    #只是清空里面的元素
#print(dict)
#
#使用dict.get(value[,不存在返回值])
print(dict.get('c','不存在'))
print(dict.get('a'))
#
#使用update对一个字典添加另一个字典
dict1 = {'a': 'apple','b' : 'banana'}
dict2 = {'g': 'grape','o' : 'orange'}
dict1.update(dict2)
print (dict1,dict2)

#
#setdefault(key[,不存在则添加元素]),对字典的key查找,如果没有则添加元素或者None,如果有,返回get(key)
print(dict1.setdefault('a'))
print(dict1.setdefault('s','strawberry'))
print(dict1.get('s','None'))
#dict3 = {'a':'apple','a':'A'}如果建立字典时有两个相同的key值,则保留后面一个value
#print(dict3)
#
#字典的排序Sorted()用法,key=lambda 创建匿名函数返回结果, dict[0]表示key排序,如果对value排序,dict[1]
print (sorted(dict.items(),key=lambda dict:dict[0]))
print(dict)