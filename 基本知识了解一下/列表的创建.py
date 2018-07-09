list = ['apple','banana','grape','orange']
print (list[-2])
print (list[1:3])
print (list[-3:-1])
list = [['apple','banana'],['grape','orange'],['watermelon'],['grapefruit']]
for i in range (len(list)):
    print ("list[%d]:"%i,end = ' ')
    for j in range (len(list[i])):
        print (list[i][j],end = ' ')
    print()
list.append(['strawberry'])#在末尾加入
list.insert(1,('berry',))#插入(位置,元素)
print (type(list[1]))
print (list)
#list.remove(['apple']) 不在list中,remove删除失败
print(list.pop())
print (list)