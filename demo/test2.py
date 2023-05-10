class File:
    def __init__(self):
        self.name = "f1"
        self.__deleted = False  # 我不让别人用这个变量
        self._type = "txt"  # 我不想别人使用这个变量

    def delete(self):
        self.__force_delete()

    def __force_delete(self):  # 我不让别人使用这个功能
        self.__deleted = True
        return True

    def _soft_delete(self):  # 我不想让别人使用这个功能
        self.__force_delete()  # 我自己可以在内部随便调用
        return True

    @property
    def type(self):
        return self._type


f = File()
print(f.type)  # 可以拿到值，但是这个类的作者不想让你直接这样拿到
print(f._soft_delete())  # 可以调用，但是这个类的作者不想让你直接调用

# 接下来的两个实验都会报错
# f.__deleted
# f.__force_delete()
