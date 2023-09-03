# ---encoding:utf-8---
# @Time    : 2023/9/2 15:14
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    :  函数参数不可变对象
# @File    : NoChangeObject.py


# 函数参数不可变对象
def change(a):
    print(id(a))  # 指向的是同一个对象
    a = 10
    print(id(a))  # 一个新对象


if __name__ == '__main__':
    a = 1
    print(id(a))
    change(a)
