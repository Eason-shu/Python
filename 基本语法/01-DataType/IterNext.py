# ---encoding:utf-8---
# @Time    : 2023/9/2 14:39
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    : 迭代器
# @File    : IterNext.py

if __name__ == '__main__':
    # 创建一个可迭代对象
    my_list = [1, 2, 3, 4, 5]
    # 获取一个迭代器
    my_iter = iter(my_list)

    # 使用迭代器遍历元素
    try:
        while True:
            element = next(my_iter)
            print(element)
    except StopIteration:
        pass