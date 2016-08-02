# -*- coding: utf-8 -*-
"""
Created on Sat Jul 09 21:13:16 2016

@author: Administrator
"""
def newusers():
    global system;
    while True:
        name=raw_input('enter a name: ')
        if not(name in system.keys()):
            break;
        else:
            print 'Existed! Please try another'
    system[name]=raw_input('set the password: ')
 
def oldusers():
   # global system;
    #Enter the  username and password
    username=raw_input('Enter the  username: ');
    password=raw_input('Enter the  password: ');
    if username in system.keys() and password == system[username]: #不能用is 判断 
        print username, 'welcome back '  
    else:  
        print 'login incorrect'  

def login():
    while True:    
        option = """
            (N) for New User Login 
            (O) for Old User Login
            (E) To Exit
            """
        print option
        opt=raw_input('Enter the option: ')
        if opt=='N':
            newusers()
        elif opt=='O':
            oldusers()
        else:
            return
        
system={};
if __name__ == '__main__':  
     login()