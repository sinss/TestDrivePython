## -*- coding: utf-8 -*-

'''
Created on Sep 24, 2015

@author: Leo
'''

import a.leo as L
import a.check as CH
import wx

if __name__ == '__main__':
    app = wx.App(redirect=True)   # Error messages go to popup window
    #top = L.Frame("<<project>>")
    top = L.TaskBarFrame(None)
    top.Show(False)
    app.MainLoop()
#     x = "員工編號"
#     CH.send_request(x.decode('utf-8').encode('big5'))