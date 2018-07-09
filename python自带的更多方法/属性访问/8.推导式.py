#属性名字 = '('或者'{'或者'[' 元素形式 for 元素 in 迭代器 [条件 if] ']'或者'}'或者')'
list = {i for i in range(10) if i % 2}
print(list)
tuple = (i for i in range(10))
print(tuple)
dict = {i:i % 2 == 0 for i in range(10)}
print(dict)
#string和集合一样有同种功能
#不过tuple返回的是对象生成器(generator),需要手动迭代:
print(next(tuple))
for i in tuple:
    print(i)