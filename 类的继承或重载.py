# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 20:38:02 2016

@author: Administrator
"""

class Fulei():
    "class of father"
    counter=0
    def __init__(self,name):
        self.name=name
        Fulei.counter+=1
        
    def greet(self):
        print 'Hi! My name is %s' %(self.name)
        print Fulei.counter
        
class Zilei(Fulei):
    'class of son'
    def greet(self):
        print 'Woof! My name is %s, my number is %d' %(self.name,self.counter)
        
if __name__=='__main__':
    lei=Zilei('Go')
    lei.greet()