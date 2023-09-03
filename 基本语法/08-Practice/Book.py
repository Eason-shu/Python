# ---encoding:utf-8---
# @Time    : 2023/9/3 19:30
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    :  书籍类
# @File    : Book.py

class Book:

    # 书籍类
    def __init__(self, name, author, price, publish, date, score, comment, url):
        self.name = name
        self.author = author
        self.price = price
        self.publish = publish
        self.date = date
        self.score = score
        self.comment = comment
        self.url = url

    # 重写str方法
    def __str__(self):
        return "书名：" + self.name + "\n作者：" + self.author + "\n价格：" + self.price + "\n出版社：" + self.publish + "\n出版日期：" + self.date + "\n评分：" + self.score + "\n评论数：" + self.comment + "\n链接：" + self.url