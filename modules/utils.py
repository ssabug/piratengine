import datetime
import os
import traceback
from math import floor
import mutagen

debug=True;
fileLogging=True;
logFile='log.txt';


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