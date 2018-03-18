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
import sys
import time
import urllib.request
from PyQt5.QtCore import QTimer, QThread
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QListWidget
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget
import ui
from consts import *


class AppURLopener(urllib.request.FancyURLopener):
    version = list(USERAGENT.values())[0]
    
urllib._urlopener = AppURLopener()


class Downloader(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.percent = 0
       
       
    def downloadprogress(self, count, blocksize, totalsize):
        '''Reporthook func of urllib.request.urlretrieve'''
        self.percent = int(count*blocksize*100/totalsize)
                       

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
                        urllib.request.urlretrieve(url, nm, reporthook=self.downloadprogress)
                    except:
                        urllib._urlopener.retrieve(url, nm, reporthook=self.downloadprogress)
                    try:
                        os.rename(nm, nm + self.detectext(nm))
                    except:
                        pass
                
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
                            urllib.request.urlretrieve(url, nm, reporthook=self.downloadprogress)
                        except:
                            urllib._urlopener.retrieve(url, nm, reporthook=self.downloadprogress)
                        try:
                            os.rename(nm, nm + self.detectext(nm))
                        except:
                            pass
                    
                self.downflag[self.tool_index] = True
            except IndexError:
                break
            except:
                self.downflag[self.tool_index] = 'Error'
            if self.tool_index == downfiles_limit: break
        self.completeflag = True
    
    
    def run(self):
        self.downloadtool(MAX_DOWN_FILES)
 
######################## End of Downloader class #################################################



class MyWin(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        
        #Setup captions
        self.setWindowTitle('FlDow')
        self.ui.pbtn_select.setText(prgtext['bselect'][lang])
        self.ui.pbtn_download.setText(prgtext['bdownload'][lang])
        self.ui.pbtn_exit.setText(prgtext['bquit'][lang])
        self.ui.menuFile.setTitle(prgtext['mfile'][lang])
        self.ui.menuHelp.setTitle(prgtext['mhelp'][lang])
        self.ui.act_exit.setText(prgtext['mexit'][lang])
        self.ui.act_f1.setText(prgtext['mf1'][lang])
        self.ui.act_aboutqt.setText(prgtext['maboutqt'][lang])
        self.ui.act_about.setText(prgtext['mabout'][lang])
        
        #Setup mainwindow
        self.setFixedSize(600, 371)
        qr = self.frameGeometry()
        qr.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(qr.topLeft())
         
        #Triggering buttons
        self.ui.pbtn_exit.clicked.connect(self.close)
        self.ui.pbtn_download.clicked.connect(self.download)
        self.ui.pbtn_select.clicked.connect(self.select)
        
        #Triggering menu items
        self.ui.act_exit.triggered.connect(self.close)
        self.ui.act_f1.triggered.connect(self.f1)
        self.ui.act_about.triggered.connect(self.about)
        self.ui.act_aboutqt.triggered.connect(self.aboutqt)
        
        #Setup listwidget
        self.ui.listw_main.setSelectionMode(QListWidget.NoSelection)
        self.ui.listw_main.setStyleSheet(
            "QListWidget::item:selected { color: green; background: #c4c4c4 }"
        )
        
        #Setup progressbar
        self.ui.prb.setMinimum(0)
        self.ui.prb.setMaximum(100)
        
        #Setup timers
        self.downstatus_timer = QTimer()
        self.downstatus_timer.setSingleShot(True)
        self.downstatus_timer.timeout.connect(self.downstatus)
        self.startprogress_timer = QTimer()
        self.startprogress_timer.setSingleShot(True)
        self.startprogress_timer.timeout.connect(self.startprogress)
        
                      
       
    def closeEvent(self, event):
        if not self.ui.pbtn_download.isEnabled() and not self.ui.pbtn_select.isEnabled():
            reply = QMessageBox.question(
                self, prgtext['attention'][lang], prgtext['downloadprogress'][lang] + ' ?',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
        else:
            reply = QMessageBox.Yes
            
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()       

       
    def downstatus(self):
        '''Callback func which monitoring status of urlretrieve'''
        if (not self.ui.pbtn_download.isEnabled()) and (
            self.down_thread.tool_index < len(selected_toolslist)
        ):
            try:
                lastitem = self.ui.listw_main.item(self.ui.listw_main.count()-1).text()
                message = prgtext['downloading'][lang] + ' %s...' % selected_toolslist[self.down_thread.tool_index]
                if lastitem != message:
                    self.ui.listw_main.addItem(message)
                    self.ui.listw_main.scrollToBottom()
                    
                if self.down_thread.downflag[self.down_thread.tool_index] == 'Error': 
                    raise urllib.request.URLError(11001)
                if self.down_thread.downflag[self.down_thread.tool_index]:
                    self.down_thread.percent = 0
                    self.ui.prb.setValue(self.down_thread.percent)
                    self.ui.listw_main.addItem(
                        prgtext['download'][lang] + ' ' +selected_toolslist[self.down_thread.tool_index]+ ' ' +
                        prgtext['complete'][lang]
                    )
                    self.ui.listw_main.scrollToBottom()
                    self.down_thread.tool_index += 1
            except: 
                self.down_thread.percent = 0
                self.ui.prb.setValue(self.down_thread.percent)
                self.ui.listw_main.addItem(
                    prgtext['errordownloading'][lang] + ' %s' % selected_toolslist[self.down_thread.tool_index]
                )
                self.ui.listw_main.scrollToBottom()
                self.down_thread.tool_index += 1
            
            self.downstatus_timer.start(500) # Calling self.downstatus
                   
        
        if self.down_thread.completeflag:
            self.ui.pbtn_download.setEnabled(True)
            self.ui.pbtn_select.setEnabled(True)
            lastitem = self.ui.listw_main.item(self.ui.listw_main.count()-1).text()
            message = prgtext['allcomplete'][lang]
            if lastitem != message:
                self.ui.listw_main.addItem(message)
                self.ui.listw_main.scrollToBottom()
                
  
    def startprogress(self):
        if not self.down_thread.completeflag:
            self.ui.prb.setValue(self.down_thread.percent)
            self.startprogress_timer.start(100) # Calling self.startprogress
    
    
    def download(self):
        #pbtn_download clicked slot
        global selected_toolslist
        self.ui.statusbar.showMessage('')
    
        if not self.ui.pbtn_select.isEnabled():
            self.ui.listw_main.setSelectionMode(QListWidget.NoSelection)
            self.ui.pbtn_select.setEnabled(True)
            curselection = self.ui.listw_main.selectedItems()
            curselection = [widgetitem.text() for widgetitem in curselection]
            self.ui.listw_main.clear()
            if not curselection:
                self.ui.listw_main.addItem(prgtext['nothingdownload'][lang])
                self.ui.listw_main.addItem(prgtext['selectdownload'][lang])
                self.ui.pbtn_download.setEnabled(False)
            selected_toolslist = curselection
            
               
        if not selected_toolslist:
            return False
       
        try:
            if not os.access('./Tools', os.F_OK): os.mkdir('./Tools')
        except:
            QMessageBox.critical(self, prgtext['error'][lang],
                                         prgtext['foldererror'][lang] + ' "Tools"')
            return False
        
        for tool in selected_toolslist:
            path = './Tools/%s' % tool
            try:
                if not os.access(path, os.F_OK): os.mkdir(path)
            except:
                QMessageBox.critical(self, prgtext['error'][lang],
                                             prgtext['foldererror'][lang] + ' "%s"' % path)
                return False
    
        self.ui.listw_main.addItem(prgtext['tryingdownload'][lang] + ':')
        self.ui.listw_main.addItems(selected_toolslist)
        self.ui.listw_main.addItem(prgtext['filessaved'][lang] + ' %s/Tools' % os.path.abspath(os.curdir))
        self.ui.pbtn_download.setEnabled(False)
        self.ui.pbtn_select.setEnabled(False)
        
        self.down_thread = Downloader()
        self.down_thread.completeflag = False
        self.down_thread.downflag = [False]*len(selected_toolslist)
        self.down_thread.tool_index, self.down_thread.percent = 0, 0
        self.downstatus()
        self.down_thread.start()
        self.startprogress()
    
        return True
   
   
    def select(self):
        #pbtn_select clicked slot
        self.ui.statusbar.showMessage(prgtext['useselectkeys'][lang])
        self.ui.pbtn_select.setEnabled(False)
        self.ui.listw_main.clear()
        self.ui.listw_main.setSelectionMode(QListWidget.ExtendedSelection)
        self.ui.listw_main.addItems(toolslist)
        for tool in selected_toolslist:
            k = toolslist.index(tool)
            self.ui.listw_main.item(k).setSelected(True)
        
 
    def f1(self):
        QMessageBox.information(self, prgtext['mf1'][lang], prgtext['f1text'][lang])
    
    def aboutqt(self):
        QMessageBox.aboutQt(self)
    
    def about(self):
        QMessageBox.information(self, prgtext['mabout'][lang] + '...', PROGRAMVER)
    
########################### End of class MyWin(QMainWindow) ######################################

def main():
    app = QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()