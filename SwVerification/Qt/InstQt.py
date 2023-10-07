
from Qt.CanQt import CanWindow
from Qt.Trace32Qt import Trace32Window

from templates import *
from Lib.Inst.Trace32Lib import *
from Lib.Inst.canLib import *
from Lib.Inst.visaLib import *


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
        self.df_inst = self._get_inst_status()
        logging_print("Current Test Environment\n{}\n".format(self.df_inst))
        # Table Contents
        self.ui_inst.tbl_inst_status.setColumnCount(len(self.df_inst.columns))
        self.ui_inst.tbl_inst_status.setHorizontalHeaderLabels(self.df_inst.columns.tolist())
        self.ui_inst.tbl_inst_status.setRowCount(len(self.df_inst.index))

        for r in range(len(self.df_inst.index)):
            for c in range(len(self.df_inst.columns)):
                self.ui_inst.tbl_inst_status.setItem(r, c, QTableWidgetItem(str(self.df_inst.iloc[r][c])))
        self.ui_inst.tbl_inst_status.resizeColumnsToContents()

    def _get_inst_status(self):
        lst_inst_data = []
        lst_inst = [i for i in Configure.set.sections() if 'system' not in i and 'XCP' not in i]
        for inst in lst_inst:
            if Configure.set[inst]['type'] == 'T32':
                lst_inst_data.append([inst, t32.status])
            elif Configure.set[inst]['type'] == 'can':
                lst_inst_data.append([inst, False if canBus.devs[inst].status == CAN_ERR else True])
            else:
                lst_inst_data.append([inst, visa.status[inst]])
        return pd.DataFrame(lst_inst_data, columns=['Name', 'Connect'])

