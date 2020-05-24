
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



def as_buttonconfig_convertor(dct):
    return ButtonConfigModel(dct['text'],dct['command'],dct['args'])

class ButtonConfigModel:
    def __init__(self, name, command, args ):
        self.text = name
        self.command = command
        self.args = args

folderJson = []
folder_json_file_location = Path(__file__).absolute().parent
file_location = folder_json_file_location/"config/folder_config.json"

with open( file_location , 'r', encoding='UTF-8' ) as f :
    folder_ListJson = json.loads( f.read() )
    folder_ListJson = str( folder_ListJson ).replace("'",'"')

bashJson = []
bash_json_file_location = Path(__file__).absolute().parent
file_location = bash_json_file_location/"config/bash_config.json"

with open( file_location , 'r', encoding='UTF-8' ) as f :
    bash_ListJson = json.loads( f.read() )
    bash_ListJson = str( bash_ListJson ).replace("'",'"')

scriptJson = []
script_json_file_location = Path(__file__).absolute().parent
file_location = script_json_file_location/"config/script_config.json"

with open( file_location , 'r', encoding='UTF-8' ) as f :
    script_ListJson = json.loads( f.read() )
    script_ListJson = str( script_ListJson ).replace("'",'"')


tab1ButtonJson = '[{"text":"AI female Folder","command":"E:/GAME/illusion_AI/v0.3/ScrewThisNoise_AI-ShoujoR3/UserData/chara/female","args":""},{"text":"IDE Folder","command":"E:/IDE","args":""},{"text":"Efficiency Folder","command":"C:/Efficiency","args":""},{"text":"SkyrimLE Folder","command":"C:/Temp/SkyrimLE","args":""},{"text":"Udemy Courses Folder","command":"E:/TuT/UdemyCourse2020/courses","args":""}]'
tab1ButtonList = json.loads( folder_ListJson , object_hook = as_buttonconfig_convertor )

tab2ButtonJson = '[{"text":"scrapy folder bash","command":"E:/localhost/virtualenv/scrapyTest","args":""},{"text":"gnatt chart bash","command":"E:/localhost/nodeP/diy/angular-gantt-chart","args":""},{"text":"SkyrimLE script source bash","command":"C:/Temp/SkyrimLE/ModOrganizer/overwrite/scripts/Source","args":""},{"text":"scrapy-skyrim-mod","command":"E:/localhost/nodeP/angularApps/scrapy-skyrim-mod","args":""},{"text":"Efficiency folder bash","command":"C:/Efficiency","args":""}]'
tab2ButtonList = json.loads( bash_ListJson , object_hook = as_buttonconfig_convertor )

tab3ButtonJson = '[{"text":"pudding 512GB plan check usage","command":"autologinPudding","args":"512"},{"text":"pudding 256GB plan check usage","command":"autologinPudding","args":"256"},{"text":"Aliyun dashboard","command":"autologinAliyunCloud","args":" "},{"text":"Vultr dashboard","command":"autologinVultr","args":" "}]'
tab3ButtonList = json.loads( script_ListJson , object_hook = as_buttonconfig_convertor )


def add_new_FolderButton( name, command, args , cb ):
    # adding new folder 
    Btn = ButtonConfigModel( name , command , args )
    print( Btn.text + "\n" ) 
    print( Btn.command ) 
    tab1ButtonList.append( Btn )
    print( len( tab1ButtonList ) )
    cb()

def add_new_FileButton( name, command, args, cb ):
    Btn = ButtonConfigModel( name , command , args )
    print( Btn.text + "\n" ) 
    print( Btn.command ) 
    print( Btn.args )

    filename, file_extension = os.path.splitext( Btn.command)
    print('filename: ' + filename + ' | extension: ' + file_extension )
    tab3ButtonList.append( Btn )


    print( len( tab3ButtonList ) )
    cb()

def ButtonConfig2Json( obj ):
    return { 
        "text": obj.text, 
        "command": obj.command, 
        "args": obj.args 
    }


def save_FolderJson():

    jsonStr = json.dumps( tab1ButtonList, default=ButtonConfig2Json, indent=4 )
    with open('config/folder_config.json', 'w', encoding='utf-8') as f:
        f.write( jsonStr )
    
    jsonStr = json.dumps( tab2ButtonList, default=ButtonConfig2Json, indent=4 )
    with open('config/bash_config.json', 'w', encoding='utf-8') as f:
        f.write( jsonStr )

    jsonStr = json.dumps( tab3ButtonList, default=ButtonConfig2Json, indent=4 )
    with open('config/script_config.json', 'w', encoding='utf-8') as f:
        f.write( jsonStr )
