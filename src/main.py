## -*- coding: utf-8 -*-

'''
Created on Sep 24, 2015

@author: Leo
'''

import a.leo as L
import a.check as CH
import wx
import datetime

if __name__ == '__main__':
<<<<<<< HEAD
#     app = wx.App(redirect=True)   # Error messages go to popup window
#     top = L.Frame("<<project>>")
#     top = L.TaskBarFrame(None)
#     top.Show(True)
#     app.MainLoop()

    app = wx.App(False)
    frame = L.Frame("Thief")
    frame.Show()
    app.MainLoop()
    
#      year = datetime.date.today().year
#      mon = datetime.date.today().month
#      day = datetime.date.today().day
#      print("{:0>4d}".format(year))
#      print("{:0>2d}".format(mon))
#      print("{:0>2d}".format(day))
#      print("{:0>2d}{:0>2d}{:0>4d}".format(mon, day, year))
#      dateStr = "{:0>2d}{:0>2d}{:0>4d}".format(mon, day, year)
#      CH.send_request("0540", dateStr)
=======
    app = wx.App(redirect=True)   # Error messages go to popup window
    #top = L.Frame("<<project>>")
    top = L.TaskBarFrame(None)
    top.Show(False)
    app.MainLoop()
#     x = "員工編號"
#     CH.send_request(x.decode('utf-8').encode('big5'))
>>>>>>> origin/master
