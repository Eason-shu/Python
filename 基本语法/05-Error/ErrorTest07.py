# ---encoding:utf-8---
# @Time    : 2023/9/3 10:26
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    : 自定义异常
# @File    : ErrorTest07.py

# 自定义异常
class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

if __name__ == '__main__':

    try:
        raise MyException("自定义异常")
    except MyException as e:
        print(e)
    finally:
        print("程序执行完毕")

