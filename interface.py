# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1217, 869)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.time_combo = QtWidgets.QComboBox(self.centralwidget)
        self.time_combo.setGeometry(QtCore.QRect(810, 30, 261, 31))
        self.time_combo.setObjectName("time_combo")
        self.time_col = QtWidgets.QTextBrowser(self.centralwidget)
        self.time_col.setGeometry(QtCore.QRect(580, 30, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.time_col.setFont(font)
        self.time_col.setObjectName("time_col")
        self.period_from = QtWidgets.QTextBrowser(self.centralwidget)
        self.period_from.setGeometry(QtCore.QRect(580, 60, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.period_from.setFont(font)
        self.period_from.setObjectName("period_from")
        self.period_to = QtWidgets.QTextBrowser(self.centralwidget)
        self.period_to.setGeometry(QtCore.QRect(580, 90, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.period_to.setFont(font)
        self.period_to.setObjectName("period_to")
        self.from_combo = QtWidgets.QDateEdit(self.centralwidget)
        self.from_combo.setGeometry(QtCore.QRect(810, 60, 261, 31))
        self.from_combo.setObjectName("from_combo")
        self.to_combo = QtWidgets.QDateEdit(self.centralwidget)
        self.to_combo.setGeometry(QtCore.QRect(810, 90, 261, 31))
        self.to_combo.setObjectName("to_combo")
        self.query_button = QtWidgets.QPushButton(self.centralwidget)
        self.query_button.setGeometry(QtCore.QRect(580, 560, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.query_button.setFont(font)
        self.query_button.setObjectName("query_button")
        self.group_by = QtWidgets.QTextBrowser(self.centralwidget)
        self.group_by.setGeometry(QtCore.QRect(580, 360, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.group_by.setFont(font)
        self.group_by.setObjectName("group_by")
        self.by_col_combo = QtWidgets.QComboBox(self.centralwidget)
        self.by_col_combo.setGeometry(QtCore.QRect(810, 360, 261, 31))
        self.by_col_combo.setObjectName("by_col_combo")
        self.agg_col = QtWidgets.QTextBrowser(self.centralwidget)
        self.agg_col.setGeometry(QtCore.QRect(580, 390, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.agg_col.setFont(font)
        self.agg_col.setObjectName("agg_col")
        self.agg_col_combo = QtWidgets.QComboBox(self.centralwidget)
        self.agg_col_combo.setGeometry(QtCore.QRect(810, 390, 261, 31))
        self.agg_col_combo.setObjectName("agg_col_combo")
        self.agg_func_combo = QtWidgets.QComboBox(self.centralwidget)
        self.agg_func_combo.setGeometry(QtCore.QRect(810, 420, 261, 31))
        self.agg_func_combo.setObjectName("agg_func_combo")
        self.agg_func = QtWidgets.QTextBrowser(self.centralwidget)
        self.agg_func.setGeometry(QtCore.QRect(580, 420, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.agg_func.setFont(font)
        self.agg_func.setObjectName("agg_func")
        self.export_button = QtWidgets.QPushButton(self.centralwidget)
        self.export_button.setGeometry(QtCore.QRect(740, 560, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.export_button.setFont(font)
        self.export_button.setObjectName("export_button")
        self.record_button = QtWidgets.QPushButton(self.centralwidget)
        self.record_button.setGeometry(QtCore.QRect(900, 560, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.record_button.setFont(font)
        self.record_button.setAutoFillBackground(False)
        self.record_button.setObjectName("record_button")
        self.recordBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.recordBrowser.setGeometry(QtCore.QRect(580, 470, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.recordBrowser.setFont(font)
        self.recordBrowser.setObjectName("recordBrowser")
        self.recordText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.recordText.setGeometry(QtCore.QRect(810, 470, 261, 31))
        self.recordText.setObjectName("recordText")
        self.filter_combo = QtWidgets.QComboBox(self.centralwidget)
        self.filter_combo.setGeometry(QtCore.QRect(580, 160, 231, 31))
        self.filter_combo.setObjectName("filter_combo")
        self.operator_combo = QtWidgets.QComboBox(self.centralwidget)
        self.operator_combo.setGeometry(QtCore.QRect(830, 160, 60, 31))
        self.operator_combo.setObjectName("operator_combo")
        self.compare_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.compare_text.setGeometry(QtCore.QRect(910, 160, 161, 31))
        self.compare_text.setObjectName("compare_text")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(980, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(980, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        self.filter_list = QtWidgets.QListWidget(self.centralwidget)
        self.filter_list.setGeometry(QtCore.QRect(580, 210, 381, 81))
        self.filter_list.setObjectName("filter_list")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1217, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.time_col.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:600;\">Time Column:</span></p></body></html>"))
        self.period_from.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:600;\">Period From:</span></p></body></html>"))
        self.period_to.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:600;\">Period To:</span></p></body></html>"))
        self.query_button.setText(_translate("MainWindow", "Query"))
        self.group_by.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:600;\">Group By:</span></p></body></html>"))
        self.agg_col.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:600;\">Aggregate Column:</span></p></body></html>"))
        self.agg_func.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:600;\">Aggregate Function:</span></p></body></html>"))
        self.export_button.setText(_translate("MainWindow", "Export"))
        self.record_button.setText(_translate("MainWindow", "Record"))
        self.recordBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:600;\">Record Name:</span></p></body></html>"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())