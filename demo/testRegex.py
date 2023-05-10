import re
import time

# pattern1 = "file"
# pattern2 = "files"
# string = "the file is in the folder"
# print("file in string", pattern1 in string)
# print("files in string", pattern2 in string)

# ptn = re.compile(r"\w+?@\w+?\.com")
#
# matched = ptn.search("mofan@mofanpy.com")
# print("mofan@mofanpy.com is a valid email:", matched)
# matched = ptn.search("mofan@mofanpy+com")
# print("mofan@mofanpy+com is a valid email:", matched)

# matched = re.search(r"\w+?@\w+?\.com", "mofan@mofanpy.com")
# print("mofan@mofanpy.com:", matched)
# string1 = "the email is mofan@mofanpy.com."
# matched = re.search(r"\w+?@\w+?\.com", string1)
# print(string1 + ":", matched)
# print(string1[matched.span()[0]], string1[matched.span()[1]])

# match = re.search(r"run\.", "I run to you run. a")
# print(match)
# print(match.group())
# print(re.search(r"ran|run", "I run to you"))
# print(re.search(r"r[au]n", "I run to you"))
# print(re.search(r"f(ou|i)nd", "I find you"))
# print(re.search(r"f(ou|i)nd", "I found you"))


# matched = re.search(r"\w+?@\w+?\.com", "mofan@mofanpy.com")
# print(matched)

# print(re.search(r"^138\d{8}$", "13812345678"))
# print(re.search(r"^138\d{8}$", "138123456780000"))


# print(re.search(r"不?爱", "我爱你"))
# print(re.search(r"不?爱", "我不爱你"))
# print(re.search(r"不.*?爱", "我不是很爱你"))
# print("中".encode("unicode-escape"))
# print(re.search(r"[\u4e00-\u9fa5]+", "我爱莫烦Python。"))
# print(re.search(r"[\u4e00-\u9fa5！？。，￥【】「」]+", "我爱莫烦。莫烦棒！"))


# print("search:", re.search(r"run", "I run to you"))
# print("match:", re.match(r"run", "I run to you"))
# print("findall:", re.findall(r"r[ua]n", "I run to you. you ran to him"))
#
# for i in re.finditer(r"r[ua]n", "I run to you. you ran to him"):
#     print("finditer:", i)
#
# print("split:", re.split(r"r[ua]n", "I run to you. you ran to him"))
# print("sub:", re.sub(r"r[ua]n", "jump", "I run to you. you ran to him"))
# print("subn:", re.subn(r"r[ua]n", "jump", "I run to you. you ran to him"))

# found = []
# for i in re.finditer(r"[\w-]+?\.jpg", "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"):
#     found.append(re.sub(r".jpg", "", i.group()))
# print(found)

# string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"
# print("without ():", re.findall(r"[\w-]+?\.jpg", string))
# print("with ():", re.findall(r"([\w-]+?)\.jpg", string))

# string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"
# match = re.finditer(r"(\d+?)-(\d+?)-(\d+?)\.jpg", string)
# for file in match:
#     print("matched string:", file.group(0), ",year:", file.group(1), ", month:", file.group(2), ", day:", file.group(3))


# string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"
# match = re.findall(r"(\d+?)-(\d+?)-(\d+?)\.jpg", string)
# for file in match:
#     print("year:", file[0], ", month:", file[1], ", day:", file[2])

# string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"
# match = re.finditer(r"(?P<y>\d+?)-(?P<m>\d+?)-(?P<d>\d+?)\.jpg", string)
# for file in match:
#     print("matched string:", file.group(0),
#         ", year:", file.group("y"),
#         ", month:", file.group("m"),
#         ", day:", file.group("d"))

# ptn, string = r"r[ua]n", "I RaN to you"
# print("without re.I:", re.search(ptn, string))
# print("with re.I:", re.search(ptn, string, flags=re.I))

# ptn = r"^ran"
# string = """I
# ran to you"""
# print("without re.M:", re.search(ptn, string))
# print("with re.M:", re.search(ptn, string, flags=re.M))
# print("with re.M and match:", re.match(ptn, string, flags=re.M))

# ptn = r"^ran"
# string = """I
# Ran to you"""
# print("with re.M and re.I:", re.search(ptn, string, flags=re.M | re.I))
#
# string = """I
# Ran to you"""
# print(re.search(r"(?im)^ran", string))

n = 1000000
# 不提前 compile
t0 = time.time()
for _ in range(n):
    re.search(r"ran", "I ran to you")
t1 = time.time()
print("不提前 compile 运行时间：", t1-t0)

# 先做 compile
ptn = re.compile(r"ran")
for _ in range(n):
    ptn.search("I ran to you")
print("提前 compile 运行时间：", time.time()-t1)
