# -*- coding: ascii -*-
"""
Created on Fri Jul 15 21:44:40 2016

@author: Administrator
"""
#del app
import wx
class Frame1(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self, parent=superior,title="Mouse Event",pos=(100,200),\
                          size=(500,500) )
        self.panel=wx.Panel(self)
        self.text1=wx.TextCtrl(self.panel,value="Hello World!", size=(200,100))
        self.panel.Bind(wx.EVT_LEFT_UP,self.Onclick)
    def Onclick(self,event):
        posm=event.GetPosition()
        wx.StaticText(parent=self.panel,label='Hello!',pos=(posm.x,posm.y))
        
if __name__=='__main__':
    app=wx.App()
    frame=Frame1(None)
    frame.Show(True)
    app.MainLoop()