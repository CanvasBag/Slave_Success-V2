# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(687, 364)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(687, 364))
        MainWindow.setMaximumSize(QtCore.QSize(687, 364))
        MainWindow.setStyleSheet("Qwidget::setFixedSize(587,334);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.prjButton = QtWidgets.QPushButton(self.centralwidget)
        self.prjButton.setGeometry(QtCore.QRect(10, 20, 51, 20))
        self.prjButton.setObjectName("prjButton")
        self.prjLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.prjLineEdit.setGeometry(QtCore.QRect(80, 20, 201, 20))
        self.prjLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prjLineEdit.setReadOnly(True)
        self.prjLineEdit.setObjectName("prjLineEdit")
        self.taskLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.taskLineEdit.setEnabled(True)
        self.taskLineEdit.setGeometry(QtCore.QRect(80, 70, 201, 20))
        self.taskLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.taskLineEdit.setReadOnly(True)
        self.taskLineEdit.setObjectName("taskLineEdit")
        self.taskButton = QtWidgets.QPushButton(self.centralwidget)
        self.taskButton.setEnabled(False)
        self.taskButton.setGeometry(QtCore.QRect(10, 70, 51, 20))
        self.taskButton.setObjectName("taskButton")
        self.slaveCkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.slaveCkBox.setGeometry(QtCore.QRect(50, 170, 181, 17))
        self.slaveCkBox.setObjectName("slaveCkBox")
        self.microCkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.microCkBox.setGeometry(QtCore.QRect(50, 230, 181, 17))
        self.microCkBox.setObjectName("microCkBox")
        self.logCkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.logCkBox.setGeometry(QtCore.QRect(50, 260, 181, 17))
        self.logCkBox.setStyleSheet("")
        self.logCkBox.setObjectName("logCkBox")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 140, 191, 191))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.runSlaveCkBox = QtWidgets.QCheckBox(self.groupBox)
        self.runSlaveCkBox.setEnabled(False)
        self.runSlaveCkBox.setGeometry(QtCore.QRect(20, 60, 141, 16))
        self.runSlaveCkBox.setObjectName("runSlaveCkBox")
        self.exportsButton = QtWidgets.QPushButton(self.groupBox)
        self.exportsButton.setEnabled(False)
        self.exportsButton.setGeometry(QtCore.QRect(40, 155, 75, 23))
        self.exportsButton.setObjectName("exportsButton")
        self.logWindow = QtWidgets.QTextBrowser(self.centralwidget)
        self.logWindow.setGeometry(QtCore.QRect(300, 20, 371, 311))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.logWindow.setFont(font)
        self.logWindow.setStyleSheet("color: rgb(93, 93, 93);\n"
"margin: 0; \n"
"padding: 0;\n"
"size: 8 px;")
        self.logWindow.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.logWindow.setTabStopWidth(80)
        self.logWindow.setObjectName("logWindow")
        self.groupBox.raise_()
        self.prjButton.raise_()
        self.prjLineEdit.raise_()
        self.taskLineEdit.raise_()
        self.taskButton.raise_()
        self.logCkBox.raise_()
        self.microCkBox.raise_()
        self.slaveCkBox.raise_()
        self.logWindow.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 687, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.prjButton, self.taskButton)
        MainWindow.setTabOrder(self.taskButton, self.slaveCkBox)
        MainWindow.setTabOrder(self.slaveCkBox, self.microCkBox)
        MainWindow.setTabOrder(self.microCkBox, self.logCkBox)
        MainWindow.setTabOrder(self.logCkBox, self.exportsButton)
        MainWindow.setTabOrder(self.exportsButton, self.prjLineEdit)
        MainWindow.setTabOrder(self.prjLineEdit, self.taskLineEdit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Slave Sucess V2.0"))
        self.prjButton.setText(_translate("MainWindow", "Prj"))
        self.taskButton.setText(_translate("MainWindow", "Task"))
        self.slaveCkBox.setText(_translate("MainWindow", "Export Slave Task"))
        self.microCkBox.setText(_translate("MainWindow", "Export Microstation Script"))
        self.logCkBox.setText(_translate("MainWindow", "Export Log File"))
        self.groupBox.setTitle(_translate("MainWindow", "Report Options"))
        self.runSlaveCkBox.setText(_translate("MainWindow", "Start Slave"))
        self.exportsButton.setText(_translate("MainWindow", "Export"))
        self.logWindow.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[TerraScan Project]</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

