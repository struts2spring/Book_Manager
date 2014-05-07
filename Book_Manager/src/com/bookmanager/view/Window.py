'''
Created on May 6, 2014

@author: vk82286
'''
from PyQt4 import QtCore, QtGui, Qt


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        widget = QtGui.QWidget()
        self.setCentralWidget(widget)

        topFiller = QtGui.QWidget()
        topFiller.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

        self.infoLabel = QtGui.QLabel("<i>Choose a menu option, or right-click to invoke a context menu</i>", alignment=QtCore.Qt.AlignCenter)
        self.infoLabel.setFrameStyle(QtGui.QFrame.StyledPanel | QtGui.QFrame.Sunken)

        bottomFiller = QtGui.QWidget()
        bottomFiller.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

        vbox = QtGui.QVBoxLayout()
        vbox.setMargin(5)
        vbox.addWidget(topFiller)
        vbox.addWidget(self.infoLabel)
        vbox.addWidget(bottomFiller)
        widget.setLayout(vbox)

        self.createActions()
        self.createMenus()
        self.initFileToolbar()
        message = "A context menu is available by right-clicking"
        self.statusBar().showMessage(message)

        self.setWindowTitle("Book Manager")
        self.setMinimumSize(160, 160)
        # self.resize(480, 320)
        self.showMaximized()
        self.setWindowIcon(QtGui.QIcon('..\..\..\..\images\PNG\png32\safe.png'))

    def contextMenuEvent(self, event):
        menu = QtGui.QMenu(self)
        menu.addAction(self.cutAct)
        menu.addAction(self.copyAct)
        menu.addAction(self.pasteAct)
        menu.exec_(event.globalPos())

    def newFile(self):
        self.infoLabel.setText("Invoked <b>File|New</b>")

    def open(self):
        self.infoLabel.setText("Invoked <b>File|Open</b>")
            
    def save(self):
        self.infoLabel.setText("Invoked <b>File|Save</b>")

    def print_(self):
        self.infoLabel.setText("Invoked <b>File|Print</b>")

    def undo(self):
        self.infoLabel.setText("Invoked <b>Edit|Undo</b>")

    def redo(self):
        self.infoLabel.setText("Invoked <b>Edit|Redo</b>")

    def cut(self):
        self.infoLabel.setText("Invoked <b>Edit|Cut</b>")

    def copy(self):
        self.infoLabel.setText("Invoked <b>Edit|Copy</b>")

    def paste(self):
        self.infoLabel.setText("Invoked <b>Edit|Paste</b>")

    def bold(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Bold</b>")

    def italic(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Italic</b>")

    def leftAlign(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Left Align</b>")

    def rightAlign(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Right Align</b>")

    def justify(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Justify</b>")

    def center(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Center</b>")

    def setLineSpacing(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Set Line Spacing</b>")

    def setParagraphSpacing(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Set Paragraph Spacing</b>")

    def about(self):
        self.infoLabel.setText("Invoked <b>Help|About</b>")
        QtGui.QMessageBox.about(self, "About Menu",
                "The <b>Menu</b> example shows how to create menu-bar menus "
                "and context menus.")

    def aboutQt(self):
        self.infoLabel.setText("Invoked <b>Help|About Qt</b>")

    def createActions(self):
        self.newAct = QtGui.QAction(QtGui.QIcon('..\..\..\..\images\New\New_32x32.png'),"&New", self,
                shortcut=QtGui.QKeySequence.New,
                statusTip="Create a new file", triggered=self.newFile)
        
        self.openAct = QtGui.QAction(QtGui.QIcon('..\..\..\..\images\Open\Open_32x32.png'),"&Open...", self,
                shortcut=QtGui.QKeySequence.Open,
                statusTip="Open an existing file", triggered=self.open)

        self.saveAct = QtGui.QAction(QtGui.QIcon('..\images\Save\Save_32x32.png'),"&Save", self,
                shortcut=QtGui.QKeySequence.Save,
                statusTip="Save the document to disk", triggered=self.save)

        self.printAct = QtGui.QAction(QtGui.QIcon('..\..\..\..\images\Print\Print_32x32.png'),"&Print...", self,
                shortcut=QtGui.QKeySequence.Print,
                statusTip="Print the document", triggered=self.print_)

        self.exitAct = QtGui.QAction(QtGui.QIcon('..\..\..\..\images\Log Out\Log Out_32x32.png'),"E&xit", self, shortcut="Ctrl+Q",
                statusTip="Exit the application", triggered=self.close)

        self.undoAct = QtGui.QAction(QtGui.QIcon('..\..\..\..\images\Undo\Undo_32x32.png'),"&Undo", self,
                shortcut=QtGui.QKeySequence.Undo,
                statusTip="Undo the last operation", triggered=self.undo)

        self.redoAct = QtGui.QAction(QtGui.QIcon('..\..\..\..\images\Redo\Redo_32x32.png'),"&Redo", self,
                shortcut=QtGui.QKeySequence.Redo,
                statusTip="Redo the last operation", triggered=self.redo)

        self.cutAct = QtGui.QAction(QtGui.QIcon('..\..\..\..\images\Cut\Cut_32x32.png'),"Cu&t", self,
                shortcut=QtGui.QKeySequence.Cut,
                statusTip="Cut the current selection's contents to the clipboard",
                triggered=self.cut)

        self.copyAct = QtGui.QAction(QtGui.QIcon('..\..\..\..\images\Copy\Copy_32x32.png'),"&Copy", self,
                shortcut=QtGui.QKeySequence.Copy,
                statusTip="Copy the current selection's contents to the clipboard",
                triggered=self.copy)

        self.pasteAct = QtGui.QAction(QtGui.QIcon('..\..\..\..\images\New\New_32x32.png'),"&Paste", self,
                shortcut=QtGui.QKeySequence.Paste,
                statusTip="Paste the clipboard's contents into the current selection",
                triggered=self.paste)

        self.boldAct = QtGui.QAction("&Bold", self, checkable=True,
                shortcut="Ctrl+B", statusTip="Make the text bold",
                triggered=self.bold)

        boldFont = self.boldAct.font()
        boldFont.setBold(True)
        self.boldAct.setFont(boldFont)

        self.italicAct = QtGui.QAction("&Italic", self, checkable=True,
                shortcut="Ctrl+I", statusTip="Make the text italic",
                triggered=self.italic)

        italicFont = self.italicAct.font()
        italicFont.setItalic(True)
        self.italicAct.setFont(italicFont)

        self.setLineSpacingAct = QtGui.QAction("Set &Line Spacing...", self,
                statusTip="Change the gap between the lines of a paragraph",
                triggered=self.setLineSpacing)

        self.setParagraphSpacingAct = QtGui.QAction(
                "Set &Paragraph Spacing...", self,
                statusTip="Change the gap between paragraphs",
                triggered=self.setParagraphSpacing)

        self.aboutAct = QtGui.QAction("&About", self,
                statusTip="Show the application's About box",
                triggered=self.about)

        self.aboutQtAct = QtGui.QAction("About &Qt", self,
                statusTip="Show the Qt library's About box",
                triggered=self.aboutQt)
        self.aboutQtAct.triggered.connect(QtGui.qApp.aboutQt)

        self.leftAlignAct = QtGui.QAction("&Left Align", self, checkable=True,
                shortcut="Ctrl+L", statusTip="Left align the selected text",
                triggered=self.leftAlign)

        self.rightAlignAct = QtGui.QAction("&Right Align", self,
                checkable=True, shortcut="Ctrl+R",
                statusTip="Right align the selected text",
                triggered=self.rightAlign)

        self.justifyAct = QtGui.QAction("&Justify", self, checkable=True,
                shortcut="Ctrl+J", statusTip="Justify the selected text",
                triggered=self.justify)

        self.centerAct = QtGui.QAction("&Center", self, checkable=True,
                shortcut="Ctrl+C", statusTip="Center the selected text",
                triggered=self.center)

        self.alignmentGroup = QtGui.QActionGroup(self)
        self.alignmentGroup.addAction(self.leftAlignAct)
        self.alignmentGroup.addAction(self.rightAlignAct)
        self.alignmentGroup.addAction(self.justifyAct)
        self.alignmentGroup.addAction(self.centerAct)
        self.leftAlignAct.setChecked(True)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.printAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.editMenu = self.menuBar().addMenu("&Edit")
        self.editMenu.addAction(self.undoAct)
        self.editMenu.addAction(self.redoAct)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.cutAct)
        self.editMenu.addAction(self.copyAct)
        self.editMenu.addAction(self.pasteAct)
        self.editMenu.addSeparator()

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

        self.formatMenu = self.editMenu.addMenu("&Format")
        self.formatMenu.addAction(self.boldAct)
        self.formatMenu.addAction(self.italicAct)
        self.formatMenu.addSeparator().setText("Alignment")
        self.formatMenu.addAction(self.leftAlignAct)
        self.formatMenu.addAction(self.rightAlignAct)
        self.formatMenu.addAction(self.justifyAct)
        self.formatMenu.addAction(self.centerAct)
        self.formatMenu.addSeparator()
        self.formatMenu.addAction(self.setLineSpacingAct)
        self.formatMenu.addAction(self.setParagraphSpacingAct)

    def initFileToolbar(self):
        self.fileToolbar = self.addToolBar('File')
        self.fileToolbar.addAction(self.newAct)
        self.fileToolbar.addAction(self.openAct)
        self.fileToolbar.addAction(self.saveAct)
        self.fileToolbar.addAction(self.printAct)
        self.fileToolbar.addSeparator()

#         opener  = QtGui.QAction(QtGui.QIcon('icons/16x16/actions/document-open.png'), 'Open', self)
#         opener.setShortcut('Ctrl+O')
#         opener.connect(opener, QtCore.SIGNAL('triggered()'), self.doFileOpen) #QtCore.SLOT('close()'))
# 
#         save  = QtGui.QAction(QtGui.QIcon('icons/16x16/actions/document-save.png'), 'Save', self)
#         save.setShortcut('Ctrl+S')
#         save.connect(save, QtCore.SIGNAL('triggered()'), self.doFileSave)
# 
#         saveas  = QtGui.QAction(QtGui.QIcon('icons/16x16/actions/document-save.png'), 'Save As', self)
#         saveas.setShortcut('Ctrl+S')
#         saveas.connect(saveas, QtCore.SIGNAL('triggered()'), self.doFileSaveAs)
# 
#         printer  = QtGui.QAction(QtGui.QIcon('icons/16x16/actions/document-print.png'), 'Print', self)
#         printer.setShortcut('Ctrl+P')
#         printer.connect(printer, QtCore.SIGNAL('triggered()'), self.doPrinter)
#         
#         exit = QtGui.QAction(QtGui.QIcon('icons/16x16/actions/process-stop.png'), 'Exit', self)
#         exit.setShortcut('Ctrl+Q')
#         self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

       
#         self.fileToolbar.addAction(opener)
#         self.fileToolbar.addAction(save)
        #self.fileToolbar.addAction(saveas)
#         self.fileToolbar.addAction(printer)
        #self.fileToolbar.addAction(exit)

if __name__ == '__main__':

    import sys, os
    root_dir = os.path.abspath(os.path.dirname(__file__)) 
    root_dir_name = os.path.split(os.path.abspath(os.path.dirname(__file__)))
    print root_dir
    print root_dir_name
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
