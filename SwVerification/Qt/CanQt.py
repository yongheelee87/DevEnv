from templates import *
from PyQt5.QtCore import pyqtSlot
from Qt.CanTraceQt import CanTraceWindow
from Lib.Inst.canLib import *


class CanWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # SET AS IMAGE WIDGETS
        self.ui_can = Ui_can()
        self.ui_can.setupUi(self)

        # QWidget 선언
        self.TraceWidget = CanTraceWindow()

        # 변수 선언 먼저
        self.CAN_Frame = ''
        self.dbc_dev = ''
        self.read_dev = ''
        self.Rx_rate = 200
        
        self.backgroundInit()
        self.connectBtnInit()
        self.connectLineInit()
        self.connectToggleInit()
        self.connectTextInit()
        self.connectCboxInit()
        
        self.Rx_timer = QTimer()
        self.Rx_timer.timeout.connect(self.func_update_rx_data)

    # noinspection PyMethodMayBeStatic
    def backgroundInit(self):
        self.ui_can.cbox_db_dev.clear()
        self.ui_can.cbox_db_dev.addItems(canBus.lst_dev)
        self.dbc_dev = self.ui_can.cbox_db_dev.currentText().strip()  # 현재 설정된 DBC dev

        self.ui_can.cbox_read_dev.clear()
        self.ui_can.cbox_read_dev.addItems(canBus.lst_dev)
        self.read_dev = self.ui_can.cbox_read_dev.currentText().strip()  # 현재 설정된 Read dev

    def connectBtnInit(self):
        self.ui_can.btn_Connect.clicked.connect(self.func_btn_Connect)
        self.ui_can.btn_dbc_load.clicked.connect(self.func_btn_dbc_load)
        self.ui_can.btn_Read_CAN_Period_Sig.clicked.connect(self.func_btn_Read_CAN_Period_Sig)
        self.ui_can.btn_Stop_CAN_Period.clicked.connect(self.func_btn_Stop_CAN_Period)
        self.ui_can.btn_send.clicked.connect(self.func_btn_send)
        self.ui_can.btn_trace.clicked.connect(self.func_btn_trace)

    def connectToggleInit(self):
        self.ui_can.btn_Rx_Read.toggled.connect(self.func_btn_Rx_Read_toggle)

    def connectLineInit(self):
        self.ui_can.line_Rx_Rate.textChanged.connect(self.func_line_Rx_Rate)
        self.ui_can.line_Rx_Rate.returnPressed.connect(self.func_line_Rx_Rate)
        if len(canBus.lst_dev) != 0:
            self.ui_can.line_dbc_path.setText(Configure.set[self.dbc_dev]['DBC_file_path'])

        self._update_status()

    def connectTextInit(self):
        self.ui_can.pText_cmd.textChanged.connect(self.func_pText_cmd)

    def connectCboxInit(self):
        self.ui_can.cbox_db_dev.currentIndexChanged.connect(self.func_cbox_db_dev)
        self.ui_can.cbox_read_dev.currentIndexChanged.connect(self.func_cbox_read_dev)

    def func_btn_trace(self):
        main_geometry = self.frameGeometry()
        self.TraceWidget.show_widget(main_geometry)

    def func_cbox_db_dev(self):
        self.dbc_dev = self.ui_can.cbox_db_dev.currentText().strip()  # 현재 설정된 DBC dev
        self.ui_can.line_dbc_path.setText(canBus.devs[self.dbc_dev].db_path)

    def func_cbox_read_dev(self):
        self.read_dev = self.ui_can.cbox_read_dev.currentText().strip()  # 현재 설정된 Read dev

    def func_btn_dbc_load(self):
        input_dbc_file = QFileDialog.getOpenFileName(self, 'Open File', './data/input/can', 'dbc File(*.dbc);; All File(*)')[0]
        if input_dbc_file:
            canBus.devs[self.dbc_dev].db_path = input_dbc_file
            canBus.devs[self.dbc_dev].db = database.load_file(input_dbc_file)  # path of .dbc file; CAN DBC 불러오기
            self.ui_can.line_dbc_path.setText(canBus.devs[self.dbc_dev].db_path)

    # noinspection PyMethodMayBeStatic
    def func_btn_Connect(self):
        if len(canBus.lst_dev) != 0:
            for dev in canBus.lst_dev:
                config = canBus.devs[dev].config
                canBus.devs[dev].connect_dev(bus_type=config['bus_type'],
                                             ch=config['channel'],
                                             app_type=config['app_type'],
                                             bit_rate=int(config['bit_rate']),
                                             data_rate=int(config['data_rate']))  # CAN device 연결
        self._update_status()

    def func_line_Frame(self):
        str_line_CAN_Frame = self.ui_can.line_Frame.text()
        self.CAN_Frame = str_line_CAN_Frame.strip()
        if self.CAN_Frame == 'Frame':
            self.CAN_Frame = ''

    def func_line_Rx_Rate(self):
        str_line_Rx_Rate = self.ui_can.line_Rx_Rate.text()
        if str_line_Rx_Rate == '':
            str_line_Rx_Rate = '200'  # 초기 값
        self.Rx_rate = int(str_line_Rx_Rate.strip())

    # noinspection PyMethodMayBeStatic
    def func_btn_Read_CAN_Period_Sig(self):
        logging_print("Activated CAN Period Signal: {}\n".format(canBus.get_all_period_msg()))

    # noinspection PyMethodMayBeStatic
    def func_btn_Stop_CAN_Period(self):
        canBus.stop_all_period_msg()

    def func_btn_Rx_Read(self):
        self.Rx_timer.start()

    def func_btn_send(self):
        try:
            lst_cmd_str = self.ui_can.pText_cmd.toPlainText().split("\n")
            read_msg = ''
            for cmd_str in lst_cmd_str:
                cmd = cmd_str.strip()
                if 'W:' in cmd[:2]:
                    lst_cmd = cmd[2:].strip().replace("'", '').split(",")
                    dev = lst_cmd[0].strip()
                    if len(lst_cmd) <= 5:
                        canBus.devs[dev].msg_period_write(lst_cmd[1].strip(), lst_cmd[2].strip(), float(lst_cmd[3].strip()), float(lst_cmd[4].strip()))
                    else:
                        canBus.devs[dev].msg_period_write(lst_cmd[1].strip(), lst_cmd[2].strip(), float(lst_cmd[3].strip()), float(lst_cmd[4].strip()), True)
                    read_msg += 'Write Msg {}\n'.format(lst_cmd)
                elif 'WP:' in cmd[:3]:
                    lst_cmd = cmd[3:].strip().replace("'", '').split(",")
                    dev = lst_cmd[0].strip()
                    if len(lst_cmd) <= 5:
                        canBus.devs[dev].msg_period_write(lst_cmd[1].strip(), lst_cmd[2].strip(), float(lst_cmd[3].strip()), float(lst_cmd[4].strip()))
                    else:
                        canBus.devs[dev].msg_period_write(lst_cmd[1].strip(), lst_cmd[2].strip(), float(lst_cmd[3].strip()), float(lst_cmd[4].strip()), True)
                    read_msg += 'Write Period Msg {}\n'.format(lst_cmd)
                elif 'R:' in cmd[:2]:
                    lst_cmd = cmd[2:].strip().replace("'", '').split(",")
                    dev = lst_cmd[0].strip()
                    can_rx_data = canBus.devs[dev].msg_read_name(frame_name=lst_cmd[1].strip())
                    read_msg += (str(can_rx_data[lst_cmd[2].strip()]) + '\n')
                elif 'T:' in cmd[:2]:
                    time.sleep(float(cmd[2:].strip()))
            self.ui_can.pText_monitor.setPlainText(read_msg)
        except ValueError:
            logging_print('Error: invalid literal in the box\n')

    def func_update_rx_data(self):
        # HEX형태로 입력한건지 메세지 이름으로 입력한건지 구분
        if '0x' in self.CAN_Frame:
            can_rx_data = canBus.devs[self.read_dev].msg_read_id(can_id=int(self.CAN_Frame, 16))
        elif self.CAN_Frame != '':
            can_rx_data = canBus.devs[self.read_dev].msg_read_name(frame_name=self.CAN_Frame)
        else:
            can_rx_data = False

        if bool(can_rx_data):
            str_can_rx_data = str(can_rx_data).replace("{", '').replace("}", '').replace(", ", '\n')
            pre_location = self.ui_can.pText_monitor.verticalScrollBar().value()
            self.ui_can.pText_monitor.setPlainText(str_can_rx_data)
            self.ui_can.pText_monitor.verticalScrollBar().setValue(pre_location)
            # print("Success: READ CAN MESSAGE: {}\n".format(can_rx_data))
        else:
            self.ui_can.pText_monitor.setPlainText("Error: READ CAN MESSAGE")
            # print("Error: READ CAN MESSAGE\n")

    @pyqtSlot(bool)
    def func_btn_Rx_Read_toggle(self, state):
        if state is True:
            self.ui_can.btn_Rx_Read.setStyleSheet("font-weight:500;color:black;background-color: #42f566;border: 1px solid black;")
            self.ui_can.btn_Rx_Read.setText("READ REAL-TIME")
            self.Rx_timer.stop()
        else:
            self.Rx_timer.setInterval(self.Rx_rate)
            self.func_line_Frame()
            self.ui_can.btn_Rx_Read.setStyleSheet("font-weight:500;color:black;background-color: rgba(255, 0, 0, 0.70);border: 1px solid black;")
            self.ui_can.btn_Rx_Read.setText("STOP READ")
            self.Rx_timer.start()

    def func_pText_cmd(self):
        if self.ui_can.pText_cmd.toPlainText().replace('\n', '') == 'Option':
            self.ui_can.pText_cmd.setPlainText('W: Write Msg (Dev, Frame, Signal, Value, Sec)\n'
                                               'WP: Write Period Msg (Dev, Frame, Signal, Value, Sec)\n'
                                               'R: Read Msg (Dev, Frame, Signal)\n'
                                               'T: Time Delay (ex. T: 0.2)\n'
                                               'Option: Display Option')

    def _update_status(self):
        lst_fail_dev = canBus.check_status()

        if len(lst_fail_dev) == 0:
            self.ui_can.line_connect_status.setText('All Connected')
            self.ui_can.line_connect_status.setStyleSheet("color:black;font-weight:600;background-color: %s;border: 1px solid transparent;" % "#42f566")
        else:
            fail_devs = ', '.join(lst_fail_dev)
            self.ui_can.line_connect_status.setText('Not Connected: {}'.format(fail_devs))
            self.ui_can.line_connect_status.setStyleSheet("color:white;font-weight:600;background-color: %s;border: 1px solid transparent;" % "rgba(255, 0, 0, 0.70)")

