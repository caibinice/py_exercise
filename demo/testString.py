# name = "莫烦Python"
# print("我的名字是" + name + "！")
# print("我的名字是%s!" % name)

# name = "莫烦Python"
# age = 18
# gender = "男"
# print("我的名字是" + name + "！我" + str(age) + "岁了，我是" + gender + "的~")
# print("我的名字是 %s !我 %d 岁了，我是 %s 的~" % (name, age, gender))

# name = "莫烦Python"
# age = 18
# gender = "男"
# print("我的名字是 %(nm)s !我 %(age)d 岁了，我是 %(gd)s 的~" % {"nm": name, "age": age, "gd": gender})

# name = "莫烦Python"
# age = 18
# height = 1.8
# print("我的名字是 %s !我 %d 岁了，我 %f 米高~" % (name, age, height))


# print("%f" % (1/3))     # 后面不限制
# print("%.2f" % (1/3))   # 后面限制 2 个位置
# print("%4d" % (1/3))    # 前面补全最大 4 个位置
# print("%5d" % 12)       # 前面补全最大 5 个位置


# name = "莫烦Python"
# age = 18
# height = 1.8
# print("我的名字是 %s !我 %d 岁了，我 %f 米高~" % (name, age, height))
# print("我的名字是 {} !我 {} 岁了，我 {} 米高~".format(name, age, height))


# name = "莫烦Python"
# age = 18
# height = 1.8
# print("我的名字是 {0} !我 {1} 岁了，我 {2} 米高~我是{0}".format(name, age, height))


# name = "莫烦Python"
# age = 18
# height = 1.8
# print("我的名字是 {nm} !我 {age} 岁了，我 {ht} 米高~我是{nm}".format(nm=name, age=age, ht=height))


# print("我 {:.3f} 米高".format(1.12345))
# print("我 {ht:.1f} 米高".format(ht=1.12345))
# print("我 {:3d} 米高".format(1))
# print("我 {:3d} 米高".format(21))


# txt = "You scored {:%}"
# print(txt.format(2.1234))

# txt = "You scored {:.2%}"
# print(txt.format(2.1234))


# name = "莫烦Python"
# age = 18
# height = 1.8
# print(f"我的名字是 {name} !我 {age} 岁了，我 {height} 米高~")
# print(f"我 {age} 岁了，明年我就{age + 1}岁了~")
#
#
# score = 2.1234
# print(f"You scored {score:.2%}")
# print(f"You scored {score:.3f}")
# print(f"You scored {12:5d}")

# 去除前后空格
print("  我不想要前后的空白，但是  中间\n的可以有\n  ".strip())

print("帮我替换掉莫烦".replace("莫烦", "沫凡"))

# 文字大小写处理
print("How ABOUT lower CaSe?".lower())
print("And upper CaSe?".upper())
print("do tiTle For me".title())

print("你|帮|我|拆分|一下|这句话".split("|"))
print("|".join(["你", "帮", "我", "重组", "一下", "这句话"]))

print("我在街头看到你".startswith("我在"))
print("我在街头看到你".startswith("街头"))
print("我在巷尾看到你".endswith("看到你"))
print("我在巷尾看到你".endswith("巷尾"))
print("我在巷尾看到你".index("巷尾"))
