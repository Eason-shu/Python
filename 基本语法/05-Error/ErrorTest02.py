# ---encoding:utf-8---
# @Time    : 2023/9/3 10:13
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    : 常见异常
# @File    : ErrorTest02.py

if __name__ == '__main__':

    # 算术异常
    print(10/0)
    # 索引异常
    arr=[1,2,3,4,5,6,7,8,9,10]
    print(arr[10])
    # 键异常
    dict={"name":"Darwin","age":18}
    print(dict('hhj'))
    # 类型异常
    print(10+"hello")
    # 值异常
    print(int("hello"))
    # 文件异常
    f=open("hello.txt","r")
    print(f.read())
