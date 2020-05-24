from pyqt5.sqlite.orm import *

def addApplication(appParams={}):
    applicationId=Application.create(name=appParams["applicationName"],
                       pluginId=appParams["pluginId"],
                       pluginFuncId=appParams["pluginFuncId"],
                       isDeleted=False)
    for configName in appParams["configMap"]:
        configValue=appParams["configMap"][configName]
        ApplicationConfig.create(applicationId=applicationId,
                                 name=configName,
                                 value=configValue,
                                 isDeleted=False)


if __name__ == '__main__':
    appParams = {
        "applicationName": "jump to folder aaa",
        "pluginId": 1,
        "pluginFuncId": 1,
        "configMap": {
            "filePath": "C:\\Users\\liden\\PycharmProjects\\pyGUI\\pyqt5\\sqlite"
        }
    }
    addApplication(appParams)