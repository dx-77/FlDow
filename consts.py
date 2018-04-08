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

import locale

__all__ = ['DEBUGFLAG', 'MAX_DOWN_FILES', 'HOURS_TO_RENEW', 'USERAGENT', 'PROGRAMVER', 'toolsdict', 
           'tools_nondirect_URL', 'toolslist', 'selected_toolslist', 'prgtext', 'lang']

DEBUGFLAG = False
           
MAX_DOWN_FILES = 999
HOURS_TO_RENEW = 3

USERAGENT = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0)'
             ' Gecko/20100101 Firefox/58.0'}

PROGRAMVER = str(
    'FlDow version 0.5.4\nCopyright (C) 2018 dx-77 <d.x77@yandex.ru>.\n'
    'Source code available at https://github.com/dx-77/FlDow\n\n'   
    'This program is free software: you can redistribute it and/or modify it under the terms '
    'of the GNU General Public License as published by the Free Software Foundation, '
    'either version 3 of the License, or (at your option) any later version. '
    'This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; '
    'without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. '
    'See the GNU General Public License for more details. '
    '\n\nYou should have received a copy of the GNU General Public License '
    'along with this program.  If not, see <http://www.gnu.org/licenses/>.'
)

tools_nondirect_URL = ['360TS', '7-Zip', 'Adwcleaner', 'AIMP', 'CCleaner', 'CPU-Z',
                     'CrystalDiskMark', 'GIMP', 'GPU-Z', 'HWMonitor', 'Inkscape', 'K-Lite',
                     'MBAM', 'Notepad++', 'OCCT', 'PartitionWizard', 'UVS', 'VLC', 'WinBox']
    
toolsdict = {
    '7-Zip': ['http://www.7-zip.org/download.html',
              'http://www.7-zip.org/download.html'],
    '360TS': [
        'https://www.360totalsecurity.com/ru/download-free-antivirus/360-total-security/?'
        'offline=1', None
    ],
    'AmmyAdmin': ['https://getfile.dokpub.com/yandex/get/https://yadi.sk/d/xCoWTJm23Rpy7E', None],
    'Adwcleaner': ['https://toolslib.net/downloads/finish/1-adwcleaner/', None],
    'AIMP': ['https://www.aimp.ru/?do=download', None],
    'Avast': ['http://files.avast.com/iavs9x/avast_free_antivirus_setup_offline.exe', None],
    'CCleaner': ['https://filehippo.com/download_ccleaner', None],
    'CDBurnerXP': ['https://cdburnerxp.se/downloadsetup.exe', None],
    'Chrome': [
        'https://dl.google.com/edgedl/chrome/install/GoogleChromeStandaloneEnterprise.msi',
        'https://dl.google.com/edgedl/chrome/install/GoogleChromeStandaloneEnterprise64.msi'
    ],
    'CPU-Z': ['https://www.cpuid.com/softwares/cpu-z.html', None],
    'CrystalDiskMark': ['https://osdn.net/projects/crystaldiskmark/releases/', None],
    'DrWeb_CureIt': ['http://ftp.drweb.com/pub/drweb/cureit/cureit.exe', None],
    'Firefox': ['https://download.mozilla.org/?product=firefox-latest-ssl&os=win&lang=ru',
               'https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=ru'],
    'FoxitReader': [
        'https://www.foxitsoftware.com/ru/downloads/latest.php?'
        'product=Foxit-Reader&platform=Windows&version=&package_type=exe&language=Russian', None
    ],
    'GIMP': ['https://www.gimp.org/downloads/', None],
    'GPU-Z': ['https://www.techpowerup.com/download/techpowerup-gpu-z/', None],
    'HASP': ['http://safenet-sentinel.ru/files/hasp_lm_setup.zip', None],
    'HijackThis': ['https://sourceforge.net/projects/hjt/files/latest/download', None],
    'HWMonitor': ['https://www.cpuid.com/softwares/hwmonitor.html', None],
    'Inkscape': [
        'https://inkscape.org/ru/download/windows/', 'https://inkscape.org/ru/download/windows/'
    ],
    'K-Lite': ['https://www.codecguide.com/download_k-lite_codec_pack_mega.htm', None],
    'KVRT': ['http://devbuilds.kaspersky-labs.com/devbuilds/KVRT/latest/full/KVRT.exe', None],
    'MBAM': ['https://ru.malwarebytes.com/mwb-download/thankyou/', None],
    'Notepad++': ['https://notepad-plus-plus.org/download/',
                  'https://notepad-plus-plus.org/download/'],
    'OCCT': ['http://www.ocbase.com/download.php?fileext=zip', None],
    'OOSU': ['https://dl5.oo-software.com/files/ooshutup10/OOSU10.exe', None], 
    'OpenedFiles': ['http://www.nirsoft.net/utils/ofview.zip',
                    'http://www.nirsoft.net/utils/ofview-x64.zip'],
    'OpenOffice': [
        'https://sourceforge.net/projects/openofficeorg.mirror/files/latest/download', None
    ],
    'BulletPassView': ['https://www.nirsoft.net/utils/bulletspassview.zip',
                       'https://www.nirsoft.net/utils/bulletspassview-x64.zip'],
    'PartitionWizard': ['https://www.partitionwizard.com/download.html', None],
    'Skype': ['https://go.skype.com/windows.desktop.download', None],
    'SumatraPDF': ['https://www.sumatrapdfreader.org/dl/SumatraPDF-3.1.2-install.exe',
                   'https://www.sumatrapdfreader.org/dl/SumatraPDF-3.1.2-64-install.exe'],
    'TeamViewer': ['https://download.teamviewer.com/download/TeamViewer_Setup.exe', None],
    'Testdisk': ['https://www.cgsecurity.org/testdisk-7.1-WIP.win.zip',
                 'https://www.cgsecurity.org/testdisk-7.1-WIP.win64.zip'],
    'UVS': ['http://dsrt.dyndns.org/uvsfiles.htm', None],
    'Victoria': ['https://getfile.dokpub.com/yandex/get/https://yadi.sk/d/xjPCpzM73Rpy7a', None],
    'VLC': ['https://www.videolan.org/vlc/index.ru.html',
            'https://www.videolan.org/vlc/index.ru.html'],
    'WinBox': ['https://mikrotik.com/download', None],
    'WinDjView': [
        'https://sourceforge.net/projects/windjview/files/latest/download?source=directory', None
    ],
    'XnView': ['http://download3.xnview.com/XnView-win-full.zip', None]
}

toolslist = sorted(toolsdict)
selected_toolslist = toolslist[:]

prgtext = {
    'mfile': ['File', 'Файл'],
    'mexit': ['Exit', 'Выход'],
    'mhelp': ['Help', 'Помощь'],
    'mf1': ['Help', 'Справка'],
    'maboutqt': ['About Qt', 'О Qt'],
    'maboutwx': ['About wx', 'О wx'],
    'mabout': ['About', 'О программе'],
    'bselect': ['Select tools', 'Выбрать программы'],
    'bdownload': ['Download tools', 'Скачать программы'],
    'bquit': ['Quit', 'Выход'],
    'useselectkeys': ['Use Left-Click, Ctrl, Shift, Ctrl-A to select tools to download',
                      'Используйте Левую кнопку мыши, Ctrl, Shift, Ctrl-A для выбора программ'],
    'appearingsoon': ['The tools list will be appearing soon...',
                      'Список программ скоро появится...'],
    'downloading': ['Downloading', 'Скачиваем'],
    'download': ['Download', 'Загрузка'],
    'complete': ['complete', 'завершена'],
    'errordownloading': ['Error downloading', 'Ошибка загрузки'],
    'allcomplete': ['All downloads complete', 'Все загрузки завершены'],
    'nothingdownload': ['Nothing to download', 'Нечего скачивать'],
    'selectdownload': ['Please select tools to download',
                       'Выберите программы для загрузки'],
    'error': ['Error', 'Ошибка'],
    'foldererror': ['Error creating folder', 'Ошибка создания папки'],
    'tryingdownload': ['Trying to download', 'Будем скачивать'],
    'filessaved': ['Files will be saved to', 'Файлы будут сохранены в'],
    'attention': ['Attention', 'Внимание'],
    'downloadprogress': ['Download in progress! Are you sure you want to exit',
                         'Идет скачивание! Вы уверены, что хотите выйти'],
    'f1text': [
        'Fldow is designed to download actual verisons of frequently* used Windows programs. '
        'Programs are downloaded to the FlDow working directory in the folder "Tools". '
        'If the downloaded program is already exists in the "Tools" folder '
        'and it was downloaded more than '+
        str(HOURS_TO_RENEW)+ ' hours ago, the program is overwritten.'
        '\n\n* at least by the FlDow author',
        'FlDow предназначена для скачивания актуальных версий часто* используемых в '
        'ОС Windows программ. Программы скачиваются в рабочий каталог FlDow в папку "Tools". ' 
        'Если скачиваемая программа уже есть в папке "Tools" '
        'и она была скачана более '+
        str(HOURS_TO_RENEW)+ ' час(а, ов) назад, то программа перезаписывается.'
        '\n\n* по крайней мере автором FlDow'
    ]
}

if locale.getdefaultlocale()[0] == 'ru_RU':
    lang = 1
else:
    lang = 0
    
if __name__ == '__main__':
    import fldow
    fldow.main()