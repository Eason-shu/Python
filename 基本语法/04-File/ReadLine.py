# ---encoding:utf-8---
# @Time    : 2023/9/2 18:06
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    : 读取某一行
# @File    : ReadLine.py

if __name__ == '__main__':
    file= open("../HelloWord.py", "r")
    # 读取文件
    print(file.readline())
    # 关闭
    file.close()
