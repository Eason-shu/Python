# ---encoding:utf-8---
# @Time    : 2023/9/3 13:38
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    : Self
# @File    : SelfTest.py

class SelfTest:
    def __init__(self):
        pass

    def __str__(self):
        return "SelfTest"

    def __del__(self):
        print("SelfTest对象被回收了")

    def __new__(cls, *args, **kwargs):
        print("创建SelfTest对象")
        return super().__new__(cls)

    def __call__(self, *args, **kwargs):

        print("SelfTest对象被调用了")

    def __getitem__(self, item):
        print("获取SelfTest对象的索引值")
        return item

if __name__ == '__main__':
    SelfTest()()
    SelfTest()[1]
    print(SelfTest())
