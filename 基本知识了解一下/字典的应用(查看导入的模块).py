#有关全局字典sys.modules模块
#sys.modules会对加载的模块保存,第二次导入模块,调用缓存,加快程序运行速度
import sys
print (sys.modules.keys())
print (sys.modules.values())
print (sys.modules['os'])

#模块过滤(查看导入新的模块)
d = sys.modules.copy()
import copy,string
print (list(zip(set(sys.modules) - set(d))))        #如果不加list(),返回的则是一个对象