# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remote.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RemoteControl(object):
    def setupUi(self, RemoteControl):
        RemoteControl.setObjectName("RemoteControl")
        RemoteControl.resize(150, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RemoteControl.sizePolicy().hasHeightForWidth())
        RemoteControl.setSizePolicy(sizePolicy)
        RemoteControl.setMinimumSize(QtCore.QSize(150, 300))
        RemoteControl.setMaximumSize(QtCore.QSize(150, 300))
        self.Power = QtWidgets.QPushButton(RemoteControl)
        self.Power.setGeometry(QtCore.QRect(40, 160, 71, 23))
        self.Power.setObjectName("Power")
        self.c_channel_up = QtWidgets.QPushButton(RemoteControl)
        self.c_channel_up.setGeometry(QtCore.QRect(30, 200, 20, 21))
        self.c_channel_up.setObjectName("c_channel_up")
        self.c_channel_down = QtWidgets.QPushButton(RemoteControl)
        self.c_channel_down.setGeometry(QtCore.QRect(30, 250, 21, 21))
        self.c_channel_down.setObjectName("c_channel_down")
        self.vol_up = QtWidgets.QPushButton(RemoteControl)
        self.vol_up.setGeometry(QtCore.QRect(90, 200, 21, 21))
        self.vol_up.setObjectName("vol_up")
        self.vol_down = QtWidgets.QPushButton(RemoteControl)
        self.vol_down.setGeometry(QtCore.QRect(90, 250, 21, 21))
        self.vol_down.setObjectName("vol_down")
        self.label = QtWidgets.QLabel(RemoteControl)
        self.label.setGeometry(QtCore.QRect(30, 230, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(RemoteControl)
        self.label_2.setGeometry(QtCore.QRect(90, 230, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(RemoteControl)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 131, 151))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(RemoteControl)
        QtCore.QMetaObject.connectSlotsByName(RemoteControl)

    def retranslateUi(self, RemoteControl):
        _translate = QtCore.QCoreApplication.translate
        RemoteControl.setWindowTitle(_translate("RemoteControl", "Form"))
        self.Power.setText(_translate("RemoteControl", "Power"))
        self.c_channel_up.setText(_translate("RemoteControl", "+"))
        self.c_channel_down.setText(_translate("RemoteControl", "-"))
        self.vol_up.setText(_translate("RemoteControl", "+"))
        self.vol_down.setText(_translate("RemoteControl", "-"))
        self.label.setText(_translate("RemoteControl", "Ch."))
        self.label_2.setText(_translate("RemoteControl", "Vol"))
        self.label_3.setText(_translate("RemoteControl", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RemoteControl = QtWidgets.QWidget()
    ui = Ui_RemoteControl()
    ui.setupUi(RemoteControl)
    RemoteControl.show()
    sys.exit(app.exec_())
