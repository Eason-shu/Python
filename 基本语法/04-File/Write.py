# ---encoding:utf-8---
# @Time    : 2023/9/2 18:04
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    : 写入文件
# @File    : Write.py

if __name__ == '__main__':
    # 打开一个文件
    f = open("foo.txt", "w")
    num = f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
    print(num)
    # 关闭打开的文件
    f.close()