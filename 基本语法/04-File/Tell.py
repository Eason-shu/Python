# ---encoding:utf-8---
# @Time    : 2023/9/2 18:10
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    :  返回文件的当前位置
# @File    : Tell.py

if __name__ == '__main__':
    file= open("../HelloWord.py", "r")
    # 读取文件
    print(file.tell())
    # 关闭
    file.close()
