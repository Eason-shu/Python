# ---encoding:utf-8---
# @Time    : 2023/9/2 14:33
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    :  Python 推导式
# @File    : Comprehensions.py

if __name__ == '__main__':
    #列表推导式
    list1 = [i for i in range(1, 10)]
    # 循环打印
    for item in list1:
        print(item)
    #集合推导式
    set1 = {i for i in range(1, 10)}
    # 循环打印
    for item in set1:
        print(item)
    #字典推导式
    dict1 = {i: i + 1 for i in range(1, 10)}
    # 循环打印
    for item in dict1:
        print(item)
    #生成器推导式
    gen1 = (i for i in range(1, 10))
    # 循环打印
    for item in gen1:
        print(item)


