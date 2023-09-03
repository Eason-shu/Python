# ---encoding:utf-8---
# @Time    : 2023/9/3 15:43
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    : Re模块
# @File    : ReModel.py

import re

if __name__ == '__main__':
    # 匹配字符串
    print(re.match("a", "abc"))
    # 匹配字符串
    print(re.search("a", "abc"))
    # 匹配字符串
    print(re.findall("a", "abc"))
    # 匹配字符串
    print(re.sub("a", "A", "abc"))
    # 匹配字符串
    print(re.split("a", "abc"))
    # 匹配字符串
    print(re.split("a", "abc", 1))
    # 正则表达式
    print(re.match("a", "abc", re.I))
