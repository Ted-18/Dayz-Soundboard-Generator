import shutil
import json
import os
from os.path import exists
from datetime import datetime

addon_name = "OBF_EA_SoundManager_Sounds"

def init():
    FileManager.createFolder("Import")
    FileManager.createFolder("Export")
    FileManager.createFolder("Export/sounds")
    SoundManagerGenerator.playerSoundSets()
    SoundManagerGenerator.positionSoundShader()
    SoundManagerGenerator.positionSoundSet()
    SoundManagerGenerator.profile()
    SoundManagerGenerator.copyFile()
    

class SoundManagerGenerator:
    def playerSoundSets():
        #VERIFICATION
        if os.path.exists("Export/playerSoundSets.cpp"):
            Logger.error("Export/playerSoundSets.cpp already exist!")
            return
        
        Logger.info("Creation of playerSoundSets...")
        Logger.debug("playerSoundSets file initialisation...")
        
        #FILE START
        FileManager.fileWrite("Export/playerSoundSets.cpp", "    //==========================================")
        FileManager.fileWrite("Export/playerSoundSets.cpp", "    //              playerSoundSets")
        FileManager.fileWrite("Export/playerSoundSets.cpp", "    //==========================================")
        
        Logger.debug("playerSoundSets file initialised")
        
        for folder in os.listdir("Import"):
            Logger.debug("Folder " + folder + "M")
            for file in os.listdir("Import/" + folder):
                Logger.debug("Creation of " + file + " playerSoundSets")
                
                FileManager.fileWrite("Export/playerSoundSets.cpp", "    class " + file[:-4] + "_" + folder + "M : default")
                FileManager.fileWrite("Export/playerSoundSets.cpp", "    {")
                FileManager.fileWrite("Export/playerSoundSets.cpp", "        sound[]=")
                FileManager.fileWrite("Export/playerSoundSets.cpp", "        {")
                FileManager.fileWrite("Export/playerSoundSets.cpp", "            \"" + addon_name + "\\sounds\\" + file[:-4] + "_" + folder + "M\",")
                FileManager.fileWrite("Export/playerSoundSets.cpp", "            1,")
                FileManager.fileWrite("Export/playerSoundSets.cpp", "            1,")
                FileManager.fileWrite("Export/playerSoundSets.cpp", "            1000")
                FileManager.fileWrite("Export/playerSoundSets.cpp", "        };")
                FileManager.fileWrite("Export/playerSoundSets.cpp", "    };")
                
                Logger.debug("Creation of " + file + " playerSoundSets done")
                
        Logger.info("Creation of playerSoundSets done")
    
        
        
        
    def positionSoundShader():
        #VERIFICATION
        if os.path.exists("Export/positionSoundShader.cpp"):
            Logger.error("Export/positionSoundShader.cpp already exist!")
            return
        
        Logger.info("Creation of positionSoundShader...")
        Logger.debug("positionSoundShader file initialisation...")
        
        #FILE START
        FileManager.fileWrite("Export/positionSoundShader.cpp", "    //==========================================")
        FileManager.fileWrite("Export/positionSoundShader.cpp", "    //              positionSoundShader")
        FileManager.fileWrite("Export/positionSoundShader.cpp", "    //==========================================")
        
        Logger.debug("positionSoundShader file initialised")
        
        for folder in os.listdir("Import"):
            Logger.debug("Folder " + folder + "M")
            #DISTANCE START
            FileManager.fileWrite("Export/positionSoundShader.cpp", "    //==========================================")
            FileManager.fileWrite("Export/positionSoundShader.cpp", "    //              Sounds " + folder + "M")
            FileManager.fileWrite("Export/positionSoundShader.cpp", "    //==========================================")
            
            for file in os.listdir("Import/" + folder):
                Logger.debug("Creation of " + file + " positionSoundShader")
                
                FileManager.fileWrite("Export/positionSoundShader.cpp", "    class " + file[:-4] + "_" + folder + "M_SoundShader")
                FileManager.fileWrite("Export/positionSoundShader.cpp", "    {")
                FileManager.fileWrite("Export/positionSoundShader.cpp", "        samples[]=")
                FileManager.fileWrite("Export/positionSoundShader.cpp", "        {")
                FileManager.fileWrite("Export/positionSoundShader.cpp", "            {")
                FileManager.fileWrite("Export/positionSoundShader.cpp", "                \"" + addon_name + "\\sounds\\" + file[:-4] + "_" + folder + "M\",")
                FileManager.fileWrite("Export/positionSoundShader.cpp", "                1")
                FileManager.fileWrite("Export/positionSoundShader.cpp", "            }")
                FileManager.fileWrite("Export/positionSoundShader.cpp", "        };")
                FileManager.fileWrite("Export/positionSoundShader.cpp", "        volume=1;")
                FileManager.fileWrite("Export/positionSoundShader.cpp", "        range=5;")
                FileManager.fileWrite("Export/positionSoundShader.cpp", "        rangeCurve[]=")
                FileManager.fileWrite("Export/positionSoundShader.cpp", "        {")
                
                Calculator.soundShader(folder)
                    
                FileManager.fileWrite("Export/positionSoundShader.cpp", "        };")
                FileManager.fileWrite("Export/positionSoundShader.cpp", "    };")
                Logger.debug("Creation of " + file + " positionSoundShader done")
        
        Logger.info("Creation of positionSoundShader done")
        
        
        
    def positionSoundSet():
        #VERIFICATION
        if os.path.exists("Export/positionSoundSet.cpp"):
            Logger.error("Export/positionSoundSet.cpp already exist!")
            return
        
        Logger.info("Creation of positionSoundSet...")
        Logger.debug("positionSoundSet file initialisation...")
        
        #FILE START
        FileManager.fileWrite("Export/positionSoundSet.cpp", "    //==========================================")
        FileManager.fileWrite("Export/positionSoundSet.cpp", "    //              positionSoundSet")
        FileManager.fileWrite("Export/positionSoundSet.cpp", "    //==========================================")
        
        Logger.debug("positionSoundSet file initialised")
        
        for folder in os.listdir("Import"):
            Logger.debug("Folder " + folder + "M")
            #DISTANCE START
            FileManager.fileWrite("Export/positionSoundSet.cpp", "    //==========================================")
            FileManager.fileWrite("Export/positionSoundSet.cpp", "    //              Sounds " + folder + "M")
            FileManager.fileWrite("Export/positionSoundSet.cpp", "    //==========================================")
            
            for file in os.listdir("Import/" + folder):
                Logger.debug("Creation of " + file + " positionSoundSet")
                
                FileManager.fileWrite("Export/positionSoundSet.cpp", "    class " + file[:-4] + "_" + folder + "M")
                FileManager.fileWrite("Export/positionSoundSet.cpp", "    {")
                FileManager.fileWrite("Export/positionSoundSet.cpp", "        soundShaders[]=")
                FileManager.fileWrite("Export/positionSoundSet.cpp", "        {")
                FileManager.fileWrite("Export/positionSoundSet.cpp", "            \"" + file[:-4] + "_" + folder + "M_SoundShader\"")
                FileManager.fileWrite("Export/positionSoundSet.cpp", "        };")
                FileManager.fileWrite("Export/positionSoundSet.cpp", "        volumeFactor=1.4;")
                FileManager.fileWrite("Export/positionSoundSet.cpp", "        volumeCurve=\"InverseSquare2Curve\";")
                FileManager.fileWrite("Export/positionSoundSet.cpp", "        spatial=1;")
                FileManager.fileWrite("Export/positionSoundSet.cpp", "        doppler=1;")
                FileManager.fileWrite("Export/positionSoundSet.cpp", "        loop=1;")
                FileManager.fileWrite("Export/positionSoundSet.cpp", "        sound3DProcessingType=\"ExplosionMedium3DProcessingType\";")
                FileManager.fileWrite("Export/positionSoundSet.cpp", "        distanceFilter=\"explosionDistanceFreqAttenuationFilter\";")
                FileManager.fileWrite("Export/positionSoundSet.cpp", "    };")
                
                Logger.debug("Creation of " + file + " positionSoundSet done")
        


        Logger.info("Creation of positionSoundSet done")
        
        
        
    def profile():
        if os.path.exists("Export/profil.json"):
            Logger.error("Export/profil.json already exist!")
            return
        
        Logger.info("Creation of profile file...")
        SoundsLists = {}
        Sounds = []
        
        for folder in os.listdir("Import"):
            Logger.debug("Folder " + folder + "M")
            for file in os.listdir("Import/" + folder):
                Sounds.append(file[:-4] + "_" + folder + "M")

        Sounds.sort()
        SoundsLists["SoundsLists"] = Sounds        
        FileManager.jsonWrite("Export/profil.json", SoundsLists)
        Logger.info("Creation of profile file done")
    
    
    
    def copyFile():
        for folder in os.listdir("Import"):
            for file in os.listdir("Import/" + folder):
                shutil.copyfile("Import/" + folder + "/" + file, "Export/sounds/" + file[:-4] + "_" + folder +"M.ogg")



class Calculator:
    def soundShader( val):  
        
        val = int(val)
        num = 0
        
        FileManager.fileWrite("Export/positionSoundShader.cpp", "            {0,1},")

        while num < int(val):
            num = num + 25
            if num < val:
                FileManager.fileWrite("Export/positionSoundShader.cpp", "            {" + str(num) + ",1},")
            else:
                if num == val:
                    FileManager.fileWrite("Export/positionSoundShader.cpp", "            {" + str(num) + ",1}")
                else:
                    FileManager.fileWrite("Export/positionSoundShader.cpp", "            {" + str(val) + ",1}")


class FileManager:
    def fileWrite(file, message):
        fileWrited = open(file, "a")
        fileWrited.write("\n" + message)
        fileWrited.close()
    
    def jsonWrite(file, array):
        fileWrited = open(file, "w")
        json.dump(array, fileWrited, indent=4, sort_keys=True)
        fileWrited.close()
        
    def createFolder(folderName):
        if not os.path.exists(folderName):
            Logger.info(folderName + " folder does not exist")
            try:
                os.mkdir(folderName)
                Logger.info(folderName + " folder was created")
            except:
                Logger.error("Unable to create the folder")
        else:
            Logger.info(folderName + " folder exist")
    
    def createFile(fileName):
        if not exists(fileName):
            Logger.info(fileName + " does not exist")
            try:
                os.mkdir(fileName)
                Logger.info(fileName + " was created")
            except:
                Logger.error("Unable to create the file")
        else:
            Logger.info(fileName + " exist")
        

class Logger:
    
    #0 debug
    #1 info
    #2 warn
    #3 error
    #4 fatal

    logLevel = 1

    def debug(error):
        if Logger.logLevel == 0:
            message = "[DEBUG] " + Time.getHMS() + " " + error
            print(message)
            FileManager.fileWrite(Time.getYMD() + " " + "logs.log", message)
            
    def info(error):
        if Logger.logLevel <= 1:
            message = "[INFO] " + Time.getHMS() + " " + error
            print(message)
            FileManager.fileWrite(Time.getYMD() + " " + "logs.log", message)
    
    def warn(error):
        if Logger.logLevel <= 2:
            message = "[WARN] " + Time.getHMS() + " " + error
            print(message)
            FileManager.fileWrite(Time.getYMD() + " " + "logs.log", message)
            
    def error(error):
        if Logger.logLevel <= 3:
            message = "[ERROR] " + Time.getHMS() + " " + error
            print(message)
            FileManager.fileWrite(Time.getYMD() + " " + "logs.log", message)
    
    def fatal(error):
        if Logger.logLevel <= 4:
            message = "[FATAL] " + Time.getHMS() + " " + error
            print(message)
            FileManager.fileWrite(Time.getYMD() + " " + "logs.log", message)


class Time:
    def getHMS():
        now = datetime.now()
        date_time_str = now.strftime("%H:%M:%S")
        return date_time_str
    
    def getYMD():
        now = datetime.now()
        date_time_str = now.strftime("%Y-%m-%d")
        return date_time_str

init()