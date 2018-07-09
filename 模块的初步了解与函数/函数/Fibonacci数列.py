def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci (n - 2)
n = int (input('请输入斐波那契数:')) - 1
print (fibonacci(n))