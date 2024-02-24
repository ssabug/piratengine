import sqlite3
import os
from modules.utils import *

class table():
    def __init__(self,data,keys):
        self.data=data;
        self.keys=keys;

class database():
    def __init__(self,path):
        self.path=path;
        self.log('connecting to database ' + path);
        self.connection = sqlite3.connect(path);
        self.log('db total_changes = ' + str(self.connection.total_changes));
        self.cursor=self.connection.cursor();
        self.tables=['Playlist','PlaylistEntity','Track','AlbumArt','ChangeLog','Information','Pack','PerformanceData','PlayListAllChildren','PlaylistAllParent','PlaylistPath','sqlite_sequence'];
        self.readAll();

    def log(self,text,source='ENDB',severity='INFO',sameline=False):
        log(text,source=source,severity=severity,sameline=sameline);
        
    def readAll(self):
        tables=self.tables;
        self.log('Reading database tables ...');
        tableCounter=0;
        for table in tables:
            self.log('  table : '  + table);
            setattr(self,table,self.readTable(table))
            tableCounter+=1;
            #for entry in getattr(self,table).data : self.log(entry);

        self.log('Read ' + str(tableCounter) + ' tables');

    def createPlaylist(self,playlistName):
        playlists=getattr(self,'Playlist',None);
        playlistEntity=getattr(self,'PlaylistEntity',None);
        information=getattr(self,'Information',None);

        if playlists is None:
            self.log('No playlist table found');
        elif playlistEntity is None:
            self.log('No playlistEntity table found');
        else:
            self.log('Creating playlist : ' + playlistName);
            
            #for key in playlists.keys:
            #    self.log(key)

            self.log('Updating Playlist table');
            id=len(playlists.data)+1;
            title=playlistName;
            parentListId=0;
            isPersisted=0;
            nextListId=0;
            lastEditTime=str(datetime.datetime.now())[:-7];
            isExplicitlyExported=0;
            data=tuple([title,parentListId,isPersisted,nextListId,lastEditTime,isExplicitlyExported]);
            self.insertVaribleIntoTable('Playlist',data)            
            self.readAll();
            
            return id;

        return -1;

    def addTrack(self,path):
        self.log('Adding ' + track + ' to database ' );
        filename=os.path.basename(filepath);
        title=filename;
        data=tuple([path,filename])
        self.log('filename:' + filename);
        self.insertVaribleIntoTable('Track',data)

    def addPlaylistEntry(self,playlistName,entryId):
        self.log('Adding ' + entry + ' to playlist ' + playlistName )
        # PlaylistEntity table
        id=len(playlistEntity.data);
        listId=id
        trackId=entryId
        #find your track here
        databaseUuid=information.data[0]['uuid'];
        self.log('Database uuid : ' + str(databaseUuid))
        nextEntityId=0
        membershipReference=0;
        #update previous nextEntityId

    def printPlaylists(self):
        self.log('Reading database available playlists ...');
        self.log(' ')
        playlists=getattr(self,'Playlist',None);

        if playlists is None:
            self.log('No playlist table found');
        else:
            self.log('Playlists :');
            for playlist in playlists.data:
                self.log(playlist['title']);
            self.log('count : '  + str(len(playlists.data)))

    def printPlaylist(self,playlistName):
        self.log('Reading database playlist : ' + playlistName)
        playlists=getattr(self,'Playlist',None);

        if playlists is None:
            self.log('No playlist table found');
        else:
            for playlist in playlists.data:
                if playlist['title'] == playlistName:

                    playlistEntities=getattr(self,'PlaylistEntity',None);

                    if playlistEntities is None:
                        self.log('No playlistEntity table found');
                    else:
                        '''
                        try:
                            searchEntity=next((x for x in self.PlaylistEntity.data if x['listId']==playlist['id']));
                            self.log( searchEntity)
                        except Exception as error:
                            handleErrors(error);
                        '''
                        for entity in self.PlaylistEntity.data:
                            if entity['listId'] == playlist['id']:
                                #self.log(entity);
                                try:
                                    searchTrack=next((x for x in self.Track.data if x['id']==entity['trackId']));
                                    self.log(searchTrack['path'])
                                except Exception as error:
                                    handleErrors(error);

    def readTable(self,tableName):
        cursor=self.cursor;
        #self.log('Database table ' + tableName + ' dump :')

        #self.connection.execute("PRAGMA table_info");
        #self.log('Database table keys: ' + tableName + ' dump :')
        cursor.execute("PRAGMA table_info({})".format(tableName));
        rows = cursor.fetchall()
        keys=[];
        for row in rows:
            #self.log(row);
            keys.append(row[1])

        tableData=[];

        cursor.execute("SELECT * FROM "+tableName);
        rows = cursor.fetchall()
        

        for row in rows:
            #self.log(row);
            tableEntry={};
            for i,key in enumerate(keys):
                tableEntry |= {key : row[i]} 
            #self.log(row);
            #self.log(tableEntry);
            tableData.append(tableEntry);

        return table(tableData,keys);

    def insertVaribleIntoTable(self,table,values):
        tableObj=getattr(self,table,None);
        try:
            for i,key in enumerate(tableObj.keys[1:]):
                if i == 0: QString="?"
                else : QString +=", ?"

            keysString='('+ ', '.join(tableObj.keys[1:]) + ")"#"(id, name, email, joining_date, salary)"
            keysQString="VALUES (" + QString + ");"
            rqst = "INSERT INTO "+ table +" " +keysString +" " + keysQString;

            sqlite_insert_with_param='"""' + rqst +'"""';

            self.cursor.execute(rqst, values)
            self.connection.commit()
            self.log(table  + ' successfully updated')

            #self.cursor.close()

        except Exception as error:
            handleErrors(error);