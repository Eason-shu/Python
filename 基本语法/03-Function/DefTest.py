# ---encoding:utf-8---
# @Time    : 2023/9/2 15:09
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    : 函数定义
# @File    : DefTest.py


# 函数定义
def printme(str):
    print(str)
    return

if __name__ == '__main__':
    printme('Hello World')
    printme('Hello Again')
    printme('Hello Python')
    # 关键字参数
    printme(str='Hello Python')
    # 默认参数
    def printinfo(name, age=35):
        print('Name:', name)
        print('Age:', age)
        return
