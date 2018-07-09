tuple = (("apple","banana"),("grape","orange"),("watermelon",),("grapefruit",))
#tuple = (("apple","banana"),("grape","orange"),("watermelon",),("grapefruit")) #当最后一个元素不再是元组时,当做str处理
for i in range(len(tuple)):
    print("tuple[%d];"%i,"",)
    for j in range(len(tuple[i])):
        print(tuple[i][j],"",)
    print()
#另一种方式
for i in tuple:
    for j in i:
        print (j,end = ' ')
    print()