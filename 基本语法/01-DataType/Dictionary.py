# ---encoding:utf-8---
# @Time    : 2023/9/2 10:24
# @Author  : Darwin_Bossen
# @Email   ：3139066125@qq.com
# @Site    :  5、Python中的字典类型
# @File    : Dictionary.py

if __name__ == '__main__':
    dict={'name':'Darwin','age':18,'salary':100.0,'flag':True}
    print('dict',dict)
    # 打印变量的类型
    print(type(dict))
    # 打印变量的内存地址
    print(id(dict))
    # 字典的长度
    print(len(dict))
    # 字典的查找
    print(dict['name'])
    # 字典的修改
    dict['name']='Bossen'
    print(dict)
    # 字典的删除
    del dict['name']
    print(dict)
    # 字典的清空
    dict.clear()
    print(dict)
    # 字典的复制
    dict={'name':'Darwin','age':18,'salary':100.0,'flag':True}
    dict1=dict.copy()
    print(dict1)
    # 字典的遍历
    for key in dict:
        print(key,dict[key])
    # 字典的嵌套
    dict2={'name':'Darwin','age':18,'salary':100.0,'flag':True,'dict':{'name':'Bossen','age':18,'salary':100.0,'flag':True}}
    print(dict2)
    # 字典的键值对
    print(dict2.items())
    # 字典的键
    print(dict2.keys())
    # 字典的值
    print(dict2.values())
    # 字典的更新
    dict2.update({'name':'Bossen','age':18,'salary':100.0,'flag':True})
    print(dict2)
    # 字典的弹出
    print(dict2.pop('name'))
    print(dict2)
    # 字典的弹出随机键值对
    print(dict2.popitem())
    print(dict2)
    # 字典的fromkeys
    dict3=dict.fromkeys(['name','age','salary','flag'])
    print(dict3)
    # 字典的get
    print(dict2.get('name'))
    # 字典的setdefault
    print(dict2.setdefault('name','Darwin'))
    print(dict2)
    # 遍历字典的键值对
    for key,value in dict2.items():
        print(key,value)
    # 遍历字典的键
    for key in dict2.keys():
        print(key)
    # 遍历字典的值
    for value in dict2.values():
        print(value)
