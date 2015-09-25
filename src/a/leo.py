'''
Created on Sep 24, 2015

@author: Leo
'''
import xml.etree.ElementTree as ET
import wx.html
import sys

ID_SETTING = wx.NewId();
ID_EXIT = wx.NewId();

def parseXml ():
    tree = ET.parse("../res/NewFile.xml")
    root = tree.getroot()
    for child in root:
        print child.tag, child.attrib
    print root[0][0].text
    print root[0][1].text
    print root[0][3].text
    print root[0][4].text
    
aboutText = """<p>Sorry, there is no information about this program. It is running on version %(wxpy)s of 
<b>wxPython</b> and %(python)s of <b>Python</b>. See <a href="http://wiki.wxpython.org">wxPython Wiki</a></p>""" 
  
class HtmlWindow(wx.html.HtmlWindow):
    def __init__(self, parent, id, size=(600,400)):
        wx.html.HtmlWindow.__init__(self,parent, id, size=size)
        if "gtk2" in wx.PlatformInfo:
            self.SetStandardFonts()

    def OnLinkClicked(self, link):
        wx.LaunchDefaultBrowser(link.GetHref())
        
class AboutBox(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "About <<project>>",
        style=wx.DEFAULT_DIALOG_STYLE|wx.THICK_FRAME|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL)
        hwin = HtmlWindow(self, -1, size=(400,200))
        vers = {}
        vers["python"] = sys.version.split()[0]
        vers["wxpy"] = wx.VERSION_STRING
        hwin.SetPage(aboutText % vers)
        btn = hwin.FindWindowById(wx.ID_OK)
        irep = hwin.GetInternalRepresentation()
        hwin.SetSize((irep.GetWidth()+25, irep.GetHeight()+10))
        self.SetClientSize(hwin.GetSize())
        self.CentreOnParent(wx.BOTH)
        self.SetFocus()
        
class TaskBarFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, style=wx.FRAME_NO_TASKBAR |
                                              wx.NO_FULL_REPAINT_ON_RESIZE)

        self.tbicon = BibTaskBarIcon(self)
        icon = wx.Icon('../res/thief.ico', wx.BITMAP_TYPE_ICO)
        self.tbicon.SetIcon(icon, '')
        
        wx.EVT_TASKBAR_LEFT_UP(self.tbicon, self.OnTaskBarLeftClick)
    
    def OnTaskBarLeftClick(self, evt):
        self.PopupMenu(self.tbicon.CreatePopupMenu())
        print "press task bar"
#         dlg = AboutBox()
#         dlg.ShowModal()
#         dlg.Destroy()

    
class BibTaskBarIcon(wx.TaskBarIcon):
    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
        icon = wx.Icon('../res/thief.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon, "title")

    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(ID_SETTING, 'Setting')
        menu.Append(ID_EXIT, 'Exit')
        self.Bind(wx.EVT_MENU, self.OnSetting, id=ID_SETTING)
        self.Bind(wx.EVT_MENU, self.OnExit, id=ID_EXIT)
        #EVT_MENU( menu, id, self.MenuSelectionCb )
        self.menu = menu;
        return self.menu
    
    def OnSetting(self, event):
        wx.MessageBox("Setting Box");
        
    def OnExit(self, event):
        self.Destroy()
        
class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, pos=(150,150), size=(350,200))
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        
        menuBar = wx.MenuBar()
        menu = wx.Menu()
        m_exit = menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Close window and exit program.")
        self.Bind(wx.EVT_MENU, self.OnClose, m_exit)
        menuBar.Append(menu, "&File")
        menu = wx.Menu()
        m_about = menu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, m_about)
        menuBar.Append(menu, "&Help")
        self.SetMenuBar(menuBar)         
        self.statusbar = self.CreateStatusBar()
        
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
             
        m_text = wx.StaticText(panel, -1, "Hello World!")
        m_text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        m_text.SetSize(m_text.GetBestSize())
        box.Add(m_text, 0, wx.ALL, 10)
             
        m_close = wx.Button(panel, wx.ID_CLOSE, "Close")
        m_close.Bind(wx.EVT_BUTTON, self.OnClose)
        box.Add(m_close, 0, wx.ALL, 10)
             
        panel.SetSizer(box)
        panel.Layout()
        
    def OnClose(self, event):
        dlg = wx.MessageDialog(self, "Do you really want to close this application?",
                               "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Destroy()
            
    def OnAbout(self, event):
        dlg = AboutBox()
        dlg.ShowModal()
        dlg.Destroy()    
    