#缩进或空格对代码的影响
def example1(num1):
    if(num1 == 1):
        num1 += 1
    return num1
def example2(num1):
    if num1 == 1 :       #if条件括号可以删除
        return num1
    num1 += 1
    return num1
num1 = 1
print (example1(num1))
num1 = 3
print (example2(num1))