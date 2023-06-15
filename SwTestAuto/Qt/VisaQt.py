from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QWidget, QVBoxLayout, QSpacerItem, QSizePolicy
from Qt.VisaWidget import VisaWidget
from Lib.Inst.visaLib import *

visa_form = uic.loadUiType("./Qt/static/ui/VisaQt.ui")[0]


class VisaView(QDialog, visa_form):
    def __init__(self, ):
        super().__init__()
        self.setupUi(self)

        self.initWidget()

    def initWidget(self):
        vertical_layout = QVBoxLayout()
        temp_widget = QWidget()
        temp_widget.setLayout(vertical_layout)

        for dev in visa.lst_dev:
            visa_widget = VisaWidget(dev)
            temp_widget.layout().addWidget(visa_widget)
        self.Area_Inst.setWidget(temp_widget)

    def show_dialog(self, main_geometry):
        self.move(main_geometry.topRight())
        self.show()
        self.activateWindow()
