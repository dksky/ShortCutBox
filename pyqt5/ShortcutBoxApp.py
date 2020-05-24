import sys
from PyQt5 import QtCore, QtWidgets, QtGui, QtWidgets, uic
from PyQt5.QtCore import QSize , Qt
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QGridLayout, QGroupBox, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from guihelper_loadconfig import *
from guihelper_methods import *
import sys
import math

# for debug
# import msvcrt 
# msvcrt.getch()


def refresh(self):
    print('refresh UI')
    generate_buttons(self, tab1ButtonList, 'folder', 2 )
    generate_buttons(self, tab2ButtonList, 'bash', 3 )
    generate_buttons(self, tab3ButtonList, 'exe', 2 )
    save_FolderJson()



class ProxyStyle(QtWidgets.QProxyStyle):
    def drawControl(self, element, option, painter, widget=None):
        if element == QtWidgets.QStyle.CE_PushButtonLabel:
            icon = QtGui.QIcon(option.icon)
            option.icon = QtGui.QIcon()
        super(ProxyStyle, self).drawControl(element, option, painter, widget)
        if element == QtWidgets.QStyle.CE_PushButtonLabel:
            if not icon.isNull():
                iconSpacing = 4
                mode = (
                    QtGui.QIcon.Normal
                    if option.state & QtWidgets.QStyle.State_Enabled
                    else QtGui.QIcon.Disabled
                )
                if (
                    mode == QtGui.QIcon.Normal
                    and option.state & QtWidgets.QStyle.State_HasFocus
                ):
                    mode = QtGui.QIcon.Active
                state = QtGui.QIcon.Off
                if option.state & QtWidgets.QStyle.State_On:
                    state = QtGui.QIcon.On
                window = widget.window().windowHandle() if widget is not None else None
                pixmap = icon.pixmap(window, option.iconSize, mode, state)
                pixmapWidth = pixmap.width() / pixmap.devicePixelRatio()
                pixmapHeight = pixmap.height() / pixmap.devicePixelRatio()
                iconRect = QtCore.QRect(
                    QtCore.QPoint(), QtCore.QSize(pixmapWidth, pixmapHeight)
                )
                iconRect.moveCenter(option.rect.center())
                iconRect.moveLeft(option.rect.left() + iconSpacing)
                iconRect = self.visualRect(option.direction, option.rect, iconRect)
                iconRect.translate(
                    self.proxy().pixelMetric(
                        QtWidgets.QStyle.PM_ButtonShiftHorizontal, option, widget
                    ),
                    self.proxy().pixelMetric(
                        QtWidgets.QStyle.PM_ButtonShiftVertical, option, widget
                    ),
                )
                painter.drawPixmap(iconRect, pixmap)

class UI_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI_MainWindow, self).__init__()
        # uic.loadUi('ui/shortbox_mockUI_gridlayout.ui', self)
        # uic.loadUi('ui/menge_ui.ui', self)
        uic.loadUi('ui/shortbox_mockUI_Tabs_gridlayout.ui', self)
        generate_buttons(self, tab1ButtonList, 'folder', 2 )
        generate_buttons(self, tab2ButtonList, 'bash', 3 )
        generate_buttons(self, tab3ButtonList, 'exe', 2 )
        self.show()

    EXIT_CODE_REBOOT = -123

    def keyPressEvent(self,e):
        if (e.key() == Qt.Key_R):
            QtWidgets.qApp.exit( UI_MainWindow.EXIT_CODE_REBOOT )


def restart():  # function connected to when menu restart button clicked
    print(' Restart App .... fired! ')
    QtWidgets.qApp.exit( UI_MainWindow.EXIT_CODE_REBOOT )

def registerFunction(self):
    self.actionReload.triggered.connect( lambda: restart() )
    self.actionAdd_Shortcut_Folder.triggered.connect( lambda: open_AddFolderShortcutDialog(self) )
    self.action_Shortcut_Application.triggered.connect( lambda : open_AddFileShortcutDialog(self) )
    self.actionSave_Settings.triggered.connect( lambda : save_settingsDialog(self) )
    # self.actionQuick_Folders.triggered.connect( lambda : self.tab_2.setCurrentIndex(1) )
    # self.actionQuick_Bash.triggered.connect( lambda : self.tab_2.setCurrentIndex(1) )
    # self.actionQuick_Application.triggered.connect( lambda : self.tab_3.setCurrentIndex(1) )


def open_AddFolderShortcutDialog(self):
    directory_ = QFileDialog.getExistingDirectory(self, "Select Folder", "./")
    print(directory_)
    basename_ = os.path.basename(directory_)
    add_new_FolderButton( basename_ , directory_ , '',  partial( refresh, self )  )

def open_AddFileShortcutDialog(self):
    fileName1, filetype = QFileDialog.getOpenFileName(self,
                                    "Select File",
                                    "./",
                                    "Exe Files (*.exe);All Files (*)")   #设置文件扩展名过滤,注意用双分号间隔
    print(fileName1,filetype)
    basename_ = os.path.basename(fileName1)
    print(basename_)
    add_new_FileButton( basename_ ,  fileName1  , "" , partial( refresh, self ) )



def save_settingsDialog(self):
    fileName2, ok2 = QFileDialog.getSaveFileName(self,
                            "File Save",
                            "./",
                            "All Files (*);;Text Files (*.txt)")

def callback( str='' ):
    print('[Clicked CallBack]: ' + str)

def generate_buttons( self , tabBtnList, type, columnPerRow = 2 ):
    # return
    if( type == 'folder'):
        gridLayoutContainer = self.gridLayoutWidget
        gridLayout = self.gridLayout
    elif( type == 'bash'):
        gridLayoutContainer = self.gridLayoutWidget_2
        gridLayout = self.gridLayout_2
    elif( type == 'exe'):
        gridLayoutContainer = self.gridLayoutWidget_3
        gridLayout = self.gridLayout_3


    index = 0
    col_index = 0
    row_index = 0
    max_columns = columnPerRow
    total = len( tabBtnList )
    for button in tabBtnList:
        # # self.folderBtnDyn.setGeometry(QtCore.QRect(50, 10, 91, 81))
        self.folderTemp =  QtWidgets.QPushButton(gridLayoutContainer)
        self.folderTemp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.folderTemp.setAcceptDrops(False)
        # self.folderTemp.setCheckable(False)
        # self.folderTemp.setAutoRepeat(False)
        # self.folderTemp.setAutoDefault(False)
        if( type == 'folder' ):
            self.folderTemp.setIcon(QtGui.QIcon("img/folder.png"))
        if( type == 'exe' ):
            self.folderTemp.setIcon(QtGui.QIcon("img/exe.png"))
        if( type == 'bash' ):
            self.folderTemp.setIcon(QtGui.QIcon("img/bash.png"))
        if( type == 'python' ):
            self.folderTemp.setIcon(QtGui.QIcon("img/python.png"))
        
        
        self.folderTemp.setIconSize(QtCore.QSize(40, 40))
        self.folderTemp.setMinimumHeight(40)
        


        if( type == 'folder'):
            self.folderTemp.setToolTip("Open: " + button.command )
            self.folderTemp.clicked.connect( partial( open_explorer , button.command ) )

        if( type == 'bash'):
            self.folderTemp.setToolTip("bash Open: " + button.command )
            self.folderTemp.clicked.connect( partial( bash_opener , button.command ) )
        
        filename, file_extension = os.path.splitext(button.command)
        # print('filename: ' + filename + ' | extension: ' + file_extension )
        if( file_extension == ".exe" ):
            type = "exe"
            self.folderTemp.setIcon(QtGui.QIcon("img/exe.png"))
        if( file_extension == ".py" ):
            type = "python"
            self.folderTemp.setIcon(QtGui.QIcon("img/python.png"))
        
        if( type == 'exe'):
            self.folderTemp.setToolTip("run exe: " + button.command )
            self.folderTemp.clicked.connect( partial( script_runner , button.command, "exe", button.args ) )

        if( type == 'python'):
            self.folderTemp.setToolTip("run python: " + button.command )
            self.folderTemp.clicked.connect( partial( script_runner , button.command, 'python', button.args ) )


        # self.folderTemp.setObjectName("folderTemp")
        self.folderTemp.setText( button.text )
        row_index = math.floor( index / max_columns ) 
        col_index = index % max_columns
        # print( str( row_index )  + " : " + str(  col_index ) )
        gridLayout.addWidget(self.folderTemp, row_index , col_index , 1 , 1 )
        index = index + 1




if __name__=="__main__":
    currentExitCode = UI_MainWindow.EXIT_CODE_REBOOT
    while currentExitCode == UI_MainWindow.EXIT_CODE_REBOOT:
        app = QtWidgets.QApplication(sys.argv)
        w = UI_MainWindow()
        registerFunction(w)

        proxy_style = ProxyStyle(app.style())
        app.setStyle(proxy_style)
        
        w.show()
        currentExitCode = app.exec_()
        app = None  # delete the QApplication object

