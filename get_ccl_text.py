import os

path = "LIBOFPACKAGE.txt"

def get_info_from_ccl():
    with open (path,"w+") as f:
        f.write(_str())


def _str():
    info_of_ccl = os.popen("pip list --outdated").read()
    return info_of_ccl