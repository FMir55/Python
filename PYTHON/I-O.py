#!/usr/bin/python2.7
# coding:utf-8
'''
Created on 2015/4/5

@author: fmir33
'''
import sys
from time import time

file_in = file('in.txt','r')
file_out= file('out.txt','w')

for line in file_in:
    for i in range(0,len(line)):
        if line[i]!="\n":
            sys.stdout.write(line[i]+',')
        else:
            sys.stdout.write(line[i])
        file_out.write(line[i])

sys.stdout.write("中原標準時間"+str(time()))
file_in.close()
file_out.close()