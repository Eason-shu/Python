# ---encoding:utf-8---
# @Time    : 2023/9/2 10:10
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    :  2、Python中的字符串类型
# @File    : String.py

if __name__ == '__main__':

    str='Hello World'
    print('str',str)
    # 打印变量的类型
    print(type(str))
    # 打印变量的内存地址
    print(id(str))
    # 字符串的切片
    print(str[0:5])
    # 字符串的拼接
    print(str+'你好')
    # 字符串的重复
    print(str*3)
    # 字符串的长度
    print(len(str))
    # 字符串的查找
    print(str.find('llo'))
    # 字符串的替换
    print(str.replace('llo','Darwin'))
    # 字符串的大小写转换
    print(str.upper())
    print(str.lower())
    # 字符串的首字母大写
    print(str.capitalize())
    # 字符串的每个单词首字母大写
    print(str.title())
    # 字符串的判断
    print(str.isalpha())
    print(str.isdigit())
    print(str.isalnum())
    # 字符串的分割
    print(str.split(' '))
    # 字符串的去空格
    print(str.strip())
    # 字符串的格式化
    print('我叫%s,今年%d岁'%('Darwin',18))
    print('我叫{0},今年{1}岁'.format('Darwin',18))
    print('我叫{name},今年{age}岁'.format(name='Darwin',age=18))
    print(f'我叫{"Darwin"},今年{18}岁')
    # 字符串的转义
    print('Hello\nWorld')
    print('Hello\tWorld')
    print('Hello\\World')
    print('Hello\'World')
    print('Hello\"World')
    print('Hello\rWorld')
    print('Hello\bWorld')
    print('Hello\fWorld')
    print('Hello\oooWorld')
    # 字符串的原始字符串
    print(r'Hello\nWorld')
    # 字符串的索引
    print(str[0])

