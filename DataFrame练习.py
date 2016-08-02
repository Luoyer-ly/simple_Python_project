# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 20:58:49 2016

@author: Administrator
"""


import pandas as pd
'''
number=['1001','1002','1003']
name=['xiaoming','xiaohong','xiaohua']
Python=['77','88','99']
Math=['87','82','91']
data=zip(number,name,Python,Math)
#dic=cl.OrderedDict('number':number,'name':name,'Python':Python,'Math':Math)
result=pd.DataFrame(data,columns=['number','name','Python','Math']) 
#解决字典索引顺序问题
result.to_excel('scores.xls')
'''
res=pd.read_excel('score.xls')#从文件中读入的数据若是数字就为int！！！
sum_score=[]
for i in range(0,len(res.index)):
    score=int(res.Python[i])+int(res.Math[i])
    sum_score.append(score)
res['Sum_score']=sum_score
res.to_excel('score1.xls')
