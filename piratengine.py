import os

from modules.playlist import *
from modules.database import *
from modules.utils import *

class piratengine():
    def __init__(self):
        self.log('###### WELCOME TO PIRATENGINE');
        self.db=None;
        
        
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
        self.log('0 - exit');     

        try:
            choice = int(input('Choose an option\n'));
            match choice:
                case 0:
                    return False;

                case 1:# LOAD DB
                    try:
                        self.db=self.loadDb();
                    except:
                        self.db=None;
                    return True;

                case 2:# PRINT PLAYLISTS
                    if self.db is None:
                        self.db=self.loadDb();
                    
                    self.db.printPlaylists();
                    return True;

                case 3:# print playlist
                    if self.db is None:
                        self.db=self.loadDb();
                        self.db.printPlaylists();

                    self.loadPlaylist(self.db);
                    return True;

                case 4:# create playlist
                    if self.db is None:
                        self.db=self.loadDb();
                        #self.db.printPlaylists();
                    playlist=input('Enter your new playlist name\n')
                    self.db.createPlaylist(playlist);
                    return True;

                case 5:# add track to playlist
                    if self.db is None:
                        self.db=self.loadDb();
                        self.db.printPlaylists();
                    playlist = input('Enter playlist name\n');
                    trackId=int(input('Enter your new playlist item trackId\n'))
                    self.db.addPlaylistEntry(playlist,trackId);
                    return True;

                case 6:# add tracks to playlist from text file
                    if self.db is None:
                        self.db=self.loadDb();
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

                case _:
                    self.log('Invalid input');
                    return True;
        except Exception as error:
            handleErrors(error);
            return True;

    def loadDb(self):
        path=input('Enter your database path ( .../Engine Library/Database2/ ) \n');
        trackDataBase=p.loadDatabase(path);
        return trackDataBase;

    def loadPlaylist(self,db):
        playlist=input('Enter your playlist name\n')
        playlistArray=db.printPlaylist(playlist);
        if playlistArray != []:
            f = open(playlist+'.txt', "w")
            for item in playlistArray:
                f.write(item+'\n');
            f.close()

    def loadDatabase(self,path):
        return database(path+'m.db');

p=piratengine();

while p.menu():
    a=True

