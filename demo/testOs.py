import os
import shutil


# print("当前目录：", os.getcwd())
# print("当前目录里有什么：", os.listdir())
#
#
# os.makedirs("project", exist_ok=True)
# print(os.path.exists("project"))

# if os.path.exists("user/mofan"):
#     print("user exist")
# else:
#     os.makedirs("user/mofan")
#     print("user created")
# print(os.listdir("user"))

# if os.path.exists("user/mofan"):
#     os.removedirs("user/mofan")
#     print("user removed")
# else:
#     print("user not exist")

# os.makedirs("user/mofan", exist_ok=True)
# with open("user/mofan/a.txt", "w") as f:
#     f.write("nothing")
# os.removedirs("user/mofan")  # 这里会报错

# shutil.rmtree("user/mofan")
# print(os.listdir("user"))

# os.makedirs("user/mofan", exist_ok=True)
# os.rename("user/mofan", "user/mofanpy")
# print(os.listdir("user"))

# shutil.rmtree("user/mofanpy")

# os.makedirs("user/mofan", exist_ok=True)
# with open("user/mofan/a.txt", "w") as f:
#     f.write("nothing")
# print(os.path.isfile("user/mofan/a.txt"))  # True
# print(os.path.exists("user/mofan/a.txt"))  # True
# print(os.path.isdir("user/mofan/a.txt"))  # False
# print(os.path.isdir("user/mofan"))  # True

# def copy(path):
#     filename = os.path.basename(path)   # 文件名
#     dir_name = os.path.dirname(path)    # 文件夹名
#     new_filename = "new_" + filename    # 新文件名
#     new_path = os.path.join(dir_name, new_filename) # 目录重组
#     shutil.copy2(path, new_path)   # 复制文件
#     return os.path.isfile(new_path), new_path
#
# copied, new_path = copy("user/mofan/a.txt")
# if copied:
#     print("copied to:", new_path)
# else:
#     print("copy failed")


def copy(path):
    dir_name, filename = os.path.split(path)
    print("dir_name:" + dir_name + ",fileName:" + filename)
    new_filename = "new2_" + filename  # 新文件名
    new_path = os.path.join(dir_name, new_filename)  # 目录重组
    shutil.copy2(path, new_path)  # 复制文件
    return os.path.isfile(new_path), new_path


copied, new_paths = copy("user/mofan/a.txt")
if copied:
    print("copied to:", new_paths)
else:
    print("copy failed")
