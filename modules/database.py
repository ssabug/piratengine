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
        
    def readAll(self,silent=False):
        tables=self.tables;
        self.log('Reading database tables ...');
        tableCounter=0;
        for table in tables:
            if not silent: self.log('  table : '  + table);
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
            self.insertVariableIntoTable('Playlist',data)            
            self.readAll(True);
            
            return id;

        return -1;

    def addTrack(self,path):
        self.log('Adding ' + track + ' to database ' );
        filename=os.path.basename(filepath);
        title=filename;
        data=tuple([path,filename])
        self.log('filename:' + filename);
        self.insertVariableIntoTable('Track',data)

    def getPlaylistEntities(self,playlistName):
        playlist=self.findPlaylist(playlistName);
        playlistEntities=getattr(self,'PlaylistEntity',None);
        entityList=[];
        if playlistEntities is None:
            self.log('No playlistEntity table found');
        else:
            
            for entity in self.PlaylistEntity.data:
                if entity['listId'] == playlist['id']:
                    entityList.append(entity);
        return entityList;
                    

    def findPlaylist(self,playlistName):
        playlists=getattr(self,'Playlist',None);
        if playlists is None:
            self.log('No playlist table found');
        else:
            for playlist in playlists.data:
                if playlist['title'] == playlistName:
                    return playlist;
        return None
    
    def findTrack(self,path='',trackId=-1):
        tracks=getattr(self,'Track',None);
        for track in tracks.data:
            if track['path'] == path and path != '':
                return track['id'];
            elif track['id'] == trackId and trackId >=0:
                return track['id'];
        return -1;

    def addPlaylistEntry(self,playlistName,entryId):
        playlist=self.findPlaylist(playlistName);

        if playlist != None:
            information=getattr(self,'Information',None);

            if information is not None:
                self.log('Adding ' + str(entryId) + ' to playlist ' + playlistName )
                listId=playlist['id'];
                databaseUuid=information.data[0]['uuid'];
                #self.log('Database uuid : ' + str(databaseUuid))
                nextEntityId=0;
                membershipReference=0;
                trackId=self.findTrack(trackId=entryId);
                if trackId >= 0:
                    data=tuple([listId,trackId,databaseUuid,nextEntityId,membershipReference]);
                    self.insertVariableIntoTable('PlaylistEntity',data);
                    self.readAll(True);
                    entityList=self.getPlaylistEntities(playlistName);
                    if len(entityList) >1:
                        idToUpdate=entityList[len(entityList)-2]['id'];
                        #self.log('id to be updated : ' + str(idToUpdate))
                        
                        for item in getattr(self,'sqlite_sequence',None).data:
                            if item['name'] == 'PlaylistEntity':
                                valueToUpdate=item['seq'];
                                #self.log('value to be put : ' + str(valueToUpdate))
                        rqst = "UPDATE PlaylistEntity SET nextEntityId = ? WHERE id = ?";
                        self.cursor.execute(rqst, (valueToUpdate,idToUpdate));
                        self.connection.commit();
                else:
                    self.log('Trackid not found ' + str(entryId))     
                #find your track here
                
                
                
                #update previous nextEntityId

    def printPlaylists(self):
        self.log('Reading database available playlists ...');
        self.log(' ')
        playlists=getattr(self,'Playlist',None);
        out=[]
        if playlists is None:
            self.log('No playlist table found');
        else:
            self.log('Playlists :');
            for playlist in playlists.data:
                self.log(playlist['title']);
                out.append(playlist['title']);
            self.log('count : '  + str(len(playlists.data)))

        return out

    def printPlaylist(self,playlistName):
        self.log('Reading database playlist : ' + playlistName)
        playlists=getattr(self,'Playlist',None);
        out=[]
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
                                    out.append(searchTrack['path']);
                                except Exception as error:
                                    handleErrors(error);
        return out;

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

    def insertVariableIntoTable(self,table,values):
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