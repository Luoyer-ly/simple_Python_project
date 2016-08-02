# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 10:47:34 2016

@author: Administrator
"""

f=open('Blowing the wind.txt','w');
lst=['apple\n','pear\n','peach\n'];
lst.insert(0,'222\n');
lst.insert(1,'author\n');
f.writelines(lst);
f.close();