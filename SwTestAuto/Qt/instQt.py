import pandas as pd
from PyQt5 import uic
from PyQt5.QtWidgets import *
from Lib.Inst.Trace32Lib import *
from Lib.Inst.canLib import *
from Lib.Inst.visaLib import *
from Lib.Inst.telnetLib import *
from Qt.Trace32Qt import Trace32View
from Qt.CanQt import CanView
from Qt.VisaQt import VisaView
from Qt.TelnetQt import TelnetView
from Lib.Common.basicFunction import *

inst_form = uic.loadUiType("./Qt/static/ui/instQt.ui")[0]


class InstView(QWidget, inst_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # QWidget 선언
        self.trace32Widget = Trace32View()
        self.canWidget = CanView()
        self.visaDialog = VisaView()
        self.telnetWidget = TelnetView()

        self.backgroundInit()
        self.connectBtnInit()

        self.update_tbl_from_df()

    def __del__(self):
        print(".... INSTRUMENT QT CLOSE.....\n")

    def backgroundInit(self):
        title = "INSTRUMENT QT"
        self.setWindowTitle(title)

    def show_widget(self, main_geometry):
        self.move(main_geometry.topRight())
        self.show()
        self.activateWindow()

    def connectBtnInit(self):
        self.btn_TRACE32.clicked.connect(self.func_btn_TRACE32)
        self.btn_CAN.clicked.connect(self.func_btn_CAN)
        self.btn_Visa.clicked.connect(self.func_btn_Visa)
        self.btn_Telnet.clicked.connect(self.func_btn_Telnet)
        self.btn_Refresh.clicked.connect(self.update_tbl_from_df)

    def func_btn_TRACE32(self):
        main_geometry = self.frameGeometry()
        self.trace32Widget.show_widget(main_geometry)

    def func_btn_CAN(self):
        main_geometry = self.frameGeometry()
        self.canWidget.show_widget(main_geometry)

    def func_btn_Visa(self):
        main_geometry = self.frameGeometry()
        self.visaDialog.show_dialog(main_geometry)

    def func_btn_Telnet(self):
        main_geometry = self.frameGeometry()
        self.telnetWidget.show_widget(main_geometry)

    def update_tbl_from_df(self):
        # 테이블 위젯 값 쓰기
        self.tbl_inst_status.clear()
        # Select Dataframe
        self.df_inst = self._get_inst_status()
        logging_print("Current Test Environment\n{}\n".format(self.df_inst))
        # Table Contents
        self.tbl_inst_status.setColumnCount(len(self.df_inst.columns))
        self.tbl_inst_status.setHorizontalHeaderLabels(self.df_inst.columns.tolist())
        self.tbl_inst_status.setRowCount(len(self.df_inst.index))

        for r in range(len(self.df_inst.index)):
            for c in range(len(self.df_inst.columns)):
                self.tbl_inst_status.setItem(r, c, QTableWidgetItem(str(self.df_inst.iloc[r][c])))
        self.tbl_inst_status.resizeColumnsToContents()

    def _get_inst_status(self):
        lst_inst_data = []
        lst_inst = [i for i in Configure.set.sections() if 'system' not in i and 'XCP' not in i]
        for inst in lst_inst:
            if inst == 'TRACE32':
                lst_inst_data.append([inst, Configure.set[inst]['type'], t32.status])
            elif inst == 'CAN':
                lst_inst_data.append([inst, Configure.set[inst]['type'], False if canBus.status == CAN_ERR else True])
            elif inst == 'TELNET':
                lst_inst_data.append([inst, Configure.set[inst]['type'], telnet.status])
            else:
                lst_inst_data.append([inst, Configure.set[inst]['type'], visa.status[inst]])
        return pd.DataFrame(lst_inst_data, columns=['Name', 'Type', 'Connection'])
