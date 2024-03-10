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
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1434, 944)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.actionLoad_database = QAction(MainWindow)
        self.actionLoad_database.setObjectName(u"actionLoad_database")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionChoose_table_columns = QAction(MainWindow)
        self.actionChoose_table_columns.setObjectName(u"actionChoose_table_columns")
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

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.BackupDBButton = QPushButton(self.gridLayoutWidget)
        self.BackupDBButton.setObjectName(u"BackupDBButton")

        self.verticalLayout_3.addWidget(self.BackupDBButton)

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

        self.TrackTable = QTableWidget(self.gridLayoutWidget)
        self.TrackTable.setObjectName(u"TrackTable")
        self.TrackTable.setMinimumSize(QSize(800, 0))

        self.gridLayout.addWidget(self.TrackTable, 3, 0, 1, 1)

        self.PlaylistContentTable = QTableWidget(self.gridLayoutWidget)
        self.PlaylistContentTable.setObjectName(u"PlaylistContentTable")
        self.PlaylistContentTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.gridLayout.addWidget(self.PlaylistContentTable, 5, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.PlaylistTable = QTableWidget(self.gridLayoutWidget)
        self.PlaylistTable.setObjectName(u"PlaylistTable")

        self.gridLayout.addWidget(self.PlaylistTable, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.FilesTableLabel = QLabel(self.gridLayoutWidget)
        self.FilesTableLabel.setObjectName(u"FilesTableLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FilesTableLabel.sizePolicy().hasHeightForWidth())
        self.FilesTableLabel.setSizePolicy(sizePolicy)
        self.FilesTableLabel.setMinimumSize(QSize(185, 0))

        self.horizontalLayout_6.addWidget(self.FilesTableLabel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.FilesFilterLabel = QLabel(self.gridLayoutWidget)
        self.FilesFilterLabel.setObjectName(u"FilesFilterLabel")

        self.horizontalLayout_6.addWidget(self.FilesFilterLabel)

        self.FilesFilter = QLineEdit(self.gridLayoutWidget)
        self.FilesFilter.setObjectName(u"FilesFilter")

        self.horizontalLayout_6.addWidget(self.FilesFilter)


        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.TrackTableLabel = QLabel(self.gridLayoutWidget)
        self.TrackTableLabel.setObjectName(u"TrackTableLabel")
        sizePolicy.setHeightForWidth(self.TrackTableLabel.sizePolicy().hasHeightForWidth())
        self.TrackTableLabel.setSizePolicy(sizePolicy)
        self.TrackTableLabel.setMinimumSize(QSize(140, 0))
        self.TrackTableLabel.setMaximumSize(QSize(16777142, 16777215))

        self.horizontalLayout_3.addWidget(self.TrackTableLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.TrackFilterLabel = QLabel(self.gridLayoutWidget)
        self.TrackFilterLabel.setObjectName(u"TrackFilterLabel")

        self.horizontalLayout_3.addWidget(self.TrackFilterLabel)

        self.TrackFilter = QLineEdit(self.gridLayoutWidget)
        self.TrackFilter.setObjectName(u"TrackFilter")

        self.horizontalLayout_3.addWidget(self.TrackFilter)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

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

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.PlaylistTableLabel = QLabel(self.gridLayoutWidget)
        self.PlaylistTableLabel.setObjectName(u"PlaylistTableLabel")
        sizePolicy.setHeightForWidth(self.PlaylistTableLabel.sizePolicy().hasHeightForWidth())
        self.PlaylistTableLabel.setSizePolicy(sizePolicy)
        self.PlaylistTableLabel.setMinimumSize(QSize(86, 0))

        self.horizontalLayout_4.addWidget(self.PlaylistTableLabel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.PlaylistFilterLabel = QLabel(self.gridLayoutWidget)
        self.PlaylistFilterLabel.setObjectName(u"PlaylistFilterLabel")

        self.horizontalLayout_4.addWidget(self.PlaylistFilterLabel)

        self.PlaylistFilter = QLineEdit(self.gridLayoutWidget)
        self.PlaylistFilter.setObjectName(u"PlaylistFilter")

        self.horizontalLayout_4.addWidget(self.PlaylistFilter)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.PlaylistContentTableLabel = QLabel(self.gridLayoutWidget)
        self.PlaylistContentTableLabel.setObjectName(u"PlaylistContentTableLabel")

        self.horizontalLayout_8.addWidget(self.PlaylistContentTableLabel)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.PlaylistContentFilterLable = QLabel(self.gridLayoutWidget)
        self.PlaylistContentFilterLable.setObjectName(u"PlaylistContentFilterLable")

        self.horizontalLayout_8.addWidget(self.PlaylistContentFilterLable)

        self.PlaylistContentFilter = QLineEdit(self.gridLayoutWidget)
        self.PlaylistContentFilter.setObjectName(u"PlaylistContentFilter")

        self.horizontalLayout_8.addWidget(self.PlaylistContentFilter)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)


        self.gridLayout.addLayout(self.horizontalLayout_7, 4, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 991, 631))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stagelinqStartButton = QPushButton(self.gridLayoutWidget_2)
        self.stagelinqStartButton.setObjectName(u"stagelinqStartButton")

        self.verticalLayout_4.addWidget(self.stagelinqStartButton)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.stagelinqDataFilterLabel = QLabel(self.gridLayoutWidget_2)
        self.stagelinqDataFilterLabel.setObjectName(u"stagelinqDataFilterLabel")

        self.horizontalLayout_5.addWidget(self.stagelinqDataFilterLabel)

        self.stagelinqDataFilter = QLineEdit(self.gridLayoutWidget_2)
        self.stagelinqDataFilter.setObjectName(u"stagelinqDataFilter")

        self.horizontalLayout_5.addWidget(self.stagelinqDataFilter)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.stagelinqTable = QTableWidget(self.gridLayoutWidget_2)
        self.stagelinqTable.setObjectName(u"stagelinqTable")

        self.verticalLayout_4.addWidget(self.stagelinqTable)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

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
        self.menuFile.addAction(self.actionChoose_table_columns)
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"piratengine", None))
        self.actionLoad_database.setText(QCoreApplication.translate("MainWindow", u"Load database", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionChoose_table_columns.setText(QCoreApplication.translate("MainWindow", u"Choose table columns", None))
        self.BackupDBButton.setText(QCoreApplication.translate("MainWindow", u"Backup database", None))
        self.CreatePlaylistButton.setText(QCoreApplication.translate("MainWindow", u"Create playlist", None))
        self.AddTrackToPlaylistButton.setText(QCoreApplication.translate("MainWindow", u"Add track(s) to playlist", None))
        self.ImportToPlaylistButton.setText(QCoreApplication.translate("MainWindow", u"Import file to playlist (txt,json,m3u)", None))
        self.ExportPlaylistButton.setText(QCoreApplication.translate("MainWindow", u"Export playlist(s) (txt,json,m3u)", None))
        self.ScanFolderButton.setText(QCoreApplication.translate("MainWindow", u"Scan database root folder for music files", None))
        self.ImportFilesButton.setText(QCoreApplication.translate("MainWindow", u"Import file(s) to Track database", None))
        self.FilesTableLabel.setText(QCoreApplication.translate("MainWindow", u"Files", None))
        self.FilesFilterLabel.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.TrackTableLabel.setText(QCoreApplication.translate("MainWindow", u"Tracks", None))
        self.TrackFilterLabel.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
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
        self.PlaylistTableLabel.setText(QCoreApplication.translate("MainWindow", u"Playlists", None))
        self.PlaylistFilterLabel.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.PlaylistContentTableLabel.setText(QCoreApplication.translate("MainWindow", u"Playlist Content", None))
        self.PlaylistContentFilterLable.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Database", None))
        self.stagelinqStartButton.setText(QCoreApplication.translate("MainWindow", u"Start StageLinQ monitor", None))
        self.stagelinqDataFilterLabel.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
#if QT_CONFIG(tooltip)
        self.stagelinqDataFilter.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.stagelinqDataFilter.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"StagelinQ", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

