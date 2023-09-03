# ---encoding:utf-8---
# @Time    : 2023/9/2 18:32
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    : 
# @File    : Os.py
import os


if __name__ == '__main__':
    # 指定目录名称
    new_directory = "D:\\test"

    # 创建新目录
    os.mkdir(new_directory)

    # 获取当前工作目录
    current_directory = os.getcwd()

    # 在新目录下创建文件
    file1_path = os.path.join(new_directory, "file1.txt")
    file2_path = os.path.join(new_directory, "file2.txt")

    with open(file1_path, "w") as file1:
        file1.write("This is file 1.")

    with open(file2_path, "w") as file2:
        file2.write("This is file 2.")

    # 列出新目录中的文件
    files_in_directory = os.listdir(new_directory)

    # 打印新目录中的文件列表
    print(f"Files in {new_directory}:")
    for filename in files_in_directory:
        print(filename)

    # 获取新目录的绝对路径
    new_directory_path = os.path.abspath(new_directory)
    print(f"Absolute path of {new_directory}: {new_directory_path}")

    # 删除新目录及其内容
    os.rmdir(new_directory)

    # 检查新目录是否存在
    if not os.path.exists(new_directory):
        print(f"{new_directory} has been deleted.")
    else:
        print(f"{new_directory} still exists.")
