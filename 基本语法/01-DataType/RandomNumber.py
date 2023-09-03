# ---encoding:utf-8---
# @Time    : 2023/9/2 11:14
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    :  随机模块
# @File    : RandomNumber.py

import random

if __name__ == '__main__':
    # 生成一个随机数
    print(random.random())
    # 生成一个指定范围的随机数
    print(random.randint(1, 10))
    # 生成一个指定范围的随机数
    print(random.randrange(1, 10))
    # 生成一个指定范围的随机数
    print(random.uniform(1, 10))
    # 生成一个指定范围的随机数
    print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    # 生成一个指定范围的随机数
    print(random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=5))
    # 生成一个指定范围的随机数
    print(random.shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    # 百分率随机数
    print(random.random() * 100)
