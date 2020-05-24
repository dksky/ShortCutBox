from pyqt5.sqlite.orm import *

import json

def installPluginsByJsonFile(jsonfile=''):
    with open(jsonfile, 'r') as f:
        content=f.read()
        pluginContentList = json.loads(content)
        for pluginJson in pluginContentList:
            checkAndInstallPlugin(pluginJson)

def installPluginByJsonFile(jsonfile=''):
    with open(jsonfile, 'r') as f:
        content=f.read()
        pluginJson = json.loads(content)
        checkAndInstallPlugin(pluginJson)

def checkAndInstallPlugin(pluginJson):
    # check whether this plugin is installed
    print("Begin to check whether plugin '" + pluginJson["name"] + "' is installed.")
    pluginList = Plugin.select(fn.COUNT(Plugin.id).alias("num")).where(Plugin.name == pluginJson["name"])
    pluginExist = False
    for p in pluginList:
        pluginExist = p.num > 0
    if not (pluginExist):
        installPlugin(pluginJson)

def installPlugin(pluginJson):
    print("Begin to install plugin '" + pluginJson["name"] + "'")
    pluginId=Plugin.create(name=pluginJson["name"],
                         description=pluginJson["description"],
                         type=pluginJson["type"],
                         isDeleted=False)

    for pluginFuncJson in pluginJson["pluginFuncs"]:
        pluginFuncJson["pluginId"] = pluginId
        installPluginFunc(pluginFuncJson)

def installPluginFunc(pluginFuncJson):
    pluginFuncId=PluginFunc.create(pluginId=pluginFuncJson["pluginId"],
                    name=pluginFuncJson["name"],
                    description=pluginFuncJson["description"],
                    type=pluginFuncJson["type"],
                    commandPrefix=pluginFuncJson["commandPrefix"],
                    commandFile=pluginFuncJson["commandFile"],
                    commandParams=pluginFuncJson["commandParams"],
                    isDeleted=False)
    for pluginFuncFormEleJson in pluginFuncJson["pluginFuncFormEles"]:
        pluginFuncFormEleJson["pluginFuncId"] = pluginFuncId
        installPluginFuncFormEle(pluginFuncFormEleJson)

def installPluginFuncFormEle(pluginFuncFormEleJson):
    pluginFuncFormEle = PluginFuncFormEle()
    pluginFuncFormEle.labelName = pluginFuncFormEleJson["labelName"]
    pluginFuncFormEle.varName = pluginFuncFormEleJson["varName"]
    pluginFuncFormEle.description = pluginFuncFormEleJson["description"]
    pluginFuncFormEle.type = pluginFuncFormEleJson["type"]
    pluginFuncFormEle.json = pluginFuncFormEleJson["json"]
    pluginFuncFormEle.create(pluginFuncId=pluginFuncFormEleJson["pluginFuncId"],
                      labelName=pluginFuncFormEleJson["labelName"],
                      varName=pluginFuncFormEleJson["varName"],
                      description=pluginFuncFormEleJson["description"],
                      type=pluginFuncFormEleJson["type"],
                      json=pluginFuncFormEleJson["json"],
                      isDeleted=False)

if __name__ == '__main__':
    installPluginsByJsonFile('plugins.json')