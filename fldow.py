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
import os
import ssl
import sys
import time
import threading
import urllib.request
import wx
import ui
from consts import *


class AppURLopener(urllib.request.FancyURLopener):
    version = list(USERAGENT.values())[0]
    
urllib._urlopener = AppURLopener()


class Downloader(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.percent = 0
        self.debugmessage = []
        
        try:
            # for correct downloading GIMP by Python 3.4.4
            ssl._create_default_https_context = ssl._create_unverified_context  
        except:
            pass
       
       
    def downloadprogress(self, count, blocksize, totalsize):
        '''Reporthook func of urllib.request.urlretrieve'''
        self.percent = int(count*blocksize*100/totalsize)
        if self.closeflag: 2/0 # Horrible piece of shit to interrupt urlretrieve thread when destroying wxpython window
                       

    def urlextract(self, url, str1, str2, charset='utf-8'):
        url = urllib.request.urlopen(url).read().decode(charset)
        url = url[url.find(str1) + len(str1):url.find(str2)]
        return url

        
    def changeurl(self, url, tool_index, x64=False):
        if selected_toolslist[tool_index] not in tools_nondirect_URL:
            return url
    
        if selected_toolslist[tool_index] == '360TS':
            url = 'https:' + self.urlextract(url, '<a class="download-link" href="',
                                             '">перезапустите ее</a>')
            
        elif selected_toolslist[tool_index] == '7-Zip':
            url = self.urlextract(url, '<TD class="Item" align="center"><A href="',
                                  '.exe">Download</A></TD>')
            url = 'http://www.7-zip.org/' + url + '.exe'
            if x64: url = url.replace('.exe', '-x64') + '.exe'
            
        elif selected_toolslist[tool_index] == 'Adwcleaner':
            url = self.urlextract(url, '<a id="downloadLink" href="', '">Click here!</a>')
        
        elif selected_toolslist[tool_index] == 'AIMP':
            url = self.urlextract(
                url, 'Скачать с сервера:</b><br/><ul><li><a href="', '">AIMP.RU</a>'
            )
            
        elif selected_toolslist[tool_index] == 'CCleaner':
            url = self.urlextract(
                url, 'active short download-button" href="', '" onclick="_gaq.push'
            )
            url = self.urlextract(
                url, '<a href="/download/file',
                '" class="text" style="text-decoration: none;" id="download-link">'
            )
            url = 'https://filehippo.com/download/file' + url
            
        elif selected_toolslist[tool_index] == 'CPU-Z':
            url = 'https://www.cpuid.com' + self.urlextract(
                url, '<a class="button icon-zip" href="',
                '"><span>zip • english <em>'
            )
            str1 = str(
                'is ready for download.\n                            </p>\n               '
                '             <p>\n                                <a class="button" href="'
            )
            url = self.urlextract(url, str1, '"><span>DOWNLOAD NOW!</span></a>')
            
        elif selected_toolslist[tool_index] == 'CrystalDiskMark':
            url = 'https://osdn.net' + self.urlextract(url, 'pref-download-btn-win32" href="',
                                                       '" title="Windows"')
            url = 'https://osdn.net' + self.urlextract(
                url, '<a class="mirror_link" target="_brank" rel="nofollow" href="',
                'zip">CrystalDiskMark'
            ) + 'zip'
                            
        elif selected_toolslist[tool_index] == 'GIMP':
            url = self.urlextract(
                url, '<span class=\'win-button\'>\n            <a\n            href="', '.exe"'
            )
            url = 'https:' + url + '.exe'
            
        elif selected_toolslist[tool_index] == 'GPU-Z':
            s = self.urlextract(
                url, '<input type="hidden" name="id" value="',
                '" />\n\t\t\t\t<input type="submit" class="button startbutton" value="Download"'
            )
            for servernumber in range(1, 10):
                dt = 'id=' + s + '&server_id='+str(servernumber)
                try:
                    url = urllib.request.urlopen(url, data=dt.encode()).geturl()
                    break
                except:
                    pass
                
        elif selected_toolslist[tool_index] == 'HWMonitor':
            url = self.urlextract(url, '<a class="button icon-zip" href="',
                                  '"><span>zip • english <em>')
            url = 'https://www.cpuid.com' + url
            url = self.urlextract(url, '<a class="button" href="', '"><span>DOWNLOAD NOW!')
            
        elif selected_toolslist[tool_index] == 'Inkscape':
            if x64:
                url = urllib.request.urlopen(url).read().decode('utf-8')
                str1 = '">installer (exe)</a></li>'
                url = url[url.find(str1) + len(str1):]
                str1 = str(
                    '<strong>64-bit Windows</strong>:</p>\n\n\t\t\t<ul>\n\t\t\t\t<li><a href="'
                )
                str2 = '">installer (exe)</a></li>'
                url = url[url.find(str1) + len(str1):url.find(str2)]
            else:
                url = self.urlextract(
                    url,
                    '<strong>32-bit Windows</strong>:</p>\n\n\t\t\t<ul>\n\t\t\t\t'
                    '<li class="clearfix"><a href="', '">installer (exe)</a></li>'
                )
            
        elif selected_toolslist[tool_index] == 'K-Lite':
            url = self.urlextract(url, 'HTTP</td><td><a href="', '">Mirror 1</a>')
                
        elif selected_toolslist[tool_index] == 'MBAM':
            url = self.urlextract(url, 'downloadUrl = "', '/";\n      setTimeout(function()')
            
        elif selected_toolslist[tool_index] == 'Notepad++':
            url = self.urlextract(
                url, 'Download 32-bit x86</h2>\r\n<ul>\r\n<li><strong><a href="',
                '"><img title="Notepad++ Download"'
            )
            url = 'https://notepad-plus-plus.org' + url
            if x64: url = url.replace('.exe', '.x64') + '.exe'
            
        elif selected_toolslist[tool_index] == 'OCCT':
            url = self.urlextract(url, 'If your download does not start, <a href="',
                                  '"> click here </a>')
            url = 'http://www.ocbase.com/' + url
                
        elif selected_toolslist[tool_index] == 'PartitionWizard':
            url = urllib.request.Request(url, headers=USERAGENT)
            url = self.urlextract(url, '<p><a href="', '" data-down="free"')
                            
        elif selected_toolslist[tool_index] == 'UVS':
            url = 'http://dsrt.dyndns.org/files/uvs_v' + self.urlextract(
                url, '<a href="/files/uvs_v', '">uVS</a>', charset='windows-1251'
            )
                
        elif selected_toolslist[tool_index] == 'VLC':
            url = 'https:' + self.urlextract(url, 'btn-dl"'+" href='", ".exe'>") + '.exe'
            if x64: url = url.replace('32', '64')
                
        elif selected_toolslist[tool_index] == 'WinBox':
            url = 'https:' + self.urlextract(
                url, 'Winbox to connect to your device, Dude to monitor your network and '
                'Netinstall for recovery and re-installation.\n</p>\n        \n         <a href="',
                'winbox.exe'
            ) + 'winbox.exe'
                
        return url
    
    
    def detectext(self, nm, url=None):
        if url:
            try:
                r = urllib.request.urlopen(url)
            except:
                return '.exe'
            b = r.read(2)
        else:
            with open(nm,'rb') as f:
                b = f.read(2)
        if b == b'MZ':
            return '.exe'
        elif b == b'\xd0\xcf':
            return '.msi'
        else:
            return '.zip'
 
 
    def downloadtool(self, downfiles_limit):
        '''Thread download func to download tools in selected_toolslist using URL in toolsdict'''
        while self.tool_index < len(selected_toolslist):
            if self.completeflag or downfiles_limit == 0: return False
            try:
                if self.downflag[self.tool_index]: continue
            
                nm = './Tools/%s/%s' % (selected_toolslist[self.tool_index],
                                        selected_toolslist[self.tool_index])
            
                url = self.changeurl(
                    toolsdict[selected_toolslist[self.tool_index]][0], self.tool_index
                )
                ext = self.detectext(nm, url)
                t = 111
                if os.access(nm + ext, os.W_OK):
                    t = (time.time() - os.path.getmtime(nm + ext)) / 3600
                    if t > HOURS_TO_RENEW:
                        try:
                            os.remove(nm + ext)
                        except:
                            pass
                if t > HOURS_TO_RENEW:
                    try:
                        filename, headers = urllib.request.urlretrieve(
                            url, nm, reporthook=self.downloadprogress
                        )
                    except ZeroDivisionError: # exiting program
                        return False
                    except:
                        filename, headers = urllib._urlopener.retrieve(
                            url, nm, reporthook=self.downloadprogress
                        )
                        
                    if DEBUGFLAG:
                        self.debugmessage = str(headers).split('\n')
                   
                    try:
                        os.rename(nm, nm + self.detectext(nm))
                    except:
                        pass
                        
                # if x64 tool version exists               
                if toolsdict[selected_toolslist[self.tool_index]][1]:
                    nm = './Tools/%s/%s_x64' % (selected_toolslist[self.tool_index],
                                                selected_toolslist[self.tool_index])
                    url = self.changeurl(
                        toolsdict[selected_toolslist[self.tool_index]][1],
                        self.tool_index, x64=True
                    )
                    ext = self.detectext(nm, url)
                    t = 222
                    if os.access(nm + ext, os.W_OK):
                        t = (time.time() - os.path.getmtime(nm + ext)) / 3600
                        if t > HOURS_TO_RENEW:
                            try:
                                os.remove(nm + ext)
                            except:
                                pass
                    if t > HOURS_TO_RENEW:
                        try:
                            filename, headers = urllib.request.urlretrieve(
                                url, nm, reporthook=self.downloadprogress
                            )
                        except ZeroDivisionError: # exiting program
                            return False
                        except:
                            filename, headers = urllib._urlopener.retrieve(
                                url, nm, reporthook=self.downloadprogress
                            )
                        
                        if DEBUGFLAG:
                            self.debugmessage = str(headers).split('\n')
                     
                        try:
                            os.rename(nm, nm + self.detectext(nm))
                        except:
                            pass
                    
                self.downflag[self.tool_index] = True
            except IndexError:
                break
            except ZeroDivisionError:
                return False # Exiting program
            except Exception as e:
                if DEBUGFLAG:
                    self.debugmessage = e
                    print (e)
                self.downflag[self.tool_index] = 'Error'
            if self.tool_index == downfiles_limit: break
        self.completeflag = True
        return True
    
    
    def run(self):
        self.downloadtool(MAX_DOWN_FILES)
         
######################## End of Downloader(Thread) class #########################################

class MyWin(ui.FrmMain):
    def __init__(self, parent):
        ui.FrmMain.__init__(self, parent)
        
        self.down_thread = Downloader()
        self.down_thread.closeflag = False
        self.down_thread.completeflag = False
        self.down_thread.downflag = [False]*len(selected_toolslist)
        self.down_thread.tool_index, self.down_thread.percent = 0, 0
       
        #Setup captions
        self.SetTitle('FlDow')
        self.btn_select.SetLabel(prgtext['bselect'][lang])
        self.btn_download.SetLabel(prgtext['bdownload'][lang])
        self.btn_exit.SetLabel(prgtext['bquit'][lang])
        self.menubar.SetLabelTop(0, prgtext['mfile'][lang])
        self.menubar.SetLabelTop(1, prgtext['mhelp'][lang])
        self.mn_exit.SetText(prgtext['mexit'][lang])
        self.mn_f1.SetText(prgtext['mf1'][lang])
        self.mn_aboutwx.SetText(prgtext['maboutwx'][lang]) 
        self.mn_about.SetText(prgtext['mabout'][lang])  
   
        #Setup mainwindow
        icon = wx.Icon()
        iconpath = 'fldow.ico'
        try:
            iconpath = sys._MEIPASS + '/' + iconpath
        except:
            pass
        icon.CopyFromBitmap(wx.Bitmap(iconpath, wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        self.Centre(wx.BOTH)
        self.SetBackgroundColour(wx.NullColour)
        
        #Triggering buttons and menu items
        self.btn_select.Bind(wx.EVT_BUTTON, self.btn_select_click)
        self.btn_download.Bind(wx.EVT_BUTTON, self.btn_download_click)
        self.btn_exit.Bind(wx.EVT_BUTTON, self.btn_exit_click)
        self.Bind(wx.EVT_MENU, self.mn_exit_click, id = self.mn_exit.GetId())
        self.Bind(wx.EVT_MENU, self.mn_about_click, id = self.mn_about.GetId())
        self.Bind(wx.EVT_MENU, self.mn_aboutwx_click, id = self.mn_aboutwx.GetId())
        self.Bind(wx.EVT_MENU, self.mn_f1_click, id = self.mn_f1.GetId())
        self.Bind(wx.EVT_CLOSE, self.onclose)
               
        #Setup progressbar
        self.gauge.SetRange(100)
        self.gauge.SetValue(0)
        
        #Setup timers
        self.downstatus_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.downstatus, self.downstatus_timer)
        self.startprogress_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.startprogress, self.startprogress_timer)
           
   
    def btn_select_click(self, event):
        #btn_select clicked slot
        self.statusbar.SetStatusText(prgtext['useselectkeys'][lang])
        self.btn_select.Disable()
        self.listbox.Clear()
                        
        self.listbox.Append(toolslist)
        
        for tool in selected_toolslist:
            self.listbox.SetStringSelection(tool)
  
  
    def downstatus(self, event):
        '''Callback func which monitoring status of urlretrieve'''
        if self.down_thread.closeflag: return False
        
        if (not self.btn_download.IsEnabled()) and (
            self.down_thread.tool_index < len(selected_toolslist)
        ):
            try:
                lastitem = self.listbox.GetString(self.listbox.GetCount() - 1)
                message = prgtext['downloading'][lang] + ' %s...' % selected_toolslist[self.down_thread.tool_index]
                if lastitem != message:
                    self.listbox.Append(message)
                    self.listbox.ScrollLines(self.listbox.GetCount())
                    
                if self.down_thread.downflag[self.down_thread.tool_index] == 'Error': 
                    raise urllib.request.URLError(11001)
                if self.down_thread.downflag[self.down_thread.tool_index]:
                    self.down_thread.percent = 0
                    self.gauge.SetValue(self.down_thread.percent)
                    self.listbox.Append(
                        prgtext['download'][lang] + ' ' +
                        selected_toolslist[self.down_thread.tool_index]+ ' ' +
                        prgtext['complete'][lang]
                    )
                    self.listbox.Append(' ')
                    self.listbox.ScrollLines(self.listbox.GetCount())
                    self.down_thread.tool_index += 1
            except: 
                self.down_thread.percent = 0
                self.gauge.SetValue(self.down_thread.percent)
                self.listbox.Append(
                    prgtext['errordownloading'][lang] + ' %s' % selected_toolslist[self.down_thread.tool_index]
                )
                self.listbox.Append(' ')
                self.listbox.ScrollLines(self.listbox.GetCount())
                self.down_thread.tool_index += 1
            
            if DEBUGFLAG:
                if self.down_thread.debugmessage:
                    try:
                        self.listbox.Append(self.down_thread.debugmessage)
                    except:
                        pass
                    print (self.down_thread.debugmessage)
                    self.down_thread.debugmessage = []
            
            if not self.down_thread.closeflag:
                self.downstatus_timer.StartOnce(500) # Calling self.downstatus
                   
        
        if self.down_thread.completeflag:
            self.btn_download.Enable()
            self.btn_select.Enable()
            lastitem = self.listbox.GetString(self.listbox.GetCount() - 1)
            message = prgtext['allcomplete'][lang]
            if lastitem != message:
                self.listbox.Append(message)
                self.listbox.ScrollLines(self.listbox.GetCount())
    
    
    def startprogress(self, event):
        if self.down_thread.closeflag: return False
        
        if not self.down_thread.completeflag:
            self.gauge.SetValue(self.down_thread.percent)
            if not self.down_thread.closeflag:
                self.startprogress_timer.StartOnce(100) # Calling self.startprogress
    
    def btn_download_click(self, event):
        #btn_download clicked slot
        global selected_toolslist
        self.statusbar.SetStatusText('')
    
        if not self.btn_select.IsEnabled():
            self.btn_select.Enable()
            curselection = [self.listbox.GetString(i) for i in self.listbox.GetSelections()]
            self.listbox.Clear()
            if not curselection:
                self.listbox.Append(prgtext['nothingdownload'][lang])
                self.listbox.Append(prgtext['selectdownload'][lang])
                self.btn_download.Disable()
            selected_toolslist = curselection
                 
        if not selected_toolslist:
            return False
       
        try:
            if not os.access('./Tools', os.F_OK): os.mkdir('./Tools')
        except:
            dlg = wx.MessageDialog(self, prgtext['foldererror'][lang] + ' "Tools"',
                                   prgtext['error'][lang], wx.ICON_ERROR | wx.OK)
            dlg.ShowModal()
            return False
        
        for tool in selected_toolslist:
            path = './Tools/%s' % tool
            try:
                if not os.access(path, os.F_OK): os.mkdir(path)
            except:
                dlg = wx.MessageDialog(self, prgtext['foldererror'][lang] + ' "%s"' % path,
                                       prgtext['error'][lang], wx.ICON_ERROR | wx.OK)
                dlg.ShowModal()
                return False
    
        self.listbox.Append(prgtext['tryingdownload'][lang] + ':')
        self.listbox.Append(selected_toolslist)
        
        self.listbox.Append(
            prgtext['filessaved'][lang] + ' %s/Tools' % os.path.abspath(os.curdir)
        )
        self.listbox.Append(' ')
        self.btn_download.Disable()
        self.btn_select.Disable()
        
        if self.down_thread.completeflag:
            self.down_thread = Downloader()
            self.down_thread.closeflag = False
            self.down_thread.completeflag = False
            self.down_thread.downflag = [False]*len(selected_toolslist)
            self.down_thread.tool_index, self.down_thread.percent = 0, 0
        self.downstatus(0)
        self.down_thread.start()
        self.startprogress(0)
    
        return True
    
    
    def onclose(self, event):
        if not self.btn_download.IsEnabled() and not self.btn_select.IsEnabled():
            dlg = wx.MessageDialog(
                self, prgtext['downloadprogress'][lang] + ' ?',
                prgtext['attention'][lang], wx.YES | wx.NO | wx.ICON_EXCLAMATION
            )
            reply = dlg.ShowModal()
        else:
            reply = wx.ID_YES
            
        if reply == wx.ID_YES:
            threads = str(threading.enumerate())
            if threads.find('Downloader') != -1:
                threadsnumber = len(threading.enumerate())
                self.down_thread.closeflag = True
                self.down_thread.completeflag = True
                while threadsnumber > 1 and len(threading.enumerate()) == threadsnumber:
                    pass
            event.Skip()
    
    def btn_exit_click(self, event):
        self.Close()
            
   
    def mn_exit_click(self, event):
        self.Close()
    
    
    def mn_about_click(self, event):
        dlg = wx.MessageDialog(self, PROGRAMVER, prgtext['mabout'][lang] + '...', wx.OK)
        dlg.ShowModal()
        
        
    def mn_aboutwx_click(self, event):
        wxversion = (
            'This program uses wxPython version %s\n'
            'wxPython is a cross platform GUI toolkit for Python\n'
            'Home-page: http://wxPython.org/\n'
            'Author: Robin Dunn\n'
            'License: wxWindows Library License (https://opensource.org/licenses/wxwindows.php)' % wx.__version__ 
        )
        dlg = wx.MessageDialog(self, wxversion, prgtext['maboutwx'][lang] + '...', wx.OK)
        dlg.ShowModal()
    
    
    def mn_f1_click(self, event):
        dlg = wx.MessageDialog(self, prgtext['f1text'][lang], prgtext['mf1'][lang], wx.OK)
        dlg.ShowModal()
######################## End of MyWin(ui.FrmMain) class ##########################################

def main():
    app = wx.App()
    wnd = MyWin(None)
    wnd.Show(True)
    app.MainLoop()

if __name__=="__main__":
    main()