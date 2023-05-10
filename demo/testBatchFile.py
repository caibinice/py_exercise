import os
import re

old_dir = "user/mofan"
new_dir = "user/mofanpy"

for filename in os.listdir(old_dir):
    file_path = os.path.join(old_dir, filename)
    os.makedirs(new_dir, exist_ok=True)
    with open(file_path, "r") as f1:
        string = f1.read()
        new_string = re.sub(r"morvanzhou.github.io", "mofanpy.com", string)
        with open(os.path.join(new_dir, "new_"+filename), "w") as f2:
            f2.write(new_string)


for filename in os.listdir(old_dir):
    if filename.startswith("new_"):
        continue
    file_path = os.path.join(new_dir, "new_"+filename)
    with open(file_path, "r") as f:
        print(file_path, ": ", f.read())
