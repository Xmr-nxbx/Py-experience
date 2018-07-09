a = int(input("请输入学生成绩(100以内):"))
if a > 100 or a < 0:
    print ("输入错误")
elif a >= 90:
    print ("A等级")
elif a >= 80:
    print ("B等级")
elif a >= 70:
    print ("C等级")
elif a >=60:
    print ("D等级")
else:
    print ("不及格")