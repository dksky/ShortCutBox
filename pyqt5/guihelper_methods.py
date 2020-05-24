import tkinter as tk 
from tkinter import ttk 
from PIL import ImageTk
from tkinter import * 
import os 
import subprocess 
import glob 
import shutil
import tkinter.messagebox
from pathlib import Path
from os.path import join
from shutil import copyfile
import sys 
import json
from functools import partial
from tkinter.filedialog import askdirectory
# from guihelper import folder_opener_window

rootWin = None


def callback():
    print("~被调用了~")

def open_explorer(path=r"C:/"):
    print('open '+ path + ' in win explorer.')
    files = os.path.abspath(path)
    path = os.path.realpath(files)
    print( files )
    os.startfile(files)

def bash_opener(path=""):
    print('bash_opener ' + path )
    command = 'cd /d "' + path + '" && start "" "C:/Program Files/Git/git-bash.exe"'
    print( command )
    os.system( command )

def login_win_opener( root ):
    login_window = tk.Toplevel(root)
    login_window.title('登录界面')       # 设置窗口的标题
    login_window.geometry('500x400')     # 设置窗口的大小
    # 画布放在login_window的顶部
    canvas = tk.Canvas(login_window, height=200, width=500)
    canvas.pack(side='top')
    image_file = ImageTk.PhotoImage(file='./screenshot1.png')
    # 以图片中心定位到 (250, 100) 的位置上
    image = canvas.create_image(250, 100, anchor='center', image=image_file)
    # 输入框的提示语
    tk.Label(login_window, text="用户名:").place(x=75, y=250, anchor='nw')
    tk.Label(login_window, text="密码  :").place(x=75, y=280, anchor='nw')

    # 两个输入框
    usr_name_var = tk.StringVar()
    password_var = tk.StringVar()
    tk.Entry(login_window, textvariable=usr_name_var).place(x=150, y=250, anchor='nw')
    tk.Entry(login_window, textvariable=password_var, show='*').place(x=150, y=280, anchor='nw')

    def login():
        user_name = usr_name_var.get()
        messagebox.showinfo(title='登录成功', message="欢迎你， {name}".format(name=user_name))
    tk.Button(login_window, text='登录', command=login).place(x=280, y=350)
    login_window.mainloop()

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def execute_function( name, args1=None ):
    print("Executing the py command: " + name + '.py' )
    if ( name!="" and args1 == None ):
        appPath = r'' + str(name) + '.py'
        print(appPath)
        subprocess.Popen( 'python ' + appPath )

    elif ( name!='' and args1 != None and args1 != ''):
        appPath = r'' + str(name) + '.py ' + str(args1)
        print(appPath)
        subprocess.Popen('python ' + appPath )

    else:
        print('command is empty!')


def script_runner( name,  type,  args1="" ):
    print('abs file name: ' + name )
    appPath = r'' + str(name)
    command = appPath + ' ' + str( args1 )
    if( type == 'exe'):
        subprocess.Popen( command  )
    if( type == ''):
        open_explorer( name )
    if( type == 'python'):
        command = 'python ' + command 
        subprocess.Popen( command )

