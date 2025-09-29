# UI_mainscreen.py
# 인공지능학부 242149 이수용

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_mainscreen.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1303, 1109)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 400))
        self.widget_4.setMaximumSize(QSize(920, 16777215))
        self.widget_4.setStyleSheet(u"background-color:rgb(173, 216, 230)")
        self.verticalLayout_12 = QVBoxLayout(self.widget_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_hide2 = QWidget(self.widget_4)
        self.widget_hide2.setObjectName(u"widget_hide2")
        self.verticalLayout_13 = QVBoxLayout(self.widget_hide2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.w_hide1 = QWidget(self.widget_hide2)
        self.w_hide1.setObjectName(u"w_hide1")
        self.horizontalLayout_6 = QHBoxLayout(self.w_hide1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.layout_hide21 = QHBoxLayout()
        self.layout_hide21.setObjectName(u"layout_hide21")
        self.label_8 = QLabel(self.w_hide1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_hide21.addWidget(self.label_8)

        self.cb_year = QComboBox(self.w_hide1)
        self.cb_year.setObjectName(u"cb_year")
        self.cb_year.setStyleSheet(u"background-color:rgb(255,255,255)")

        self.layout_hide21.addWidget(self.cb_year)


        self.verticalLayout_2.addLayout(self.layout_hide21)

        self.layout_hide22 = QHBoxLayout()
        self.layout_hide22.setObjectName(u"layout_hide22")
        self.label_4 = QLabel(self.w_hide1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_hide22.addWidget(self.label_4)

        self.cb_major = QComboBox(self.w_hide1)
        self.cb_major.setObjectName(u"cb_major")
        self.cb_major.setStyleSheet(u"background-color:rgb(255,255,255)")

        self.layout_hide22.addWidget(self.cb_major)


        self.verticalLayout_2.addLayout(self.layout_hide22)

        self.layout_hide23 = QHBoxLayout()
        self.layout_hide23.setObjectName(u"layout_hide23")
        self.label_7 = QLabel(self.w_hide1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_hide23.addWidget(self.label_7)

        self.cb_grade = QComboBox(self.w_hide1)
        self.cb_grade.setObjectName(u"cb_grade")
        self.cb_grade.setStyleSheet(u"background-color:rgb(255,255,255)")

        self.layout_hide23.addWidget(self.cb_grade)


        self.verticalLayout_2.addLayout(self.layout_hide23)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)


        self.verticalLayout_13.addWidget(self.w_hide1)

        self.w_hide2 = QWidget(self.widget_hide2)
        self.w_hide2.setObjectName(u"w_hide2")
        self.verticalLayout_8 = QVBoxLayout(self.w_hide2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.layout_hide11 = QHBoxLayout()
        self.layout_hide11.setObjectName(u"layout_hide11")
        self.label_37 = QLabel(self.w_hide2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(16777215, 21))
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_hide11.addWidget(self.label_37)

        self.credit = QLineEdit(self.w_hide2)
        self.credit.setObjectName(u"credit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.credit.sizePolicy().hasHeightForWidth())
        self.credit.setSizePolicy(sizePolicy)
        self.credit.setMaximumSize(QSize(60, 70))
        self.credit.setStyleSheet(u"background-color:rgb(255,255,255)")

        self.layout_hide11.addWidget(self.credit)


        self.verticalLayout_8.addLayout(self.layout_hide11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_38 = QLabel(self.w_hide2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_38)

        self.lb_credit = QLabel(self.w_hide2)
        self.lb_credit.setObjectName(u"lb_credit")
        font = QFont()
        font.setBold(True)
        self.lb_credit.setFont(font)
        self.lb_credit.setStyleSheet(u"background-color:rgb(255,255,255)")
        self.lb_credit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lb_credit)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)


        self.verticalLayout_13.addWidget(self.w_hide2)


        self.horizontalLayout_8.addWidget(self.widget_hide2)

        self.textEdit_search = QTextEdit(self.widget_4)
        self.textEdit_search.setObjectName(u"textEdit_search")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit_search.sizePolicy().hasHeightForWidth())
        self.textEdit_search.setSizePolicy(sizePolicy1)
        self.textEdit_search.setMaximumSize(QSize(16777215, 50))
        self.textEdit_search.setStyleSheet(u"background-color:rgb(255,255,255)")

        self.horizontalLayout_8.addWidget(self.textEdit_search)

        self.Button_search = QPushButton(self.widget_4)
        self.Button_search.setObjectName(u"Button_search")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Button_search.sizePolicy().hasHeightForWidth())
        self.Button_search.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.Button_search)


        self.verticalLayout_12.addLayout(self.horizontalLayout_8)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_9 = QWidget(self.widget_4)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"background-color: lightgray;")
        self.verticalLayout_3 = QVBoxLayout(self.widget_9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_5 = QWidget(self.widget_9)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.l1 = QLabel(self.widget_5)
        self.l1.setObjectName(u"l1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.l1.sizePolicy().hasHeightForWidth())
        self.l1.setSizePolicy(sizePolicy3)
        self.l1.setMinimumSize(QSize(0, 0))
        self.l1.setMaximumSize(QSize(16777215, 16777215))
        self.l1.setStyleSheet(u"background-color: lightgray;\n"
"            font-weight: bold;\n"
"            border: 1px solid #aaa;")
        self.l1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.l1.setWordWrap(False)

        self.horizontalLayout_12.addWidget(self.l1)

        self.l2 = QLabel(self.widget_5)
        self.l2.setObjectName(u"l2")
        sizePolicy3.setHeightForWidth(self.l2.sizePolicy().hasHeightForWidth())
        self.l2.setSizePolicy(sizePolicy3)
        self.l2.setMinimumSize(QSize(0, 0))
        self.l2.setMaximumSize(QSize(16777215, 16777215))
        self.l2.setStyleSheet(u"background-color: lightgray;\n"
"            font-weight: bold;\n"
"            border: 1px solid #aaa;")
        self.l2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.l2.setWordWrap(False)

        self.horizontalLayout_12.addWidget(self.l2)

        self.l3 = QLabel(self.widget_5)
        self.l3.setObjectName(u"l3")
        sizePolicy3.setHeightForWidth(self.l3.sizePolicy().hasHeightForWidth())
        self.l3.setSizePolicy(sizePolicy3)
        self.l3.setMinimumSize(QSize(0, 0))
        self.l3.setMaximumSize(QSize(16777215, 16777215))
        self.l3.setStyleSheet(u"background-color: lightgray;\n"
"            font-weight: bold;\n"
"            border: 1px solid #aaa;")
        self.l3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.l3.setWordWrap(False)

        self.horizontalLayout_12.addWidget(self.l3)

        self.l4 = QLabel(self.widget_5)
        self.l4.setObjectName(u"l4")
        sizePolicy3.setHeightForWidth(self.l4.sizePolicy().hasHeightForWidth())
        self.l4.setSizePolicy(sizePolicy3)
        self.l4.setMinimumSize(QSize(0, 0))
        self.l4.setMaximumSize(QSize(16777215, 16777215))
        self.l4.setStyleSheet(u"background-color: lightgray;\n"
"            font-weight: bold;\n"
"            border: 1px solid #aaa;")
        self.l4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.l4.setWordWrap(False)

        self.horizontalLayout_12.addWidget(self.l4)

        self.l5 = QLabel(self.widget_5)
        self.l5.setObjectName(u"l5")
        sizePolicy3.setHeightForWidth(self.l5.sizePolicy().hasHeightForWidth())
        self.l5.setSizePolicy(sizePolicy3)
        self.l5.setMinimumSize(QSize(0, 0))
        self.l5.setMaximumSize(QSize(16777215, 16777215))
        self.l5.setStyleSheet(u"background-color: lightgray;\n"
"            font-weight: bold;\n"
"            border: 1px solid #aaa;")
        self.l5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.l5.setWordWrap(False)

        self.horizontalLayout_12.addWidget(self.l5)

        self.l6 = QLabel(self.widget_5)
        self.l6.setObjectName(u"l6")
        sizePolicy3.setHeightForWidth(self.l6.sizePolicy().hasHeightForWidth())
        self.l6.setSizePolicy(sizePolicy3)
        self.l6.setMinimumSize(QSize(0, 0))
        self.l6.setMaximumSize(QSize(16777215, 16777215))
        self.l6.setStyleSheet(u"background-color: lightgray;\n"
"            font-weight: bold;\n"
"            border: 1px solid #aaa;")
        self.l6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.l6.setWordWrap(False)

        self.horizontalLayout_12.addWidget(self.l6)

        self.l7 = QLabel(self.widget_5)
        self.l7.setObjectName(u"l7")
        sizePolicy3.setHeightForWidth(self.l7.sizePolicy().hasHeightForWidth())
        self.l7.setSizePolicy(sizePolicy3)
        self.l7.setMinimumSize(QSize(0, 0))
        self.l7.setMaximumSize(QSize(16777215, 16777215))
        self.l7.setStyleSheet(u"background-color: lightgray;\n"
"            font-weight: bold;\n"
"            border: 1px solid #aaa;")
        self.l7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.l7.setWordWrap(False)

        self.horizontalLayout_12.addWidget(self.l7)

        self.l8 = QLabel(self.widget_5)
        self.l8.setObjectName(u"l8")
        sizePolicy3.setHeightForWidth(self.l8.sizePolicy().hasHeightForWidth())
        self.l8.setSizePolicy(sizePolicy3)
        self.l8.setMinimumSize(QSize(0, 0))
        self.l8.setMaximumSize(QSize(16777215, 16777215))
        self.l8.setStyleSheet(u"background-color: lightgray;\n"
"            font-weight: bold;\n"
"            border: 1px solid #aaa;")
        self.l8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.l8.setWordWrap(False)

        self.horizontalLayout_12.addWidget(self.l8)

        self.l9 = QLabel(self.widget_5)
        self.l9.setObjectName(u"l9")
        sizePolicy3.setHeightForWidth(self.l9.sizePolicy().hasHeightForWidth())
        self.l9.setSizePolicy(sizePolicy3)
        self.l9.setMinimumSize(QSize(0, 0))
        self.l9.setMaximumSize(QSize(16777215, 16777215))
        self.l9.setStyleSheet(u"background-color: lightgray;\n"
"            font-weight: bold;\n"
"            border: 1px solid #aaa;")
        self.l9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.l9.setWordWrap(False)

        self.horizontalLayout_12.addWidget(self.l9)

        self.l10 = QLabel(self.widget_5)
        self.l10.setObjectName(u"l10")
        sizePolicy3.setHeightForWidth(self.l10.sizePolicy().hasHeightForWidth())
        self.l10.setSizePolicy(sizePolicy3)
        self.l10.setStyleSheet(u"background-color: lightgray;\n"
"            font-weight: bold;\n"
"            border: 1px solid #aaa;")
        self.l10.setWordWrap(False)

        self.horizontalLayout_12.addWidget(self.l10)

        self.l11 = QLabel(self.widget_5)
        self.l11.setObjectName(u"l11")
        sizePolicy3.setHeightForWidth(self.l11.sizePolicy().hasHeightForWidth())
        self.l11.setSizePolicy(sizePolicy3)
        self.l11.setMaximumSize(QSize(50, 16777215))
        self.l11.setStyleSheet(u"background-color: lightgray;\n"
"            font-weight: bold;\n"
"            border: 1px solid #aaa;")
        self.l11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.l11.setWordWrap(False)

        self.horizontalLayout_12.addWidget(self.l11)


        self.verticalLayout_3.addWidget(self.widget_5)


        self.verticalLayout_4.addWidget(self.widget_9)

        self.scrollArea = QScrollArea(self.widget_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color:rgb(255,255,255)")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 890, 568))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.verticalLayout_12.addLayout(self.verticalLayout_4)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.widget_hide1 = QWidget(self.widget_4)
        self.widget_hide1.setObjectName(u"widget_hide1")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_hide1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.widget_hide1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_9)

        self.cb_gyear = QComboBox(self.widget_hide1)
        self.cb_gyear.setObjectName(u"cb_gyear")
        self.cb_gyear.setStyleSheet(u"background-color:rgb(255,255,255)")

        self.horizontalLayout_9.addWidget(self.cb_gyear)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.widget_hide1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_10)

        self.cb_semester = QComboBox(self.widget_hide1)
        self.cb_semester.setObjectName(u"cb_semester")
        self.cb_semester.setStyleSheet(u"background-color:rgb(255,255,255)")

        self.horizontalLayout_10.addWidget(self.cb_semester)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_11)

        self.Button_generate = QPushButton(self.widget_hide1)
        self.Button_generate.setObjectName(u"Button_generate")
        sizePolicy.setHeightForWidth(self.Button_generate.sizePolicy().hasHeightForWidth())
        self.Button_generate.setSizePolicy(sizePolicy)
        self.Button_generate.setMaximumSize(QSize(300, 16777215))
        self.Button_generate.setStyleSheet(u"background-color:rgb(255,255,255)")

        self.horizontalLayout_2.addWidget(self.Button_generate)


        self.horizontalLayout_23.addWidget(self.widget_hide1)

        self.Button_switch = QPushButton(self.widget_4)
        self.Button_switch.setObjectName(u"Button_switch")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Button_switch.sizePolicy().hasHeightForWidth())
        self.Button_switch.setSizePolicy(sizePolicy4)

        self.horizontalLayout_23.addWidget(self.Button_switch)


        self.verticalLayout_12.addLayout(self.horizontalLayout_23)


        self.verticalLayout_6.addWidget(self.widget_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy5)
        self.widget_6.setMinimumSize(QSize(0, 160))
        self.widget_6.setMaximumSize(QSize(16777215, 160))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.widget_6)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy6)
        self.scrollArea_2.setMinimumSize(QSize(0, 160))
        self.scrollArea_2.setMaximumSize(QSize(16777215, 160))
        self.scrollArea_2.setStyleSheet(u"background-color:rgb(255,255,255)")
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 908, 160))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.logedit = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.logedit.setObjectName(u"logedit")
        sizePolicy5.setHeightForWidth(self.logedit.sizePolicy().hasHeightForWidth())
        self.logedit.setSizePolicy(sizePolicy5)
        self.logedit.setMinimumSize(QSize(0, 160))
        self.logedit.setMaximumSize(QSize(16777215, 160))
        self.logedit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.logedit.setUndoRedoEnabled(True)
        self.logedit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.logedit, 1, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_15.addWidget(self.scrollArea_2)


        self.verticalLayout.addWidget(self.widget_6)


        self.verticalLayout_6.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_12 = QWidget(self.centralwidget)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMaximumSize(QSize(16777215, 70))
        self.widget_12.setStyleSheet(u"background-color:rgb(255, 204, 153)")
        self.horizontalLayout = QHBoxLayout(self.widget_12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Button_portal = QPushButton(self.widget_12)
        self.Button_portal.setObjectName(u"Button_portal")
        self.Button_portal.setStyleSheet(u"background-color:rgb(255,255,255)")

        self.horizontalLayout.addWidget(self.Button_portal)

        self.Button_bring_basic = QPushButton(self.widget_12)
        self.Button_bring_basic.setObjectName(u"Button_bring_basic")
        self.Button_bring_basic.setStyleSheet(u"background-color:rgb(255,255,255)")

        self.horizontalLayout.addWidget(self.Button_bring_basic)

        self.Button_my_content = QPushButton(self.widget_12)
        self.Button_my_content.setObjectName(u"Button_my_content")
        self.Button_my_content.setStyleSheet(u"background-color:rgb(255,255,255)")

        self.horizontalLayout.addWidget(self.Button_my_content)

        self.Button_current_content = QPushButton(self.widget_12)
        self.Button_current_content.setObjectName(u"Button_current_content")
        self.Button_current_content.setStyleSheet(u"background-color:rgb(255,255,255)")

        self.horizontalLayout.addWidget(self.Button_current_content)


        self.verticalLayout_5.addWidget(self.widget_12)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color:rgb(255,255,255)")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tu6t = QWidget(self.widget)
        self.tu6t.setObjectName(u"tu6t")
        self.tu6t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.tu6t, 16, 2, 1, 1)

        self.label_27 = QLabel(self.widget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_27, 18, 0, 1, 1)

        self.tu6b = QWidget(self.widget)
        self.tu6b.setObjectName(u"tu6b")
        self.tu6b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.tu6b, 18, 2, 1, 1)

        self.th7t = QWidget(self.widget)
        self.th7t.setObjectName(u"th7t")
        self.th7t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.th7t, 19, 4, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.m3b = QWidget(self.widget)
        self.m3b.setObjectName(u"m3b")
        self.m3b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.m3b, 6, 1, 1, 1)

        self.tu4t = QWidget(self.widget)
        self.tu4t.setObjectName(u"tu4t")
        self.tu4t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.tu4t, 10, 2, 1, 1)

        self.m5b = QWidget(self.widget)
        self.m5b.setObjectName(u"m5b")
        self.m5b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.m5b, 10, 1, 1, 1)

        self.f3t = QWidget(self.widget)
        self.f3t.setObjectName(u"f3t")
        self.f3t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.f3t, 5, 5, 1, 1)

        self.th1t = QWidget(self.widget)
        self.th1t.setObjectName(u"th1t")
        self.th1t.setStyleSheet(u"background-color:\"#F2F2F2\"")
        self.horizontalLayout_22 = QHBoxLayout(self.th1t)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")

        self.gridLayout_2.addWidget(self.th1t, 1, 4, 1, 1)

        self.th5m = QWidget(self.widget)
        self.th5m.setObjectName(u"th5m")
        self.th5m.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.th5m, 14, 4, 1, 1)

        self.f1t = QWidget(self.widget)
        self.f1t.setObjectName(u"f1t")
        self.f1t.setStyleSheet(u"background-color:\"#F2F2F2\"")
        self.verticalLayout_36 = QVBoxLayout(self.f1t)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")

        self.gridLayout_2.addWidget(self.f1t, 1, 5, 1, 1)

        self.label_20 = QLabel(self.widget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_20, 9, 0, 1, 1)

        self.m6t = QWidget(self.widget)
        self.m6t.setObjectName(u"m6t")
        self.m6t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.m6t, 11, 1, 1, 1)

        self.w4t = QWidget(self.widget)
        self.w4t.setObjectName(u"w4t")
        self.w4t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.w4t, 7, 3, 1, 1)

        self.m4b = QWidget(self.widget)
        self.m4b.setObjectName(u"m4b")
        self.m4b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.m4b, 8, 1, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy7)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)

        self.tu7m = QWidget(self.widget)
        self.tu7m.setObjectName(u"tu7m")
        self.tu7m.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.tu7m, 20, 2, 1, 1)

        self.tu1t = QWidget(self.widget)
        self.tu1t.setObjectName(u"tu1t")
        self.tu1t.setStyleSheet(u"background-color:\"#F2F2F2\"")
        self.horizontalLayout_4 = QHBoxLayout(self.tu1t)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.gridLayout_2.addWidget(self.tu1t, 1, 2, 1, 1)

        self.tu5b = QWidget(self.widget)
        self.tu5b.setObjectName(u"tu5b")
        self.tu5b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.tu5b, 15, 2, 1, 1)

        self.f3b = QWidget(self.widget)
        self.f3b.setObjectName(u"f3b")
        self.f3b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.f3b, 6, 5, 1, 1)

        self.label_28 = QLabel(self.widget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_28, 16, 0, 1, 1)

        self.m9t = QWidget(self.widget)
        self.m9t.setObjectName(u"m9t")
        self.m9t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.m9t, 17, 1, 1, 1)

        self.f2t = QWidget(self.widget)
        self.f2t.setObjectName(u"f2t")
        self.f2t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.f2t, 3, 5, 1, 1)

        self.label_33 = QLabel(self.widget)
        self.label_33.setObjectName(u"label_33")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy8)
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout_2.addWidget(self.label_33, 0, 2, 1, 1)

        self.w8t = QWidget(self.widget)
        self.w8t.setObjectName(u"w8t")
        self.w8t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.w8t, 15, 3, 1, 1)

        self.th2b = QWidget(self.widget)
        self.th2b.setObjectName(u"th2b")
        self.th2b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.th2b, 6, 4, 1, 1)

        self.label_26 = QLabel(self.widget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_26, 13, 0, 1, 1)

        self.f7t = QWidget(self.widget)
        self.f7t.setObjectName(u"f7t")
        self.f7t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.f7t, 13, 5, 1, 1)

        self.m8b = QWidget(self.widget)
        self.m8b.setObjectName(u"m8b")
        self.m8b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.m8b, 16, 1, 1, 1)

        self.f1b = QWidget(self.widget)
        self.f1b.setObjectName(u"f1b")
        self.f1b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.f1b, 2, 5, 1, 1)

        self.tu1b = QWidget(self.widget)
        self.tu1b.setObjectName(u"tu1b")
        self.tu1b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.tu1b, 3, 2, 1, 1)

        self.m1b = QWidget(self.widget)
        self.m1b.setObjectName(u"m1b")
        self.m1b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.m1b, 2, 1, 1, 1)

        self.f2b = QWidget(self.widget)
        self.f2b.setObjectName(u"f2b")
        self.f2b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.f2b, 4, 5, 1, 1)

        self.label_21 = QLabel(self.widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_21, 10, 0, 1, 1)

        self.th4m = QWidget(self.widget)
        self.th4m.setObjectName(u"th4m")
        self.th4m.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.th4m, 11, 4, 1, 1)

        self.label_24 = QLabel(self.widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_24, 12, 0, 1, 1)

        self.m10b = QWidget(self.widget)
        self.m10b.setObjectName(u"m10b")
        self.m10b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.m10b, 20, 1, 1, 1)

        self.th7m = QWidget(self.widget)
        self.th7m.setObjectName(u"th7m")
        self.th7m.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.th7m, 20, 4, 1, 1)

        self.f10t = QWidget(self.widget)
        self.f10t.setObjectName(u"f10t")
        self.f10t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.f10t, 19, 5, 1, 1)

        self.w5t = QWidget(self.widget)
        self.w5t.setObjectName(u"w5t")
        self.w5t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.w5t, 9, 3, 1, 1)

        self.f5b = QWidget(self.widget)
        self.f5b.setObjectName(u"f5b")
        self.f5b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.f5b, 10, 5, 1, 1)

        self.tu5m = QWidget(self.widget)
        self.tu5m.setObjectName(u"tu5m")
        self.tu5m.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.tu5m, 14, 2, 1, 1)

        self.f5t = QWidget(self.widget)
        self.f5t.setObjectName(u"f5t")
        self.f5t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.f5t, 9, 5, 1, 1)

        self.tu1m = QWidget(self.widget)
        self.tu1m.setObjectName(u"tu1m")
        self.tu1m.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.tu1m, 2, 2, 1, 1)

        self.label_35 = QLabel(self.widget)
        self.label_35.setObjectName(u"label_35")
        sizePolicy8.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy8)
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout_2.addWidget(self.label_35, 0, 4, 1, 1)

        self.w10t = QWidget(self.widget)
        self.w10t.setObjectName(u"w10t")
        self.w10t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.w10t, 19, 3, 1, 1)

        self.tu4b = QWidget(self.widget)
        self.tu4b.setObjectName(u"tu4b")
        self.tu4b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.tu4b, 12, 2, 1, 1)

        self.m3t = QWidget(self.widget)
        self.m3t.setObjectName(u"m3t")
        self.m3t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.m3t, 5, 1, 1, 1)

        self.w6b = QWidget(self.widget)
        self.w6b.setObjectName(u"w6b")
        self.w6b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.w6b, 12, 3, 1, 1)

        self.th4b = QWidget(self.widget)
        self.th4b.setObjectName(u"th4b")
        self.th4b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.th4b, 12, 4, 1, 1)

        self.tu3m = QWidget(self.widget)
        self.tu3m.setObjectName(u"tu3m")
        self.tu3m.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.tu3m, 8, 2, 1, 1)

        self.w4b = QWidget(self.widget)
        self.w4b.setObjectName(u"w4b")
        self.w4b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.w4b, 8, 3, 1, 1)

        self.th1b = QWidget(self.widget)
        self.th1b.setObjectName(u"th1b")
        self.th1b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.th1b, 3, 4, 1, 1)

        self.tu2b = QWidget(self.widget)
        self.tu2b.setObjectName(u"tu2b")
        self.tu2b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.tu2b, 6, 2, 1, 1)

        self.w9t = QWidget(self.widget)
        self.w9t.setObjectName(u"w9t")
        self.w9t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.w9t, 17, 3, 1, 1)

        self.w10b = QWidget(self.widget)
        self.w10b.setObjectName(u"w10b")
        self.w10b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.w10b, 20, 3, 1, 1)

        self.w5b = QWidget(self.widget)
        self.w5b.setObjectName(u"w5b")
        self.w5b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.w5b, 10, 3, 1, 1)

        self.m9b = QWidget(self.widget)
        self.m9b.setObjectName(u"m9b")
        self.m9b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.m9b, 18, 1, 1, 1)

        self.tu6m = QWidget(self.widget)
        self.tu6m.setObjectName(u"tu6m")
        self.tu6m.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.tu6m, 17, 2, 1, 1)

        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_17, 6, 0, 1, 1)

        self.m5t = QWidget(self.widget)
        self.m5t.setObjectName(u"m5t")
        self.m5t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.m5t, 9, 1, 1, 1)

        self.tu2m = QWidget(self.widget)
        self.tu2m.setObjectName(u"tu2m")
        self.tu2m.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.tu2m, 5, 2, 1, 1)

        self.f10b = QWidget(self.widget)
        self.f10b.setObjectName(u"f10b")
        self.f10b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.f10b, 20, 5, 1, 1)

        self.th3m = QWidget(self.widget)
        self.th3m.setObjectName(u"th3m")
        self.th3m.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.th3m, 8, 4, 1, 1)

        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_22, 11, 0, 1, 1)

        self.w7b = QWidget(self.widget)
        self.w7b.setObjectName(u"w7b")
        self.w7b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.w7b, 14, 3, 1, 1)

        self.f4t = QWidget(self.widget)
        self.f4t.setObjectName(u"f4t")
        self.f4t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.f4t, 7, 5, 1, 1)

        self.f8t = QWidget(self.widget)
        self.f8t.setObjectName(u"f8t")
        self.f8t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.f8t, 15, 5, 1, 1)

        self.label_36 = QLabel(self.widget)
        self.label_36.setObjectName(u"label_36")
        sizePolicy8.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy8)
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout_2.addWidget(self.label_36, 0, 5, 1, 1)

        self.th1m = QWidget(self.widget)
        self.th1m.setObjectName(u"th1m")
        self.th1m.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.th1m, 2, 4, 1, 1)

        self.th4t = QWidget(self.widget)
        self.th4t.setObjectName(u"th4t")
        self.th4t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.th4t, 10, 4, 1, 1)

        self.th5t = QWidget(self.widget)
        self.th5t.setObjectName(u"th5t")
        self.th5t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.th5t, 13, 4, 1, 1)

        self.label_34 = QLabel(self.widget)
        self.label_34.setObjectName(u"label_34")
        sizePolicy8.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy8)
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout_2.addWidget(self.label_34, 0, 3, 1, 1)

        self.w6t = QWidget(self.widget)
        self.w6t.setObjectName(u"w6t")
        self.w6t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.w6t, 11, 3, 1, 1)

        self.m6b = QWidget(self.widget)
        self.m6b.setObjectName(u"m6b")
        self.m6b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.m6b, 12, 1, 1, 1)

        self.m2t = QWidget(self.widget)
        self.m2t.setObjectName(u"m2t")
        self.m2t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.m2t, 3, 1, 1, 1)

        self.m7b = QWidget(self.widget)
        self.m7b.setObjectName(u"m7b")
        self.m7b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.m7b, 14, 1, 1, 1)

        self.f6b = QWidget(self.widget)
        self.f6b.setObjectName(u"f6b")
        self.f6b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.f6b, 12, 5, 1, 1)

        self.f9t = QWidget(self.widget)
        self.f9t.setObjectName(u"f9t")
        self.f9t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.f9t, 17, 5, 1, 1)

        self.tu2t = QWidget(self.widget)
        self.tu2t.setObjectName(u"tu2t")
        self.tu2t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.tu2t, 4, 2, 1, 1)

        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_15, 4, 0, 1, 1)

        self.w1b = QWidget(self.widget)
        self.w1b.setObjectName(u"w1b")
        self.w1b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.w1b, 2, 3, 1, 1)

        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_18, 7, 0, 1, 1)

        self.f8b = QWidget(self.widget)
        self.f8b.setObjectName(u"f8b")
        self.f8b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.f8b, 16, 5, 1, 1)

        self.th2t = QWidget(self.widget)
        self.th2t.setObjectName(u"th2t")
        self.th2t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.th2t, 4, 4, 1, 1)

        self.th3t = QWidget(self.widget)
        self.th3t.setObjectName(u"th3t")
        self.th3t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.th3t, 7, 4, 1, 1)

        self.th6t = QWidget(self.widget)
        self.th6t.setObjectName(u"th6t")
        self.th6t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.th6t, 16, 4, 1, 1)

        self.label_25 = QLabel(self.widget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_25, 15, 0, 1, 1)

        self.w7t = QWidget(self.widget)
        self.w7t.setObjectName(u"w7t")
        self.w7t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.w7t, 13, 3, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy8.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy8)
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.w1t = QWidget(self.widget)
        self.w1t.setObjectName(u"w1t")
        self.w1t.setStyleSheet(u"background-color:\"#F2F2F2\"")
        self.verticalLayout_35 = QVBoxLayout(self.w1t)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")

        self.gridLayout_2.addWidget(self.w1t, 1, 3, 1, 1)

        self.w2b = QWidget(self.widget)
        self.w2b.setObjectName(u"w2b")
        self.w2b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.w2b, 4, 3, 1, 1)

        self.f6t = QWidget(self.widget)
        self.f6t.setObjectName(u"f6t")
        self.f6t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.f6t, 11, 5, 1, 1)

        self.f7b = QWidget(self.widget)
        self.f7b.setObjectName(u"f7b")
        self.f7b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.f7b, 14, 5, 1, 1)

        self.w8b = QWidget(self.widget)
        self.w8b.setObjectName(u"w8b")
        self.w8b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.w8b, 16, 3, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.f4b = QWidget(self.widget)
        self.f4b.setObjectName(u"f4b")
        self.f4b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.f4b, 8, 5, 1, 1)

        self.label_31 = QLabel(self.widget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_31, 17, 0, 1, 1)

        self.th6m = QWidget(self.widget)
        self.th6m.setObjectName(u"th6m")
        self.th6m.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.th6m, 17, 4, 1, 1)

        self.tu4m = QWidget(self.widget)
        self.tu4m.setObjectName(u"tu4m")
        self.tu4m.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.tu4m, 11, 2, 1, 1)

        self.m2b = QWidget(self.widget)
        self.m2b.setObjectName(u"m2b")
        self.m2b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.m2b, 4, 1, 1, 1)

        self.f9b = QWidget(self.widget)
        self.f9b.setObjectName(u"f9b")
        self.f9b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.f9b, 18, 5, 1, 1)

        self.th2m = QWidget(self.widget)
        self.th2m.setObjectName(u"th2m")
        self.th2m.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.th2m, 5, 4, 1, 1)

        self.m7t = QWidget(self.widget)
        self.m7t.setObjectName(u"m7t")
        self.m7t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.m7t, 13, 1, 1, 1)

        self.m10t = QWidget(self.widget)
        self.m10t.setObjectName(u"m10t")
        self.m10t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.m10t, 19, 1, 1, 1)

        self.label_30 = QLabel(self.widget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_30, 19, 0, 1, 1)

        self.m1t = QWidget(self.widget)
        self.m1t.setObjectName(u"m1t")
        self.m1t.setStyleSheet(u"background-color:\"#F2F2F2\"")
        self.horizontalLayout_3 = QHBoxLayout(self.m1t)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.gridLayout_2.addWidget(self.m1t, 1, 1, 1, 1)

        self.label_19 = QLabel(self.widget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_19, 8, 0, 1, 1)

        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_16, 5, 0, 1, 1)

        self.w9b = QWidget(self.widget)
        self.w9b.setObjectName(u"w9b")
        self.w9b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.w9b, 18, 3, 1, 1)

        self.w3t = QWidget(self.widget)
        self.w3t.setObjectName(u"w3t")
        self.w3t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.w3t, 5, 3, 1, 1)

        self.m4t = QWidget(self.widget)
        self.m4t.setObjectName(u"m4t")
        self.m4t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.m4t, 7, 1, 1, 1)

        self.th5b = QWidget(self.widget)
        self.th5b.setObjectName(u"th5b")
        self.th5b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.th5b, 15, 4, 1, 1)

        self.th3b = QWidget(self.widget)
        self.th3b.setObjectName(u"th3b")
        self.th3b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.th3b, 9, 4, 1, 1)

        self.w3b = QWidget(self.widget)
        self.w3b.setObjectName(u"w3b")
        self.w3b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.w3b, 6, 3, 1, 1)

        self.w2t = QWidget(self.widget)
        self.w2t.setObjectName(u"w2t")
        self.w2t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.w2t, 3, 3, 1, 1)

        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_23, 14, 0, 1, 1)

        self.m8t = QWidget(self.widget)
        self.m8t.setObjectName(u"m8t")
        self.m8t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.m8t, 15, 1, 1, 1)

        self.tu7t = QWidget(self.widget)
        self.tu7t.setObjectName(u"tu7t")
        self.tu7t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.tu7t, 19, 2, 1, 1)

        self.tu3t = QWidget(self.widget)
        self.tu3t.setObjectName(u"tu3t")
        self.tu3t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.tu3t, 7, 2, 1, 1)

        self.th6b = QWidget(self.widget)
        self.th6b.setObjectName(u"th6b")
        self.th6b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.th6b, 18, 4, 1, 1)

        self.tu3b = QWidget(self.widget)
        self.tu3b.setObjectName(u"tu3b")
        self.tu3b.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.tu3b, 9, 2, 1, 1)

        self.tu5t = QWidget(self.widget)
        self.tu5t.setObjectName(u"tu5t")
        self.tu5t.setStyleSheet(u"background-color:\"#F2F2F2\"")

        self.gridLayout_2.addWidget(self.tu5t, 13, 2, 1, 1)

        self.label_32 = QLabel(self.widget)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_32, 20, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.widget)

        self.mainlabel = QLabel(self.centralwidget)
        self.mainlabel.setObjectName(u"mainlabel")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.mainlabel.sizePolicy().hasHeightForWidth())
        self.mainlabel.setSizePolicy(sizePolicy9)
        self.mainlabel.setMinimumSize(QSize(363, 0))
        self.mainlabel.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift Condensed"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.mainlabel.setFont(font1)
        self.mainlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.mainlabel)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\uc785\ud559\ub144\ub3c4", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uc804\uacf5 \uc120\ud0dd", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\ud559\ub144", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\ud559\uc810\uc124\uc815", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\ub0a8\uc740\ud559\uc810", None))
        self.lb_credit.setText("")
        self.Button_search.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9", None))
        self.l1.setText(QCoreApplication.translate("MainWindow", u"\uacfc\ubaa9\ucf54\ub4dc", None))
        self.l2.setText(QCoreApplication.translate("MainWindow", u"\uc785\ud559\ub144\ub3c4", None))
        self.l3.setText(QCoreApplication.translate("MainWindow", u"\uc804\uacf5", None))
        self.l4.setText(QCoreApplication.translate("MainWindow", u"\ud559\ub144", None))
        self.l5.setText(QCoreApplication.translate("MainWindow", u"\ud559\uae30", None))
        self.l6.setText(QCoreApplication.translate("MainWindow", u"\uad50\uacfc\uad6c\ubd84", None))
        self.l7.setText(QCoreApplication.translate("MainWindow", u"\uad50\uacfc\ubaa9\uba85", None))
        self.l8.setText(QCoreApplication.translate("MainWindow", u"\ud559\uc810", None))
        self.l9.setText(QCoreApplication.translate("MainWindow", u"\uc218\uac15\uc5ec\ubd80", None))
        self.l10.setText(QCoreApplication.translate("MainWindow", u"\uc218\uac15\uacc4\ud68d\uc11c", None))
        self.l11.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\ub144\ub3c4", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\ud559\uae30", None))
        self.Button_generate.setText(QCoreApplication.translate("MainWindow", u"\uc0dd\uc131\n"
"\ud558\uae30", None))
        self.Button_switch.setText(QCoreApplication.translate("MainWindow", u"\uc804\ud658\ud558\uae30", None))
        self.logedit.setPlainText("")
        self.Button_portal.setText(QCoreApplication.translate("MainWindow", u"\ud3ec\ud0c8\n"
"\ub85c\uadf8\uc778", None))
        self.Button_bring_basic.setText(QCoreApplication.translate("MainWindow", u"\uae30\ucd08 \uc218\uac15\n"
" \uac00\uc838\uc624\uae30", None))
        self.Button_my_content.setText(QCoreApplication.translate("MainWindow", u"\ub0b4 \uc218\uac15 \ub0b4\uc5ed\n"
"\uac00\uc838\uc624\uae30", None))
        self.Button_current_content.setText(QCoreApplication.translate("MainWindow", u"\ub0b4 \ud604\uc7ac \uc218\uac15\n"
" \uac00\uc838\uc624\uae30", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"17:30", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"09:30", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"13:00", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"10:00", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"16:30", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\ud654", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"15:00", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"13:30", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"14:30", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\ubaa9", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"11:30", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"14:00", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\uae08", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\uc218", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"10:30", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"12:00", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"16:00", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc6d4", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"09:00", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"17:00", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"18:00", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"12:30", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"11:00", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"15:30", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"18:30", None))
        self.mainlabel.setText(QCoreApplication.translate("MainWindow", u"\uc218\uac15 \uc2e0\uccad \ubcf4\uc870 \ud504\ub85c\uadf8\ub7a8 by \uc774\uc218\uc6a9", None))
    # retranslateUi

