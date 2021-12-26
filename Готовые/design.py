# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\design.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindows(object):
    def setupUi(self, MainWindows):
        MainWindows.setObjectName("MainWindows")
        MainWindows.resize(409, 697)
        self.centralwidget = QtWidgets.QWidget(MainWindows)
        self.centralwidget.setObjectName("centralwidget")
        self.abzas = QtWidgets.QCheckBox(self.centralwidget)
        self.abzas.setGeometry(QtCore.QRect(110, 420, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.abzas.setFont(font)
        self.abzas.setObjectName("abzas")
        self.apa = QtWidgets.QCheckBox(self.centralwidget)
        self.apa.setGeometry(QtCore.QRect(110, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.apa.setFont(font)
        self.apa.setObjectName("apa")
        self.azadliq = QtWidgets.QCheckBox(self.centralwidget)
        self.azadliq.setGeometry(QtCore.QRect(110, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.azadliq.setFont(font)
        self.azadliq.setObjectName("azadliq")
        self.date = QtWidgets.QDateEdit(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(97, 20, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.date.setFont(font)
        self.date.setObjectName("date")
        self.Btn = QtWidgets.QPushButton(self.centralwidget)
        self.Btn.setGeometry(QtCore.QRect(120, 630, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Btn.setFont(font)
        self.Btn.setObjectName("Btn")
        self.azertag = QtWidgets.QCheckBox(self.centralwidget)
        self.azertag.setGeometry(QtCore.QRect(110, 140, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.azertag.setFont(font)
        self.azertag.setObjectName("azertag")
        self.meydan = QtWidgets.QCheckBox(self.centralwidget)
        self.meydan.setGeometry(QtCore.QRect(110, 170, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.meydan.setFont(font)
        self.meydan.setObjectName("meydan")
        self.moderator = QtWidgets.QCheckBox(self.centralwidget)
        self.moderator.setGeometry(QtCore.QRect(110, 200, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.moderator.setFont(font)
        self.moderator.setObjectName("moderator")
        self.modern = QtWidgets.QCheckBox(self.centralwidget)
        self.modern.setGeometry(QtCore.QRect(110, 230, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.modern.setFont(font)
        self.modern.setObjectName("modern")
        self.musavat = QtWidgets.QCheckBox(self.centralwidget)
        self.musavat.setGeometry(QtCore.QRect(110, 450, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.musavat.setFont(font)
        self.musavat.setObjectName("musavat")
        self.qafqazinfo = QtWidgets.QCheckBox(self.centralwidget)
        self.qafqazinfo.setGeometry(QtCore.QRect(110, 260, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.qafqazinfo.setFont(font)
        self.qafqazinfo.setObjectName("qafqazinfo")
        self.trend = QtWidgets.QCheckBox(self.centralwidget)
        self.trend.setGeometry(QtCore.QRect(110, 320, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.trend.setFont(font)
        self.trend.setObjectName("trend")
        self.report = QtWidgets.QCheckBox(self.centralwidget)
        self.report.setGeometry(QtCore.QRect(110, 290, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.report.setFont(font)
        self.report.setObjectName("report")
        self.turan = QtWidgets.QCheckBox(self.centralwidget)
        self.turan.setGeometry(QtCore.QRect(110, 350, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.turan.setFont(font)
        self.turan.setObjectName("turan")
        self.yenisabah = QtWidgets.QCheckBox(self.centralwidget)
        self.yenisabah.setGeometry(QtCore.QRect(110, 380, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.yenisabah.setFont(font)
        self.yenisabah.setObjectName("yenisabah")
        self.yeniavaz = QtWidgets.QCheckBox(self.centralwidget)
        self.yeniavaz.setGeometry(QtCore.QRect(110, 480, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.yeniavaz.setFont(font)
        self.yeniavaz.setObjectName("yeniavaz")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(130, 420, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(170, 550, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10)
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 550, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindows.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindows)
        self.statusbar.setObjectName("statusbar")
        MainWindows.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindows)
        QtCore.QMetaObject.connectSlotsByName(MainWindows)

    def retranslateUi(self, MainWindows):
        _translate = QtCore.QCoreApplication.translate
        MainWindows.setWindowTitle(_translate("MainWindows", "NEWS PARSER"))
        self.abzas.setText(_translate("MainWindows", "abzas.net"))
        self.apa.setText(_translate("MainWindows", "apa.az"))
        self.azadliq.setText(_translate("MainWindows", "azadliq.org"))
        self.Btn.setText(_translate("MainWindows", "START"))
        self.azertag.setText(_translate("MainWindows", "azertag.az"))
        self.meydan.setText(_translate("MainWindows", "meydan.tv"))
        self.moderator.setText(_translate("MainWindows", "moderator.az"))
        self.modern.setText(_translate("MainWindows", "modern.az"))
        self.musavat.setText(_translate("MainWindows", "musavat.com"))
        self.qafqazinfo.setText(_translate("MainWindows", "qafqazinfo.az"))
        self.trend.setText(_translate("MainWindows", "trend.az"))
        self.report.setText(_translate("MainWindows", "report.az"))
        self.turan.setText(_translate("MainWindows", "turan.az"))
        self.yenisabah.setText(_translate("MainWindows", "yenisabah.az"))
        self.yeniavaz.setText(_translate("MainWindows", "yeniavaz.az"))
        self.label.setText(_translate("MainWindows", "Axınların\n"
"   sayı"))
