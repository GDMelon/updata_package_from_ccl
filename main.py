from subprocess import call
from . import get_package_list

def main():
    ori = "-i http://pypi.douban.com/simple"
    # lst = ("astroid","certifi","Django","isort","lazy-object-proxy",
    # "numpy","opencv-python","Pillow","pylint","pytz","requests",
    # "setuptools","six","typed-ast","urllib3","wrapt")
    lst = get_package_list.get_list()
    for dist in lst:
        print("Now is Updating {}".format(dist))
        call("pip install --upgrade " + dist + ori, shell=True)

if __name__() == "__main_()" :
    main()