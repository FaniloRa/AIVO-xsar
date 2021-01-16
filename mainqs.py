# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fronti.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets

import cv2
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from butterworth import Butter
import sys
import cv2
import numpy as np
import scipy.signal as sig
import scipy.ndimage as ndi
import matplotlib.pyplot as plt




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1279, 829)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.background = QFrame(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 1281, 791))
        self.background.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(51, 60, 72, 255));\n"
"}")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.header = QFrame(self.background)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(-11, 0, 1291, 51))
        self.header.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(68, 80, 95, 255));\n"
"}")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 0, 71, 51))
        self.label.setStyleSheet(u"QLabel{\n"
"color:white;\n"
"font-size:25px;\n"
"font-family:\"Brush Script MT\", \"cursive\";\n"
"font-weight:bold;\n"
"}")
        self.vertical_menu = QFrame(self.background)
        self.vertical_menu.setObjectName(u"vertical_menu")
        self.vertical_menu.setGeometry(QRect(990, 0, 291, 791))
        self.vertical_menu.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(56, 67, 79, 255));\n"
"}")
        self.vertical_menu.setFrameShape(QFrame.StyledPanel)
        self.vertical_menu.setFrameShadow(QFrame.Raised)
        self.chart = QFrame(self.vertical_menu)
        self.chart.setObjectName(u"chart")
        self.chart.setGeometry(QRect(20, 100, 251, 161))
        self.chart.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(36, 42, 50, 255));\n"
"}")
        self.chart.setFrameShape(QFrame.StyledPanel)
        self.chart.setFrameShadow(QFrame.Raised)
        self.plotChart = QLabel(self.chart)
        self.plotChart.setObjectName(u"plotChart")
        self.plotChart.setGeometry(QRect(0, 0, 251, 161))
        self.rotateLeft = QPushButton(self.vertical_menu)
        self.rotateLeft.setObjectName(u"rotateLeft")
        self.rotateLeft.setGeometry(QRect(20, 270, 41, 31))
        self.rotateLeft.setStyleSheet(u"QPushButton{\n"
"image: url(./histogram.png);\n"
"border:none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(39, 50, 63, 255));\n"
"}")
        self.skeleton = QPushButton(self.vertical_menu)
        self.skeleton.setObjectName(u"skeleton")
        self.skeleton.setGeometry(QRect(71, 270, 41, 31))
        self.skeleton.setStyleSheet(u"QPushButton{\n"
"image: url(./skeleton.png);\n"
"border:none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(39, 50, 63, 255));\n"
"}")
        self.rotateAll = QPushButton(self.vertical_menu)
        self.rotateAll.setObjectName(u"rotateAll")
        self.rotateAll.setGeometry(QRect(125, 270, 41, 31))
        self.rotateAll.setStyleSheet(u"QPushButton{\n"
"image: url(./rotate.png);\n"
"border:none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(39, 50, 63, 255));\n"
"}")
        self.symetric = QPushButton(self.vertical_menu)
        self.symetric.setObjectName(u"symetric")
        self.symetric.setGeometry(QRect(177, 270, 41, 31))
        self.symetric.setStyleSheet(u"QPushButton{\n"
"image: url(./print.png);\n"
"border:none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(39, 50, 63, 255));\n"
"}")
        self.translate = QPushButton(self.vertical_menu)
        self.translate.setObjectName(u"translate")
        self.translate.setGeometry(QRect(230, 270, 41, 31))
        self.translate.setStyleSheet(u"QPushButton{\n"
"image: url(./save.png);\n"
"border:none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(39, 50, 63, 255));\n"
"}")
        self.Red = QSlider(self.vertical_menu)
        self.Red.setObjectName(u"Red")
        self.Red.setGeometry(QRect(70, 360, 181, 22))
        self.Red.setOrientation(Qt.Horizontal)
        self.Green = QSlider(self.vertical_menu)
        self.Green.setObjectName(u"Green")
        self.Green.setGeometry(QRect(70, 400, 181, 22))
        self.Green.setOrientation(Qt.Horizontal)
        self.Bleu = QSlider(self.vertical_menu)
        self.Bleu.setObjectName(u"Bleu")
        self.Bleu.setGeometry(QRect(70, 440, 181, 22))
        self.Bleu.setOrientation(Qt.Horizontal)
        self.Rouge = QLabel(self.vertical_menu)
        self.Rouge.setObjectName(u"Rouge")
        self.Rouge.setGeometry(QRect(10, 357, 51, 21))
        self.Rouge.setStyleSheet(u"QLabel{\n"
"color:white;\n"
"font-size:15px;\n"
"}")
        self.label_2 = QLabel(self.vertical_menu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 399, 51, 21))
        self.label_2.setStyleSheet(u"QLabel{\n"
"color:white;\n"
"font-size:15px;\n"
"}")
        self.label_3 = QLabel(self.vertical_menu)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(12, 440, 51, 21))
        self.label_3.setStyleSheet(u"QLabel{\n"
"color:white;\n"
"font-size:15px;\n"
"}")
        self.label_4 = QLabel(self.vertical_menu)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 750, 81, 16))
        self.label_4.setStyleSheet(u"QLabel{\n"
"color:white;\n"
"}")
        self.erosion_2 = QLabel(self.vertical_menu)
        self.erosion_2.setObjectName(u"erosion_2")
        self.erosion_2.setGeometry(QRect(10, 480, 51, 21))
        self.erosion_2.setStyleSheet(u"QLabel{\n"
"color:white;\n"
"font-size:15px;\n"
"}")
        self.erosion = QSlider(self.vertical_menu)
        self.erosion.setObjectName(u"erosion")
        self.erosion.setGeometry(QRect(70, 480, 181, 22))
        self.erosion.setMinimum(-5)
        self.erosion.setMaximum(5)
        self.erosion.setValue(0)
        self.erosion.setSliderPosition(0)
        self.erosion.setOrientation(Qt.Horizontal)
        self.horizontalSlider = QSlider(self.vertical_menu)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(70, 520, 181, 22))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.min = QLabel(self.vertical_menu)
        self.min.setObjectName(u"min")
        self.min.setGeometry(QRect(10, 520, 51, 21))
        self.min.setStyleSheet(u"QLabel{\n"
"color:white;\n"
"font-size:15px;\n"
"}")
        self.max = QSlider(self.vertical_menu)
        self.max.setObjectName(u"max")
        self.max.setGeometry(QRect(70, 563, 181, 22))
        self.max.setOrientation(Qt.Horizontal)
        self.label_10 = QLabel(self.vertical_menu)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 560, 51, 21))
        self.label_10.setStyleSheet(u"QLabel{\n"
"color:white;\n"
"font-size:15px;\n"
"}")
        self.upload = QFrame(self.background)
        self.upload.setObjectName(u"upload")
        self.upload.setGeometry(QRect(110, 100, 711, 511))
        self.upload.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(36, 42, 50, 255));\n"
"}")
        self.upload.setFrameShape(QFrame.StyledPanel)
        self.upload.setFrameShadow(QFrame.Raised)
        self.import_image = QLabel(self.upload)
        self.import_image.setObjectName(u"import_image")
        self.import_image.setGeometry(QRect(10, 10, 691, 491))
        self.outils = QFrame(self.background)
        self.outils.setObjectName(u"outils")
        self.outils.setGeometry(QRect(0, 90, 61, 431))
        self.outils.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(56, 67, 79, 255));\n"
"\n"
"}")
        self.outils.setFrameShape(QFrame.StyledPanel)
        self.outils.setFrameShadow(QFrame.Raised)
        self.ajouter = QPushButton(self.outils)
        self.ajouter.setObjectName(u"ajouter")
        self.ajouter.setGeometry(QRect(12, 10, 41, 31))
        self.ajouter.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(34, 44, 55, 255));\n"
"border:none;\n"
"	image: url(./open.png);\n"
"border-radius:10px;\n"
"box-shadow:50px;\n"
"}")
        self.filtrer = QPushButton(self.outils)
        self.filtrer.setObjectName(u"filtrer")
        self.filtrer.setGeometry(QRect(12, 50, 41, 29))
        self.filtrer.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(34, 44, 55, 255));\n"
"border:none;\n"
"border-radius:10px;\n"
"box-shadow:50px;\n"
"	image: url(./filter.png);\n"
"}")
        self.contour = QPushButton(self.outils)
        self.contour.setObjectName(u"contour")
        self.contour.setGeometry(QRect(10, 90, 42, 31))
        self.contour.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(34, 44, 55, 255));\n"
"border:none;\n"
"	image: url(./contour.png);\n"
"border-radius:10px;\n"
"}")
        self.pushButton = QPushButton(self.outils)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 130, 43, 31))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(34, 44, 55, 255));\n"
"border:none;\n"
"border-radius:10px;\n"
"	image: url(./blur.png);\n"
"}")
        self.pushButton_2 = QPushButton(self.outils)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 170, 43, 31))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(34, 44, 55, 255));\n"
"border:none;\n"
"	image: url(./equalisation.png);\n"
"\n"
"border-radius:10px;\n"
"}")
        self.noise = QPushButton(self.outils)
        self.noise.setObjectName(u"noise")
        self.noise.setGeometry(QRect(10, 210, 43, 31))
        self.noise.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(34, 44, 55, 255));\n"
"border:none;\n"
"	image: url(./noise.png);\n"
"border-radius:10px;\n"
"}")
        self.denoise = QPushButton(self.outils)
        self.denoise.setObjectName(u"denoise")
        self.denoise.setGeometry(QRect(11, 250, 43, 31))
        self.denoise.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(34, 44, 55, 255));\n"
"border:none;\n"
"	image: url(./convolution.png);\n"
"border-radius:10px;\n"
"}")
        self.zoom_plus = QPushButton(self.outils)
        self.zoom_plus.setObjectName(u"zoom_plus")
        self.zoom_plus.setGeometry(QRect(11, 290, 43, 31))
        self.zoom_plus.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(34, 44, 55, 255));\n"
"border:none;\n"
"	image: url(./plus.png);\n"
"border-radius:10px;\n"
"}")
        self.zoom_moins = QPushButton(self.outils)
        self.zoom_moins.setObjectName(u"zoom_moins")
        self.zoom_moins.setGeometry(QRect(11, 330, 43, 31))
        self.zoom_moins.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(34, 44, 55, 255));\n"
"border:none;\n"
"	image: url(./moinss.png);\n"
"border-radius:10px;\n"
"}")
        self.label_5 = QLabel(self.background)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(850, 100, 121, 16))
        self.label_5.setStyleSheet(u"QLabel{\n"
"color:white;\n"
"font-size:15px;\n"
"font-family:century gothic;\n"
"font-weight:bold;\n"
"}")
        self.filtrage_gauss = QPushButton(self.background)
        self.filtrage_gauss.setObjectName(u"filtrage_gauss")
        self.filtrage_gauss.setGeometry(QRect(850, 240, 111, 31))
        self.filtrage_gauss.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(39, 47, 55, 255));\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-family:century gothic;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.filtrage_bilateral = QPushButton(self.background)
        self.filtrage_bilateral.setObjectName(u"filtrage_bilateral")
        self.filtrage_bilateral.setGeometry(QRect(850, 190, 111, 31))
        self.filtrage_bilateral.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(39, 47, 55, 255));\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-family:century gothic;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.median_filter = QPushButton(self.background)
        self.median_filter.setObjectName(u"median_filter")
        self.median_filter.setGeometry(QRect(850, 140, 111, 31))
        self.median_filter.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(39, 47, 55, 255));\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-family:century gothic;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.label_6 = QLabel(self.background)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(860, 320, 101, 20))
        self.label_6.setStyleSheet(u"QLabel{\n"
"color:white;\n"
"font-size:15px;\n"
"font-family:century gothic;\n"
"font-weight:bold;\n"
"}")
        self.fd1 = QPushButton(self.background)
        self.fd1.setObjectName(u"fd1")
        self.fd1.setGeometry(QRect(850, 350, 111, 31))
        self.fd1.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(39, 47, 55, 255));\n"
"border:none;\n"
"color:white;\n"
"font-family:century gothic;\n"
"font-weight:bold;\n"
"}")
        self.fd2 = QPushButton(self.background)
        self.fd2.setObjectName(u"fd2")
        self.fd2.setGeometry(QRect(850, 400, 111, 31))
        self.fd2.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(39, 47, 55, 255));\n"
"border:none;\n"
"color:white;\n"
"font-family:century gothic;\n"
"font-weight:bold;\n"
"}")
        self.fd3 = QPushButton(self.background)
        self.fd3.setObjectName(u"fd3")
        self.fd3.setGeometry(QRect(850, 450, 111, 31))
        self.fd3.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(39, 47, 55, 255));\n"
"border:none;\n"
"color:white;\n"
"font-family:century gothic;\n"
"font-weight:bold;\n"
"}")
        self.traitement1 = QFrame(self.background)
        self.traitement1.setObjectName(u"traitement1")
        self.traitement1.setGeometry(QRect(110, 630, 141, 131))
        self.traitement1.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(36, 42, 50, 255));\n"
"\n"
"border-radius:15px;\n"
"}")
        self.traitement1.setFrameShape(QFrame.StyledPanel)
        self.traitement1.setFrameShadow(QFrame.Raised)
        self.trait1 = QLabel(self.traitement1)
        self.trait1.setObjectName(u"trait1")
        self.trait1.setGeometry(QRect(6, 0, 131, 131))
        self.trait1.setStyleSheet(u"QLabel{\n"
"border-radius:15px;\n"
"}\n"
"")
        self.traitement2 = QFrame(self.background)
        self.traitement2.setObjectName(u"traitement2")
        self.traitement2.setGeometry(QRect(300, 630, 141, 131))
        self.traitement2.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(36, 42, 50, 255));\n"
"\n"
"border-radius:15px;\n"
"}")
        self.traitement2.setFrameShape(QFrame.StyledPanel)
        self.traitement2.setFrameShadow(QFrame.Raised)
        self.trait2 = QLabel(self.traitement2)
        self.trait2.setObjectName(u"trait2")
        self.trait2.setGeometry(QRect(6, 3, 131, 121))
        self.trait2.setStyleSheet(u"QLabel{\n"
"border-radius:15px;\n"
"}")
        self.traitement3 = QFrame(self.background)
        self.traitement3.setObjectName(u"traitement3")
        self.traitement3.setGeometry(QRect(480, 630, 141, 131))
        self.traitement3.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(36, 42, 50, 255));\n"
"border-radius:15px;\n"
"}")
        self.traitement3.setFrameShape(QFrame.StyledPanel)
        self.traitement3.setFrameShadow(QFrame.Raised)
        self.trait3 = QLabel(self.traitement3)
        self.trait3.setObjectName(u"trait3")
        self.trait3.setGeometry(QRect(6, -1, 131, 131))
        self.trait3.setStyleSheet(u"QLabel{\n"
"border-radius:15px;\n"
"}")
        self.traitement4 = QFrame(self.background)
        self.traitement4.setObjectName(u"traitement4")
        self.traitement4.setGeometry(QRect(669, 630, 151, 131))
        self.traitement4.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.767045, x2:0, y2:0.813, stop:1 rgba(36, 42, 50, 255));\n"
"\n"
"border-radius:15px;\n"
"}\n"
"")
        self.traitement4.setFrameShape(QFrame.StyledPanel)
        self.traitement4.setFrameShadow(QFrame.Raised)
        self.trait4 = QLabel(self.traitement4)
        self.trait4.setObjectName(u"trait4")
        self.trait4.setGeometry(QRect(6, 3, 141, 121))
        self.trait4.setStyleSheet(u"QLabel{\n"
"border-radius:15px;\n"
"}")
        self.vertical_menu.raise_()
        self.header.raise_()
        self.upload.raise_()
        self.outils.raise_()
        self.label_5.raise_()
        self.filtrage_gauss.raise_()
        self.filtrage_bilateral.raise_()
        self.median_filter.raise_()
        self.label_6.raise_()
        self.fd1.raise_()
        self.fd2.raise_()
        self.fd3.raise_()
        self.traitement1.raise_()
        self.traitement2.raise_()
        self.traitement3.raise_()
        self.traitement4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1279, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"XSAR", None))
        self.plotChart.setText("")
        self.rotateLeft.setText("")
        self.skeleton.setText("")
        self.rotateAll.setText("")
        self.symetric.setText("")
        self.translate.setText("")
        self.Rouge.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"xsar TOUCH", None))
        self.erosion_2.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.min.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.import_image.setText("")
        self.ajouter.setText("")
        self.filtrer.setText("")
        self.contour.setText("")
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.noise.setText("")
        self.denoise.setText("")
        self.zoom_plus.setText("")
        self.zoom_moins.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"FTILTRAGE FLOU", None))
        self.filtrage_gauss.setText(QCoreApplication.translate("MainWindow", u"GAUSS", None))
        self.filtrage_bilateral.setText(QCoreApplication.translate("MainWindow", u"BILATERAL", None))
        self.median_filter.setText(QCoreApplication.translate("MainWindow", u"MEDIAN", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"FILTRAGE", None))
        self.fd1.setText(QCoreApplication.translate("MainWindow", u"DIREC X1", None))
        self.fd2.setText(QCoreApplication.translate("MainWindow", u"DIREC X2", None))
        self.fd3.setText(QCoreApplication.translate("MainWindow", u"DIREC X3", None))
        self.trait1.setText("")
        self.trait2.setText("")
        self.trait3.setText("")
        self.trait4.setText("")
    # retranslateUi

    # retranslateUi



        ################   APPEL A LA FONCTION ####################

        self.ajouter.clicked.connect(self.open_img)
        self.rotateAll.clicked.connect(self.rotation)
        self.contour.clicked.connect(self.contourIm)
        self.trait2.mousePressEvent = self.niveauxGris
        self.trait3.mousePressEvent = self.binarisation
        self.trait4.mousePressEvent = self.binarisation_invesrion
        self.trait1.mousePressEvent = self.reset
        self.rotateLeft.clicked.connect(self.egalisationHist)
        self.pushButton.clicked.connect(self.flou)
        self.zoom_moins.clicked.connect(self.zoom_min)
        self.zoom_plus.clicked.connect(self.zoom_max)
        self.noise.clicked.connect(self.bruitage)
        self.denoise.clicked.connect(self.convolution)
       
 
        

        #BOOLEAN SHOW ET HIDE FILTRAGE CONTENU
        self.label_5.setHidden(True)
        self.median_filter.setHidden(True)
        self.filtrage_bilateral.setHidden(True)
        self.filtrage_gauss.setHidden(True)

        self.label_6.setHidden(True)
        self.fd1.setHidden(True)
        self.fd2.setHidden(True)
        self.fd3.setHidden(True)

        ###########################################

        self.filtrer.clicked.connect(self.filtrages)
        
        self.fd1.clicked.connect(self.filtrage_dir1)
        self.fd2.clicked.connect(self.filtrage_dir2)
        self.fd3.clicked.connect(self.filtrage_dir2)

        self.pushButton.clicked.connect(self.filtre_flou)

        self.median_filter.clicked.connect(self.flou_median)
        self.filtrage_bilateral.clicked.connect(self.flou_bilaterals)
        self.filtrage_gauss.clicked.connect(self.flou_gausss)


        self.Red.valueChanged.connect(self.opacitey)
        self.Green.valueChanged.connect(self.gauss_slide)
        self.Bleu.valueChanged.connect(self.echelle)
        self.erosion.valueChanged.connect(self.eroder)
        

        self.pushButton_2.clicked.connect(self.showSliderCanny)
        self.horizontalSlider.valueChanged.connect(self.Canny)
        self.max.valueChanged.connect(self.Canny)

        self.filename = None
        self.tmp = None
        self.opacite = 0
        self.flou = 0

   ###################################################################################################################################################
   ###################################################################################################################################################
   ###################################################################################################################################################
   ###################################################################################################################################################
    
    #Début ouverture images
    def open_img(self):
        fname, filter = QFileDialog.getOpenFileName()
        if fname:
            self.loadImage(fname)
        else:
            print("Invalid Image")

    def loadImage(self, fname):
        self.image = cv2.imread(fname)
        self.tmp = self.image
        self.displayImage()

    def displayImage(self, window=1):
        qformat = QImage.Format_Indexed8

        if len(self.image.shape) == 3:
            if(self.image.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        
        thresh = 144
        max_val = 255
        img = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)

        frame = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        img2 = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_Indexed8)
        
        
        ret, binaire_inversion = cv2.threshold(frame, thresh, max_val, cv2.THRESH_BINARY_INV) 
        img3 = QImage(binaire_inversion, binaire_inversion.shape[1], binaire_inversion.shape[0], binaire_inversion.strides[0], QImage.Format_Indexed8)

        ret, binaire = cv2.threshold(frame, thresh, max_val, cv2.THRESH_BINARY)
        img4 = QImage(binaire, binaire.shape[1], binaire.shape[0], binaire.strides[0], QImage.Format_Indexed8)
        
        img = img.rgbSwapped()  
        img2 = img2.rgbSwapped() 
        img4 = img4.rgbSwapped()     
        if window == 1:  
            #image à l'origine    
            self.trait1.setScaledContents(True)
            self.trait1.setPixmap(QPixmap.fromImage(img))
            self.trait1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            
            #image traité en gris 
            self.trait2.setScaledContents(True)
            self.trait2.setPixmap(QPixmap.fromImage(img2))
            self.trait2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

            #Binarisation Inversion
            self.trait3.setScaledContents(True)
            self.trait3.setPixmap(QPixmap.fromImage(img3))
            self.trait3.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

            #image traité Binarisation
            self.trait4.setScaledContents(True)
            self.trait4.setPixmap(QPixmap.fromImage(img4))
            self.trait4.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            
            #image image traité
            self.import_image.setPixmap(QPixmap.fromImage(img))
            self.import_image.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        if window == 2:
            
            self.import_image.setPixmap(QPixmap.fromImage(img))
            self.import_image.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.Rouge.setText("OPACI")
        self.label_2.setText("GAUSS")
        self.label_3.setText("ECHEL")
        self.erosion_2.setText("DE")
        self.min.setHidden(True)
        self.max.setHidden(True)
        self.horizontalSlider.setHidden(True)
        self.label_10.setHidden(True)
   
   ###################################################################################################################################################

    #Bruitage 
    def bruitage(self):
        self.image = self.tmp
        s_vs_p = 0.7
        taille = 0.04
        out = np.copy(self.image)
        #En mode sel
        num_sel = np.ceil(taille * self.image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_sel))
                  for i in self.image.shape]
        out[coords] = 1
        #mode
        num_pepper = np.ceil(taille * self.image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
                  for i in self.image.shape]
        out[coords] = 0
        self.image = out
        self.displayImage(2)

####################################################################################################################################################

    #REGLE SLIDER GAUSS    
    def gauss_slide(self, g):
        self.image = self.tmp
        self.image = cv2.GaussianBlur(self.image, (5, 5), g)
        self.displayImage(2)


####################################################################################################################################################

    #REGLAGE ECHELLE
    def echelle(self , c):
        self.image = self.tmp
        self.image = cv2.resize(self.image, None, fx=c, fy=c, interpolation=cv2.INTER_CUBIC)
        self.displayImage(2)

####################################################################################################################################################

    #DE (Dilatation erision)
    def eroder(self , iter):
        self.image = self.tmp
        if iter > 0 :
            kernel = np.ones((4, 7), np.uint8)
            self.image = cv2.erode(self.tmp, kernel, iterations=iter)
        else :
            kernel = np.ones((2, 6), np.uint8)
            self.image = cv2.dilate(self.image, kernel, iterations=iter*-1)
        self.displayImage(2)


####################################################################################################################################################
    #Début rotation image 
    def rotation(self):
        rows, cols, steps = self.image.shape
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1) 
        self.image = cv2.warpAffine(self.image, M, (cols, rows))
        self.displayImage(2)

   ####################################################################################################################################################
    
    # NIVEAUX DE GRIS ON CLICK LABEL TRAIT1
    def niveauxGris(self, image):
        self.image = self.tmp

        b, v, r = cv2.split(self.image)
        y = 0.299*r + 0.587*v + 0.114*b  # operation matricielle
        y = y.astype(np.uint8)

        # calcule l'histogramme de l'image
        # preparer un vecteur de 256 zeros pour chaque gris
        histo = np.zeros(256, int)
        for i in range(0, self.image.shape[0]):  # enumere les lignes
            for j in range(0, self.image.shape[1]):  # enumere les colonnes
                histo[y[i, j]] = histo[y[i, j]] + 1

        # calcule l'histogramme cumule hc
        hc = np.zeros(256, int)  # prepare un vecteur de 256 zeros
        hc[0] = histo[0]
        for i in range(1, 256):
            hc[i] = histo[i] + hc[i-1]  # formule pour calculer hc

        # normalise l'histogramme cumule hc
        nbpixels = y.size  
        hc = hc / nbpixels * 255

        # utilisation hc comme table de conversion des niveau de gris
        # histogramme cumule desire et transformation ponctuelle a chercher
        for i in range(0, y.shape[0]):
            for j in range(0, y.shape[1]):
                y[i, j] = hc[y[i, j]]

        # frame = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        img2 = QImage(y, y.shape[1], y.shape[0],
                      y.strides[0], QImage.Format_Indexed8)

        self.import_image.setPixmap(QPixmap.fromImage(img2))
        self.import_image.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

   #################################################################################################################################################### 


    #BINARISATION
    def binarisation(self,image):
        self.image = self.tmp
        sary=cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
        min_val = 145
        max_val = 255
        ret, binaire = cv2.threshold(sary, min_val, max_val, cv2.THRESH_BINARY_INV)
        img2 = QImage(binaire, binaire.shape[1], binaire.shape[0], binaire.strides[0], QImage.Format_Indexed8)
        self.import_image.setPixmap(QPixmap.fromImage(img2))
        self.import_image.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


  #################################################################################################################################################### 

      #INVESRSION DE BINARISATION
    def binarisation_invesrion(self,image):
        self.image = self.tmp
        sary=cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
        min_val = 145
        max_val = 255
        ret, binaire = cv2.threshold(sary, min_val, max_val, cv2.THRESH_BINARY)
        img2 = QImage(binaire, binaire.shape[1], binaire.shape[0], binaire.strides[0], QImage.Format_Indexed8)
        self.import_image.setPixmap(QPixmap.fromImage(img2))
        self.import_image.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

  #################################################################################################################################################### 

    #egalisation d'histograme
    def egalisationHist(self):
        self.image = self.tmp
        sary_traite = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        R, G, B = cv2.split(sary_traite)
        sortie_1_R = cv2.equalizeHist(R)
        sortie_1_G = cv2.equalizeHist(G)
        sortie_1_B = cv2.equalizeHist(B)

        
        self.image = cv2.merge((sortie_1_B,sortie_1_G, sortie_1_R))
        
        
        plt.hist(sortie_1_R.ravel(),1000,[0,390])
        plt.hist(sortie_1_G.ravel(),1000,[0,390])
        plt.hist(sortie_1_B.ravel(),1000,[0,390])
        plt.show()
        self.displayImage(2)

  #################################################################################################################################################### 

    #CONTOURS D'IMAGES
    def contourIm(self):
            self.image = self.tmp
            min_val = 160
            max_val = 255
            minimal = np.array([60,60,60])
            maximal = np.array([250,250,250])
            image_traitement = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            ret, mask =  cv2.threshold(image_traitement, min_val, max_val, cv2.THRESH_BINARY_INV)
            cont, contour = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            self.image = cv2.drawContours(self.image,cont,-1,(0,0,255),2)
            self.displayImage(2)
            
 #################################################################################################################################################### 
    
    #FLOU D'IMAGES    
    def flou(self):
        self.image = self.tmp
        self.image = cv2.blur(self.image, (5, 5))
        self.displayImage(2)

#################################################################################################################################################### 

    #Zoom moins 
    def zoom_min(self):
        self.image = cv2.resize(self.image, None, fx=0.75, fy=0.75, interpolation=cv2.INTER_CUBIC)
        self.displayImage(2)                          

####################################################################################################################################################               

    #Zoom plus 
    def zoom_max(self):
        self.image = cv2.resize(self.image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
        self.displayImage(2)             

####################################################################################################################################################               

     #Appel à tous les fonctions de filtrages
    def filtrages(self):
        self.label_6.setHidden(False)    
        self.fd1.setHidden(False)
        self.fd2.setHidden(False)
        self.fd3.setHidden(False)

####################################################################################################################################################

####################################################################################################################################################

    #Filtrage directionnel X1 
    def filtrage_dir1(self):
        self.image = self.tmp
        kernel = np.ones((3, 3), np.float32) / 9
        self.image = cv2.filter2D(self.image, -1, kernel)
        self.displayImage(2)

####################################################################################################################################################

    #Filtrage directionnel X2
    def filtrage_dir2(self):
        self.image = self.tmp
        kernel = np.ones((4, 4), np.float32) / 9
        self.image = cv2.filter2D(self.image, -1, kernel)
        self.displayImage(2)

####################################################################################################################################################

    #Filtrage directionnel X3
    def filtrage_dir3(self):
        self.image = self.tmp
        kernel = np.ones((5, 5), np.float32) / 25
        self.image = cv2.filter2D(self.image, -1, kernel)
        self.displayImage(2)

####################################################################################################################################################

    #Appel fonction de filtrage flou
    def filtre_flou(self):
        self.label_5.setHidden(False)    
        self.median_filter.setHidden(False)
        self.filtrage_bilateral.setHidden(False)
        self.filtrage_gauss.setHidden(False)

####################################################################################################################################################        

    #FLou median
    def flou_median(self):
        self.image = self.tmp
        self.image = cv2.medianBlur(self.image,5)
        self.displayImage(2)

####################################################################################################################################################

    # filtrage Flou bilateral 
    def flou_bilaterals(self):
        self.image = self.tmp
        self.image = cv2.bilateralFilter(self.image,9,75,75)
        self.displayImage(2)

####################################################################################################################################################

    # Filtrage FLou de gauss
    def flou_gausss(self):
        self.image = self.tmp
        self.image = cv2.GaussianBlur(self.image,(5,5),0)
        self.displayImage(2)

####################################################################################################################################################

    #REGLAGE D'OPACITE SLIDER
    def opacitey(self, opacite):
        self.image = self.tmp
        opacite = opacite*0.1
        invOpacite = 1.0 /opacite
        table = np.array([((i / 255.0) ** invOpacite) * 255
            for i in np.arange(0, 256)]).astype("uint8")

        self.image = cv2.LUT(self.image, table)
        self.displayImage(2)


    #convolution
    def convolution(self):
            self.image = self.tmp
            k = np.array(([0,-1,0],[-1,5,-1],[0,-1,0]), np.float32)
            output = cv2.filter2D(self.image, -1,k)
            self.image = output
            self.displayImage(2)



####################################################################################################################################################

    def showSliderCanny(self):
        self.min.setHidden(False)
        self.max.setHidden(False)
        self.horizontalSlider.setHidden(False)            
        self.max.setHidden(False)
        self.label_10.setHidden(False)
        self.horizontalSlider.setHidden(False)



    def Canny(self):
        self.image = self.tmp
        can = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = cv2.Canny(can, self.horizontalSlider.value(), self.max.value())
        self.displayImage(2)      

    def reset(self,img):
        self.image = self.tmp
        self.displayImage(2)
    
    ####################################################################################################################################################

            

    

    
  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
