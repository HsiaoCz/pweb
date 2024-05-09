# 打开文件
file = open("./2344.txt", "r")

# 读取文件
# readlines() 一行一行
print(file.readlines())

# 记得关闭文件
file.close()

# 以只写模式打开文件
file1 = open("./2345.txt", "w")
file1.write("hello world")
file1.close()

# encoding=utf-8
# 将这个写在第一行可以告诉解释器，该文件的编码格式是UTF-8
# 避免中文乱码
# 编码格式
# python解释器使用的是Uincode(内存)
# python .py文件在磁盘上使用的是UTF_8存储
print("Hello 中国")
