# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:53:47 2016

@author: Administrator
"""
#重新使用之前需要在命令中使用del app
import wx
app=wx.App()
frame=wx.Frame(None,title='Hello World')
frame.Show(True)
app.MainLoop()