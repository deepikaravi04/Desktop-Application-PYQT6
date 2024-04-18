# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenlrlkfa.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.DropShadowFrame = QFrame(self.centralwidget)
        self.DropShadowFrame.setObjectName(u"DropShadowFrame")
        self.DropShadowFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(56, 58, 89);\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.DropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.DropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.DropShadowFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 80, 661, 71))
        font = QFont()
        font.setFamilies([u"Sans"])
        font.setPointSize(30)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.DropShadowFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 140, 661, 21))
        font1 = QFont()
        font1.setFamilies([u"Sans"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.DropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 260, 561, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_3 = QLabel(self.DropShadowFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 290, 661, 21))
        font2 = QFont()
        font2.setFamilies([u"Sans"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.DropShadowFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 350, 621, 21))
        font3 = QFont()
        font3.setFamilies([u"Sans"])
        font3.setPointSize(10)
        font3.setBold(False)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.DropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("SplashScreen", u"MARKET MANAGER <strong>PRO</strong>", None))
        self.label_2.setText(QCoreApplication.translate("SplashScreen", u"<strong>Trade</strong> Faster Smater", None))
        self.label_3.setText(QCoreApplication.translate("SplashScreen", u"loading....", None))
        self.label_4.setText(QCoreApplication.translate("SplashScreen", u"INTERACTIVE BROKERS", None))
    # retranslateUi

