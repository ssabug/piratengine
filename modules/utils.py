import datetime
import os
import sys
import shutil
import traceback
import json
import mutagen
from math import floor

def getHomeDir():
    detectedOS=sys.platform.lower();
    homeDirectory=os.path.expanduser("~");
    programConfigDirectory="piratengine";
    configSubDir="";

    if "linux" in detectedOS:
        configSubDir=os.path.join(".config",programConfigDirectory);
    elif detectedOS == "darwin":
        configSubDir=os.path.join("Documents",programConfigDirectory);
    elif "win" in detectedOS :
        configSubDir=os.path.join(".config",programConfigDirectory);

    if configSubDir != "":
        configDirectory=os.path.abspath(os.path.join(homeDirectory,configSubDir));
        return configDirectory;
        
    return None;

if getHomeDir() != None:
    configFilePath=os.path.join(getHomeDir(),"config.json");
    if not os.path.exists(configFilePath):
        configFilePath=os.path.join("data","config.json");
else:
    configFilePath=os.path.join("data","config.json");

def getConfigParameter(section,parameter): 
    f=open(configFilePath);
    data = json.load(f);
    f.close();
    return data[section][parameter];

def setConfigParameter(section,parameter,value):
    f=open(configFilePath);
    data = json.load(f);
    f.close();

    oldValue=getConfigParameter(section,parameter);

    if isinstance(data[section][parameter],list):
        oldValue.append(value);
        newValue=oldValue;
    else:
        newValue=value;

    data[section][parameter]=newValue;

    jsonOutput = json.dumps(data,indent=4);
 
    f=open(configFilePath, "w");
    f.write(jsonOutput, );

def getConfigDirectory():
    global configFilePath;
    detectedOS=sys.platform.lower();
    homeDirectory=os.path.expanduser("~");
    programConfigDirectory="piratengine";
    configSubDir="";

    if "linux" in detectedOS:
        configSubDir=os.path.join(".config",programConfigDirectory);
    elif detectedOS == "darwin":
        configSubDir=os.path.join("Documents",programConfigDirectory);
    elif "win" in detectedOS :
        configSubDir=os.path.join(".config",programConfigDirectory);

    if configSubDir != "":
        configDirectory=os.path.abspath(os.path.join(homeDirectory,configSubDir));
        
        if not os.path.exists(configDirectory):
            print("creating folder : " + configDirectory);
            os.makedirs(configDirectory);
        if not os.path.exists(configDirectory):
            print("error configuration directory not found : " + configDirectory);
            return None;

        homeConfigFilePath=os.path.join(configDirectory,"config.json")
        if not os.path.exists(homeConfigFilePath):
            shutil.copyfile(configFilePath,homeConfigFilePath);
            configFilePath=homeConfigFilePath;
            logFilePathNew=os.path.join(configDirectory,"log.txt");
            setConfigParameter('general','logFile',logFilePathNew);
            setConfigParameter('gui','lastSelectedDBPath',"");
            if "logFile" in globals():
                global logFile;
                logFile=getConfigParameter('general','logFile');

        configFilePath=homeConfigFilePath;
        return configDirectory;
    else:
        return None

debug=getConfigParameter('general','debug');
fileLogging=getConfigParameter('general','fileLogging');
logFile=getConfigParameter('general','logFile');

def log(msg,source='NONE',severity='INFO',sameline=False):  
    
    if not isinstance(msg,str):
        msg=str(msg);

    if isinstance(msg,list) or isinstance(msg,tuple):
        message= str(datetime.datetime.now() ) + ' [ ' + source + ' ] ' + str(msg)
    else:   
        message= str(datetime.datetime.now() ) + ' [ ' + source + ' ] ' + msg
    #if len(message) > 2000:
    #    message = str(datetime.datetime.now() ) + ' [ ' + source + ' ] ' +'Message too long '
    if debug :
        if sameline:
            print (message,end = '')
        else:
            print (message)
    if fileLogging :
            f = open(logFile, "a")  # append mode
            f.write(message + "\n")
            f.close()

    return msg

def handleErrors(error,module="MAIN"):
    log("EXCEPTION " + str(type(error).__name__) + " " + str(error) ,module);
    stack = traceback.extract_stack()[:-3] + traceback.extract_tb(error.__traceback__);  # add limit=?? 
    for i,l in enumerate(stack):
        log(str(stack[len(stack)-1-i]),module) # An error occurred: NameError – name 'x' is not defined

def run_fast_scandir(dir, ext):    # dir: str, ext: list
    subfolders, files = [], []

    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in ext:
                files.append(f.path)


    for dir in list(subfolders):
        sf, f = run_fast_scandir(dir, ext)
        subfolders.extend(sf)
        files.extend(f)
    return subfolders, files

def dateToTimestamp(date):
    return floor(datetime.datetime.timestamp(date));

def getAudioBitrate(path):
    if os.path.exists(path):     
        return (mutagen.File(path).info.bitrate)/1000;
    else:
        log('file not found : ' +path);
    return -1;

def getAudioLength(path):
    if os.path.exists(path):     
        return floor(mutagen.File(path).info.length);
    else:
        log('file not found : ' +path);
    return -1;
