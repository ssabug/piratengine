import os
import pathlib
from tr import tr
from modules.utils import *
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget,QFileDialog,QMessageBox,QInputDialog,QTabWidget,QSpacerItem)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1434, 953)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.actionLoad_database = QAction(MainWindow)
        self.actionLoad_database.setObjectName(u"actionLoad_database")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 1411, 901))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 1381, 851))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.FilesTable = QTableWidget(self.gridLayoutWidget)
        self.FilesTable.setObjectName(u"FilesTable")

        self.gridLayout.addWidget(self.FilesTable, 5, 0, 1, 1)

        self.TrackTableLabel = QLabel(self.gridLayoutWidget)
        self.TrackTableLabel.setObjectName(u"TrackTableLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TrackTableLabel.sizePolicy().hasHeightForWidth())
        self.TrackTableLabel.setSizePolicy(sizePolicy)
        self.TrackTableLabel.setMinimumSize(QSize(714, 0))

        self.gridLayout.addWidget(self.TrackTableLabel, 2, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.DBPathTextEdit = QTextEdit(self.gridLayoutWidget)
        self.DBPathTextEdit.setObjectName(u"DBPathTextEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.DBPathTextEdit.sizePolicy().hasHeightForWidth())
        self.DBPathTextEdit.setSizePolicy(sizePolicy1)
        self.DBPathTextEdit.setMinimumSize(QSize(0, 10))
        self.DBPathTextEdit.setBaseSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.DBPathTextEdit)

        self.DBLoadButton = QPushButton(self.gridLayoutWidget)
        self.DBLoadButton.setObjectName(u"DBLoadButton")

        self.horizontalLayout.addWidget(self.DBLoadButton)

        self.DBChooseDirButton = QPushButton(self.gridLayoutWidget)
        self.DBChooseDirButton.setObjectName(u"DBChooseDirButton")

        self.horizontalLayout.addWidget(self.DBChooseDirButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.DBTable = QTableWidget(self.gridLayoutWidget)
        self.DBTable.setObjectName(u"DBTable")

        self.horizontalLayout_2.addWidget(self.DBTable)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.FilesTableLabel = QLabel(self.gridLayoutWidget)
        self.FilesTableLabel.setObjectName(u"FilesTableLabel")

        self.gridLayout.addWidget(self.FilesTableLabel, 4, 0, 1, 1)

        self.PlaylistTableLabel = QLabel(self.gridLayoutWidget)
        self.PlaylistTableLabel.setObjectName(u"PlaylistTableLabel")

        self.gridLayout.addWidget(self.PlaylistTableLabel, 2, 1, 1, 1)

        self.TrackTable = QTableWidget(self.gridLayoutWidget)
        self.TrackTable.setObjectName(u"TrackTable")
        self.TrackTable.setMinimumSize(QSize(800, 0))

        self.gridLayout.addWidget(self.TrackTable, 3, 0, 1, 1)

        self.PlaylistContentTable = QTableWidget(self.gridLayoutWidget)
        self.PlaylistContentTable.setObjectName(u"PlaylistContentTable")
        self.PlaylistContentTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.gridLayout.addWidget(self.PlaylistContentTable, 5, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.CreatePlaylistButton = QPushButton(self.gridLayoutWidget)
        self.CreatePlaylistButton.setObjectName(u"CreatePlaylistButton")

        self.verticalLayout_3.addWidget(self.CreatePlaylistButton)

        self.AddTrackToPlaylistButton = QPushButton(self.gridLayoutWidget)
        self.AddTrackToPlaylistButton.setObjectName(u"AddTrackToPlaylistButton")

        self.verticalLayout_3.addWidget(self.AddTrackToPlaylistButton)

        self.ImportToPlaylistButton = QPushButton(self.gridLayoutWidget)
        self.ImportToPlaylistButton.setObjectName(u"ImportToPlaylistButton")

        self.verticalLayout_3.addWidget(self.ImportToPlaylistButton)

        self.ExportPlaylistButton = QPushButton(self.gridLayoutWidget)
        self.ExportPlaylistButton.setObjectName(u"ExportPlaylistButton")

        self.verticalLayout_3.addWidget(self.ExportPlaylistButton)

        self.ScanFolderButton = QPushButton(self.gridLayoutWidget)
        self.ScanFolderButton.setObjectName(u"ScanFolderButton")

        self.verticalLayout_3.addWidget(self.ScanFolderButton)

        self.ImportFilesButton = QPushButton(self.gridLayoutWidget)
        self.ImportFilesButton.setObjectName(u"ImportFilesButton")

        self.verticalLayout_3.addWidget(self.ImportFilesButton)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.PlaylistTable = QTableWidget(self.gridLayoutWidget)
        self.PlaylistTable.setObjectName(u"PlaylistTable")

        self.gridLayout.addWidget(self.PlaylistTable, 3, 1, 1, 1)

        self.PlaylistContentTableLabel = QLabel(self.gridLayoutWidget)
        self.PlaylistContentTableLabel.setObjectName(u"PlaylistContentTableLabel")

        self.gridLayout.addWidget(self.PlaylistContentTableLabel, 4, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1434, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionLoad_database)
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"piratengine", None))
        self.actionLoad_database.setText(QCoreApplication.translate("MainWindow", u"Load database", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.TrackTableLabel.setText(QCoreApplication.translate("MainWindow", u"Tracks", None))
        self.DBPathTextEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.DBLoadButton.setText(QCoreApplication.translate("MainWindow", u"Load db", None))
        self.DBChooseDirButton.setText(QCoreApplication.translate("MainWindow", u"Choose dir", None))
        self.FilesTableLabel.setText(QCoreApplication.translate("MainWindow", u"Files", None))
        self.PlaylistTableLabel.setText(QCoreApplication.translate("MainWindow", u"Playlists", None))
        self.CreatePlaylistButton.setText(QCoreApplication.translate("MainWindow", u"Create playlist", None))
        self.AddTrackToPlaylistButton.setText(QCoreApplication.translate("MainWindow", u"Add track(s) to playlist", None))
        self.ImportToPlaylistButton.setText(QCoreApplication.translate("MainWindow", u"Import to playlist", None))
        self.ExportPlaylistButton.setText(QCoreApplication.translate("MainWindow", u"Export playlist(s)", None))
        self.ScanFolderButton.setText(QCoreApplication.translate("MainWindow", u"Scan folder for music files", None))
        self.ImportFilesButton.setText(QCoreApplication.translate("MainWindow", u"Import file(s) to Track database", None))
        self.PlaylistContentTableLabel.setText(QCoreApplication.translate("MainWindow", u"Playlist Content", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Database", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"StagelinQ", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

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
    
    def DBLoadButton_click(self):
        self.log('Load Database clicked');
        self.DBLoadButton.text='Loading...';
        self.DBLoadButton.update();
        databasePath=self.DBPathTextEdit.toPlainText();

        if databasePath == '' :
            databasePath = str(QFileDialog.getExistingDirectory(self, "Select Database2 folder"));
            self.DBPathTextEdit.setHtml(databasePath);
            self.log(databasePath);
        
        if os.path.exists(databasePath):
            self.piratengine.db=self.piratengine.loadDb(databasePath);
            setConfigParameter('gui','lastSelectedDBPath',databasePath);
            self.loadInformation();

            #self.DBTable.update();

            self.DBLoadButton.text='Load db'

            self.loadTracks();

            self.loadPlaylists();
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
        displayedKeys=['filename', 'path'];
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
        tracks=self.piratengine.db.printPlaylist(self.piratengine.db.Playlist.data[self.PlaylistTable.selectedIndexes()[0].row()]['title']);
        self.PlaylistContentTable.setRowCount(len(tracks));
        self.PlaylistContentTable.setColumnCount(2);
        self.PlaylistContentTable.setColumnWidth(0,self.PlaylistContentTable.width()*2)
        for i,track in enumerate(tracks):
            self.PlaylistContentTable.setItem(i,0,QTableWidgetItem(track));

    def ScanFolderButton_click(self):
        path = str(QFileDialog.getExistingDirectory(self, "Select folder to be scanned"));
        
        if os.path.exists(path):
            files=self.piratengine.db.addFolderToDatabase(path);
            setattr(self,'scannedFilesList',files);
            self.FilesTable.setRowCount(len(files));
            self.FilesTable.setColumnCount(1);
            self.FilesTable.setHorizontalHeaderLabels(['filename']);
            self.FilesTable.setColumnWidth(0,self.FilesTable.width());

            for i,f in enumerate(files):
                self.FilesTable.setItem(i,0,QTableWidgetItem(f));

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
                    newTrackPath=scannedFileList[line.row()];
                    
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
            playlist=self.piratengine.db.Playlist.data[self.PlaylistTable.selectedIndexes()[0].row()]['title']
            self.log('Playlist ' + playlist )
            playlistHeaders=[self.PlaylistTable.horizontalHeaderItem(r).text() for r in range(self.PlaylistTable.columnCount())];
            #playlist=self.PlaylistTable.itemAt(selected[0].row(),playlistHeaders.index('title')).text();
            trackHeaders=[self.TrackTable.horizontalHeaderItem(r).text() for r in range(self.TrackTable.columnCount())];
            pathColumnIndex=trackHeaders.index('path');
            #playlist=self.PlaylistTable.itemAt(selected[0].row(),0).text();
            #self.PlaylistTable.verticalHeaderItem()

            #playlist=self.PlaylistTable.itemAt(selected[0].row(),0).text();
            selectedTracks=self.TrackTable.selectedIndexes()

            for track in selectedTracks:
                trackPath=self.piratengine.db.Track.data[track.row()]['path']
                #trackPath=self.TrackTable.itemAt(track.row(),pathColumnIndex).text();          

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