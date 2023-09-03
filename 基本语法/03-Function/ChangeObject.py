# ---encoding:utf-8---
# @Time    : 2023/9/2 15:17
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    : 函数参数可变对象
# @File    : ChangeObject.py

# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4])
   print ("函数内取值: ", mylist)
   return

if __name__ == '__main__':
    # 调用changeme函数
    mylist = [10,20,30]
    changeme( mylist )
    print ("函数外取值: ", mylist)