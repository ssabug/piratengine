import sys
import inspect
#from PySide6 import QtCore, QtGui, QtWidgets
#from PySide6.QtUiTools import QUiLoader
from PySide6 import QtWidgets

from modules.utils import *
from modules.mainGui import Ui_MainWindow

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

    
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self,piratengine):
            super(MainWindow, self).__init__()
            self.setupUi(self);
            self.initCallbacks();
            self.piratengine=piratengine;
            '''
            for name, obj in inspect.getmembers(MainWindowCustomCode):
                
            #get all module classes
                if inspect.isfunction(obj) and name != '__init__':
                    #self.log('name = ' + name + ', obj = ' + str(obj));
                    setattr(Ui_MainWindow, name, obj)
                    self.log('function ' + name + ' added to window');

            Ui_MainWindow.initCallbacks(Ui_MainWindow);
            '''

        def log(self,text,source='GUIM',severity='INFO',sameline=False):
            log(text,source=source,severity=severity,sameline=sameline);

class MainWindowCustomCode():
        def __init__(self):
            a=True

        def log(self,text,source='GUIM',severity='INFO',sameline=False):
            log(text,source=source,severity=severity,sameline=sameline);

        def initCallbacks(self):
            self.DBLoadButton.clicked.connect(self.DBLoadButton_click);
        
        def DBLoadButton_click(self):
            self.log('Load Database clicked');


