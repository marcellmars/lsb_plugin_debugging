# -*- coding: utf-8 -*-

import os
import sys
import subprocess

def make_library_json(path):
    with open("{}static/data.js".format(path)) as r:
        js = r.read()[10:-1]
        with open("{}static/library.json".format(path), "wb") as w:
            ljson = w.write(js)
    print("{}/static/library.json was made.".format(path))

def rsync(path, rpath):
    r = subprocess.Popen('rsync -avhtuW --progress "{0}" "{1}"'.format(path, rpath),
                         stdout=subprocess.PIPE, shell=True)
    while r.poll() is None:
        print(r.stdout.readline())
    print(r.stdout.read())
    print("rsync finished...")

if __name__ == '__main__':
    if len(sys.argv) > 2:
        path = sys.argv[1]
        rpath = sys.argv[2]
        if os.path.exists("{}static/data.js".format(path)):
            make_library_json(path)
            rsync(path, rpath)
            sys.exit(0)
    else:
        print("Usage: {} local_path remote_path".format(sys.argv[0]))
