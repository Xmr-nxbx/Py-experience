dict = {'a' : 'apple','b' : 'banana','g' : 'grape','o' : 'orange'}
print('使用for in 带入key,输出dict[key]:')
for k in dict:
    print ('dict[%s]'%k,dict[k])
print('使用dict.items(),输出key,value的元组的列表:')
print(dict.items())
print(type(dict.items))
print('使用(key,value)for in 带入,循环输出dict[key] = value:')
for (key,value) in dict.items():
    print('dict[%s]'%key,value)
#混合字典建立:
dict ={'a':('apple',),'bo':{'b':'banana','o':'orange'},'g':['grape','grapefruit']}
print (dict['a'])
print (dict['a'][0])
print (dict['bo'])
print (dict['bo']['b'])
print (dict['g'])
print (dict['g'][1])
