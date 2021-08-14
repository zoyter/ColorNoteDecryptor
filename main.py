import sys, os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextBrowser

import decryptor


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

class frmMain(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('frmMain.ui', self)
        self.setAcceptDrops(True)
        self.all_data = []
        self.FileToDecrypt = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            self.FileToDecrypt = f
            self.textBrowser.setText(f)
        decryptor.DecryptColorNote(self.FileToDecrypt,self.all_data)
        self.textBrowser.setText('\n'.join(self.all_data))

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    #decryptor.main()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = frmMain()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
