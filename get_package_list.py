import os
from . import get_ccl_text


lib_text = "LIBOFPACKAGE.txt"
bas_path = os.getcwd()
doc_lst = os.listdir(bas_path)
# 指向文件
path = os.path.join(bas_path,lib_text)

# 查询升级列表
def get_list():
    lib_lst = []
    if lib_text in doc_lst:
        # 如果目录下存在“lib.txt”文件
        pass
    else:
        # 调用getText方法生成txt
        get_ccl_text.get_info_from_ccl()

# 读取txt文件，提取待升级列表
    with open(path) as f:
        r = f.readlines()
        for i in range(2,len(r)):
            r_1 = r[i].split(" ")[0]
            lib_lst.append(r_1)
    return lib_lst

            