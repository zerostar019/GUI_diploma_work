from main_ui import Ui_MainWindow
from info import Ui_Form
import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets


def start_main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
        
    
    
if __name__ == "__main__":
    start_main()