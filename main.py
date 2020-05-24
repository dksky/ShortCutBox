import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import loginPage

def click_success():
    print("successfully!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = loginPage.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.actionfolders.triggered.connect(click_success)
    sys.exit(app.exec_())