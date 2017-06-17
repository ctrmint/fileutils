#!/usr/bin/env python
# Handy file utils

import os


class myfile(object):
    def __init__(self, path):
        self.filename = path
        self.type = ""
        self.filesize = os.path.getsize(self.filename)
        self.last_modification_time = os.path.getmtime(self.filename)
        self.last_access_time = os.path.getatime(self.filename)
        self.creation_time = os.path.getctime(self.filename)

    def printsize(self):
        print "file : " + self.filename + " : has size = " + str(self.filesize)

    def printattribs(self):
        print self.filename
        print self.filesize
        print self.last_modification_time
        print self.last_access_time
        print self.creation_time

def getfilesfromdir(directory, depth):
    # directory - the starting directory to be scanned for files
    # depth is the level to dig, 0 is cwd, 1 is first subdirectory
    file_paths = []
    i = 0
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
        if i >= depth:
            break
    return (file_paths)


def main():
    files = []
    filestoprocess = getfilesfromdir(".", 0)
    for file in filestoprocess:
        files.append(myfile(file))
    files[0].printattribs()
    return


if __name__ == '__main__':
    main()