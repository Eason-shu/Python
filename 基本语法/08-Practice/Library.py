# ---encoding:utf-8---
# @Time    : 2023/9/3 19:32
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    : 图书类
# @File    : Library.py

from Book import Book

# 图书馆类
class Library:

    def __init__(self):
        self.book_list = []


    def __str__(self):
        return str(len(self.book_list)) + "本书"

    # 显示所有书籍
    def showBook(self):
        for book in self.book_list:
            print(book)
            print("--------------------------------------------------")
    # 添加书籍
    def addBook(self, book):
        self.book_list.append(book)

    # 删除书籍
    def delBook(self, book):
        if book in self.book_list:
            self.book_list.remove(book)
            print("删除成功")
        else:
            print("删除失败")
    # 查找书籍
    def findBook(self, name):
        for book in self.book_list:
            if book.name == name:
                print(book)
                return book
        print("查无此书")
        return None
    # 修改书籍
    def modifyBook(self, book):
        if book in self.book_list:
            self.book_list.remove(book)
            self.book_list.append(book)
            print("修改成功")
        else:
            print("修改失败")

    # 保存书籍
    def saveBook(self):
        with open("book.txt", "w", encoding="utf-8") as f:
            for book in self.book_list:
                f.write(book.name + "," + book.author + "," + book.price + "," + book.publish + "," + book.date + "," + book.score + "," + book.comment + "," + book.url + "\n")
        print("保存成功")

    # 加载书籍
    def loadBook(self):
        with open("book.txt", "r", encoding="utf-8") as f:
            while True:
                line = f.readline()
                if line == "":
                    break
                book = line.split(",")
                self.book_list.append(book)
        print("加载成功")

    # 排序
    def sortBook(self):
        self.book_list.sort(key=lambda book:book.score, reverse=True)
        print("排序成功")

if __name__ == '__main__':
        library = Library()
        while True:
            print("1.添加书籍")
            print("2.删除书籍")
            print("3.查找书籍")
            print("4.修改书籍")
            print("5.显示所有书籍")
            print("6.保存书籍")
            print("7.加载书籍")
            print("8.排序")
            print("0.退出")
            num = input("请输入操作序号：")
            if num == "1":
                name = input("请输入书名：")
                author = input("请输入作者：")
                price = input("请输入价格：")
                publish = input("请输入出版社：")
                date = input("请输入出版日期：")
                score = input("请输入评分：")
                comment = input("请输入评论数：")
                url = input("请输入链接：")

                book = Book(name, author, price, publish, date, score, comment, url)
                library.addBook(book)
            elif num == "2":
                name = input("请输入书名：")
                book = library.findBook(name)
                library.delBook(book)
            elif num == "3":
                name = input("请输入书名：")
                library.findBook(name)
            elif num == "4":
                name = input("请输入书名：")
                book = library.findBook(name)
                if book != None:
                    author = input("请输入作者：")
                    price = input("请输入价格：")
                    publish = input("请输入出版社：")
                    date = input("请输入出版日期：")
                    score = input("请输入评分：")
                    comment = input("请输入评论数：")
                    url = input("请输入链接：")
                    book = Book(name, author, price, publish, date, score, comment, url)
                    library.modifyBook(book)
            elif num == "5":
                library.showBook()
            elif num == "6":
                library.saveBook()
            elif num == "7":
                library.loadBook()
            elif num == "8":
                library.sortBook()
            elif num == "0":
                break


