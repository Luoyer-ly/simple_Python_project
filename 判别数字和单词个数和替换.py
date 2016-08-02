# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 14:32:12 2016

@author: Administrator
"""
def word_len(a):#有数字的就不是单词了
    for ch in a: 
        if ch.isdigit():
            return False;
    return True;
str='I like Python very much 2333 because Python is very cute 666.'
num_count=0;
total_count=0;
word_count=0;
div_list=str.split(' ',len(str));
for ch in str[0:]:
    if ch.isdigit():
        num_count+=1;
    if ch.isalnum():
        total_count+=1;
print '数字的个数是%d，所有字符的个数是%d'%(num_count,total_count)
for wrd in div_list:
    if not wrd.isdigit():
        if word_len(wrd): 
            word_count+=1;
print '单词的个数是%d' %(word_count)
name=raw_input("Input someone's name: ");
name_index=str.find('Python');
print str[0:name_index]+name+str[name_index+6:]
    