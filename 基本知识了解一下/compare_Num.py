#随机生成两个数字,比较大小
import random

def compareNum(num1 , num2):
    if(num1 <num2 ):
        return "数字2比数字1大"
    elif (num1 == num2):
        return "数字1和数字2相等"
    else:
        return "数字1比数字2大"
num1 = random.randrange(1,9)
num2 = random.randrange(1,9)
print ("num1 = ",num1)
print ("num2 = ",num2)
print (compareNum(num1,num2))
