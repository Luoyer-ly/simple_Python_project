# -*- coding: utf-8 -*-
"""
Created on Mon Jun 06 13:56:50 2016

@author: Administrator
"""
def divby37(k):
    return (k%37==0)


flag=True
for i in range(100,1000):
    if i%37==0:
        x=i/100
        y=i/10-x*100
        z=i-x*100-y*10
        try1=x+y*100+z*10
        try2=x*10+z*100+y
        if divby37(try1) and divby37(try2): #python没有&&和||，只有and和or
            print i,    #不换行输出方法
            continue
        else:
            flag=False           
            break
if flag:
    print "\nThe proposition is true"
else:
    print "\nThe proposition is false"
  