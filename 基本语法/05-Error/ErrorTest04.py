# ---encoding:utf-8---
# @Time    : 2023/9/3 10:19
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    :  异常处理: try/except...else
# @File    : ErrorTest04.py

if __name__ == '__main__':
    try:
        print(10/1)
    except Exception as e:
        print(e)
    else:
        print("程序执行完毕")