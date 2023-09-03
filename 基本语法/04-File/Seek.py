# ---encoding:utf-8---
# @Time    : 2023/9/2 18:12
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    :  移动文件的读取指针到指定位置
# @File    : Seek.py

if __name__ == '__main__':
    file= open("../HelloWord.py", "r")
    # 读取文件
    print(file.seek(3))
    # 关闭
    file.close()


