# ---encoding:utf-8---
# @Time    : 2023/9/3 14:34
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    : Os模块
# @File    : OsModel.py
import os

if __name__ == '__main__':
    # 获取当前目录
    print(os.getcwd())
    # 获取当前目录的父目录
    print(os.path.dirname(os.getcwd()))
    # 遍历当前目录下的所有文件
    print(os.listdir(os.getcwd()))
    # 创建目录
    os.mkdir("test")
    # 删除目录
    os.rmdir("test")
    # 重命名
    os.rename("test", "test1")
    # 删除文件
    os.remove("test1")
    # 判断文件是否存在
    print(os.path.exists("test1"))

