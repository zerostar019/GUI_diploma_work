from PyQt5 import QtCore, QtGui, QtWidgets
import win_sys
import json

class MainWindow_1(QtWidgets.QMainWindow):         
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Info")
        MainWindow.resize(548, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 8, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 3, 0, 1, 2)
        self.processor = QtWidgets.QLabel(self.frame_2)
        self.processor.setText("")
        self.processor.setAlignment(QtCore.Qt.AlignCenter)
        self.processor.setWordWrap(True)
        self.processor.setObjectName("processor")
        self.gridLayout_2.addWidget(self.processor, 0, 1, 1, 1)
        self.sound = QtWidgets.QLabel(self.frame_2)
        self.sound.setText("")
        self.sound.setAlignment(QtCore.Qt.AlignCenter)
        self.sound.setWordWrap(True)
        self.sound.setObjectName("sound")
        self.gridLayout_2.addWidget(self.sound, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)
        self.gpu = QtWidgets.QLabel(self.frame_2)
        self.gpu.setText("")
        self.gpu.setAlignment(QtCore.Qt.AlignCenter)
        self.gpu.setWordWrap(True)
        self.gpu.setObjectName("gpu")
        self.gridLayout_2.addWidget(self.gpu, 2, 1, 1, 1)
        self.hdd = QtWidgets.QLabel(self.frame_2)
        self.hdd.setText("")
        self.hdd.setAlignment(QtCore.Qt.AlignCenter)
        self.hdd.setWordWrap(True)
        self.hdd.setObjectName("hdd")
        self.gridLayout_2.addWidget(self.hdd, 8, 1, 1, 1)
        self.ram = QtWidgets.QLabel(self.frame_2)
        self.ram.setText("")
        self.ram.setAlignment(QtCore.Qt.AlignCenter)
        self.ram.setWordWrap(True)
        self.ram.setObjectName("ram")
        self.gridLayout_2.addWidget(self.ram, 6, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.frame_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 5, 0, 1, 2)
        self.line_4 = QtWidgets.QFrame(self.frame_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 7, 0, 1, 2)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.check_computer)
        
        
    def get_title_menu(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(f"Computer: {win_sys.getMachine_addr()}\n[+] {text}")
        msg.exec_()
        

    def check_computer(self):
        with open('data.json', 'r', encoding='utf-8') as data:
            info = json.load(data)
            computer_info = info.get(str(win_sys.getMachine_addr()))
            for key, value in computer_info.items():
                if key == "Процессор":
                    if value == win_sys.get_processor_info():
                        continue
                    else:
                        self.get_title_menu(text="Процессор был поменян!!!")
                elif key == "Видеокарта":
                    if value == win_sys.get_gpu():
                        continue
                    else:
                        self.get_title_menu(text="The GPU was changed\n from {} to {}".format(value, win_sys.get_gpu()))
                elif key == "Звуковая карта":
                    if value == win_sys.get_sound():
                        continue
                    else:
                        self.get_title_menu(text="Была поменяна звуковая карта")
                elif key == "Оперативная память":
                    if value == win_sys.get_RAM():
                        continue
                    else:
                        self.get_title_menu(text="Была поменяна оперативная память")
                elif key == "Жесткий диск":
                    if value == win_sys.get_hdd():
                        continue
                    else:
                        self.get_title_menu(text="Был поменян жесткий диск")
                
                                        
    def get_all_computer(self):
        try:
            '''
            Получаем данные компьютера
            '''
            self.processor.setText(win_sys.get_processor_info()) # Получаем данные процессора
            self.gpu.setText(win_sys.get_gpu())
            self.sound.setText(win_sys.get_sound())
            self.ram.setText(win_sys.get_RAM())
            self.hdd.setText(win_sys.get_hdd())
            with open('data.json', 'r', encoding='utf-8') as inf:
                info = json.load(inf)
                if info.get(str(win_sys.getMachine_addr())):
                    pass
                else:
                    diction = {
                            str(win_sys.getMachine_addr()): {
                            "Процессор": win_sys.get_processor_info(),
                            "Видеокарта": win_sys.get_gpu(),
                            "Звуковая карта": win_sys.get_sound(),
                            "Оперативная память": win_sys.get_RAM(),
                            "Жесткий диск": win_sys.get_hdd(),
                        }
                        
                        
                    }
                    with open('data.json', 'a', encoding='utf-8') as data:
                        json.dump(diction, data, indent=4, ensure_ascii=False)
        except:
            pass
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Процессор</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Видеокарта</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Звуковая карта</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Жесткий диск</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Оперативная память</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Проверить"))


