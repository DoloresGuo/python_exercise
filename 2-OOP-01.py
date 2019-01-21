"""
定义一个学生的类，用来描述学生
"""
class Student():
    pass
# 定义一个类如果没有内容必须加pass

# 定义一个对象
mingyue = Student()

# 定义一个类，用来描述学Python的学生
class PythonStudent():
    name = None
    #用None给不确定的值占位赋值
    age = 18
    course = "Python"

    def doHomework(self):
        print("我在做作业")
        #推荐在函数末尾用return语句
        return None
# 实例化一个叫yueyue的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有传递进入函数
yueyue.doHomework()

class Student():
    pass

    def say(self):
        self.name = "aaaa"
        self.age = "18"
        print("My name is {}".format(self.name))
        print("My age is {}".format(self.age))

yueyue = Student()
yueyue.say()

