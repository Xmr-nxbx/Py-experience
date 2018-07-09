tuple1 = ("orange")
print (tuple1[0])   #当作元组,而程序生成的是str
print (type(tuple1))

tuple2 = ("orange",) #有一个句号,表示元组(可以多个数据输入,)
print (tuple2)
print (type(tuple2))

#确认某个元素的格式:type() 或者 isinstance(元素,格式)
print(isinstance(tuple,str))