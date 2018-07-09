set1 = {1,2,3}
print (type(set1))
#unknown = {}
#unknown = set()
#print (type(unknown))
#集合建立用set_n = set()或者{元素},否则识别成字典
#添加:add() 添加多个update([元素]) 删除:remove(value),不能更改元素
set1.add(5)
set1.remove(1)
print (set1)

#像元组一样不能添加删除元素:frozenset()
set1 = frozenset(set1)
#set1.remove(3)
#此时不能改变数据