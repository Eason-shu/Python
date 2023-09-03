# ---encoding:utf-8---
# @Time    : 2023/9/2 13:16
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    :  IF语句
# @File    : IF.py


if __name__ == '__main__':
    age = 25
    if age < 18:
        print("未成年人")
    elif age >= 18 and age < 65:
        print("成年人")
    else:
        print("老年人")
