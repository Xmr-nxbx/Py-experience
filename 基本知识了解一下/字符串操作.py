str1 = '学习学习再学习'
print (str1.count('学习'))
print (str1.find('再'))
print (str1.index('习'))     #从左往右进行,如果没有找到,find返回-1,index返回错误ValueError
list1 = str1.split(sep = '习')      #分割sep表示分割标准,maxsplit默认-1,表示最大分割次数
print (list1)
print ('习'.join(list1))              #列表中的str合并
#格式化练习(位置参数,关键词参数):
str2 = '{0}format:{1:.2f}'.format('数字',1.23456)
str3 = '{a}format:{b:.2f}'.format(a = '数字',b = 1.23456)
print(str2)
print(str3)
#格式化操作符号:'%'
print ('%c'%97) #格式化字符及ASC2码
print ('%s'%str3)
print ('%#o'%89)
print ('%.14f科学计数法:%e'%(0.00000002344567,0.00000002344567))    #%e或者%E科学计数法格式化浮点数
#转义字符:\(a->系统响铃,b->退格,t->横向制表符,v->纵向制表符,r->回车,f->换页)
print('\t')