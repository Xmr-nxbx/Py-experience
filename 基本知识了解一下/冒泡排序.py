def bubble_sort(num):
    for j in range(0,len(num)-1):
        for i in range(len(num)-1,j,-1):
            if(num[i] < num[i-1]):
                num[i],num[i-1] = num[i-1],num[i]
    print ("结果是:",num)
num=input("请输入数组:").split(" ")
bubble_sort(num)
print (num[int(input("请输入数组中的位置:"))-1])