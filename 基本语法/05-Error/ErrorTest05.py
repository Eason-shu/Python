# ---encoding:utf-8---
# @Time    : 2023/9/3 10:21
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    : try-finally
# @File    : ErrorTest05.py

if __name__ == '__main__':
    # 读取文件
    try:
        f = open("hello.txt", "r")
        print(f.read())
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()
        print("程序执行完毕")
