#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("fldow.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.prb = QtWidgets.QProgressBar(self.centralwidget)
        self.prb.setGeometry(QtCore.QRect(10, 260, 581, 23))
        self.prb.setProperty("value", 0)
        self.prb.setObjectName("prb")
        self.pbtn_select = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_select.setGeometry(QtCore.QRect(10, 290, 167, 31))
        self.pbtn_select.setObjectName("pbtn_select")
        self.pbtn_download = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_download.setEnabled(True)
        self.pbtn_download.setGeometry(QtCore.QRect(220, 290, 167, 31))
        self.pbtn_download.setCheckable(False)
        self.pbtn_download.setChecked(False)
        self.pbtn_download.setAutoDefault(False)
        self.pbtn_download.setDefault(False)
        self.pbtn_download.setFlat(False)
        self.pbtn_download.setObjectName("pbtn_download")
        self.pbtn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_exit.setGeometry(QtCore.QRect(420, 290, 167, 31))
        self.pbtn_exit.setObjectName("pbtn_exit")
        self.listw_main = QtWidgets.QListWidget(self.centralwidget)
        self.listw_main.setGeometry(QtCore.QRect(10, 10, 581, 231))
        self.listw_main.setStyleSheet("")
        self.listw_main.setAlternatingRowColors(False)
        self.listw_main.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listw_main.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.listw_main.setObjectName("listw_main")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStatusTip("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.act_exit = QtWidgets.QAction(MainWindow)
        self.act_exit.setObjectName("act_exit")
        self.act_f1 = QtWidgets.QAction(MainWindow)
        self.act_f1.setObjectName("act_f1")
        self.act_aboutqt = QtWidgets.QAction(MainWindow)
        self.act_aboutqt.setObjectName("act_aboutqt")
        self.act_about = QtWidgets.QAction(MainWindow)
        self.act_about.setObjectName("act_about")
        self.menuFile.addAction(self.act_exit)
        self.menuHelp.addAction(self.act_f1)
        self.menuHelp.addAction(self.act_aboutqt)
        self.menuHelp.addAction(self.act_about)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
if __name__ == '__main__':
    import fldow
    fldow.main()