#如果带入元组或者列表则用到*打包和解包
#字典用到**操作:
def test1(**params):
    for each in params.items():
        print (each)
dict1 = {'a':'apple','b':'banana'}
test1(**dict1)
#注意,打包和解包都是两个*