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

                case 3:# PRINT PLAYLIST
                    if self.db is None:
                        self.db=self.loadDb();
                        self.db.printPlaylists();

                    self.loadPlaylist(self.db);
                    return True;
                case _:
                    self.log('Invalid input');
                    return True;
        except Exception as error:
            handleErrors(error);
            return True;

    def loadDb(self):
        path=input('Enter your database path\n');
        trackDataBase=p.loadDatabase(path);
        return trackDataBase;

    def loadPlaylist(self,db):
        playlist=input('Enter your playlist name\n')
        db.printPlaylist(playlist);

    def loadDatabase(self,path):
        return database(path+'m.db');

p=piratengine();

while p.menu():
    a=True
