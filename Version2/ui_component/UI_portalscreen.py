# UI_portalscreen.py
# 인공지능학부 242149 이수용

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_portalscreen.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QStatusBar)

from Version2.ui_component.Custom import MyLineEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(430, 250)
        MainWindow.setMinimumSize(QSize(430, 250))
        MainWindow.setMaximumSize(QSize(430, 250))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color:rgb(255,244,128)\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 15pt;\n"
"font-weight: bold;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size: 9pt;\n"
"font-weight: bold;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEditID = MyLineEdit(self.widget)
        
        self.lineEditID.setObjectName(u"lineEditID")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lineEditID.setFont(font)
        self.lineEditID.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font-weight:bold;\n"
"font-size:10pt;")

        self.horizontalLayout_2.addWidget(self.lineEditID)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-size: 9pt;\n"
"font-weight: bold;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEditPW = MyLineEdit(self.widget)
        self.lineEditPW.setObjectName(u"lineEditPW")
        self.lineEditPW.setFont(font)
        self.lineEditPW.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font-weight:bold;\n"
"font-size:10pt;")
        self.lineEditPW.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText)

        self.horizontalLayout.addWidget(self.lineEditPW)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.Button_login = QPushButton(self.widget)
        self.Button_login.setObjectName(u"Button_login")
        self.Button_login.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font-size: 11pt;\n"
"font-weight: bold;")

        self.verticalLayout_2.addWidget(self.Button_login)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc804\ub0a8\ub300 \ud3ec\ud138 \uc815\ubcf4 \uc785\ub825", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"portal ID", None))
        self.lineEditID.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"portal Pw", None))
        self.lineEditPW.setText("")
        self.Button_login.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8\uc778 \uc2dc\ub3c4", None))
    # retranslateUi



from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt




