import os
bas_path = os.getcwd()
dirname = "lib.txt"
path = os.path.join(bas_path,dirname)
# print(path)

with open(path) as f:
    r = f.readlines()
    for i in range(2,len(r)):
        r_1 = r[i].split(" ")[0]