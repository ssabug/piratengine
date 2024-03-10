import os
import sys
import pathlib

from modules.database import *
from modules.stagelinq import *
from modules.utils import *
from modules.gui import *

class piratengine():
    def __init__(self):
        self.log('###### WELCOME TO PIRATENGINE');
        self.db=None;
        self.gui=None;
        self.stagelinq=None;
               
    def log(self,text,source='PRTE',severity='INFO',sameline=False):
        log(text,source=source,severity=severity,sameline=sameline);

    def menu(self):
        self.log(" ");
        self.log('Available functions');
        self.log('1 - load database');
        self.log('2 - print available playlists');
        self.log('3 - print playlist content');
        self.log('4 - create playlist');
        self.log('5 - add track to playlist (via trackId)');
        self.log('6 - add tracks to playlist (via text file)');
        self.log('7 - export playlist to text file');
        self.log('8 - scan folder and add them to tracks');
        self.log('9 - add individual file to tracks');
        self.log('0 - exit');     

        try:
            choice = int(input('Choose an option\n'));
            match choice:
                case 0:
                    return False;

                case 1:# LOAD DB
                    try:
                        self.db=self.loadDbUI();
                    except:
                        self.db=None;
                    return True;

                case 2:# PRINT PLAYLISTS
                    if self.db is None:
                        self.db=self.loadDbUI();
                    
                    self.db.printPlaylists();
                    return True;

                case 3:# print playlist
                    if self.db is None:
                        self.db=self.loadDbUI();
                    self.db.printPlaylists();
                    self.loadPlaylist(self.db,silent=False);
                    return True;

                case 4:# create playlist
                    if self.db is None:
                        self.db=self.loadDbUI();
                        #self.db.printPlaylists();
                    playlist=input('Enter your new playlist name\n')
                    self.db.createPlaylist(playlist);
                    return True;

                case 5:# add track to playlist
                    if self.db is None:
                        self.db=self.loadDbUI();
                    self.db.printPlaylists();
                    playlist = input('Enter playlist name\n');
                    trackId=int(input('Enter your new playlist item trackId\n'))
                    self.db.addPlaylistEntry(playlist,trackId);
                    return True;

                case 6:# add tracks to playlist from text file
                    if self.db is None:
                        self.db=self.loadDbUI();
                    self.db.printPlaylists();
                    playlist = input('Enter playlist name\n');
                    
                    playlistFile=input('Enter the path to the tracks txt file\n');

                    if os.path.isfile(playlistFile):
                        f= open(playlistFile, 'r');
                        for line in f:
                            trackId=self.db.findTrack(path=line[:-1]);
                            if trackId >=0:
                                self.db.addPlaylistEntry(playlist,trackId);
                            else:
                                self.log('Track not found : ' + line[:-1])
                            #self.log('line : ' + line[:-1])
                        f.close();
                    else:
                        self.log('File not found : ' + playlistFile)

                    return True;

                case 7:# write playlist to txt file
                    if self.db is None:
                        self.db=self.loadDbUI();
                    self.db.printPlaylists();

                    self.loadPlaylist(self.db,True);
                    return True;

                case 8: #scan folder
                    if self.db is None:
                        self.db=self.loadDbUI();
                    path=input('Enter folder path\n');
                    if os.path.exists(path):
                        self.db.addFolderToDatabase(path);
                    else:
                        self.log('Folder does not exist :' + path)
                    return True;

                case 9: #add track
                    if self.db is None:
                        self.db=self.loadDbUI();
                    path=input('Enter full absolute path of file to be added \n');
                    
                    if os.path.exists(path):
                        
                        self.db.addTrack(path);
                    else:
                        self.log('Folder does not exist :' + path)
                    
                    #self.db.addTrack(path);
                    return True;

                case _:
                    self.log('Invalid input');
                    return True;
        except Exception as error:
            handleErrors(error);
            return True;

    def loadDbUI(self):
        path=input('Enter your database path ( .../Engine Library/Database2/ ) \n');
        trackDataBase=self.loadDb(path);
        return trackDataBase;

    
    def loadDb(self,path):
        trackDataBase=database(os.path.join(path,'m.db'));
        return trackDataBase;

    def loadPlaylist(self,db,writeToFile=False,playlist='',silent=True):
        if playlist == '':
            playlist=input('Enter your playlist name\n')
        playlistArray,trackObjectArray=db.printPlaylist(playlist,silent);
        if playlistArray != [] and writeToFile:
            f = open(playlist+'.txt', "w")
            for item in playlistArray:
                f.write(item+'\n');
            f.close()
                               
    def exportPlaylist(self,db,playlistName,outfilePath):
        playlistArray,trackObjectArray=db.printPlaylist(playlistName);
        excludedKeys=['trackData','overviewWaveFormData','beatData','quickCues','loops']
                               
        extension = pathlib.Path(outfilePath).suffix[1:];
                               
        f = open(outfilePath, "w");
                               
        for i,item in enumerate(trackObjectArray):
            path=item['path']                  
            if extension == 'txt':
                f.write(path+'\n');
            
            elif extension == 'json':
                if i == 0 :
                    jsonDict={"playlist" : {'title' : playlistName, 'tracks':[]}}
                
                trackObject={}
                for key in item:
                    if key not in excludedKeys:
                        value=item[key]
                        if not (isinstance(value,int) or isinstance(value,bool) or isinstance(value,float) ) :
                            value=str(value);
                        trackObject |= { key : value}
            
                jsonDict['playlist']['tracks'].append(trackObject);
                                   
            elif extension == 'm3u':
                if i != 0 :
                    f.write('\n');
                f.write('#EXTINF:-1 ' + os.path.basename(path) +'\n');
                f.write(item+'\n');
                               
        if extension == 'json':           
            f.write(json.dumps(jsonDict));
                               
        f.close();

    def importPlaylist(self,path,playlist):
        self.log('Importing playlist file ' + path);

        if os.path.exists(path):
            extension = pathlib.Path(path).suffix[1:];
                               
            f = open(path, "r");

            if extension == 'txt':
                for line in f:
                    self.log(self.db.addTrackToPlaylist(playlist,trackPath=line[:-1]));

            elif extension == 'json':
                playlistDict=json.load(f);
                for track in playlistDict['playlist']['tracks']:
                    self.log(self.db.addTrackToPlaylist(playlist,trackPath=track['path']));

            elif extension == 'm3u':
                for line in str(f.read()).split('#EXTINF'):
                    for l in line.split('\n'):
                        if ":" not in l and l != '':
                            self.log(self.db.addTrackToPlaylist(playlist,trackPath=l));
            
            f.close();

            self.log('Importing file to playlist ended :' + path)
        else:
            self.log('File does not exist :' + path)
        
    
    def trackInPlaylist(self,track,playlist):
        if self.db != None:
            for track in trackDataBase:
                if track['path'] == trackPath:
                    return True;
        return False

    def startStagelinq(self):
        if self.stagelinq != None:
            del self.stagelinq;
        
        self.log('Starting stagelinq');
        self.stagelinq=stagelinq(self);

    def stagelinqNewData(self):
        self.gui.stagelinqUpdateData();

    def initGui(self):
        self.gui=GUI(self);

    def close(self):
        self.log('Exiting program ... ');
        if self.stagelinq != None:
            self.log('Stopping StageLinQ')
            #self.stagelinq.thread.close();
            #self.stagelinq.thread.join(1);
            del self.stagelinq;

        self.log('Program terminated');
        exit()

def printHelp():
    print('Usage :');
    print('python piratengine.py --option');
    print('option :');
    print('--nogui  : Disables Qt GUI');
    print('--help   : Prints this text');

def main():
    inputArgs=sys.argv

    if len(inputArgs)>1:
        option=inputArgs[1];

        if '--nogui' in inputArgs:
            useGui=False;
        else:
            useGui=True;

        if option != "--nogui":
            printHelp();
            exit();

    p=piratengine();

    if useGui:
        p.initGui();
    else:
        while p.menu():
            a=True

    p.close();


main()
        


