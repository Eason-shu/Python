# ---encoding:utf-8---
# @Time    : 2023/9/2 10:15
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    :  3、Python中的列表类型
# @File    : List.py

if __name__ == '__main__':
    arr=[1,2,3,4,5,6,7,8,9,10]
    print('arr',arr)
    # 打印变量的类型
    print(type(arr))
    # 打印变量的内存地址
    print(id(arr))
    # 列表的切片
    print(arr[0:5])
    # 列表的拼接
    print(arr+[11,12,13,14,15])
    # 列表的重复
    print(arr*3)
    # 列表的长度
    print(len(arr))
    # 列表的查找
    print(arr.index(5))
    # 列表的替换
    arr[0]=100
    print(arr)
    # 列表的删除
    del arr[0]
    print(arr)
    # 列表的排序
    arr.sort()
    print(arr)
    # 列表的反转
    arr.reverse()
    print(arr)
    # 列表的追加
    arr.append(100)
    print(arr)
    # 列表的插入
    arr.insert(0,100)
    print(arr)
    # 列表的删除
    arr.remove(100)
    print(arr)
    # 列表的弹出
    print(arr.pop())
    print(arr)
    # 列表的清空
    arr.clear()
    print(arr)
    # 列表的复制
    arr=[1,2,3,4,5,6,7,8,9,10]
    arr1=arr.copy()
    print(arr1)
    # 列表的统计
    print(arr.count(1))
    # 列表的嵌套
    arr2=[1,2,3,4,5,6,7,8,9,10,[11,12,13,14,15]]
    print(arr2)
    # 列表的遍历
    for i in arr2:
        print(i)
    # 列表的推导式
    arr3=[i for i in range(1,11)]
    print(arr3)
    # 列表的推导式
    arr4=[i for i in range(1,11) if i%2==0]
    print(arr4)
    # 列表的推导式
    arr5=[i for i in range(1,11) if i%2==0 if i%3==0]
    print(arr5)