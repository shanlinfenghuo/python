#! /usr/bin/python

import os
import os.path

path1 = "/root/lvmdisk"
path2 = "/usr"
def CheckDir(fdir, path1, path2):
	if os.path.isdir(fdir):
		if os.path.exists(path2 + fdir):
			listdir = os.listdir(path1 + fdir)
			for eachDir in listdir:
				path1 = path1 + fdir
				path2 = path2 + fdir
				CheckDir(eachDir, path1, path2)
		else:
			dirpath1 = path1 + fdir
			dirpath2 = path2 + fdir
			os.system("mv -rf  %s %s" % (dirpath1, dirpath2))

if __name__ == '__main__':
	dirlist = os.listdir("/root/lvmdisk/usr")
	for eachDir in dirlist:
		CheckDir(eachDir, path1, path2)
