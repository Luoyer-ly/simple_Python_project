# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 14:14:32 2016

@author: Administrator
"""

str='My moral standing is: 0.98765'
find_index=str.find(':' ,0 ,len(str))
num=float(str[find_index+1::])
print num