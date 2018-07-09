#class小写,类名一般大写字母开头,函数名用小写字母开头
class Man():            ###加或不加()区别不算大,()里放被继承的类
    name = 'MoFaShi'
    age = 20
    sex = 'male'
    marry = False
    def itsName(self):
        print('他的名字是:',self.name)
    def itsAge(self):
        print('他有%d岁了'%self.age)
    def itsSex(self):
        print("他的性别是",self.sex)
    def itsMarry(self):
        print('是否已婚:',self.marry)

if __name__ == '__main__':
    man = Man()
    man.itsName()
    man.itsAge()
    man.itsSex()
    man.itsMarry()