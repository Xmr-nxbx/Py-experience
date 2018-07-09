#需要一个函数和一个可迭代对象,返回对象map
print (list(map(lambda x,y: x ** y,range(10),range(10,0,-1))))
#总之,类似于filter(函数或者lambda函数,可迭代对象1[,可迭代对象2...])
#map(函数或者lambda函数,可迭代对象[,可迭代对象...])函数中有多个元素时,可迭代对象数 = 元素的个数
print (list(map(lambda x,y,z:x + y + z,range(10),range(10,20),range(20,30))))