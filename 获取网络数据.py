# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 21:33:45 2016

@author: Administrator
"""

import urllib
str1='http://tieba.baidu.com/p/100000000'
for i in range(10):
    r=urllib.urlopen(str1+str(i))
    doc=open('100000000'+str(i)+'.html','wb')
    doc.write(r)
    doc.close()