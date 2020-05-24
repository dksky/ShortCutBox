# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 60, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 72, 15))
        self.label_2.setObjectName("label_2")
        self.userNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.userNameInput.setGeometry(QtCore.QRect(140, 60, 113, 21))
        self.userNameInput.setObjectName("userNameInput")
        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(140, 90, 113, 21))
        self.passwordInput.setObjectName("passwordInput")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuMy_Favourite = QtWidgets.QMenu(self.menubar)
        self.menuMy_Favourite.setObjectName("menuMy_Favourite")
        self.menuMy_Favourite_2 = QtWidgets.QMenu(self.menuMy_Favourite)
        self.menuMy_Favourite_2.setObjectName("menuMy_Favourite_2")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPlugins = QtWidgets.QAction(MainWindow)
        self.actionPlugins.setObjectName("actionPlugins")
        self.actionAdd_Button = QtWidgets.QAction(MainWindow)
        self.actionAdd_Button.setObjectName("actionAdd_Button")
        self.actionfolders = QtWidgets.QAction(MainWindow)
        self.actionfolders.setObjectName("actionfolders")
        self.actionbuttons = QtWidgets.QAction(MainWindow)
        self.actionbuttons.setObjectName("actionbuttons")
        self.actiontypes = QtWidgets.QAction(MainWindow)
        self.actiontypes.setObjectName("actiontypes")
        self.menuMy_Favourite_2.addAction(self.actionfolders)
        self.menuMy_Favourite_2.addAction(self.actionbuttons)
        self.menuMy_Favourite_2.addAction(self.actiontypes)
        self.menuMy_Favourite.addAction(self.menuMy_Favourite_2.menuAction())
        self.menuMy_Favourite.addAction(self.actionAdd_Button)
        self.menuSettings.addAction(self.actionPlugins)
        self.menubar.addAction(self.menuMy_Favourite.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "UserName: "))
        self.label_2.setText(_translate("MainWindow", "Password: "))
        self.menuMy_Favourite.setTitle(_translate("MainWindow", "WorkSpace"))
        self.menuMy_Favourite_2.setTitle(_translate("MainWindow", "My Favourite"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionPlugins.setText(_translate("MainWindow", "Plugins"))
        self.actionAdd_Button.setText(_translate("MainWindow", "Add Button"))
        self.actionfolders.setText(_translate("MainWindow", "folders"))
        self.actionbuttons.setText(_translate("MainWindow", "buttons"))
        self.actiontypes.setText(_translate("MainWindow", "types"))
