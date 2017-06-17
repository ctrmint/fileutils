#!/usr/bin/env python
# Handy file utils

import os


class myfile(object):
    def __init__(self):
        self.name = filename
        self.size = 0
        self.type = ""

    def getsize(self):
        print "get size"


def getfilesfromdir(directory, depth):
    # directory - the starting directory to be scanned for files
    # depth is the level to dig, 0 is cwd, 1 is first subdirectory
    file_paths = []
    i = 0
    depth
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
        i += 1
        if i > depth:
            break
    return (file_paths)


def main():
    getfilesfromdir("/Users/mark/PycharmProjects/fileutils", 0)
    return


if __name__ == '__main__':
    main()