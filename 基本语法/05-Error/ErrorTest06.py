# ---encoding:utf-8---
# @Time    : 2023/9/3 10:24
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    : raise 异常
# @File    : ErrorTest06.py

if __name__ == '__main__':
    try:
        print(10/0)
    except Exception as e:
        raise e
    finally:
        print("程序执行完毕")
