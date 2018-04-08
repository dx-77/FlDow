#!/usr/bin/env python
#
#This file is part of FlDow project
#Copyright (C) 2018 dx-77 <d.x77@yandex.ru>.
#GitHub : https://github.com/dx-77
#
#This program is free software: you can redistribute it and/or modify it under the terms
#of the GNU General Public License as published by the Free Software Foundation,
#either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
#without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#See the GNU General Public License for more details.
# 
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class FrmMain
###########################################################################

class FrmMain(wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__(
            self, parent, id = wx.ID_ANY, title = u"FlDow",
            pos = wx.DefaultPosition, size = wx.Size(600,371),
            style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL
        )
        
        self.SetSizeHints(wx.Size(-1,-1), wx.Size(-1,-1))
        
        bSizer3 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer4 = wx.BoxSizer(wx.VERTICAL)
        
        listboxChoices = []
        self.listbox = wx.ListBox(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(600,200), listboxChoices, wx.LB_EXTENDED
        )
        bSizer4.Add(self.listbox, 0, wx.ALL, 5)
        
        self.gauge = wx.Gauge(
            self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size(600,20), wx.GA_HORIZONTAL
        )
        self.gauge.SetValue(0) 
        self.gauge.SetMinSize(wx.Size(600,20))
        self.gauge.SetMaxSize(wx.Size(600,20))
        
        bSizer4.Add(self.gauge, 0, wx.ALL, 5)
        
        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.btn_select = wx.Button(
            self, wx.ID_ANY, u"Select", wx.DefaultPosition, wx.Size(187,50), 0
        )
        bSizer6.Add(self.btn_select, 0, wx.ALL, 5)
        
        self.btn_download = wx.Button(
            self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.Size(187,50), 0
        )
        bSizer6.Add(self.btn_download, 0, wx.ALL, 5)
        
        self.btn_exit = wx.Button(
            self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.Size(187,50), 0
        )
        bSizer6.Add(self.btn_exit, 0, wx.ALL, 5)
                
        bSizer4.Add(bSizer6, 1, wx.EXPAND, 5)
                
        bSizer3.Add(bSizer4, 1, wx.EXPAND, 5)
                
        self.SetSizer(bSizer3)
        self.Layout()
        self.statusbar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.menubar = wx.MenuBar(0)
        self.mn_file = wx.Menu()
        self.mn_exit = wx.MenuItem(
            self.mn_file, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mn_file.Append(self.mn_exit)
        
        self.menubar.Append(self.mn_file, u"File") 
        
        self.mn_help = wx.Menu()
        self.mn_f1 = wx.MenuItem(self.mn_help, wx.ID_ANY, u"Help", wx.EmptyString, wx.ITEM_NORMAL)
        self.mn_help.Append(self.mn_f1)
        
        self.mn_aboutwx = wx.MenuItem(
            self.mn_help, wx.ID_ANY, u"About wx", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mn_help.Append(self.mn_aboutwx)
        
        self.mn_about = wx.MenuItem(
            self.mn_help, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mn_help.Append(self.mn_about)
        
        self.menubar.Append(self.mn_help, u"Help") 
        
        self.SetMenuBar(self.menubar)
        
    def __del__(self):
        pass

if __name__ == '__main__':
    import fldow
    fldow.main()