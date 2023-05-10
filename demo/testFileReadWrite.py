from demo.test import create_name
# print(create_name())


# f = open("new_file.txt", "w")   # 创建并打开
# f.write("some text...")         # 在文件里写东西
# f.close()                       # 关闭

# with open("new_file2.txt", "w") as f:
#     f.writelines(["some text for file2...\n", "2nd line\n"])

# f = open("new_file2.txt", "r")
# print(f.read())
# f.close()

# with open("new_file2.txt", "r") as f:
#     print(f.readlines())

# with open("new_file2.txt", "r") as f:
#     while True:
#         line = f.readline()
#         print(line)
#         if not line:
#             break

# with open("chinese.txt", "wb") as f:
#     f.write("这是中文的，this is Chinese".encode("gbk"))

# with open("chinese.txt", "r") as f:
#     print(f.read())

# with open("chinese.txt", "r", encoding="gbk") as f:
#     print(f.read())
#     #print(f.read().decode('gbk'))  # windows在本机尝试，可以试试这个


# with open("new_file.txt", "r") as f:
#     print(f.read())
# with open("new_file.txt", "r+") as f:
#     f.write("text has been replaced")
#     f.seek(0)       # 将开始读的位置从写入的最后位置调到开头
#     print(f.read())
#

with open("new_file.txt", "a+") as f:
    print(f.read())
    f.write("\nadd new line")
    f.seek(0)       # 将开始读的位置从写入的最后位置调到开头
    print(f.read())


