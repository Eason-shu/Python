# ---encoding:utf-8---
# @Time    : 2023/9/2 13:20
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    : for循环
# @File    : FOR.py
if __name__ == '__main__':
    # for循环
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d*%d=%d' % (j, i, i * j), end='\t')
        print()

    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)

    for x in "banana":
        print(x)

    for x in range(6):
        print(x)

