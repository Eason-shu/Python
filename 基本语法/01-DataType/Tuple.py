# ---encoding:utf-8---
# @Time    : 2023/9/2 10:21
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    : 4、Python中的元组类型
# @File    : Tuple.py

if __name__ == '__main__':
    tup=(1,2,3,4,5,6,7,8,9,10)
    print('tup',tup)
    # 打印变量的类型
    print(type(tup))
    # 打印变量的内存地址
    print(id(tup))
    # 元组的切片
    print(tup[0:5])
    # 元组的拼接
    print(tup+(11,12,13,14,15))
    # 元组的重复
    print(tup*3)
    # 元组的长度
    print(len(tup))
    # 元组的查找
    print(tup.index(5))
    # 元组的统计
    print(tup.count(1))
    # 元组的嵌套
    tup1=(1,2,3,4,5,6,7,8,9,10,(11,12,13,14,15))
    print(tup1)
    # 元组的转换
    arr=[1,2,3,4,5,6,7,8,9,10]
    tup2=tuple(arr)
    print(tup2)
    # 元组的解包
    a,b,c,d,e,f,g,h,i,j=tup2
    print(a,b,c,d,e,f,g,h,i,j)
    #元组的遍历
    for i in tup2:
        print(i)
    # 元组的比较
    tup3=(1,2,3,4,5,6,7,8,9,10)
    tup4=(1,2,3,4,5,6,7,8,9,10)
    print(tup3==tup4)
    print(tup3>tup4)
    print(tup3<tup4)


