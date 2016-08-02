# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 18:47:10 2016

@author: Administrator
"""

import pandas as pd
singer=['The rolling stones','Beatles',"Guns N' Roses",'Metallica']
song=['Satisfaction','Let It Be',"Don't Cry",'Nothing Else Matters']
res=pd.DataFrame({'Singer':singer,'Song':song})
res.to_csv('singerandsong.csv')

rd=pd.read_csv('singerandsong.csv')
print rd['Singer']