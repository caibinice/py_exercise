def create_name():
    return "new_file.txt"


class File:
    def __init__(self, name, create_time="today"):
        self.name = name
        self.create_time = create_time

    def get_info(self):
        return self.name + " is created at " + self.create_time


class Video(File):  # 继承了 File 的属性和功能
    def __init__(self, name, window_size=(1080, 720)):
        # 将共用属性的设置导入 File 父类
        super().__init__(name=name)
        self.window_size = window_size


class Text(File):  # 继承了 File 的属性和功能
    def __init__(self, name, language="zh-cn"):
        # 将共用属性的设置导入 File 父类
        super().__init__(name=name)
        self.language = language

    # 也可以在子类里复用父类功能
    def get_more_info(self):
        return self.get_info() + ", using language of " + self.language





# v = Video("my_video")
# t = Text("my_text")
# print(v.get_info())  # 调用父类的功能
# print(t.create_time)  # 调用父类的属性
# print(t.language)  # 调用自己的属性
# print(t.get_more_info())  # 调用自己加工父类的功能
