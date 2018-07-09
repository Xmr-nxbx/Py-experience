import myModule2
print ('count =',myModule2.func())
myModule2._count = 10
print ('count =',myModule2._count)
#再一次import myModule时不会改变_count
import myModule2
print ('count =',myModule2.func())