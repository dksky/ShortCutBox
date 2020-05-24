import zipfile
import os,shutil

def copyZip(srcfile, distfile):
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(distfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.copyfile(srcfile,distfile)
        print ("copy %s -> %s"%( srcfile,distfile))

def writeZip(zipFile, fromDir):
    with zipfile.ZipFile(zipFile, mode='w') as zipf:
       zipf.write('../plugins/launch/launchTest.py')
       zipf.write('../plugins/launch/plugins.json')
    zipf = zipfile.ZipFile(zipFile)
    print (zipf.namelist())

def extract(zipFile, targetDir):
    zipf = zipfile.ZipFile(zipFile)
    if not(os.path.isdir(targetDir)):
        os.mkdir(targetDir)
    zipf.extractall(targetDir) #extract all file to channel1 dir

def handleSelectedPlugin(pluginName, pluginPath):
    copiedToPath="../plugins/" + pluginName + ".zip"
    copyZip(pluginPath, copiedToPath)
    zipFIleName = os.path.basename(copiedToPath)
    targetDir = "../plugins/" + zipFIleName.split(".")[0]
    extract(copiedToPath, targetDir)


if __name__ == '__main__':
    srcPath = "C:\\Users\\liden\\PycharmProjects\\pyGUI\\launch111.zip"
    handleSelectedPlugin("launch", srcPath)
    #C:\\Users\\liden\\PycharmProjects\\pyGUI
    #writeZip(zipFile="../plugins/launch.zip", fromDir="C:\\Users\\liden\\PycharmProjects\\pyGUI\\pyqt5\\plugins\\launch")