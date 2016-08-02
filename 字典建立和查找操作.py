# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 20:20:49 2016

@author: Administrator
"""

n_list=['xiaoyun','xiaohong','xiaoteng','xiaoyi','xiaoyang']
qq_list=['88888','5555555','11111','1234321','1212121']
dalao_dict=dict(zip(n_list,qq_list))
while True:
    name = raw_input("Please input the name: ")
    if name in dalao_dict.keys():
        print  "%s's QQ number: %s" %(name,dalao_dict[name])
        break
    else:
        print "%s is not in the dict, please try again. " %(name)
print "Who has the nice QQ number?"
for names in dalao_dict.keys():
    if len(dalao_dict[names])<=5:
        print names
