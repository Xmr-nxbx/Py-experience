list1 = ['apple','banana']
list2 = ['grape','orange']
#两个列表相加,方法1:用extend()
list1.extend(list2)
print (list1)
list3 = ['watermelon']
#方法2:使用运算符号操作'+'
list1 = list1 + list3
print (list1)
#或者用 +=
list1 += ['grapefruit']
print (list1)
#甚至可以用 * 不可以用 -
list1 = ['strawberry','blackberry'] * 2
print (list1)
list3 = list1.copy()
print('list3是list1的复制:',list3)
#骚操作:从第一个数据比大小,一旦被确定胜负,输出结果
list1 = [123,456]
list2 = [234,345]
print (list1 > list2)
print (list1 + [789])
list1 = list1 + [123]
print(list1.index(123))
#序列的方法:zip()返回迭代参数元组,,enumerate()返回序列和迭代参数的二元组
list1 = [1,2,3,5,6,7]
tuple1 = ('s','a','w','d')
str1 = 'laststr'
for each in zip(list1,str1,tuple1):
    print (each)
for each in enumerate(list1):
    print (each)