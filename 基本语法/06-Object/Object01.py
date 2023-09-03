# ---encoding:utf-8---
# @Time    : 2023/9/3 13:58
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    : 多继承
# @File    : Object01.py

# 多继承的格式：
# class 类名(父类1， 父类2， 父类3， ...):
#     pass


class A:
    def __init__(self):
        self.name = "A"

    def say(self):
        print("A")


class B:
    def __init__(self):
        self.name = "B"

    def say(self):
        print("B")


class C(A, B):
    def __init__(self):
        super().__init__()
        self.name = "C"


if __name__ == '__main__':
    c = C()
    print(c.name)
    c.say()