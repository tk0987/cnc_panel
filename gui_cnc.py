# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
"""
CNC control panel

designed for specific cnc machine, which rely on relative coordinates

not pretty, but working
"""
# from PyQt6 import QtCore, QtGui, QtWidgets
# from PyQt6.QtWidgets import QGridLayout
import sys
import serial
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QLabel, QLayout, QLineEdit, QListView,QFileDialog,QDialog,
    QProgressBar, QPushButton, QSizePolicy, QTabWidget,
    QWidget)
from PySide6 import QtWidgets
from PIL import Image
import numpy as np
from datetime import datetime
import re
import matplotlib.pyplot as plt
import socket

# Pico W IP address in AP mode is usually 192.168.4.1
global pico_ip
global port
pico_ip = '192.168.4.1'
port = 8000

global step_per_rev 
step_per_rev=200
global com
com="COM4"

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        # Main.setWindowModality(Qt.WindowModality.ApplicationModal)
        Main.resize(1500, 865)
        Main.setWindowOpacity(0.5)
        Main.setStyleSheet(u"QWidget {\n"
"    background-color: #2E2E2E; /* Dark background color */\n"
"    color: white; /* White text color */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #3E3E3E;\n"
"    color: white;\n"
"    border: 1px solid #555555;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #3E3E3E;\n"
"    color: white;\n"
"    border: 1px solid #555555;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"}\n"
"QProgressBar {\n"
"    border: 2px solid #555555;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    background-color: #3E3E3E;\n"
"    color: white; /* Text color */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #D3D3D3; /* Yellow color for the progress bar */\n"
"    width: 20px;\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(Main)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.tabWidget = QTabWidget(Main)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.line_7 = QFrame(self.tab)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_7, 0, 1, 1, 2)

        self.line_21 = QFrame(self.tab)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.Shape.HLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_21, 1, 1, 1, 2)

        self.line_9 = QFrame(self.tab)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_9, 2, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_4, 7, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.line_5 = QFrame(self.tab)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_5, 3, 0, 1, 1)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_4.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_4.addWidget(self.pushButton_4, 4, 0, 1, 1)

        self.line_6 = QFrame(self.tab)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_6, 1, 0, 1, 1)

        self.line_8 = QFrame(self.tab)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_8, 8, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_4.addWidget(self.pushButton_3, 7, 0, 1, 1)

        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.line_3 = QFrame(self.tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 7, 3, 1, 1)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_2, 2, 2, 1, 1)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_3, 4, 2, 1, 1)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label, 0, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_4.addWidget(self.pushButton_2, 2, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.tab)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_4, 7, 1, 1, 1)

        self.line_4 = QFrame(self.tab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_4, 5, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.tab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_3, 4, 1, 1, 1)

        self.line_11 = QFrame(self.tab)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_11, 5, 0, 1, 1)

        self.line_12 = QFrame(self.tab)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_12, 5, 2, 1, 1)

        self.line_13 = QFrame(self.tab)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_13, 3, 1, 1, 1)

        self.line_14 = QFrame(self.tab)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_14, 3, 2, 1, 1)

        self.line_15 = QFrame(self.tab)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_15, 1, 1, 1, 1)

        self.line_16 = QFrame(self.tab)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.Shape.HLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_16, 1, 2, 1, 1)

        self.line_17 = QFrame(self.tab)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.Shape.HLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_17, 8, 2, 1, 1)

        self.line_18 = QFrame(self.tab)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.Shape.HLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_18, 8, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 2, 1, 1, 2)

        self.listView = QListView(self.tab)
        self.listView.setObjectName(u"listView")

        self.gridLayout_3.addWidget(self.listView, 3, 1, 1, 2)

        self.line_10 = QFrame(self.tab)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_10, 4, 1, 1, 1)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line, 5, 1, 1, 1)

        self.line_20 = QFrame(self.tab)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.Shape.HLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_20, 5, 2, 1, 1)

        self.line_19 = QFrame(self.tab)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.Shape.HLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_19, 6, 1, 1, 2)


        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.Send = QWidget()
        self.Send.setObjectName(u"Send")
        self.gridLayout_8 = QGridLayout(self.Send)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_6 = QPushButton(self.Send)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_6.addWidget(self.pushButton_6, 1, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.Send)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_6.addWidget(self.pushButton_8, 3, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.Send)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_6.addWidget(self.pushButton_9, 4, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.Send)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_5.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.pushButton_5.setToolTipDuration(0)

        self.gridLayout_6.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.Send)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_6.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.Send)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEdit_5, 4, 2, 1, 1)

        self.lineEdit_6 = QLineEdit(self.Send)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEdit_6, 3, 2, 1, 1)

        self.line_23 = QFrame(self.Send)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShadow(QFrame.Shadow.Raised)
        self.line_23.setLineWidth(9)
        self.line_23.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_6.addWidget(self.line_23, 2, 2, 1, 1)

        self.label_5 = QLabel(self.Send)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_5.setAutoFillBackground(True)
        self.label_5.setStyleSheet(u"font: 600 16pt \"URW Bookman\";")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_5, 0, 2, 1, 1)

        self.line_24 = QFrame(self.Send)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.Shape.VLine)
        self.line_24.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.line_24, 0, 1, 1, 1)

        self.line_25 = QFrame(self.Send)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.Shape.VLine)
        self.line_25.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.line_25, 1, 1, 1, 1)

        self.graphicsView = QGraphicsView(self.Send)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_6.addWidget(self.graphicsView, 1, 2, 1, 1)

        self.label_6 = QLabel(self.Send)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_6, 3, 1, 1, 1)

        self.label_7 = QLabel(self.Send)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_7, 4, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.Send)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"font: 600 11pt \"Ubuntu Sans\";")

        self.gridLayout_6.addWidget(self.pushButton_10, 2, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Send, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.line_2 = QFrame(Main)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.progress = QProgressBar(Main)
        self.progress.setObjectName(u"progressBar")
        self.progress.setValue(0)

        self.gridLayout_2.addWidget(self.progress, 1, 0, 1, 1)


        self.retranslateUi(Main)

        self.tabWidget.setCurrentIndex(1)
        
        self.pushButton.clicked.connect(self.button3Clicked)
        self.pushButton_2.clicked.connect(self.button2Clicked_x)
        self.pushButton_3.clicked.connect(self.b5Clicked_z)
        self.pushButton_4.clicked.connect(self.b4Clicked_y)
        self.pushButton_5.clicked.connect(self.sendTo_CNC)
        self.pushButton_6.clicked.connect(self.matplotlib_plot)
        self.pushButton_7.clicked.connect(self.gcode_coords)
        self.pushButton_8.clicked.connect(self.imageshow_plot)
        self.pushButton_9.clicked.connect(self.sculpting)
        self.pushButton_10.clicked.connect(self.imageshow)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        # _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(QCoreApplication.translate("Main", u"CNC", None))
        self.label_4.setText(QCoreApplication.translate("Main", u"[mm]", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Main", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("Main", u"Move ALL", None))
        self.pushButton_4.setText(QCoreApplication.translate("Main", u"Y", None))
        self.pushButton_3.setText(QCoreApplication.translate("Main", u"Z", None))
        self.lineEdit.setText(QCoreApplication.translate("Main", u"50", None))
        self.label_2.setText(QCoreApplication.translate("Main", u"[mm]", None))
        self.label_3.setText(QCoreApplication.translate("Main", u"[mm]", None))
        self.label.setText(QCoreApplication.translate("Main", u"scale: [step/mm]", None))
        self.pushButton_2.setText(QCoreApplication.translate("Main", u"X", None))
        self.lineEdit_4.setText(QCoreApplication.translate("Main", u"0", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Main", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Main", u"Move Engines", None))
        self.pushButton_6.setText(QCoreApplication.translate("Main", u"Plot coords\n"
"in\n"
"Matplotlib", None))
        self.pushButton_8.setText(QCoreApplication.translate("Main", u"Plot\n"
"Image", None))
        self.pushButton_9.setText(QCoreApplication.translate("Main", u"Sculpt\n"
"Image", None))
        self.pushButton_5.setText(QCoreApplication.translate("Main", u"Send coords", None))
        self.pushButton_7.setText(QCoreApplication.translate("Main", u"Load\n"
"GCODE", None))
        self.lineEdit_5.setText(QCoreApplication.translate("Main", u"0.004", None))
        self.lineEdit_6.setText(QCoreApplication.translate("Main", u"1", None))
        self.label_5.setText(QCoreApplication.translate("Main", u"Preview:", None))
        self.label_6.setText(QCoreApplication.translate("Main", u"Z-scale: mm/gv", None))
        self.label_7.setText(QCoreApplication.translate("Main", u"XY-scale: mm/px", None))
        self.pushButton_10.setText(QCoreApplication.translate("Main", u"Drill\n"
"Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Send), QCoreApplication.translate("Main", u"Sending and work", None))
    # retranslateUi
    def matplotlib_plot(self):
        file = QFileDialog.getOpenFileName(MainWindow, "Open File", "", "All Files (*)")
        if file[0]:
            temp = []
            f = open(file[0], "r",encoding='utf-8')
            for line in f:
                el=line.split("   ")
                temp.append([float(el[0]),float(el[1]),float(el[2])])
            f.close()
            temp_array = np.array(temp)
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            x, y, z = temp_array.T
            ax.plot(x, y, z, c='r', linestyle='-', label='Lines', linewidth=0.07)
            ax.set_xlabel('X-axis')
            ax.set_ylabel('Y-axis')
            ax.set_zlabel('Z-axis')
            ax.legend()
            plt.show()
    def send_gcode_To_CNC(self,file):
        global step_per_rev
        global com
        global pico_ip
        global port
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((pico_ip, port))
        except ConnectionError as e:
            print("wifi fail!")
            sys.exit(1)
        

        steps_per_mm = int(step_per_rev / 0.8)
        
        temp = np.asarray(file, dtype=np.float32)
        now = datetime.now()
        fname = now.strftime(f"%d_%m_%Y__%H_%M_%S_sended")
        f2 = open(str(fname) + ".txt", "w")
        com=str(self.COMs.text())
        try:
            s = serial.Serial(com, 115200)
        except Exception as e:
            pass
        
        for index in range(0, len(temp), 1):
            if index>=1:
                delta_x = int((temp[index-1,0]-temp[index,0]) * steps_per_mm)
                delta_y = int((temp[index-1,1]-temp[index,1]) * steps_per_mm)
                delta_z = int((temp[index-1,2]-temp[index,2]) * steps_per_mm)
                
                data = f"{delta_x} {delta_y} {delta_z}\n"
                # s.write(data.encode("utf-8"))
                client_socket.sendall(data.encode())
                f2.write(f"{delta_x} {delta_y} {delta_z}\n")
            self.progress.setValue(int(np.floor(float(100.0*index/len(temp)))))
            
            while True:
                a = client_socket.recv(5)
                print(a)
                
                if a == "ok":
                    
                    break
            # print("ok")
            print(index)
        
        # f.close()
        f2.close()
    def gcode_coords(self):
        # global step_per_rev
        # steps_per_mm = int(step_per_rev / 0.8)
        file = QFileDialog.getOpenFileName(MainWindow, "Open File", "", "All Files (*)")
        if file[0]:
            temp = []
            f = open(file[0], "r",encoding='utf-8')

            def arch_cw(x_prev, y_prev, i, j, x, y):
                radius = 0.0
                angle_arch = 0.0

                try:
                    if i == 0.0 and j == 0.0:
                        angle_arch = 0.0
                    else:
                        radius = np.sqrt(i**2 + j**2)
                        ai_denominator = (y_prev - j)
                        axy_denominator = (x_prev + i - x)
                        
                        if abs(ai_denominator) < 1e-6 or abs(axy_denominator) < 1e-6:
                            ai = 0.0
                            axy = 0.0
                        else:
                            ai = (x_prev - i) / ai_denominator
                            axy = (y_prev + j - y) / axy_denominator
                        
                        if (1 + ai * axy) < 1e-6:
                            angle_arch = 0.0
                        else:
                            angle_arch = np.arctan(abs(ai - axy) / (1 + ai * axy))
                            
                        if x == x_prev and y == y_prev:
                            angle_arch = 2 * np.pi
                        if x < x_prev or y < y_prev:
                            angle_arch = 2 * np.pi - angle_arch

                    decrement = 0.01
                    arc_points = []
                    while angle_arch >= 0.0:
                        angle_arch -= decrement
                        x_arc = i + radius * np.cos(angle_arch)
                        y_arc = j + radius * np.sin(angle_arch)
                        arc_points.append((x_arc, y_arc))

                    return arc_points
                except Exception as e:
                    print(f"Error in arch_cw: {e}")
                    return []
            def arch_ccw(x_prev, y_prev, i, j, x, y):
                radius = 0.0
                angle_arch = 0.0

                try:
                    if i == 0.0 and j == 0.0:
                        angle_arch = 0.0
                    else:
                        radius = np.sqrt(i**2 + j**2)
                        ai_denominator = (y_prev - j)
                        axy_denominator = (x_prev + i - x)
                        
                        if abs(ai_denominator) < 1e-6 or abs(axy_denominator) < 1e-6:
                            ai = 0.0
                            axy = 0.0
                        else:
                            ai = (x_prev - i) / ai_denominator
                            axy = (y_prev + j - y) / axy_denominator
                        
                        if (1 + ai * axy) < 1e-6:
                            angle_arch = 0.0
                        else:
                            angle_arch = np.arctan(abs(ai - axy) / (1 + ai * axy))
                            
                        if x == x_prev and y == y_prev:
                            angle_arch = 2 * np.pi
                        if x < x_prev or y < y_prev:
                            angle_arch = 2 * np.pi - angle_arch

                    increment = 0.01
                    arc_points = []
                    dummy=0.0
                    while dummy <= angle_arch:
                        angle_arch += increment
                        x_arc = i + radius * np.cos(dummy)
                        y_arc = j + radius * np.sin(dummy)
                        arc_points.append((x_arc, y_arc))

                    return arc_points
                except Exception as e:
                    print(f"Error in arch_cw: {e}")
                    return []
            
            lines = [line for line in f]
            temp = []
            index = 0
            z = 0.0
            x = 0.0
            y = 0.0
            x_prev = 0.0
            y_prev = 0.0
            # z_prev = 0.0
# 
            for line2 in lines:
                try:
                    x_prev = x
                    y_prev = y
                    # z_prev = z
                    i = 0.0
                    j = 0.0
                    feed_rate = 1.0
                    k = 0.0
                    g = 0.0
                    parts = re.findall(r'([A-Z]+)([+-]?\d+(?:\.\d+)?)', line2)
                    for part in parts:
                        code, value = part
                        value = float(value)
                        if code == 'X':
                            x = value
                        if code == 'Y':
                            y = value
                        if code == 'Z':
                            z = value
                        if code == 'I':
                            i = value
                        if code == 'J':
                            j = value
                        if code == 'K':
                            k = value
                        if code == 'F':
                            feed_rate = value
                        if code == 'G':
                            g = value
                        
                    if i != 0.0 or j != 0.0:
                        if g==2:
                            arc_points = arch_cw(x_prev, y_prev, i, j, x, y)
                        if g==3:
                            arc_points = arch_ccw(x_prev, y_prev, i, j, x, y)
                        for point in arc_points:
                            x1, y1 = point
                            x1 = x_prev + x1
                            y1 = y_prev + y1
                            temp.append([x1, y1, z])
                    else:
                        temp.append([x, y, z])
                    
                    index += 1
                    self.progress.setValue(int(np.floor(float(100.0*index/len(lines)))))

                except Exception as e:
                    print(f"Error parsing line: {line2}")
                    print(f"Error message: {e}")
            now = datetime.now()
            fname=now.strftime(f"%d_%m_%Y__%H_%M_%S_gcode-decoded")
            f2=open(str(fname)+".txt","w")
            index=0
            for element in temp:
                index+=1
                f2.writelines(str(element[0])+"   "+str(element[1])+"   "+str(element[2])+"\n")
                self.progress.setValue(int(np.floor(float(100.0*index/len(temp)))))
            f2.close()
    def sendTo_CNC(self):
        global step_per_rev
        global com
        global pico_ip
        global port
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((pico_ip, port))
        

        steps_per_mm = int(step_per_rev / 0.8)
        file = QFileDialog.getOpenFileName(MainWindow, "Open File", "", "All Files (*)")
        if file[0]:
            temp = []
            with open(file[0], "r") as f:
                indexx=0
                for line in f:
                    parts = re.findall(r"[-+]?\d*\.\d+|\d+(?:[eE][-+]?\d+)?", line)
                    indexx+=1
                    try:
                        a, b, c = map(float, parts)
                        temp.append([a, b, c])
                    except ValueError as e:
                        print("Error parsing line:", line)
            print(1)
            f.close()

            temp = np.asarray(temp)
            now = datetime.now()
            fname = now.strftime(f"%d_%m_%Y__%H_%M_%S_sended")
            f2 = open(str(fname) + ".txt", "w")
            try:
                com=str(self.COMs.text())
                s = serial.Serial(com, 115200)
            except:
                print(Exception)
            print(2)
            indexxx=0
            print(len(temp))
            while True:
                print(indexxx)
                if indexxx>=1:
                    print(indexxx)
                    delta_x = int((temp[indexxx-1,0]-temp[indexxx,0]) * steps_per_mm)
                    delta_y = int((temp[indexxx-1,1]-temp[indexxx,1]) * steps_per_mm)
                    delta_z = int((temp[indexxx-1,2]-temp[indexxx,2]) * steps_per_mm)
                    
                    data = f"{delta_x} {delta_y} {delta_z}\n"
                    print(3)
                    try:
                        # s.write(data.encode("utf-8"))
                        client_socket.sendall(data.encode())
                        print(4)
                    except:
                        print(Exception)
                    f2.write(data)
                    self.progress.setValue(int(np.floor(float(100.0*indexxx/len(temp)))))
                
                    while True:
                        a = client_socket.recv(5)
                        print(a)
                        
                        if a == "ok":
                            break
                indexxx+=1
                if indexxx>=len(temp):
                    break
                # print("ok")
                print(indexxx)

    def coord(self,file):  
        
        now = datetime.now()
        fname=now.strftime(f"%d_%m_%Y__%H_%M_%S_drill")
        f=open(str(fname)+".txt","w")
        array=np.asanyarray(file)
        scaleXY=float(str(self.lineEdit_6.text()))
        scaleZ=float(str(self.lineEdit_5.text()))

        for row in range(len(array)):
            if row % 2 == 0:
                for column in range(len(array[0])):
                    x=row*scaleXY
                    y=column*scaleXY
                    if np.shape(array) == (len(array),len(array[0]),3):
                        if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>0:
                            z=(255.0-array[row,column,0]/3-array[row,column,1]/3-array[row,column,2]/3)*scaleZ+1*scaleZ
                    if np.shape(array) == (len(array),len(array[0]),4): #_____________________________________format typu PNG ma 4 wartości - kształt tensora: (x, y, 4)
                        if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>0:
                            z=(255.0-array[row,column,0]/3-array[row,column,1]/3-array[row,column,2]/3)*scaleZ+1*scaleZ
                    if np.shape(array) == (len(array),len(array[0]),1):
                        if (array[row,column,0])>0:
                            z=(255.0-array[row,column,0])*scaleZ+1*scaleZ
                    if np.shape(array) == (len(array),len(array[0])):
                        if (array[row,column])>0:
                            z=(255.0-array[row,column])*scaleZ+1*scaleZ
                    if z>0:
                        f.writelines(str(x)+"   "+str(y)+"   "+str(0.0)+"\n")
                        f.writelines(str(x)+"   "+str(y)+"   "+str(z)+"\n")
                        f.writelines(str(x)+"   "+str(y)+"   "+str(0.0)+"\n")
            if row % 2 == 1:
                for column in range(len(array[0])-1,-1,-1):
                    x=row*scaleXY
                    y=column*scaleXY
                    if np.shape(array) == (len(array),len(array[0]),3):
                        if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>0:
                            z=(255.0-array[row,column,0]/3-array[row,column,1]/3-array[row,column,2]/3)*scaleZ+1*scaleZ
                    if np.shape(array) == (len(array),len(array[0]),4):
                        if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>0:
                            z=(255.0-array[row,column,0]/3-array[row,column,1]/3-array[row,column,2]/3)*scaleZ+1*scaleZ
                    if np.shape(array) == (len(array),len(array[0]),1):
                        if (array[row,column,0])>0:
                            z=(255.0-array[row,column,0])*scaleZ+1*scaleZ
                    if np.shape(array) == (len(array),len(array[0])):
                        if (array[row,column])>0:
                            z=(255.0-array[row,column])*scaleZ+1*scaleZ
                    if z>0:
                        f.writelines(str(x)+"   "+str(y)+"   "+str(0.0)+"\n")
                        f.writelines(str(x)+"   "+str(y)+"   "+str(z)+"\n")
                        f.writelines(str(x)+"   "+str(y)+"   "+str(0.0)+"\n")
            self.progress.setValue(int(np.floor(float(100.0*row/len(array)))))
        f.close()
                

    def imageshow(self): #
        file=QFileDialog.getOpenFileName(MainWindow, "Open File", "", "All Files (*)") 
        if file[0]:
            image = QImage(file[0])
            fibrile=Image.open(file[0])

            self.scene.addPixmap(QPixmap(image))
            self.graphicsView.setScene(self.scene)
            Ui_Main.coord(self,fibrile)

    def button3Clicked(self):   
        global step_per_rev 
        global com
        global pico_ip
        global port
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((pico_ip, port))

        scale=float(self.lineEdit.text())
        steps_y=int(float(self.lineEdit_3.text())/scale)
        steps_x=int(float(self.lineEdit_2.text())/scale)
        steps_z=int(float(self.lineEdit_4.text())/scale)
        com=str(self.COMs.text())
        s = serial.Serial(com, 115200)
        data = f"{steps_x} {steps_y} {steps_z}\n"
        # s.write(data.encode("utf-8"))
        client_socket.sendall(data.encode())
        
    def button2Clicked_x(self):
        
        global step_per_rev 
        global com
        global pico_ip
        global port
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((pico_ip, port))
        scale=float(self.lineEdit.text())
        steps=np.floor(float(self.lineEdit_2.text()))
        com=str(self.COMs.text())
        s = serial.Serial(com, 115200)
        data = f"{int(steps/scale)} {0} {0}\n"
        # s.write(data.encode("utf-8"))
        client_socket.sendall(data.encode())

    def b4Clicked_y(self):  
        global step_per_rev
        global com 
        global pico_ip
        global port
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((pico_ip, port))
        scale=float(self.lineEdit.text())
        steps=np.floor(float(self.lineEdit_3.text()))
        com=str(self.COMs.text())
        s = serial.Serial(com, 115200)
        data = f"{0} {int(steps/scale)} {0}\n"
        client_socket.sendall(data.encode())
        # s.write(data.encode("utf-8"))
       
    def b5Clicked_z(self):   
        global step_per_rev 
        global com
        global pico_ip
        global port
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((pico_ip, port))
        scale=float(self.lineEdit.text())
        steps=np.floor(float(self.lineEdit_4.text()))
        com=str(self.COMs.text())
        print(com)
        s = serial.Serial(com, 115200)
        data = f"{0} {0} {int(steps/scale)}\n"
        try:
            # s.write(data.encode("utf-8"))
            client_socket.sendall(data.encode())
        except Exception as e:
            print(e)


    def coord_plot(self,file):   
        now = datetime.now()
        fname=now.strftime(f"%d_%m_%Y__%H_%M_%S_plot")
        f=open(str(fname)+".txt","w")
        array=np.asanyarray(file)
        scaleXY=float(str(self.lineEdit_6.text()))
        scaleZ=float(str(self.lineEdit_5.text()))

        for row in range(len(array)):
            if row % 2 == 0:
                for column in range(len(array[0])):
                        x=row*scaleXY
                        y=column*scaleXY
                        if np.shape(array) == (len(array),len(array[0]),3):
                            if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>0:
                                    z=1*scaleZ
                            else:
                                    z=0
                        if np.shape(array) == (len(array),len(array[0]),4): #_____________________________________format typu PNG ma 4 wartości - kształt tensora: (x, y, 4)
                            if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>0:
                                    z=1/scaleZ
                            else:
                                    z=0
                        if np.shape(array) == (len(array),len(array[0]),1):
                            if (array[row,column,0])>0:
                                    z=1/scaleZ
                            else:
                                    z=0
                        if np.shape(array) == (len(array),len(array[0])):
                            if (array[row,column])>0:
                                    z=1/scaleZ
                            else:
                                    z=0
                        f.writelines(str(x)+"   "+str(y)+"   "+str(z)+"\n")
            if row % 2 == 1:
                for column in range(len(array[0])-1,-1,-1):
                        x=row*scaleXY
                        y=column*scaleXY
                        if np.shape(array) == (len(array),len(array[0]),3):
                            if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>0:
                                    z=1*scaleZ
                            else:
                                    z=0
                        if np.shape(array) == (len(array),len(array[0]),4): 
                            if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>0:
                                    z=1*scaleZ
                            else:
                                    z=0
                        if np.shape(array) == (len(array),len(array[0]),1):
                            if (array[row,column,0])>0:
                                    z=1*scaleZ
                            else:
                                    z=0
                        if np.shape(array) == (len(array),len(array[0])):
                            if (array[row,column])>0:
                                    z=1*scaleZ
                            else:
                                    z=0
                        f.writelines(str(x)+"   "+str(y)+"   "+str(z)+"\n")
            self.progress.setValue(int(np.floor(float(100.0*row/len(array)))))
        f.close()

    def sculpting(self,file):
        file=QFileDialog.getOpenFileName(MainWindow, "Open File", "", "All Files (*)") 
        if file[0]:
            image = QImage(file[0])
            fibrile=Image.open(file[0])

            self.scene.addPixmap(QPixmap(image))
            self.graphicsView.setScene(self.scene)
            now = datetime.now()
            fname=now.strftime(f"%d_%m_%Y__%H_%M_%S_sculpt")
            f=open(str(fname)+".txt","w")
            array=np.asanyarray(fibrile)

        
            scaleXY=float(str(self.lineEdit_6.text()))
            scaleZ=float(str(self.lineEdit_5.text()))
            ind=0

            for row in range(len(array)):
                ind+=1
                if row % 2 == 0:
                    for column in range(len(array[0])):
                            x=row*scaleXY
                            y=column*scaleXY
                            if np.shape(array) == (len(array),len(array[0]),3):
                                if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>=0:
                                    z=(array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)*scaleZ

                            if np.shape(array) == (len(array),len(array[0]),4): 
                                if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>=0:
                                    z=(array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)*scaleZ

                            if np.shape(array) == (len(array),len(array[0]),1):
                                if (array[row,column,0])>=0:
                                    z=array[row,column,0]*scaleZ

                            if np.shape(array) == (len(array),len(array[0])):
                                if (array[row,column])>=0:
                                    z=array[row,column]*scaleZ

                            f.writelines(str(x)+"   "+str(y)+"   "+str(z)+"\n")

                if row % 2 == 1:
                    for column in range(len(array[0])-1,-1,-1):
                        x=row*scaleXY
                        y=column*scaleXY
                        if np.shape(array) == (len(array),len(array[0]),3):
                            if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>=0:
                                z=(array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)*scaleZ

                        if np.shape(array) == (len(array),len(array[0]),4): 
                            if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>=0:
                                z=(array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)*scaleZ

                        if np.shape(array) == (len(array),len(array[0]),1):
                            if (array[row,column,0])>=0:
                                z=(array[row,column,0])*scaleZ

                        if np.shape(array) == (len(array),len(array[0])):
                            if (array[row,column])>=0:
                                z=(array[row,column])*scaleZ
                        f.writelines(str(x)+"   "+str(y)+"   "+str(z)+"\n")
                self.progress.setValue(int(np.floor(float(100.0*row/len(array)))))
        f.close()
    def imageshow_plot(self): 
        file=QFileDialog.getOpenFileName(MainWindow, "Open File", "", "All Files (*)")
        if file[0]:
            image = QImage(file[0])
            fibrile=Image.open(file[0])

            self.scene.addPixmap(QPixmap(image))
            self.graphicsView.setScene(self.scene)
            self.coord_plot(fibrile)


    def matplotlib_plot(self):
        file = QFileDialog.getOpenFileName(MainWindow, "Open File", "", "All Files (*)")
        if file[0]:
            temp = []
            f = open(file[0], "r",encoding='utf-8')
            for line in f:
                el=line.split("   ")
                temp.append([float(el[0]),float(el[1]),float(el[2])])
            f.close()
            temp_array = np.array(temp)
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            x, y, z = temp_array.T
            ax.plot(x, y, z, c='r', linestyle='-', label='Lines', linewidth=0.07)
            ax.set_xlabel('X-axis')
            ax.set_ylabel('Y-axis')
            ax.set_zlabel('Z-axis')
            ax.legend()
            plt.show()
    def send_gcode_To_CNC(self,file):
        global step_per_rev
        global com
        global pico_ip
        global port
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((pico_ip, port))

        steps_per_mm = int(step_per_rev / 0.8)
        
        temp = np.asarray(file, dtype=np.float32)
        now = datetime.now()
        fname = now.strftime(f"%d_%m_%Y__%H_%M_%S_sended")
        f2 = open(str(fname) + ".txt", "w")
        com=str(self.COMs.text())
        try:
            s = serial.Serial(com, 115200)
        except Exception as e:
            pass
        
        for index in range(0, len(temp), 1):
            if index>=1:
                delta_x = int((temp[index-1,0]-temp[index,0]) * steps_per_mm)
                delta_y = int((temp[index-1,1]-temp[index,1]) * steps_per_mm)
                delta_z = int((temp[index-1,2]-temp[index,2]) * steps_per_mm)
                
                data = f"{delta_x} {delta_y} {delta_z}\n"
                # s.write(data.encode("utf-8"))
                client_socket.sendall(data.encode())
                f2.write(f"{delta_x} {delta_y} {delta_z}\n")
            self.progress.setValue(int(np.floor(float(100.0*index/len(temp)))))
            
            while True:
                a = client_socket.recv(5)
                print(a)
                
                if a == "ok":
                    
                    break
            # print("ok")
            print(index)
        
        # f.close()
        f2.close()
    def gcode_coords(self):
        # global step_per_rev
        # steps_per_mm = int(step_per_rev / 0.8)
        file = QFileDialog.getOpenFileName(MainWindow, "Open File", "", "All Files (*)")
        if file[0]:
            temp = []
            f = open(file[0], "r",encoding='utf-8')

            def arch_cw(x_prev, y_prev, i, j, x, y):
                radius = 0.0
                angle_arch = 0.0

                try:
                    if i == 0.0 and j == 0.0:
                        angle_arch = 0.0
                    else:
                        radius = np.sqrt(i**2 + j**2)
                        ai_denominator = (y_prev - j)
                        axy_denominator = (x_prev + i - x)
                        
                        if abs(ai_denominator) < 1e-6 or abs(axy_denominator) < 1e-6:
                            ai = 0.0
                            axy = 0.0
                        else:
                            ai = (x_prev - i) / ai_denominator
                            axy = (y_prev + j - y) / axy_denominator
                        
                        if (1 + ai * axy) < 1e-6:
                            angle_arch = 0.0
                        else:
                            angle_arch = np.arctan(abs(ai - axy) / (1 + ai * axy))
                            
                        if x == x_prev and y == y_prev:
                            angle_arch = 2 * np.pi
                        if x < x_prev or y < y_prev:
                            angle_arch = 2 * np.pi - angle_arch

                    decrement = 0.01
                    arc_points = []
                    while angle_arch >= 0.0:
                        angle_arch -= decrement
                        x_arc = i + radius * np.cos(angle_arch)
                        y_arc = j + radius * np.sin(angle_arch)
                        arc_points.append((x_arc, y_arc))

                    return arc_points
                except Exception as e:
                    print(f"Error in arch_cw: {e}")
                    return []
            def arch_ccw(x_prev, y_prev, i, j, x, y):
                radius = 0.0
                angle_arch = 0.0

                try:
                    if i == 0.0 and j == 0.0:
                        angle_arch = 0.0
                    else:
                        radius = np.sqrt(i**2 + j**2)
                        ai_denominator = (y_prev - j)
                        axy_denominator = (x_prev + i - x)
                        
                        if abs(ai_denominator) < 1e-6 or abs(axy_denominator) < 1e-6:
                            ai = 0.0
                            axy = 0.0
                        else:
                            ai = (x_prev - i) / ai_denominator
                            axy = (y_prev + j - y) / axy_denominator
                        
                        if (1 + ai * axy) < 1e-6:
                            angle_arch = 0.0
                        else:
                            angle_arch = np.arctan(abs(ai - axy) / (1 + ai * axy))
                            
                        if x == x_prev and y == y_prev:
                            angle_arch = 2 * np.pi
                        if x < x_prev or y < y_prev:
                            angle_arch = 2 * np.pi - angle_arch

                    increment = 0.01
                    arc_points = []
                    dummy=0.0
                    while dummy <= angle_arch:
                        angle_arch += increment
                        x_arc = i + radius * np.cos(dummy)
                        y_arc = j + radius * np.sin(dummy)
                        arc_points.append((x_arc, y_arc))

                    return arc_points
                except Exception as e:
                    print(f"Error in arch_cw: {e}")
                    return []
            
            lines = [line for line in f]
            temp = []
            index = 0
            z = 0.0
            x = 0.0
            y = 0.0
            x_prev = 0.0
            y_prev = 0.0
            # z_prev = 0.0
# 
            for line2 in lines:
                try:
                    x_prev = x
                    y_prev = y
                    # z_prev = z
                    i = 0.0
                    j = 0.0
                    feed_rate = 1.0
                    k = 0.0
                    g = 0.0
                    parts = re.findall(r'([A-Z]+)([+-]?\d+(?:\.\d+)?)', line2)
                    for part in parts:
                        code, value = part
                        value = float(value)
                        if code == 'X':
                            x = value
                        if code == 'Y':
                            y = value
                        if code == 'Z':
                            z = value
                        if code == 'I':
                            i = value
                        if code == 'J':
                            j = value
                        if code == 'K':
                            k = value
                        if code == 'F':
                            feed_rate = value
                        if code == 'G':
                            g = value
                        
                    if i != 0.0 or j != 0.0:
                        if g==2:
                            arc_points = arch_cw(x_prev, y_prev, i, j, x, y)
                        if g==3:
                            arc_points = arch_ccw(x_prev, y_prev, i, j, x, y)
                        for point in arc_points:
                            x1, y1 = point
                            x1 = x_prev + x1
                            y1 = y_prev + y1
                            temp.append([x1, y1, z])
                    else:
                        temp.append([x, y, z])
                    
                    index += 1
                    self.progress.setValue(int(np.floor(float(100.0*index/len(lines)))))

                except Exception as e:
                    print(f"Error parsing line: {line2}")
                    print(f"Error message: {e}")
            now = datetime.now()
            fname=now.strftime(f"%d_%m_%Y__%H_%M_%S_gcode-decoded")
            f2=open(str(fname)+".txt","w")
            index=0
            for element in temp:
                index+=1
                f2.writelines(str(element[0])+"   "+str(element[1])+"   "+str(element[2])+"\n")
                self.progress.setValue(int(np.floor(float(100.0*index/len(temp)))))
            f2.close()
    def sendTo_CNC(self):
        global step_per_rev
        global com
        global pico_ip
        global port
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((pico_ip, port))

        steps_per_mm = int(step_per_rev / 0.8)
        file = QFileDialog.getOpenFileName(MainWindow, "Open File", "", "All Files (*)")
        if file[0]:
            temp = []
            with open(file[0], "r") as f:
                indexx=0
                for line in f:
                    parts = re.findall(r"[-+]?\d*\.\d+|\d+(?:[eE][-+]?\d+)?", line)
                    indexx+=1
                    try:
                        a, b, c = map(float, parts)
                        temp.append([a, b, c])
                    except ValueError as e:
                        print("Error parsing line:", line)
            print(1)
            f.close()

            temp = np.asarray(temp)
            now = datetime.now()
            fname = now.strftime(f"%d_%m_%Y__%H_%M_%S_sended")
            f2 = open(str(fname) + ".txt", "w")
            try:
                com=str(self.COMs.text())
                s = serial.Serial(com, 115200)
            except:
                print(Exception)
            print(2)
            indexxx=0
            print(len(temp))
            while True:
                print(indexxx)
                if indexxx>=1:
                    print(indexxx)
                    delta_x = int((temp[indexxx-1,0]-temp[indexxx,0]) * steps_per_mm)
                    delta_y = int((temp[indexxx-1,1]-temp[indexxx,1]) * steps_per_mm)
                    delta_z = int((temp[indexxx-1,2]-temp[indexxx,2]) * steps_per_mm)
                    
                    data = f"{delta_x} {delta_y} {delta_z}\n"
                    print(3)
                    try:
                        # s.write(data.encode("utf-8"))
                        client_socket.sendall(data.encode())
                        print(4)
                    except:
                        print(Exception)
                    f2.write(data)
                    self.progress.setValue(int(np.floor(float(100.0*indexxx/len(temp)))))
                
                    while True:
                        a = client_socket.recv(5)
                        print(a)
                        
                        if a == "ok":
                            break
                indexxx+=1
                if indexxx>=len(temp):
                    break
                # print("ok")
                print(indexxx)

    def coord(self,file):  
        
        now = datetime.now()
        fname=now.strftime(f"%d_%m_%Y__%H_%M_%S_drill")
        f=open(str(fname)+".txt","w")
        array=np.asanyarray(file)
        scaleXY=float(str(self.lineEdit_6.text()))
        scaleZ=float(str(self.lineEdit_5.text()))

        for row in range(len(array)):
            if row % 2 == 0:
                for column in range(len(array[0])):
                    x=row*scaleXY
                    y=column*scaleXY
                    if np.shape(array) == (len(array),len(array[0]),3):
                        if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>0:
                            z=(255.0-array[row,column,0]/3-array[row,column,1]/3-array[row,column,2]/3)*scaleZ+1*scaleZ
                    if np.shape(array) == (len(array),len(array[0]),4): #_____________________________________format typu PNG ma 4 wartości - kształt tensora: (x, y, 4)
                        if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>0:
                            z=(255.0-array[row,column,0]/3-array[row,column,1]/3-array[row,column,2]/3)*scaleZ+1*scaleZ
                    if np.shape(array) == (len(array),len(array[0]),1):
                        if (array[row,column,0])>0:
                            z=(255.0-array[row,column,0])*scaleZ+1*scaleZ
                    if np.shape(array) == (len(array),len(array[0])):
                        if (array[row,column])>0:
                            z=(255.0-array[row,column])*scaleZ+1*scaleZ
                    if z>0:
                        f.writelines(str(x)+"   "+str(y)+"   "+str(0.0)+"\n")
                        f.writelines(str(x)+"   "+str(y)+"   "+str(z)+"\n")
                        f.writelines(str(x)+"   "+str(y)+"   "+str(0.0)+"\n")
            if row % 2 == 1:
                for column in range(len(array[0])-1,-1,-1):
                    x=row*scaleXY
                    y=column*scaleXY
                    if np.shape(array) == (len(array),len(array[0]),3):
                        if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>0:
                            z=(255.0-array[row,column,0]/3-array[row,column,1]/3-array[row,column,2]/3)*scaleZ+1*scaleZ
                    if np.shape(array) == (len(array),len(array[0]),4):
                        if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>0:
                            z=(255.0-array[row,column,0]/3-array[row,column,1]/3-array[row,column,2]/3)*scaleZ+1*scaleZ
                    if np.shape(array) == (len(array),len(array[0]),1):
                        if (array[row,column,0])>0:
                            z=(255.0-array[row,column,0])*scaleZ+1*scaleZ
                    if np.shape(array) == (len(array),len(array[0])):
                        if (array[row,column])>0:
                            z=(255.0-array[row,column])*scaleZ+1*scaleZ
                    if z>0:
                        f.writelines(str(x)+"   "+str(y)+"   "+str(0.0)+"\n")
                        f.writelines(str(x)+"   "+str(y)+"   "+str(z)+"\n")
                        f.writelines(str(x)+"   "+str(y)+"   "+str(0.0)+"\n")
            self.progress.setValue(int(np.floor(float(100.0*row/len(array)))))
        f.close()
                

    def imageshow(self): #
        file=QFileDialog.getOpenFileName(MainWindow, "Open File", "", "All Files (*)") 
        if file[0]:
            image = QImage(file[0])
            fibrile=Image.open(file[0])

            self.scene.addPixmap(QPixmap(image))
            self.graphicsView.setScene(self.scene)
            Ui_Main.coord(self,fibrile)

    def button3Clicked(self):   
        global step_per_rev 
        global com
        global pico_ip
        global port
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((pico_ip, port))

        scale=float(self.lineEdit.text())
        steps_y=int(float(self.lineEdit_3.text())/scale)
        steps_x=int(float(self.lineEdit_2.text())/scale)
        steps_z=int(float(self.lineEdit_4.text())/scale)
        com=str(self.COMs.text())
        s = serial.Serial(com, 115200)
        data = f"{steps_x} {steps_y} {steps_z}\n"
        # s.write(data.encode("utf-8"))
        client_socket.sendall(data.encode())
        
    def button2Clicked_x(self):
        
        global step_per_rev 
        global com
        global pico_ip
        global port
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((pico_ip, port))
        scale=float(self.lineEdit.text())
        steps=np.floor(float(self.lineEdit_2.text()))
        com=str(self.COMs.text())
        s = serial.Serial(com, 115200)
        data = f"{int(steps/scale)} {0} {0}\n"
        # s.write(data.encode("utf-8"))
        client_socket.sendall(data.encode())

    def b4Clicked_y(self):  
        global step_per_rev
        global com 
        global pico_ip
        global port
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((pico_ip, port))
        scale=float(self.lineEdit.text())
        steps=np.floor(float(self.lineEdit_3.text()))
        com=str(self.COMs.text())
        s = serial.Serial(com, 115200)
        data = f"{0} {int(steps/scale)} {0}\n"
        client_socket.sendall(data.encode())
        # s.write(data.encode("utf-8"))

    def b5Clicked_z(self):   
        global step_per_rev 
        global com
        global pico_ip
        global port
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((pico_ip, port))
        scale=float(self.lineEdit.text())
        steps=np.floor(float(self.lineEdit_4.text()))
        com=str(self.COMs.text())
        print(com)
        s = serial.Serial(com, 115200)
        data = f"{0} {0} {int(steps/scale)}\n"
        try:
            # s.write(data.encode("utf-8"))
            client_socket.sendall(data.encode())
        except Exception as e:
            print(e)


    def coord_plot(self,file):   
        now = datetime.now()
        fname=now.strftime(f"%d_%m_%Y__%H_%M_%S_plot")
        f=open(str(fname)+".txt","w")
        array=np.asanyarray(file)
        scaleXY=float(str(self.lineEdit_6.text()))
        scaleZ=float(str(self.lineEdit_5.text()))

        for row in range(len(array)):
            if row % 2 == 0:
                for column in range(len(array[0])):
                        x=row*scaleXY
                        y=column*scaleXY
                        if np.shape(array) == (len(array),len(array[0]),3):
                            if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>0:
                                    z=1*scaleZ
                            else:
                                    z=0
                        if np.shape(array) == (len(array),len(array[0]),4): #_____________________________________format typu PNG ma 4 wartości - kształt tensora: (x, y, 4)
                            if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>0:
                                    z=1/scaleZ
                            else:
                                    z=0
                        if np.shape(array) == (len(array),len(array[0]),1):
                            if (array[row,column,0])>0:
                                    z=1/scaleZ
                            else:
                                    z=0
                        if np.shape(array) == (len(array),len(array[0])):
                            if (array[row,column])>0:
                                    z=1/scaleZ
                            else:
                                    z=0
                        f.writelines(str(x)+"   "+str(y)+"   "+str(z)+"\n")
            if row % 2 == 1:
                for column in range(len(array[0])-1,-1,-1):
                        x=row*scaleXY
                        y=column*scaleXY
                        if np.shape(array) == (len(array),len(array[0]),3):
                            if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>0:
                                    z=1*scaleZ
                            else:
                                    z=0
                        if np.shape(array) == (len(array),len(array[0]),4): 
                            if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>0:
                                    z=1*scaleZ
                            else:
                                    z=0
                        if np.shape(array) == (len(array),len(array[0]),1):
                            if (array[row,column,0])>0:
                                    z=1*scaleZ
                            else:
                                    z=0
                        if np.shape(array) == (len(array),len(array[0])):
                            if (array[row,column])>0:
                                    z=1*scaleZ
                            else:
                                    z=0
                        f.writelines(str(x)+"   "+str(y)+"   "+str(z)+"\n")
            self.progress.setValue(int(np.floor(float(100.0*row/len(array)))))
        f.close()

    def sculpting(self,file):
        file=QFileDialog.getOpenFileName(MainWindow, "Open File", "", "All Files (*)") 
        if file[0]:
            image = QImage(file[0])
            fibrile=Image.open(file[0])

            self.scene.addPixmap(QPixmap(image))
            self.graphicsView.setScene(self.scene)
            now = datetime.now()
            fname=now.strftime(f"%d_%m_%Y__%H_%M_%S_sculpt")
            f=open(str(fname)+".txt","w")
            array=np.asanyarray(fibrile)

        
            scaleXY=float(str(self.lineEdit_6.text()))
            scaleZ=float(str(self.lineEdit_5.text()))
            ind=0

            for row in range(len(array)):
                ind+=1
                if row % 2 == 0:
                    for column in range(len(array[0])):
                            x=row*scaleXY
                            y=column*scaleXY
                            if np.shape(array) == (len(array),len(array[0]),3):
                                if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>=0:
                                    z=(array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)*scaleZ

                            if np.shape(array) == (len(array),len(array[0]),4): 
                                if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>=0:
                                    z=(array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)*scaleZ

                            if np.shape(array) == (len(array),len(array[0]),1):
                                if (array[row,column,0])>=0:
                                    z=array[row,column,0]*scaleZ

                            if np.shape(array) == (len(array),len(array[0])):
                                if (array[row,column])>=0:
                                    z=array[row,column]*scaleZ

                            f.writelines(str(x)+"   "+str(y)+"   "+str(z)+"\n")

                if row % 2 == 1:
                    for column in range(len(array[0])-1,-1,-1):
                        x=row*scaleXY
                        y=column*scaleXY
                        if np.shape(array) == (len(array),len(array[0]),3):
                            if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>=0:
                                z=(array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)*scaleZ

                        if np.shape(array) == (len(array),len(array[0]),4): 
                            if (array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)>=0:
                                z=(array[row,column,0]/3+array[row,column,1]/3+array[row,column,2]/3)*scaleZ

                        if np.shape(array) == (len(array),len(array[0]),1):
                            if (array[row,column,0])>=0:
                                z=(array[row,column,0])*scaleZ

                        if np.shape(array) == (len(array),len(array[0])):
                            if (array[row,column])>=0:
                                z=(array[row,column])*scaleZ
                        f.writelines(str(x)+"   "+str(y)+"   "+str(z)+"\n")
                self.progress.setValue(int(np.floor(float(100.0*row/len(array)))))
        f.close()
    def imageshow_plot(self): 
        file=QFileDialog.getOpenFileName(MainWindow, "Open File", "", "All Files (*)")
        if file[0]:
            image = QImage(file[0])
            fibrile=Image.open(file[0])

            self.scene.addPixmap(QPixmap(image))
            self.graphicsView.setScene(self.scene)
            self.coord_plot(fibrile)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()  
    ui = Ui_Main()
    ui.setupUi(MainWindow)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((pico_ip, port))
    MainWindow.show()
    print("Window should now be visible.")
    
    sys.exit(app.exec())
    client_socket.close()
