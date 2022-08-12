from PyQt5 import QtWidgets
from television import *

class Controller(QtWidgets.QMainWindow, Ui_RemoteControl):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.tv = Television()

        self.Power.clicked.connect(lambda : self.tv_power())
        self.vol_up.clicked.connect(lambda: self.tv_volume_up())
        self.vol_down.clicked.connect(lambda: self.tv_volume_down())
        self.c_channel_down.clicked.connect(lambda: self.tv_channel_down())
        self.c_channel_up.clicked.connect(lambda: self.tv_channel_up())

    def tv_power(self):
        self.tv.power()
        self.label_3.setText(self.tv.__str__())

    def tv_volume_up(self):
        self.tv.volume_up()
        self.label_3.setText(self.tv.__str__())

    def tv_volume_down(self):
        self.tv.volume_down()
        self.label_3.setText(self.tv.__str__())

    def tv_channel_down(self):
        self.tv.channel_down()
        self.label_3.setText(self.tv.__str__())

    def tv_channel_up(self):
        self.tv.channel_up()
        self.label_3.setText(self.tv.__str__())





