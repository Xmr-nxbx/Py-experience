def test1(key):
    print ('带入的值是:',key)
def test2(key = '500'):
    print ('key的值是:',key)
test1(1)
#test2中游默认函数(普通的是关键字函数)
print(test2()) #None指的是返回值是None,任何的函数都有返回值
def test3(*params):
    print (params)
    print ("第1个值为:",params[0])
list = [1,2,3,4,5]
test3(*list)        #*可以传递多个值,带入时解包,进入函数后打包
test3(list)
def test4(key):
    if key == 1:
        return 1,2,3,4              #返回元组
    else:
        return [1,2,3,4]            #返回列表
print ('1带入test4:',test4(1))
print ('test4的另一个结果:',test4(0))
#全局变量和局部变量:
def test5():
    print ('全局key1:',key1)
    key2 = 1
key1 = 3
test5()
#print('局部变量key2:',key2)        NameError在调用函数后,局部变量就被删除2