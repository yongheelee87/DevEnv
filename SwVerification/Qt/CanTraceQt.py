from templates import *
from PyQt5.QtCore import pyqtSlot
from Lib.Inst import canBus


class CanTraceWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # SET AS IMAGE WIDGETS
        self.ui_cantrc = Ui_cantrace()
        self.ui_cantrc.setupUi(self)

        # 변수 선언 먼저
        self.CAN_Frame = ''
        self.Rx_rate = 200

        self.ui_cantrc.pText_monitor1 = None
        self.ui_cantrc.pText_monitor2 = None
        self.ui_cantrc.pText_monitor3 = None
        self.ui_cantrc.pText_monitor4 = None
        self.ui_cantrc.pText_monitor5 = None

        self.lst_monitor = [self.ui_cantrc.pText_monitor0, self.ui_cantrc.pText_monitor1, self.ui_cantrc.pText_monitor2, self.ui_cantrc.pText_monitor3, self.ui_cantrc.pText_monitor4, self.ui_cantrc.pText_monitor5]
        for i in range(len(canBus.lst_dev)-1):
            self.set_monitor(i+1)
        
        self.connectLineInit()
        self.connectToggleInit()

        self.Rx_timer = QTimer()
        self.Rx_timer.timeout.connect(self.func_update_rx_data)

    def connectToggleInit(self):
        self.ui_cantrc.btn_Rx_Read.toggled.connect(self.func_btn_Rx_Read_toggle)

    def connectLineInit(self):
        self.ui_cantrc.line_Rx_Rate.textChanged.connect(self.func_line_Rx_Rate)
        self.ui_cantrc.line_Rx_Rate.returnPressed.connect(self.func_line_Rx_Rate)

    def set_monitor(self, ind):
        self.lst_monitor[ind] = QPlainTextEdit(self.ui_cantrc.frame)
        self.lst_monitor[ind].setObjectName(u"pText_monitor_3")

        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lst_monitor[ind].sizePolicy().hasHeightForWidth())
        self.lst_monitor[ind].setSizePolicy(sizePolicy1)

        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.lst_monitor[ind].setFont(font1)

        self.ui_cantrc.horizontalLayout_2.addWidget(self.lst_monitor[ind])

    def show_widget(self, main_geometry):
        self.move(main_geometry.topRight())
        self.show()
        self.activateWindow()

    def func_line_Rx_Rate(self):
        str_line_Rx_Rate = self.ui_cantrc.line_Rx_Rate.text()
        if str_line_Rx_Rate == '':
            str_line_Rx_Rate = '200'  # 초기 값
        self.Rx_rate = int(str_line_Rx_Rate.strip())

    def func_btn_Rx_Read(self):
        self.Rx_timer.start()

    def func_update_rx_data(self):
        idx = 0
        for dev in canBus.lst_dev:
            str_rx = f'{dev}\n\n'
            for id in canBus.devs[dev].rx.msg_dict.keys():
                can_rx_data = canBus.devs[dev].msg_read_id(can_id=int(id))
                if bool(can_rx_data):
                    str_can_rx_data = f'Frame: {str(canBus.devs[dev].get_msg_name(int(id)))}\n'
                    str_can_rx_data += str(can_rx_data).replace("{", '').replace("}", '').replace(", ", '\n')
                    str_rx += f'{str_can_rx_data}\n\n'
            pre_location = self.lst_monitor[idx].verticalScrollBar().value()
            self.lst_monitor[idx].setPlainText(str_rx)
            self.lst_monitor[idx].verticalScrollBar().setValue(pre_location)
            idx += 1

    @pyqtSlot(bool)
    def func_btn_Rx_Read_toggle(self, state):
        if state is True:
            self.ui_cantrc.btn_Rx_Read.setStyleSheet("font-weight:500;color:black;background-color: #42f566;border: 1px solid black;")
            self.ui_cantrc.btn_Rx_Read.setText("READ REAL-TIME")
            self.Rx_timer.stop()
        else:
            self.Rx_timer.setInterval(self.Rx_rate)
            self.ui_cantrc.btn_Rx_Read.setStyleSheet("font-weight:500;color:black;background-color: rgba(255, 0, 0, 0.70);border: 1px solid black;")
            self.ui_cantrc.btn_Rx_Read.setText("STOP READ")
            self.Rx_timer.start()
