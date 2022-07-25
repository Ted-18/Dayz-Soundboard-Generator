from copy import copy
from crypt import methods
from glob import glob
from http.client import SWITCHING_PROTOCOLS
import json
from mimetypes import init
import os
from os.path import exists
import shutil
import string
from datetime import datetime


def init():
    FileManager.createFolder("Import")
    FileManager.createFolder("Export")
    

class FileManager:
    def createFolder(folderName):
        if not os.path.exists(folderName):
            Logger.setInfo(folderName + " folder does not exist")
            try:
                os.mkdir(folderName)
                Logger.setInfo(folderName + " folder was created")
            except:
                Logger.setError("Unable to create the file")
        else:
            Logger.setInfo(folderName + " folder exist")


class Logger:
    
    #0 trace
    #1 debug
    #2 info
    #3 warn
    #4 error
    #5 fatal

    logLevel = 2

    def setTrace(error):
        if Logger.logLevel == 0:
            print("[TRACE]" , Logger.getDate() , error)
            
    def setDebug(error):
        if Logger.logLevel <= 1:
            print("[DEBUG]" , Logger.getDate() , error)

    def setInfo(error):
        if Logger.logLevel <= 2:
            print("[INFO]" , Logger.getDate() , error)
    
    def setWarn(error):
        if Logger.logLevel <= 3:
            print("[WARN]" , Logger.getDate() , error)
            
    def setError(error):
        if Logger.logLevel <= 4:
            print("[ERROR]" , Logger.getDate() , error)
    
    def setFatal(error):
        if Logger.logLevel <= 5:
            print("[FATAL]" , Logger.getDate() , error)
            
    def getDate():
        now = datetime.now()
        date_time_str = now.strftime("%H:%M:%S")
        return date_time_str

init()