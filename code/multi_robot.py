#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 16:03:17 2022

@author: hasan
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import threading
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import robots


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 400)
        MainWindow.setMinimumSize(QtCore.QSize(540, 400))
        MainWindow.setMaximumSize(QtCore.QSize(540, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.etiket_hiz = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.etiket_hiz.setFont(font)
        self.etiket_hiz.setObjectName("etiket_hiz")
        self.gridLayout_2.addWidget(self.etiket_hiz, 0, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.etiket_lineer = QtWidgets.QLabel(self.centralwidget)
        self.etiket_lineer.setObjectName("etiket_lineer")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.etiket_lineer)
        self.line_lineer = QtWidgets.QLineEdit(self.centralwidget)
        self.line_lineer.setReadOnly(True)
        self.line_lineer.setObjectName("line_lineer")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_lineer)
        self.gridLayout_2.addLayout(self.formLayout, 1, 1, 1, 1)
        self.etiket_kontrol = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.etiket_kontrol.setFont(font)
        self.etiket_kontrol.setObjectName("etiket_kontrol")
        self.gridLayout_2.addWidget(self.etiket_kontrol, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.buton_sag = QtWidgets.QPushButton(self.centralwidget)
        self.buton_sag.setObjectName("buton_sag")
        self.gridLayout.addWidget(self.buton_sag, 1, 2, 1, 1)
        self.buton_dur = QtWidgets.QPushButton(self.centralwidget)
        self.buton_dur.setObjectName("buton_dur")
        self.gridLayout.addWidget(self.buton_dur, 1, 1, 1, 1)
        self.buton_sol = QtWidgets.QPushButton(self.centralwidget)
        self.buton_sol.setObjectName("buton_sol")
        self.gridLayout.addWidget(self.buton_sol, 1, 0, 1, 1)
        self.buton_ileri = QtWidgets.QPushButton(self.centralwidget)
        self.buton_ileri.setObjectName("buton_ileri")
        self.gridLayout.addWidget(self.buton_ileri, 0, 1, 1, 1)
        self.buton_geri = QtWidgets.QPushButton(self.centralwidget)
        self.buton_geri.setObjectName("buton_geri")
        self.gridLayout.addWidget(self.buton_geri, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 1)
        self.etiket_konum = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.etiket_konum.setFont(font)
        self.etiket_konum.setObjectName("etiket_konum")
        self.gridLayout_2.addWidget(self.etiket_konum, 4, 1, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.etiket_x = QtWidgets.QLabel(self.centralwidget)
        self.etiket_x.setObjectName("etiket_x")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.etiket_x)
        self.line_x = QtWidgets.QLineEdit(self.centralwidget)
        self.line_x.setReadOnly(True)
        self.line_x.setObjectName("line_x")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_x)
        self.etiket_y = QtWidgets.QLabel(self.centralwidget)
        self.etiket_y.setObjectName("etiket_y")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.etiket_y)
        self.line_y = QtWidgets.QLineEdit(self.centralwidget)
        self.line_y.setReadOnly(True)
        self.line_y.setObjectName("line_y")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_y)
        self.gridLayout_2.addLayout(self.formLayout_2, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robot Kontrol Arayüzü"))
        self.etiket_hiz.setText(_translate("MainWindow", "Tur Göstergesi"))
        self.etiket_lineer.setText(_translate("MainWindow", "Tur Bilgisi"))
        self.etiket_kontrol.setText(_translate("MainWindow", "Tur Kontrol"))
        self.buton_sag.setText(_translate("MainWindow", "Oda_1"))
        self.buton_dur.setText(_translate("MainWindow", "Oda_2"))
        self.buton_sol.setText(_translate("MainWindow", "Oda_3"))
        self.buton_ileri.setText(_translate("MainWindow", "Koridor_1"))
        self.buton_geri.setText(_translate("MainWindow", "Koridor_2"))
        self.etiket_konum.setText(_translate("MainWindow", "Konum Göstergesi"))
        self.etiket_x.setText(_translate("MainWindow", "Konum X (m):"))
        self.etiket_y.setText(_translate("MainWindow", "Konum Y (m):"))
        
        rospy.init_node("robot_arayuz")
        #self.pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=10)
        self.pub = rospy.Publisher('tb3_1/cmd_vel', Twist, queue_size=10)
        self.hiz_mesaji = Twist()
        rospy.Subscriber("tb3_1/odom",Odometry,self.odomCallback)
        
        
        self.buton_dur.clicked.connect(self.start)
        self.buton_ileri.clicked.connect(self.bos_tur)
        self.buton_geri.clicked.connect(self.bos_tur_2)
        self.buton_sol.clicked.connect(self.yuklu_tur)
        self.buton_sag.clicked.connect(self.yuklu_tur_2)
        
        self.line_x.setText(str(0.0))
        self.line_y.setText(str(0.0))
    
    def odomCallback(self,mesaj):
        self.line_x.setText(str(round(mesaj.pose.pose.position.x,4)))
        self.line_y.setText(str(round(mesaj.pose.pose.position.y,4)))
    
    def start(self): #Oda2
        r0 = threading.Thread(target=robots.robot0_hareket, args=(1,2))
        r0.start()
        r1 = threading.Thread(target=robots.robot1_hareket, args=(1,3))
        r1.start()
        r2 = threading.Thread(target=robots.robot2_hareket, args=(1,4))
        r2.start()
        self.line_lineer.setText("Harekete Geçildi")
    
    def bos_tur(self): #Koridor
        r0 = threading.Thread(target=robots.robot0_hareket, args=(5,1))
        r0.start()
        r1 = threading.Thread(target=robots.robot1_hareket, args=(5,2))
        r1.start()
        r2 = threading.Thread(target=robots.robot2_hareket, args=(5,3))
        r2.start()
        self.line_lineer.setText("Harekete Geçildi")
        
    def bos_tur_2(self): #Koridor2
        r0 = threading.Thread(target=robots.robot0_hareket, args=(-4,3.5))
        r0.start()
        r1 = threading.Thread(target=robots.robot1_hareket, args=(-4,2.5))
        r1.start()
        r2 = threading.Thread(target=robots.robot2_hareket, args=(-4,1.5))
        r2.start()
        self.line_lineer.setText("Harekete Geçildi")
        
    def yuklu_tur(self):#Oda3
        r0 = threading.Thread(target=robots.robot0_hareket, args=(5.5,-1.5))
        r0.start()
        r1 = threading.Thread(target=robots.robot1_hareket, args=(5.5,-2.5))
        r1.start()
        r2 = threading.Thread(target=robots.robot2_hareket, args=(5.5,-3.5))
        r2.start()
        self.line_lineer.setText("Harekete Geçildi")
        
    def yuklu_tur_2(self):#Oda1
        r0 = threading.Thread(target=robots.robot0_hareket, args=(-6.5,0))
        r0.start()
        r1 = threading.Thread(target=robots.robot1_hareket, args=(-6.5,1))
        r1.start()
        r2 = threading.Thread(target=robots.robot2_hareket, args=(-6.5,2))
        r2.start()
        self.line_lineer.setText("Harekete Geçildi")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())