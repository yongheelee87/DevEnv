from templates import *
from Lib.Common import logging_print
from Lib.Inst import get_inst_status
from . CanQt import CanWindow
from . Trace32Qt import Trace32Window


class InstWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # SET AS IMAGE WIDGETS
        self.ui_inst = Ui_inst()
        self.ui_inst.setupUi(self)

        # QWidget 선언
        self.canWidget = CanWindow()
        self.t32Widget = Trace32Window()

        self.ui_inst.stackedWidget.addWidget(self.canWidget)
        self.ui_inst.stackedWidget.addWidget(self.t32Widget)
        self.ui_inst.stackedWidget.setCurrentWidget(self.canWidget)

        self.connectBtnInit()

        self.df_inst = None
        self.update_tbl_from_df()

    def connectBtnInit(self):
        self.ui_inst.btn_TRACE32.clicked.connect(self.func_btn_TRACE32)
        self.ui_inst.btn_CAN.clicked.connect(self.func_btn_CAN)
        self.ui_inst.btn_Visa.clicked.connect(self.func_btn_Visa)
        self.ui_inst.btn_Refresh.clicked.connect(self.update_tbl_from_df)

    def func_btn_TRACE32(self):
        self.ui_inst.stackedWidget.setCurrentWidget(self.t32Widget)

    def func_btn_CAN(self):
        self.ui_inst.stackedWidget.setCurrentWidget(self.canWidget)

    def func_btn_Visa(self):
        self.ui_inst.stackedWidget.setCurrentWidget(self.ui_inst.new_page)

    def update_tbl_from_df(self):
        # 테이블 위젯 값 쓰기
        self.ui_inst.tbl_inst_status.clear()
        # Select Dataframe
        self.df_inst = get_inst_status()  # Instruments status 가져오기
        logging_print(f"Current Test Environment\n{self.df_inst}\n")
        # Table Contents
        self.ui_inst.tbl_inst_status.setColumnCount(len(self.df_inst.columns))
        self.ui_inst.tbl_inst_status.setHorizontalHeaderLabels(self.df_inst.columns)
        self.ui_inst.tbl_inst_status.setRowCount(len(self.df_inst.index))

        for r in range(len(self.df_inst.index)):
            for c in range(len(self.df_inst.columns)):
                self.ui_inst.tbl_inst_status.setItem(r, c, QTableWidgetItem(str(self.df_inst.iloc[r][c])))
        self.ui_inst.tbl_inst_status.resizeColumnsToContents()
