#导入任意:
import random
print (random.randint(0,10))
print (random.randrange(0,11))  #两句意思差不多

#导入系统用法:Operate System:OS
import os
#文件访问一般是通过OS实现
print(os.getcwd())          #当前工作目录
os.chdir('D:\\')            #改变当前工作目录change
print ('在%s路径下的文件:\n'%os.getcwd(),os.listdir())             #列出当前的工作目录的文件
#
#mkdir()创建新的文件夹,如果存在返回错误FileExistsError
os.mkdir('新建文件夹之测试文件')

#
#makedirs()创建多层文件夹(与mkdir不同,有s)'.\'相当于当前目录###同理mkdir,makedirs()如果存在目录,返回错误
os.makedirs(r'.\a\b\c')    #r的存在可以不用重写,
#删除:
#删除文件用remove(),删除目录用rmdir(),删除多个目录用removedirs()
os.remove('1.txt')
os.rmdir('新建文件夹之测试文件')
os.removedirs(r'.\a\b\c')
print ('在%s路径下的文件:\n'%os.getcwd(),os.listdir())
#walk(path)返回path中所有子目录('路径',[包含目录],[包含文件])