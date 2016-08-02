# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
flag=raw_input("Start the game? y/n\n");
ans=random.randint(1,10) #随机数
while(flag=='y'):
    number=input("please input a number between 1~10\n");
    if(number==ans):
        print "Right!\n"
        break
    elif(number<ans):
        print "Too small!\n"
    else:
        print "Too big!\n"
    flag=raw_input("Play again? y/n\n");
else:
    print "Goodbye\n"
        