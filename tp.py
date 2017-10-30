#coding=utf-8  
import os
import sys
from xpinyin import Pinyin

def chinesetopinyin(filename):
	filename= unicode(filename,'utf-8')
	rec = p.get_pinyin(filename,'')
	return rec

p = Pinyin()
floder = raw_input("输入文件名: ")
path = '/mnt/c/Users/lzy/Documents/WeChat Files/duduxiaozhu123123/Files/'+floder
for filename in os.listdir(path):
	filenamearr = filename.split('.', 1 )
	newname = chinesetopinyin(filenamearr[0])
	oldpath = path+'/'+filename
	newpath = path+'/'+newname+'.'+filenamearr[1]
	print oldpath
	print newpath
	os.renames(oldpath,newpath)


