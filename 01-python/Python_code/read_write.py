"""
文件操作3大步
1.打开
2.读或写
3.关闭
"""
# 传入文件名和标示符 标识符'r'表示读
# print(f.read() ) # 输出调用read()方法，一次读取文件的全部内容
# f.close() # 调用close()方法关闭文件

# 不推荐这么写
# f = open(r'01-python\Python_code\hello python.txt', 'w',encoding="utf-8") 
# # 传入标识符'w'或者'wb'表示写文本文件或写二进制文件
# f.write('Hello, world!') # 写入文件
# f.close() # 调用close()方法关闭文件

# with open(r'01-python\Python_code\hello python.txt', 'w',encoding="utf-8") as f: 
#     # 以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）
#     # 如果要追加到文件末尾，可以传入'a'以追加（append）模式写入
#     f.write('Hello, world!')


