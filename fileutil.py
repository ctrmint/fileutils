#!/usr/bin/env python
# Handy file utils

import os
import gzip
import shutil


class myfile(object):
    def __init__(self, path):
        self.filename = path
        self.type = ""
        self.filesize = os.path.getsize(self.filename)
        self.last_modification_time = os.path.getmtime(self.filename)
        self.last_access_time = os.path.getatime(self.filename)
        self.creation_time = os.path.getctime(self.filename)
        self.script_modified = 0
        self.script_compress = 0
        self.compression_delta = 0

    def printsize(self):
        print "file : " + self.filename + " : has size = " + str(self.filesize)

    def printattribs(self):
        print self.filename
        print self.filesize
        print self.last_modification_time
        print self.last_access_time
        print self.creation_time

    def ransomware_crypto(self):
        print "your files are being encrypted....lolz"      # just kidding

    def compressfile(self, verbosity, syslog):
        print "Syslog setting: " +str(syslog)
        if verbosity == 1:
            print "Compressing file: " + self.filename + " : Size : " + str(self.filesize)
            if self.script_compress == 0:
                with open(self.filename, 'rb') as f_in, gzip.open((str(self.filename)+".gz"), 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
                print "Compression complete"
                self.filename = (str(self.filename)+".gz")
                self.filesize = os.path.getsize(self.filename)
                print "Compressed file: " + self.filename + " : Size : " + str(self.filesize)
            else:
                print "already compressed ???"
        else:
            if self.script_compress == 0:
                with open(self.filename, 'rb') as f_in, gzip.open((str(self.filename)+".gz"), 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
                self.filename = (str(self.filename)+".gz")
                self.filesize = os.path.getsize(self.filename)
            else:
                print "already compressed ???"

        self.script_modified = 1
        self.script_compressed = 1


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
    filestoprocess = getfilesfromdir("/Users/mark/PycharmProjects/fileutils/files", 0)
    for file in filestoprocess:
        files.append(myfile(file))
    files[0].compressfile(1, 0)
    return


if __name__ == '__main__':
    main()