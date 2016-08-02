# -*- coding: utf-8 -*-
"""
Created on Fri Jul 08 23:57:22 2016

@author: Administrator
"""

def countchar(str):
    str=str.lower();
    countlist=[0]*26 ;   
    for ch in str:
        if ch>='a' and ch<='z':
            countlist[ord(ch)-97]+=1;
    print countlist;


input_str=raw_input();
countchar(input_str);