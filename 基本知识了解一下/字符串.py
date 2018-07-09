#3中表达字符串方式  单引号  双引号  三引号
#单引号和双引号表达相同             #符号都有的时候,外面的符号省略
str1 = '"Hello World"'
print (str1)
str2 = "'Hello World'"
print (str2)
#三引号中如果有双引号,双引号保留,三引号里面不能加单引号
str3 = '''I said:"Hello World"'''
print (str3)
#三引号还可以制作文档字符串,每个对象都有一个属性:__doc__(描述对象的作用)
class Hello:
    '''准备printhello world'''
    print ("Hello World")  #惊了,类要提前运行
print (Hello.__doc__)


#如果输出特殊字符,前面加\:\',\",\\