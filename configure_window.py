# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configure_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_configure_window(object):
    def setupUi(self, configure_window):
        configure_window.setObjectName(_fromUtf8("configure_window"))
        configure_window.resize(603, 363)
        self.centralwidget = QtGui.QWidget(configure_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.test_label = QtGui.QLabel(self.centralwidget)
        self.test_label.setGeometry(QtCore.QRect(80, 100, 211, 161))
        self.test_label.setText(_fromUtf8(""))
        self.test_label.setObjectName(_fromUtf8("test_label"))
        self.node_details = QtGui.QFrame(self.centralwidget)
        self.node_details.setGeometry(QtCore.QRect(50, 20, 441, 201))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 217, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 185, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 76, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 102, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(153, 204, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 217, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 185, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 76, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 102, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(153, 204, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 76, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 217, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 185, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 76, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 102, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 76, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 76, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.node_details.setPalette(palette)
        self.node_details.setAutoFillBackground(True)
        self.node_details.setFrameShape(QtGui.QFrame.StyledPanel)
        self.node_details.setFrameShadow(QtGui.QFrame.Raised)
        self.node_details.setObjectName(_fromUtf8("node_details"))
        self.NodeLabel = QtGui.QLabel(self.node_details)
        self.NodeLabel.setGeometry(QtCore.QRect(140, 0, 191, 41))
        self.NodeLabel.setTextFormat(QtCore.Qt.RichText)
        self.NodeLabel.setScaledContents(True)
        self.NodeLabel.setObjectName(_fromUtf8("NodeLabel"))
        self.analog_count = QtGui.QSpinBox(self.node_details)
        self.analog_count.setGeometry(QtCore.QRect(80, 60, 42, 22))
        self.analog_count.setMaximum(1000)
        self.analog_count.setObjectName(_fromUtf8("analog_count"))
        self.label_4 = QtGui.QLabel(self.node_details)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 71, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.node_details)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 71, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.digital_count = QtGui.QSpinBox(self.node_details)
        self.digital_count.setGeometry(QtCore.QRect(80, 120, 42, 22))
        self.digital_count.setMaximum(1000)
        self.digital_count.setObjectName(_fromUtf8("digital_count"))
        self.sensors = QtGui.QFrame(self.node_details)
        self.sensors.setGeometry(QtCore.QRect(130, 40, 271, 151))
        self.sensors.setFrameShape(QtGui.QFrame.Box)
        self.sensors.setFrameShadow(QtGui.QFrame.Raised)
        self.sensors.setObjectName(_fromUtf8("sensors"))
        self.analog_sensors_list = QtGui.QComboBox(self.sensors)
        self.analog_sensors_list.setGeometry(QtCore.QRect(10, 60, 71, 22))
        self.analog_sensors_list.setObjectName(_fromUtf8("analog_sensors_list"))
        self.label_6 = QtGui.QLabel(self.sensors)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 61, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.sensors)
        self.label_7.setGeometry(QtCore.QRect(180, 90, 61, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.sensors)
        self.label_8.setGeometry(QtCore.QRect(0, 30, 91, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.digital_sensors_list = QtGui.QComboBox(self.sensors)
        self.digital_sensors_list.setGeometry(QtCore.QRect(170, 60, 81, 22))
        self.digital_sensors_list.setObjectName(_fromUtf8("digital_sensors_list"))
        self.label_9 = QtGui.QLabel(self.sensors)
        self.label_9.setGeometry(QtCore.QRect(170, 30, 81, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.analog_sensor_input = QtGui.QSpinBox(self.sensors)
        self.analog_sensor_input.setGeometry(QtCore.QRect(20, 120, 42, 22))
        self.analog_sensor_input.setObjectName(_fromUtf8("analog_sensor_input"))
        self.digital_sensor_input = QtGui.QSpinBox(self.sensors)
        self.digital_sensor_input.setGeometry(QtCore.QRect(190, 120, 42, 22))
        self.digital_sensor_input.setObjectName(_fromUtf8("digital_sensor_input"))
        self.label_11 = QtGui.QLabel(self.sensors)
        self.label_11.setGeometry(QtCore.QRect(20, 10, 47, 13))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.sensors)
        self.label_12.setGeometry(QtCore.QRect(180, 10, 47, 13))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 250, 131, 61))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
       
        configure_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(configure_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        configure_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(configure_window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        configure_window.setStatusBar(self.statusbar)

        self.retranslateUi(configure_window)
        QtCore.QMetaObject.connectSlotsByName(configure_window)

    def retranslateUi(self, configure_window):
        configure_window.setWindowTitle(_translate("configure_window", "MainWindow", None))
        self.NodeLabel.setText(_translate("configure_window", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Node</span></p></body></html>", None))
        self.label_4.setText(_translate("configure_window", "<html><head/><body><p align=\"center\">Analog count</p></body></html>", None))
        self.label_5.setText(_translate("configure_window", "Digital Count", None))
        self.label_6.setText(_translate("configure_window", "Analog Input", None))
        self.label_7.setText(_translate("configure_window", "Digital Input", None))
        self.label_8.setText(_translate("configure_window", "<html><head/><body><p align=\"center\">Analog Sensors </p></body></html>", None))
        self.label_9.setText(_translate("configure_window", "<html><head/><body><p align=\"center\">Digital Sensors</p></body></html>", None))
        self.label_11.setText(_translate("configure_window", "<html><head/><body><p align=\"center\">Analog</p></body></html>", None))
        self.label_12.setText(_translate("configure_window", "<html><head/><body><p align=\"center\">Digital</p></body></html>", None))
        self.pushButton.setText(_translate("configure_window", "OK", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    configure_window = QtGui.QMainWindow()
    ui = Ui_configure_window()
    ui.setupUi(configure_window)
    configure_window.show()
    sys.exit(app.exec_())

