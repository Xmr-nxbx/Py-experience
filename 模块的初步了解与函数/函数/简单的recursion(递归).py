import sys
sys.setrecursionlimit(10000)
def recursion(x):
    if x == 1:
        return 1
    elif x < 1:
        return '输入错误'
    else:
        return x * recursion (x - 1)
x = int (input("请输入阶乘数:"))
print (recursion(x))