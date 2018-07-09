#字典创建方法有多个
#直接创建:
dict1 = {}
dict1['a'] = 'apple'
print (dict1)
#fromkeys()创建:
dict2 = {}
dict2 = dict.fromkeys(('a'),('apple'))      #如果用dict2.fromkeys()则有可能不能保存dict2数据
print (dict2)
#用dict方法创建:
dict3 = dict({'a':'apple'})
print (dict3)
dict4 = dict(a = 'apple', b = 'banana')
print (dict4)
dict5 = dict([('a','apple'),('b','banana')])
print (dict5)