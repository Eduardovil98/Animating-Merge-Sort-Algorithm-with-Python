# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'merge_algorithmXjeCPU.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 600)
        MainWindow.setMinimumSize(QSize(1200, 600))
        MainWindow.setMaximumSize(QSize(1200, 600))
        MainWindow.setStyleSheet(u"#frame_3{\n"
"	background-color: rgb(65, 65, 65);\n"
"}\n"
"/************************** QLABEL STYLE ****************************/\n"
"QLabel{\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"#label{\n"
"	background-color: rgb(65, 65, 65);\n"
"}\n"
"/************************** QPUSH BUTTON ****************************/\n"
"QPushButton{\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font-weight: 900;\n"
"	border-radius: 8px;\n"
"	padding: 5px 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(221, 0, 0);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-right: 2px;\n"
"	background-color: rgb(182, 0, 0);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(386, 40, 50, 50))
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setMaximumSize(QSize(50, 50))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(438, 40, 50, 50))
        self.label_3.setMinimumSize(QSize(50, 50))
        self.label_3.setMaximumSize(QSize(50, 50))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(490, 40, 50, 50))
        self.label_4.setMinimumSize(QSize(50, 50))
        self.label_4.setMaximumSize(QSize(50, 50))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(542, 40, 50, 50))
        self.label_5.setMinimumSize(QSize(50, 50))
        self.label_5.setMaximumSize(QSize(50, 50))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(594, 40, 50, 50))
        self.label_6.setMinimumSize(QSize(50, 50))
        self.label_6.setMaximumSize(QSize(50, 50))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(646, 40, 50, 50))
        self.label_7.setMinimumSize(QSize(50, 50))
        self.label_7.setMaximumSize(QSize(50, 50))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"")
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(698, 40, 50, 50))
        self.label_8.setMinimumSize(QSize(50, 50))
        self.label_8.setMaximumSize(QSize(50, 50))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(750, 40, 50, 50))
        self.label_9.setMinimumSize(QSize(50, 50))
        self.label_9.setMaximumSize(QSize(50, 50))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.frame_2)

        self.line_2 = QFrame(self.frame_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(150, 30))
        self.pushButton_2.setMaximumSize(QSize(150, 30))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.pushButton_2.setFont(font2)

        self.horizontalLayout.addWidget(self.pushButton_2, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setMaximumSize(QSize(150, 30))
        self.pushButton.setFont(font2)

        self.horizontalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Merge Sort Visualization", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Merge Sort Visualization", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">1</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">2</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">3</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">4</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">5</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">6</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">7</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">8</p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Sort", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Change numbers", None))
    # retranslateUi

