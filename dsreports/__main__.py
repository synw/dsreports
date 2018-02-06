import os
import shutil


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def run():
    here = os.path.dirname(os.path.realpath(__file__))
    cwd = os.getcwd()
    if not os.path.exists(here + "/site"):
        os.makedirs(here + "/site")
    print("Copying site template ...")
    copytree(here + "/site", cwd + "/site")
    print("Ok")


if __name__ == '__main__':
    run()
