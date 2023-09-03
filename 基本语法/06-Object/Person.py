# ---encoding:utf-8---
# @Time    : 2023/9/3 13:30
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    :  类定义
# @File    : Person.py

# 类的定义格式：
class Person:
    # 类属性
    name = ""
    age = 0
    # 初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 类方法
    def say(self):
        print("my name is {0}, I am {1} years old".format(self.name, self.age))
    # 类方法
    def __str__(self):
        return "my name is {0}, I am {1} years old".format(self.name, self.age)
    # 类方法
    def __del__(self):
        print("对象被回收了")

    def __new__(cls, *args, **kwargs):
        print("创建对象")
        return super().__new__(cls)

    def __call__(self, *args, **kwargs):
        print("对象被调用了")

    def __getitem__(self, item):
        print("获取对象的索引值")
        return item



if __name__ == '__main__':
    Person("Darwin", 18).say()