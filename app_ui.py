from PyQt5 import QtCore, QtGui, QtWidgets
from info import Ui_Form

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(480, 641)
        MainWindow.setMaximumSize(QtCore.QSize(500, 700))
        MainWindow.setSizeIncrement(QtCore.QSize(5, 0))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)

        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
    #    MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(480, 630))
        self.centralwidget.setMaximumSize(QtCore.QSize(482, 641))
        self.centralwidget.setStyleSheet("QWidget{\n"
"    opacity: 0;\n"
"    border-radius: 30px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(480, 630))
        self.frame.setMaximumSize(QtCore.QSize(482, 641))
        self.frame.setStyleSheet("QFrame{\n"
"    background: rgba(0, 128, 0, 0.3);\n"
"    border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(50, 50, 381, 101))
        self.frame_2.setStyleSheet("QFrame{\n"
"    background: transparent;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("#label:before{\n"
"    background: transparent;\n"
"    border: 3px white;\n"
"}\n"
"#label:hover{\n"
"    background-color: grey;\n"
"    border: 20px white;\n"
"}")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/add/desktop.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setProperty("Expand", sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"}\n"
"\n"
"#label_2:before{\n"
"    background: transparent;\n"
"    border: 3px white;\n"
"}\n"
"#label_2:hover{\n"
"    background-color: grey;\n"
"    border: 20px white;\n"
"}")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/add/desktop.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"}\n"
"#label_3:before{\n"
"    background-color: transparent;\n"
"    border: 3px white;\n"
"}\n"
"#label_3:hover{\n"
"    background-color: grey;\n"
"    border: 20px white;\n"
"}")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/add/desktop.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(50, 300, 381, 101))
        self.frame_3.setStyleSheet("QFrame{\n"
"    background: transparent;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(50)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"}\n"
"#label_7:before{\n"
"    background: transparent;\n"
"    border: 3px white;\n"
"}\n"
"#label_7:hover{\n"
"    background-color: grey;\n"
"    border: 20px white;\n"
"}")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/add/desktop.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"}\n"
"#label_8:before{\n"
"    background: transparent;\n"
"    border: 3px white;\n"
"}\n"
"#label_8:hover{\n"
"    background-color: grey;\n"
"    border: 20px white;\n"
"}")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/add/desktop.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"}\n"
"\n"
"#label_9:before{\n"
"    background: transparent;\n"
"    border: 3px white;\n"
"}\n"
"#label_9:hover{\n"
"    background-color: grey;\n"
"    border: 20px white;\n"
"}")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/add/desktop.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(-260, 210, 1131, 41))
        self.label_10.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"}")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/add/minus (2).png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(70, 150, 61, 71))
        self.label_12.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"}")
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/add/ethernet.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(210, 150, 61, 71))
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setAutoFillBackground(False)
        self.label_13.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"}")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/add/ethernet.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(350, 150, 61, 71))
        self.label_14.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"}")
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap(":/add/ethernet.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(210, 240, 61, 61))
        self.label_15.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"}")
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap(":/add/ethernet_2.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(350, 240, 61, 61))
        self.label_16.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"}")
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(":/add/ethernet_2.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(70, 240, 61, 61))
        self.label_17.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"}")
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap(":/add/ethernet_2.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(40, 430, 391, 151))
        self.frame_4.setStyleSheet("QFrame{\n"
"    background: transparent;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 321, 35))
        self.label_11.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"}")
        self.label_11.setObjectName("label_11")
        self.label_18 = QtWidgets.QLabel(self.frame_4)
        self.label_18.setGeometry(QtCore.QRect(10, 50, 211, 35))
        self.label_18.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"}")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_4)
        self.label_19.setGeometry(QtCore.QRect(10, 90, 181, 35))
        self.label_19.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"}")
        self.label_19.setObjectName("label_19")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(180, 600, 111, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: red;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"#pushButton:before{\n"
"    background-color: red;\n"
"}\n"
"#pushButton:hover{\n"
"    background-color: green;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Network View"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">Состояние системы:    </span><span style=\" font-size:22pt; font-weight:600; color:#00a200;\">OK</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">Подключено:    </span><span style=\" font-size:22pt; font-weight:600; color:#00a200;\">6</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">Ошибки:    </span><span style=\" font-size:22pt; font-weight:600; color:#00a200;\">0</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Закрыть"))
import res


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
