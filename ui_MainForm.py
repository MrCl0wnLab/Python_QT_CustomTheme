# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainFormeBIMnh.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1599, 941)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_Direita = QFrame(self.centralwidget)
        self.frame_Direita.setObjectName(u"frame_Direita")
        self.frame_Direita.setMinimumSize(QSize(700, 0))
        self.frame_Direita.setFrameShape(QFrame.StyledPanel)
        self.frame_Direita.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_Direita)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.frame_Direita)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 300))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.radioButton = QRadioButton(self.frame)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.frame)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_2.addWidget(self.radioButton_2)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_10 = QPushButton(self.groupBox)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_2.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.groupBox)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_2.addWidget(self.pushButton_11)

        self.pushButton_9 = QPushButton(self.groupBox)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_2.addWidget(self.pushButton_9)

        self.pushButton_6 = QPushButton(self.groupBox)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.groupBox)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_2.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.groupBox)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_2.addWidget(self.pushButton_5)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer)

        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.frame)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.spinBox = QSpinBox(self.frame)
        self.spinBox.setObjectName(u"spinBox")

        self.verticalLayout_2.addWidget(self.spinBox)

        self.spinBox_2 = QSpinBox(self.frame)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_2.addWidget(self.spinBox_2)


        self.verticalLayout.addWidget(self.frame)

        self.tabWidget = QTabWidget(self.frame_Direita)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 2, 1, 1)

        self.textEdit = QTextEdit(self.tab)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_2.addWidget(self.textEdit, 1, 2, 1, 1)

        self.progressBar = QProgressBar(self.tab)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout_2.addWidget(self.progressBar, 2, 2, 1, 1)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.horizontalLayout.addWidget(self.frame_Direita)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer)

        self.frame_Esquerda = QFrame(self.centralwidget)
        self.frame_Esquerda.setObjectName(u"frame_Esquerda")
        self.frame_Esquerda.setMinimumSize(QSize(658, 0))
        self.frame_Esquerda.setFrameShape(QFrame.StyledPanel)
        self.frame_Esquerda.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_Esquerda)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget_2 = QTableWidget(self.frame_Esquerda)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.gridLayout.addWidget(self.tableWidget_2, 1, 0, 1, 1)

        self.calendarWidget = QCalendarWidget(self.frame_Esquerda)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setSelectionMode(QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)

        self.gridLayout.addWidget(self.calendarWidget, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_Esquerda)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1599, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Column_00", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Column_01", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Column_02", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Column_03", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Column_05", None));
    # retranslateUi

