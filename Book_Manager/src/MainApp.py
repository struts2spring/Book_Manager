'''
Created on May 6, 2014

@author: vk82286
'''
from PyQt4 import QtCore, QtGui
from com.bookmanager.view.Window import MainWindow
import sys,os

def main():
    root_dir = os.path.abspath(os.path.dirname(__file__)) 
    root_dir_name = os.path.split(os.path.abspath(os.path.dirname(__file__)))
    print root_dir
    print root_dir_name
    
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
