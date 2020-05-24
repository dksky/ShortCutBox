from pyqt5.sqlite.orm import *

def init():
    if not(Menu.table_exists()):
        Menu.create_table()
        Menu.create(name='Home',
                    description='This is the homepage.',
                    isLeaf=True,
                    isSystemMenu=True,
                    order=1,
                    isDeleted=False)
        Menu.create(name='Plugins',
                    description='This is the Plugins Market.',
                    isLeaf=True,
                    isSystemMenu=True,
                    order=10000,
                    isDeleted=False)

    if not(Folder.table_exists()):
        Folder.create_table()
    if not (Plugin.table_exists()):
        Plugin.create_table()
    if not (PluginFunc.table_exists()):
        PluginFunc.create_table()
    if not (PluginFuncFormEle.table_exists()):
        PluginFuncFormEle.create_table()
    if not (Application.table_exists()):
        Application.create_table()
    if not (ApplicationConfig.table_exists()):
        ApplicationConfig.create_table()


if __name__ == '__main__':
    init()