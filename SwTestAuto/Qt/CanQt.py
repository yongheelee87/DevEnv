import time
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QTimer, pyqtSlot
from Qt.XcpQt import XcpView
from Lib.Inst.canLib import *

Can_form = uic.loadUiType("./Qt/static/ui/CanQt.ui")[0]


class CanView(QWidget, Can_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.backgroundInit()
        self.connectBtnInit()
        self.connectLineInit()
        self.connectToggleInit()
        self.connectTextInit()

        # QWidget 선언
        self.XcpWidget = XcpView()

        self.CAN_Frame = ''
        self.Rx_rate = 200
        self.Rx_timer = QTimer()
        self.Rx_timer.timeout.connect(self.func_update_rx_data)

    def __del__(self):
        print(".... CAN QT CLOSE.....\n")

    def backgroundInit(self):
        canBus.check_status()

    def connectBtnInit(self):
        self.btn_CAN_XCP.clicked.connect(self.func_btn_CAN_XCP)
        self.btn_Connect.clicked.connect(self.func_btn_Connect)
        self.btn_CAN_Write.clicked.connect(self.func_btn_CAN_Write)
        self.btn_CAN_Write_Period.clicked.connect(self.func_btn_CAN_Write_Period)
        self.btn_Read_CAN_Period_Sig.clicked.connect(self.func_btn_Read_CAN_Period_Sig)
        self.btn_Stop_CAN_Period.clicked.connect(self.func_btn_Stop_CAN_Period)
        self.btn_dbc_load.clicked.connect(self.func_btn_dbc_load)
        self.btn_send.clicked.connect(self.func_btn_send)

    def connectToggleInit(self):
        self.btn_Rx_Read.toggled.connect(self.func_btn_Rx_Read_toggle)

    def connectLineInit(self):
        self.line_Rx_Rate.textChanged.connect(self.func_line_Rx_Rate)
        self.line_Rx_Rate.returnPressed.connect(self.func_line_Rx_Rate)
        if 'CAN' in Configure.set.sections():
            self.line_dbc_path.setText(Configure.set['CAN']['DBC_file_path'])

        self._update_status()

    def connectTextInit(self):
        self.pText_cmd.textChanged.connect(self.func_pText_cmd)

    def show_widget(self, main_geometry):
        self.move(main_geometry.topRight())
        self.show()
        self.activateWindow()

    def func_btn_dbc_load(self):
        dbc_name = QFileDialog.getOpenFileName(self, 'Open File', './data/input/can', 'dbc File(*.dbc);; All File(*)',
                                               options=QFileDialog.DontUseNativeDialog)
        input_dbc_file = dbc_name[0]
        if input_dbc_file:
            self.line_dbc_path.setText(input_dbc_file)
            self._update_dbc(input_dbc_file)

    def func_btn_CAN_XCP(self):
        main_geometry = self.frameGeometry()
        self.XcpWidget.show_widget(main_geometry)

    # noinspection PyMethodMayBeStatic
    def func_btn_CAN_Write(self):
        canBus.msg_write(self.line_CAN_Frame.text().strip(), self.line_CAN_Signal.text().strip(),
                         float(self.line_CAN_Value.text().strip()), float(self.line_CAN_Period.text().strip()))

    # noinspection PyMethodMayBeStatic
    def func_btn_CAN_Write_Period(self):
        canBus.msg_period_write(self.line_CAN_Frame.text().strip(), self.line_CAN_Signal.text().strip(),
                                float(self.line_CAN_Value.text().strip()), float(self.line_CAN_Period.text().strip()))

    # noinspection PyMethodMayBeStatic
    def func_btn_Connect(self):
        canBus.connect_dev(bus_type=Configure.set['CAN']['bus_type'],
                           ch=Configure.set['CAN']['channel'],
                           app_type=Configure.set['CAN']['app_type'],
                           bit_rate=int(Configure.set['CAN']['bit_rate']),
                           data_rate=int(Configure.set['CAN']['data_rate']))  # CAN BUS 연결
        self._update_status()

    def func_line_Frame(self):
        str_line_CAN_Frame = self.line_Frame.text()
        self.CAN_Frame = str_line_CAN_Frame.strip()
        if self.CAN_Frame == 'Frame':
            self.CAN_Frame = ''

    def func_line_Rx_Rate(self):
        str_line_Rx_Rate = self.line_Rx_Rate.text()
        if str_line_Rx_Rate == '':
            str_line_Rx_Rate = '200'  # 초기 값
        self.Rx_rate = int(str_line_Rx_Rate.strip())

    # noinspection PyMethodMayBeStatic
    def func_btn_Read_CAN_Period_Sig(self):
        logging_print("Activated CAN Period Signal: {}\n".format(canBus.tx_data))

    # noinspection PyMethodMayBeStatic
    def func_btn_Stop_CAN_Period(self):
        canBus.msg_stop_period_write()

    def func_btn_Rx_Read(self):
        self.Rx_timer.start()

    def func_btn_send(self):
        try:
            lst_cmd_str = self.pText_cmd.toPlainText().split("\n")
            read_msg = ''
            for cmd_str in lst_cmd_str:
                cmd = cmd_str.strip()
                if 'W:' in cmd[:2]:
                    lst_cmd = cmd[2:].strip().split(",")
                    canBus.msg_write(lst_cmd[0].strip(), lst_cmd[1].strip(), float(lst_cmd[2].strip()),
                                     float(lst_cmd[3].strip()))
                    read_msg += 'Write Msg {}\n'.format(lst_cmd)
                elif 'WP:' in cmd[:3]:
                    lst_cmd = cmd[3:].strip().split(",")
                    canBus.msg_period_write(lst_cmd[0].strip(), lst_cmd[1].strip(), float(lst_cmd[2].strip()),
                                            float(lst_cmd[3].strip()))
                    read_msg += 'Write Period Msg {}\n'.format(lst_cmd)
                elif 'R:' in cmd[:2]:
                    lst_cmd = cmd[2:].strip().split(",")
                    can_rx_data = canBus.msg_read_name(frame_name=lst_cmd[0].strip())
                    read_msg += (str(can_rx_data[lst_cmd[1].strip()]) + '\n')
                elif 'T:' in cmd[:2]:
                    time.sleep(float(cmd[2:].strip()))
            self.pText_monitor.setPlainText(read_msg)
        except ValueError:
            logging_print('Error: invalid literal in the box\n')

    def func_update_rx_data(self):
        # HEX형태로 입력한건지 메세지 이름으로 입력한건지 구분
        if '0x' in self.CAN_Frame:
            can_rx_data = canBus.msg_read_id(can_id=int(self.CAN_Frame, 16))
        elif self.CAN_Frame != '':
            can_rx_data = canBus.msg_read_name(frame_name=self.CAN_Frame)
        else:
            can_rx_data = False

        if bool(can_rx_data):
            str_can_rx_data = str(can_rx_data).replace("{", '').replace("}", '').replace(", ", '\n')
            pre_location = self.pText_monitor.verticalScrollBar().value()
            self.pText_monitor.setPlainText(str_can_rx_data)
            self.pText_monitor.verticalScrollBar().setValue(pre_location)
            # print("Success: READ CAN MESSAGE: {}\n".format(can_rx_data))
        else:
            self.pText_monitor.setPlainText("Error: READ CAN MESSAGE")
            # print("Error: READ CAN MESSAGE\n")

    @pyqtSlot(bool)
    def func_btn_Rx_Read_toggle(self, state):
        if state is True:
            self.btn_Rx_Read.setStyleSheet("background-color: #42f566;border: 1px solid black;")
            self.btn_Rx_Read.setText("READ REAL-TIME")
            self.Rx_timer.stop()
        else:
            self.Rx_timer.setInterval(self.Rx_rate)
            self.func_line_Frame()
            self.btn_Rx_Read.setStyleSheet("background-color: rgba(255, 0, 0, 0.70);border: 1px solid black;")
            self.btn_Rx_Read.setText("STOP READ")
            self.Rx_timer.start()

    def func_pText_cmd(self):
        if self.pText_cmd.toPlainText().replace('\n', '') == 'Option':
            self.pText_cmd.setPlainText('W: Write Msg (Frame, Signal, Value, Sec)\n'
                                        'WP: Write Period Msg (Frame, Signal, Value, Sec)\n'
                                        'R: Read Msg (Frame, Signal)\n'
                                        'T: Time Delay (ex. T: 0.2)\n'
                                        'Option: Display Option')

    def _update_status(self):
        if canBus.status != CAN_ERR:
            self.line_connect_status.setText('Connected')
            self.line_connect_status.setStyleSheet("background-color: %s;border: 1px solid transparent;" % "#42f566")
        else:
            self.line_connect_status.setText('Not Connected')
            self.line_connect_status.setStyleSheet(
                "background-color: %s;border: 1px solid transparent;" % "rgba(255, 0, 0, 0.70)")

    # noinspection PyMethodMayBeStatic
    def _update_dbc(self, path):
        canBus.db = database.load_file(path)  # path of .dbc file; CAN DBC 불러오기
        if 'XCP' in Configure.set.sections():
            canBus.xcp.xcp_rx_id = canBus._get_msg_id(Configure.set['XCP']['xcp_rx_name'])  # XCP RX ID 업데이트
            canBus.can_rx.xcp_id = canBus._get_msg_id(Configure.set['XCP']['xcp_tx_name'])  # XCP TX ID 업데이트
