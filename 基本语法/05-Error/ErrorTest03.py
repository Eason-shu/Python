# ---encoding:utf-8---
# @Time    : 2023/9/3 10:17
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    : 异常处理
# @File    : ErrorTest03.py

if __name__ == '__main__':
    try:
        print(10/0)
    except Exception as e:
        print(e)
    finally:
        print("程序执行完毕")