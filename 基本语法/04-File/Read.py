# ---encoding:utf-8---
# @Time    : 2023/9/2 17:58
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    : 打开文件
# @File    : Read.py

if __name__ == '__main__':
   file= open("../HelloWord.py", "r")
   # 读取文件
   print(file.read())
   # 关闭
   file.close()
