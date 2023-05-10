import json

# data = {"filename": "f1.txt", "create_time": "today", "size": 111}
# j = json.dumps(data)
# print(j)
# print(type(j))

data = {"filename": "f1.txt", "create_time": "today", "size": 111}
with open("data.json", "w") as f:
    json.dump(data, f)

print("直接当纯文本读：")
with open("data.json", "r") as f:
    print(f.read())

print("用 json 加载了读：")
with open("data.json", "r") as f:
    new_data = json.load(f)
print("字典读取：", new_data["filename"])


