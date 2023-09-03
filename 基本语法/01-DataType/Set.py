# ---encoding:utf-8---
# @Time    : 2023/9/2 14:25
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    :  Set集合
# @File    : Set.py

if __name__ == '__main__':
    set1 = {1, 2, 3, 4}  # 直接使用大括号创建集合
    set2 = set([4, 5, 6, 7])  # 使用 set() 函数从列表创建集合
    print(set1)
    # 集合的基本操作
    # 1.添加元素
    set1.add(5)
    print(set1)
    # 2.删除元素
    set1.remove(5)
    print(set1)
    # 3.集合的并集
    print(set1 | set2)
    # 4.集合的交集
    print(set1 & set2)
    # 5.集合的差集
    print(set1 - set2)
    # 6.集合的对称差
    print(set1 ^ set2)
    # 7.判断元素是否在集合中
    print(1 in set1)
    print(1 not in set1)
    # 8.判断子集和超集
    print(set1 <= set2)
    print(set1 >= set2)
    # 9.清空集合
    set1.clear()
    print(set1)
    # 10.集合的长度
    print(len(set2))
    # 11.集合的拷贝
    set3 = set2.copy()
    print(set3)
    # 12.集合的遍历
    for item in set2:
        print(item)


