#! /usr/bin/env python
# -*- coding:utf-8 -*-

import platform
import subprocess
import getopt
import sys

sys_flag = platform.system()

def deal_command(str):
	p = subprocess.Popen(str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():    
		print line

if __name__ == '__main__':
	msg = '''
	Quickscan Usage
	python quickscan.py option
		Windows
		-h  Get help
		-r {User name}  Check rencent open file 
						Such as -r administrator
		--process Check thread
		--pid={1,2,3} Lookup detailed process informations
					  Such as --pid=112,223,32
		--set Lookup system variables
		*nux
		-h Get help
		--add={'File name'} Check feils changed within 24 hours
							--add=*.php
	'''
	if len(sys.argv) < 2:
		print msg
	options, args = getopt.getopt(sys.argv[1:], "r:h",['pid=','process','set','add'])
	for opt, arg in options:
		if opt == '-h':
			print msg
		if sys_flag == "Windows":
			if opt == '-r':
				user_name = arg
				print u'----------Rencent Open File----------'
				if user_name == None:
					deal_command('dir C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Recent /od')
				else:
					deal_command('dir C:\Users\\'+user_name+'\AppData\Roaming\Microsoft\Windows\Recent /od')
				print '--------------------------------------'
			if opt == '--process':
				print u'--------------Process-----------------'
				deal_command('netstat -ano | findstr ESTABLISHED')
				print '---------------------------------------'
			if opt == '--pid':
				pids = arg
				pids = pids.split(',')
				print u'----------Process Detail--------------'
				for i in pids:
					deal_command('tasklist /svc | findstr '+i)
				print '---------------------------------------'
			if opt == '--set':
				print u'----------System variables--------------'
				deal_command('set')
				print '-----------------------------------------'
		if sys_flag == "*nux":
			if opt == '--add':
				file = arg
				print u'-------------File list-----------------'
				deal_command('find ./ -mtime 0 -name "'+file+'"')
				print '-----------------------------------------'