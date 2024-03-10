import sys
import inspect
import pathlib
#from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtWidgets

from modules.utils import *
from modules.mainGui import Ui_MainWindow

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,QTimer,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget,QFileDialog,QMessageBox,QInputDialog,QTabWidget,QSpacerItem,
    QLineEdit,
    QTextEdit, QVBoxLayout, QWidget)

class GUI():
    def __init__(self,piratengine):
        '''
        loader = QUiLoader();
        app = QtWidgets.QApplication(sys.argv);
        window = loader.load("modules/main.ui", None);
        window.show();
        app.exec();
        '''
        
        self.log('Initialisation start')
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = MainWindow(piratengine)
        self.window.show()
        self.app.exec()

    def log(self,text,source='GUID',severity='INFO',sameline=False):
        log(text,source=source,severity=severity,sameline=sameline);

    
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):#(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self,piratengine):
            '''
            loader = QUiLoader();
            self = loader.load("modules/main.ui", None);
            for name, obj in inspect.getmembers(MainWindowCustomCode):
                
                if inspect.isfunction(obj) and name != '__init__':
                    setattr(self, name, obj)
            
            self.piratengine=piratengine;
            self.piratengine.gui=self;        
           
            self.initCallbacks(self);

            '''
            super(MainWindow, self).__init__()
            self.setupUi(self);
            for name, obj in inspect.getmembers(MainWindowCustomCode):
                
                if inspect.isfunction(obj) and name != '__init__':
                    setattr(MainWindow, name, obj)
            
            self.piratengine=piratengine;
            self.piratengine.gui=self;        
           
            self.initCallbacks();
            
                   

class MainWindowCustomCode():
    def __init__(self):
        a=True

    def log(self,text,source='GUIM',severity='INFO',sameline=False):
            log(text,source=source,severity=severity,sameline=sameline);

    def initCallbacks(self):
        self.DBLoadButton.clicked.connect(self.DBLoadButton_click);
        self.ScanFolderButton.clicked.connect(self.ScanFolderButton_click);
        self.PlaylistTable.itemSelectionChanged.connect(self.loadPlaylistContents);
        self.CreatePlaylistButton.clicked.connect(self.CreatePlaylistButton_click);
        self.AddTrackToPlaylistButton.clicked.connect(self.AddTrackToPlaylistButton_click);
        self.DBPathTextEdit.setHtml(getConfigParameter("gui","lastSelectedDBPath"));
        self.ExportPlaylistButton.clicked.connect(self.ExportPlaylistButton_click);
        self.ImportFilesButton.clicked.connect(self.ImportFilesButton_click);
        self.DBChooseDirButton.clicked.connect(self.DBChooseDirButton_click);
        self.ImportToPlaylistButton.clicked.connect(self.ImportToPlaylistButton_click);
        self.stagelinqStartButton.clicked.connect(self.stagelinqStartButton_click);
        self.stagelinqDataFilter.textChanged.connect(self.stagelinqUpdateData);
        self.BackupDBButton.clicked.connect(self.BackupDBButton_clicked);
        self.TrackFilter.textChanged.connect(self.TrackTableFilter_textChanged);
        self.PlaylistFilter.textChanged.connect(self.PlaylistTableFilter_textChanged);7
        self.FilesFilter.textChanged.connect(self.FilesFilter_textChanged);
        self.PlaylistContentFilter.textChanged.connect(self.PlaylistContentFilter_textChanged);
        self.TrackTable.itemSelectionChanged.connect(self.TrackTable_selectionChanged);
        self.FilesTable.itemSelectionChanged.connect(self.FilesTable_selectionChanged);
        self.actionLoad_database.triggered.connect(self.DBLoadButton_click);

        self.BackupDBButton.setEnabled(False);
        self.CreatePlaylistButton.setEnabled(False);
        self.AddTrackToPlaylistButton.setEnabled(False);
        self.ImportToPlaylistButton.setEnabled(False)
        self.ExportPlaylistButton.setEnabled(False);
        self.ImportFilesButton.setEnabled(False);
        self.ScanFolderButton.setEnabled(False);

        keys=['key','value'];
        self.stagelinqTable.setColumnCount(len(keys));
        self.stagelinqTable.setHorizontalHeaderLabels(keys);
        
        self.stagelinqTable.setColumnWidth(0,1000/len(keys))#self.stagelinqTable.width()
        self.stagelinqTable.setColumnWidth(1,1000/len(keys))#self.stagelinqTable.width()

    def TrackTable_selectionChanged(self):
        selectedPlaylist=self.PlaylistTable.selectedIndexes();
        selectedTracks=self.TrackTable.selectedIndexes();
        
        #for e in selectedTracks:
        #    self.log(e.siblingAtColumn(0).data())
            #self.log(self.TrackTable.itemAt(e,0).text());

        if selectedPlaylist != [] and selectedTracks != []: #and self.PlaylistFilter.text() == '' and self.TrackFilter.text() == '':
            self.AddTrackToPlaylistButton.setEnabled(True);
        else:
            self.AddTrackToPlaylistButton.setEnabled(False);

    def FilesTable_selectionChanged(self):
        selectedFiles=self.FilesTable.selectedIndexes();

        if len(selectedFiles) > 0:# and self.FilesFilter.text() == '':
            self.ImportFilesButton.setEnabled(True);
        else:
            self.ImportFilesButton.setEnabled(False);


    def nonBlockingPopup(self,title,text):
        msgBox=QMessageBox(self);
        msgBox.setWindowTitle(title);
        msgBox.setText(text);
        msgBox.setStandardButtons(QMessageBox.StandardButtons());
        msgBox.setWindowModality(Qt.NonModal)
        msgBox.show();
        msgBox.update();
    
        return msgBox;

    def nonBlockingPopupUpdate(self,msgBox,title='',text=''):
        if title != '' :
            msgBox.setWindowTitle(title);
        if text != '':
            msgBox.setText(text);   
        msgBox.update();
        msgBox.show();

    def nonBlockingPopupClose(self,popup):
        popup.accept();
        popup.close();

    def DBChooseDirPopup(self):
        databasePath = str(QFileDialog.getExistingDirectory(self, "Select Database2 folder"));
        self.DBPathTextEdit.setHtml(databasePath);
        self.log(databasePath);
        return databasePath

    def DBChooseDirButton_click(self):
        self.log('Choose Database path clicked');
        databasePath=self.DBChooseDirPopup();

        self.DBLoadButton_click();


    def DBLoadButton_click(self):
        print(str(type(self)))
        self.log('Load Database clicked');
        databasePath=self.DBPathTextEdit.toPlainText();

        if databasePath == '' :
            databasePath=self.DBChooseDirPopup();
        
        if os.path.exists(databasePath):
            
            popup=self.nonBlockingPopup("Please wait","Database is loading...");

            self.piratengine.db=self.piratengine.loadDb(databasePath);
            setConfigParameter('gui','lastSelectedDBPath',databasePath);
            self.loadInformation();

            #self.DBTable.update();

            self.DBLoadButton.text='Load db'

            self.nonBlockingPopupUpdate(popup,'Loading tracks...');
            self.loadTracks();

            self.nonBlockingPopupUpdate(popup,'Loading playlists...');
            self.loadPlaylists();

            self.nonBlockingPopupClose(popup);

            self.BackupDBButton.setEnabled(True);
            self.CreatePlaylistButton.setEnabled(True);
            #self.AddTrackToPlaylistButton.setEnabled(True);
            #self.ImportToPlaylistButton.setEnabled(True)
            #self.ExportPlaylistButton.setEnabled(True);
            #self.ImportFilesButton.setEnabled(True);
            self.ScanFolderButton.setEnabled(True);
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Folder does not exist")
            button = dlg.exec()

    def loadInformation(self):
        self.DBTable.setRowCount(5)
        self.DBTable.setColumnCount(2)
        self.DBTable.setHorizontalHeaderLabels(["Property", "Value"]);

        self.DBTable.setItem(0, 0, QTableWidgetItem('UUID'));
        self.DBTable.setItem(0, 1, QTableWidgetItem(self.piratengine.db.Information.data[0]['uuid']));

        self.DBTable.setItem(1, 0, QTableWidgetItem('db schema version'));
        version=str(self.piratengine.db.Information.data[0]['schemaVersionMajor']) + '.' + str(self.piratengine.db.Information.data[0]['schemaVersionMinor']) + '.' + str(self.piratengine.db.Information.data[0]['schemaVersionPatch']);
        self.DBTable.setItem(1, 1,QTableWidgetItem(version));
        
        self.DBTable.setItem(2, 0, QTableWidgetItem('Current played indiciator'));
        self.DBTable.setItem(2, 1, QTableWidgetItem(str(self.piratengine.db.Information.data[0]['currentPlayedIndiciator'])));

        self.DBTable.setItem(3, 0, QTableWidgetItem('last RekordBox library import counter'));
        self.DBTable.setItem(3, 1, QTableWidgetItem(str(self.piratengine.db.Information.data[0]['lastRekordBoxLibraryImportReadCounter'])));

        self.DBTable.setItem(4, 0, QTableWidgetItem('database tables'));
        self.DBTable.setItem(4, 1, QTableWidgetItem(str(self.piratengine.db.tables)));

        self.DBTable.setColumnWidth(0,self.DBTable.width()*1/3)
        self.DBTable.setColumnWidth(1,self.DBTable.width()*2/3)

    def loadTracks(self):
        displayedKeys=['path', 'filename'];
        self.TrackTable.setColumnCount(len(displayedKeys));
        self.TrackTable.setHorizontalHeaderLabels(displayedKeys);
        self.TrackTable.setRowCount(len(self.piratengine.db.Track.data));
        
        self.TrackTable.setColumnWidth(0,self.TrackTable.width()/len(displayedKeys))
        self.TrackTable.setColumnWidth(1,self.TrackTable.width()/len(displayedKeys))

        for row,track in enumerate(self.piratengine.db.Track.data):
            writeColumn=0;
            for column,key in enumerate(track):
                if key in displayedKeys:
                    self.TrackTable.setItem(row,writeColumn,QTableWidgetItem(str(track[key])))
                    writeColumn+=1;

                    #self.log(key + ' : ' + str(track[key]))

        

    def loadPlaylists(self):

        displayedKeys=['title', 'lastEditTime'];

        self.PlaylistTable.setColumnCount(len(displayedKeys));
        self.PlaylistTable.setHorizontalHeaderLabels(displayedKeys);
        self.PlaylistTable.setRowCount(len(self.piratengine.db.Playlist.data));
        self.PlaylistTable.setColumnWidth(0,self.PlaylistTable.width()/len(displayedKeys))
        self.PlaylistTable.setColumnWidth(1,self.PlaylistTable.width()/len(displayedKeys))

        for row,playlist in enumerate(self.piratengine.db.Playlist.data):
            
            for column,key in enumerate(playlist):
                    
                if key in displayedKeys:
                    self.PlaylistTable.setItem(row,displayedKeys.index(key),QTableWidgetItem(str(playlist[key])))

                    #self.log(key + ' : ' + str(track[key]))
    def loadPlaylistContents(self):
        selectedPlaylists=self.PlaylistTable.selectedIndexes()
        if len(selectedPlaylists) == 1 :
            self.ImportToPlaylistButton.setEnabled(True);
            self.ExportPlaylistButton.setEnabled(True);

            playlistHeaders=[self.PlaylistTable.horizontalHeaderItem(r).text() for r in range(self.PlaylistTable.columnCount())];
            titleColumnIndex=playlistHeaders.index('title')
            playlist=selectedPlaylists[titleColumnIndex].siblingAtColumn(0).data();

            tracks,trackObjectArray=self.piratengine.db.printPlaylist(playlist);
            self.PlaylistContentTable.setRowCount(len(tracks));
            self.PlaylistContentTable.setColumnCount(2);
            self.PlaylistContentTable.setColumnWidth(0,self.PlaylistContentTable.width()*2)
            for i,track in enumerate(tracks):
                self.PlaylistContentTable.setItem(i,0,QTableWidgetItem(track));  
        elif len(selectedPlaylists)>1:
            self.ExportPlaylistButton.setEnabled(True);
            self.ImportToPlaylistButton.setEnabled(False);
            self.AddTrackToPlaylistButton.setEnabled(False);
        else:
            self.AddTrackToPlaylistButton.setEnabled(False);
            self.ExportPlaylistButton.setEnabled(False);
            self.ImportToPlaylistButton.setEnabled(False);


    def ScanFolderButton_click(self):
        #path = str(QFileDialog.getExistingDirectory(self, "Select folder to be scanned"));
        path=str(pathlib.Path(self.piratengine.db.path).parents[2])
        self.log('Scanning database root path : ' + path);

        if os.path.exists(path):
            popup=self.nonBlockingPopup("Please wait","Scanning folder");
            files=self.piratengine.db.addFolderToDatabase(path);
            if files != []:
                setattr(self,'scannedFilesList',files);
                self.loadScannedFiles(files,popup);
            else:
                self.nonBlockingPopupClose(popup);
                dlg = QMessageBox(self);
                dlg.setWindowTitle("Error");
                dlg.setText("Please check terminal window/log to see error");
                button = dlg.exec();

        else:
            dlg = QMessageBox(self);
            dlg.setWindowTitle("Error");
            dlg.setText("Folder does not exist : " + path);
            button = dlg.exec();      
                

    def loadScannedFiles(self,files,popup=None):
        fileCount=len(files)
        self.FilesTable.setRowCount(fileCount);
        
        self.FilesTable.setColumnCount(1);
        self.FilesTable.setHorizontalHeaderLabels(['filename']);
        self.FilesTable.setColumnWidth(0,self.FilesTable.width());

        for i,f in enumerate(files):
            self.FilesTable.setItem(i,0,QTableWidgetItem(f));
            if popup != None : self.nonBlockingPopupUpdate(popup,str(i) + '/' + str(fileCount) )

        if popup != None : self.nonBlockingPopupClose(popup);

    def ImportFilesButton_click(self):
        selected=self.FilesTable.selectedIndexes();
        
        if len(selected) == 0 :
            dlg = QMessageBox(self);
            dlg.setWindowTitle("Error");
            dlg.setText("Select file(s) in the 'Files' table");
            button = dlg.exec();

        else:
            
            for line in selected:
                newTrackPath=self.FilesTable.itemAt(line.row(),0).text();
                scannedFileList=getattr(self,'scannedFilesList',None);
                if scannedFileList != None :
                    #newTrackPath=scannedFileList[line.row()];
                    newTrackPath=line.siblingAtColumn(0).data();
                    
                    if '../' in newTrackPath[:4]:
                        newTrackPath=newTrackPath.replace('../',str(pathlib.Path(self.piratengine.db.path).parents[2])+'/')

                    result=self.piratengine.db.addTrack(newTrackPath);
                    if result:
                        self.log('track added : ' + newTrackPath) ;
                        self.piratengine.db.readAll(True);
                    else : self.log('track not added');

            self.loadTracks();

    def CreatePlaylistButton_click(self):
        text, ok = QInputDialog.getText(self, 'Playlist name', 'Enter new playlist name:');
        if text != '':
            self.log('New playlist : ' + text );
            self.piratengine.db.createPlaylist(text);
            self.loadPlaylists();

    def AddTrackToPlaylistButton_click(self):
        selected=self.PlaylistTable.selectedIndexes();
        
        if len(selected) == 0 or len(selected) > 1:
            dlg = QMessageBox(self);
            dlg.setWindowTitle("Error");
            dlg.setText("Select one playlist in the table");
            button = dlg.exec();
            
        else:
            playlistHeaders=[self.PlaylistTable.horizontalHeaderItem(r).text() for r in range(self.PlaylistTable.columnCount())];
            titleColumnIndex=playlistHeaders.index('title')
            playlist=selected[titleColumnIndex].siblingAtColumn(0).data();
            #playlist=self.piratengine.db.Playlist.data[self.PlaylistTable.selectedIndexes()[0].row()]['title']
            self.log('Playlist ' + playlist );
            
            #playlist=self.PlaylistTable.itemAt(selected[0].row(),playlistHeaders.index('title')).text();
            trackHeaders=[self.TrackTable.horizontalHeaderItem(r).text() for r in range(self.TrackTable.columnCount())];
            pathColumnIndex=trackHeaders.index('path');
            #playlist=self.PlaylistTable.itemAt(selected[0].row(),0).text();
            #self.PlaylistTable.verticalHeaderItem()

            #playlist=self.PlaylistTable.itemAt(selected[0].row(),0).text();
            selectedTracks=self.TrackTable.selectedIndexes()

            for track in selectedTracks:
                trackPath=track.siblingAtColumn(pathColumnIndex).data()
                #trackPath=self.piratengine.db.Track.data[track.row()]['path']          

                trackId=self.piratengine.db.findTrack(path=trackPath);
                #trackId=self.piratengine.db.Track.data[track.row()]['id'];

                if trackId >=0:
                    self.piratengine.db.addPlaylistEntry(playlist,trackId);
                    self.log('added ' + trackPath)
                else:
                    self.log('Track not found : ' + trackPath);

            self.loadPlaylistContents();
            
    def ExportPlaylistButton_click(self):
        
        selected=self.PlaylistTable.selectedIndexes();

        if len(selected) == 0 :
            dlg = QMessageBox(self);
            dlg.setWindowTitle("Error");
            dlg.setText("Select one playlist in the table");
            button = dlg.exec();

        else:
            for i,sel in enumerate(selected):
                playlist=self.piratengine.db.Playlist.data[sel.row()]['title']
                self.log('Playlist ' + playlist )

                if len(selected)>1:
                    if i == 0:
                        dialog=QFileDialog.getSaveFileName(self, "Save playlist", os.path.join(os.path.expanduser('~'),playlist),"Text (*.txt);;JSON (*.json);;M3U (*.m3u)");
                    else :
                        dialog=(os.path.join(os.path.dirname(outfilePath),playlist),'*.'+extension+' ');
                else:
                    dialog=QFileDialog.getSaveFileName(self, "Save playlist", os.path.join(os.path.expanduser('~'),playlist),"Text (*.txt);;JSON (*.json);;M3U (*.m3u)");
                
                if dialog[0] != '':
                    extension=dialog[1][dialog[1].index('*.')+2:-1];
                    outfilePath=dialog[0]+'.'+extension;
                    self.log('Exported file : ' + outfilePath)
                    self.piratengine.exportPlaylist(self.piratengine.db,playlist,outfilePath);

    def ImportToPlaylistButton_click(self):

        selected=self.PlaylistTable.selectedIndexes();

        if len(selected) != 1:
            dlg = QMessageBox(self);
            dlg.setWindowTitle("Error");
            dlg.setText("Select one playlist in the table");
            button = dlg.exec();

        else:
            playlist=self.piratengine.db.Playlist.data[selected[0].row()]['title'];
            dialog=QFileDialog.getOpenFileName(self, "Import playlist", os.path.expanduser('~'),"Text (*.txt);;JSON (*.json);;M3U (*.m3u)");
            path=dialog[0];
            if path != '':
                popup=self.nonBlockingPopup("Loading "+ path +" ...","Playlist is updated...");
                self.piratengine.importPlaylist(path,playlist);
                self.nonBlockingPopupUpdate(popup,title='Loading tracks..');
                self.nonBlockingPopupClose(popup);
                self.loadPlaylists();
                self.loadPlaylistContents();

    def TrackTableFilter_textChanged(self):
        displayedKeys=['filename', 'path']
        defaultField='path';
        if not self.filterTable(filterWidget=self.TrackFilter,tableWidget=self.TrackTable,data=self.piratengine.db.Track.data,displayedKeys=displayedKeys,defaultField=defaultField):
            self.loadTracks();
            status=True;
        else:
            status=False;

        #self.AddTrackToPlaylistButton.setEnabled(status);


    def PlaylistTableFilter_textChanged(self):
        displayedKeys=['title', 'lastEditTime'];
        defaultField='title';
        if not self.filterTable(filterWidget=self.PlaylistFilter,tableWidget=self.PlaylistTable,data=self.piratengine.db.Playlist.data,displayedKeys=displayedKeys,defaultField=defaultField):
            self.loadPlaylists();
            status=True;
        else:
            status=False;

        #self.AddTrackToPlaylistButton.setEnabled(status);
        #self.ImportToPlaylistButton.setEnabled(status);
        #self.ExportPlaylistButton.setEnabled(status);

    def FilesFilter_textChanged(self):

        fileScanCache=self.piratengine.db.fileScanCache;
        
        if fileScanCache != []:
            if self.filterTable(filterWidget=self.FilesFilter,tableWidget=self.FilesTable,data=fileScanCache,displayedKeys=[],defaultField=''):
                status=False;
            else:
                status=True;
                scannedFilesList=getattr(self,'scannedFilesList',None);
                if scannedFilesList !=None :
                    self.loadScannedFiles(scannedFilesList);
                        
        #self.ImportFilesButton.setEnabled(status);

    def PlaylistContentFilter_textChanged(self):
        data,trackObjectArray=self.piratengine.db.printPlaylist(self.piratengine.db.Playlist.data[self.PlaylistTable.selectedIndexes()[0].row()]['title']);
        if not self.filterTable(filterWidget=self.PlaylistContentFilter,tableWidget=self.PlaylistContentTable,data=data,displayedKeys=[],defaultField=''):
          self.loadPlaylistContents();


    def filterTable(self,filterWidget="",tableWidget="",data=[],displayedKeys=[],defaultField=''):

        filterText=filterWidget.text();

        def tableFilter(item,field):
            return usedFilter.lower() in item[field].lower() 

        filterArray=filterText.split(',');

        results=[]

        
        for i,filterEntry in enumerate(filterArray):
            if displayedKeys != []: 
                if ':' in filterEntry:
                    usedFilter=filterEntry[filterEntry.index(':')+1:];
                    columnName=filterEntry[:filterEntry.index(':')];

                    if columnName in data[0].keys():
                        column=list(data[0].keys()).index(columnName)
                    else:
                        column=defaultField;

                elif i == 0:
                    usedFilter=filterEntry
                    column=0;
                    columnName=defaultField;
            else:
                column=0;
                columnName=column;
                usedFilter=filterEntry;
            
            if len(usedFilter)>3:
                if displayedKeys != []: 
                    results.append(filter(lambda x: usedFilter.lower() in x[columnName].lower(), data))
                else:
                    #if usedFilter.lower() in .lower()
                    results.append(filter(lambda x: usedFilter.lower() in x.lower(), data))
        #self.log('column ' + str(column) + ', columnName = ' + str(columnName))
        #self.log('usedFilter : ' + str(usedFilter))
        tableWidget.setRowCount(0);
        #self.log('len(results) = ' + str(len(results)))
        if len(results)>0:
            register=[]
            for r in results:
                for row,t in enumerate(list(r)):
                    tableWidget.setRowCount(row+1);
                    if t not in register:
                        register.append(t)
                        #self.log(t[columnName])
                        writeColumn=0;
                        if isinstance(t,dict):
                            for key in t:
                                if key in displayedKeys:
                                    #tableWidget.setRowCount(tableWidget.rowCount()+1);
                                    tableWidget.setItem(row,writeColumn,QTableWidgetItem(str(t[key])));
                                    writeColumn+=1;
                        else:
                            #tableWidget.setRowCount(tableWidget.rowCount()+1);
                            tableWidget.setItem(row,writeColumn,QTableWidgetItem(str(t)));       
            return True
        else:
            return False
            #for row,track in enumerate(self.piratengine.db.Track.data):

    def BackupDBButton_clicked(self):
        if self.piratengine.db != None:
            title='Backup Done';
            message='Database backup saved : ' + self.piratengine.db.backup();
        else:
            title='Error'
            message='No database found';

        dlg = QMessageBox(self);
        dlg.setWindowTitle(title);
        dlg.setText(message);
        button = dlg.exec();


    def stagelinqStartButton_click(self):
        try:
            self.piratengine.startStagelinq();
            setattr(self,'timer',QTimer(self));
            self.timer.timeout.connect(self.stagelinqUpdateData)
            self.timer.start(2000);
            self.stagelinqStartButton.text='Stop StageLinQ Monitor'
        except Exception as error:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText(str(type(error).__name__) + " " + str(error))
            button = dlg.exec();

    def stagelinqUpdateData(self):
        #self.log('Refresh stagelinq data');

        filter=self.stagelinqDataFilter.text();
        #self.log('filter = ' + filter)

        if hasattr(self,'piratengine'):
            data=self.piratengine.stagelinq.data;
                    
            writeRow=0;

            for row,key in enumerate(data):

                if ( filter.lower() in key.lower() and filter != "" ) or filter == '' :
                    self.stagelinqTable.setRowCount(writeRow+1);
                    dataKeys=data[key].keys();

                    if 'string' in dataKeys:
                        value=data[key]['string'];
                    elif 'state' in dataKeys:
                        value=data[key]['state'];
                    elif 'value' in dataKeys:
                        value=data[key]['value'];
                    else:
                        value=str(data[key]);

                    self.stagelinqTable.setItem(writeRow,0,QTableWidgetItem(str(key)));
                    self.stagelinqTable.setItem(writeRow,1,QTableWidgetItem(str(value)));

                    writeRow+=1