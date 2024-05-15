import os
import time
from templates import *
from Lib.Common import logging_print
from Lib.Inst import t32


class Trace32Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # SET AS IMAGE WIDGETS
        self.ui_t32 = Ui_trace32()
        self.ui_t32.setupUi(self)
        self.cmm_path = os.path.join('./data/input/script', 'removed.cmm')

        self.backgroundInit()
        self.connectBtnInit()
        self.connectLineInit()
        self.connectTextInit()

    def backgroundInit(self):
        t32.check_status()

    def connectBtnInit(self):
        self.ui_t32.btn_Connect.clicked.connect(self.func_btn_Connect)
        self.ui_t32.btn_cmm_load.clicked.connect(self.func_btn_cmm_load)
        self.ui_t32.btn_send.clicked.connect(self.func_btn_send)

    def connectLineInit(self):
        self._update_status()

    def connectTextInit(self):
        self.ui_t32.pText_cmd.textChanged.connect(self.func_pText_cmd)

    def func_btn_Connect(self):
        t32.connect_dev()
        self._update_status()

    def func_btn_cmm_load(self):
        input_cmm_file = QFileDialog.getOpenFileName(self, 'Open File', os.path.dirname(self.cmm_path), 'cmm File(*.cmm);; All File(*)')[0]
        if input_cmm_file:
            self.ui_t32.line_cmm_path.setText(input_cmm_file)
            t32.cmd(f"CD.DO {input_cmm_file}")
            self.cmm_path = input_cmm_file

    def func_btn_send(self):
        try:
            lst_cmd_str = self.ui_t32.pText_cmd.toPlainText().split("\n")
            read_msg = ''
            for cmd_str in lst_cmd_str:
                cmd = cmd_str.strip()
                if 'W:' in cmd[:2]:
                    lst_cmd = cmd[2:].strip().split(",")
                    str_value = lst_cmd[1].strip()
                    value = float(str_value) if '.' in str_value else int(str_value)
                    t32.write_symbol(symbol=lst_cmd[0].strip(), value=value)
                    read_msg += f'Write Msg {lst_cmd}\n'
                elif 'R:' in cmd[:2]:
                    val = t32.read_symbol(symbol=cmd[2:].strip())
                    if val is None:
                        val = 'None'
                    read_msg += f'Read Msg: {str(val)}\n'
                elif 'T:' in cmd[:2]:
                    time.sleep(float(cmd[2:].strip()))
            self.ui_t32.pText_monitor.setPlainText(read_msg)
        except ValueError:
            logging_print('Error: invalid literal in the box\n')

    def func_pText_cmd(self):
        if self.ui_t32.pText_cmd.toPlainText().replace('\n', '') == 'Option':
            self.ui_t32.pText_cmd.setPlainText('W: Write Msg (Symbol, Value)\n'
                                               'R: Read Msg (Symbol)\n'
                                               'T: Time Delay (ex. T: 0.2)\n'
                                               'Option: Display Option')

    def _update_status(self):
        if t32.status is True:
            self.ui_t32.line_connect_status.setText('Connected')
            self.ui_t32.line_connect_status.setStyleSheet("color:black;font-weight:600;background-color: %s;border: 1px solid transparent;" % "#42f566")
        else:
            self.ui_t32.line_connect_status.setText('Not Connected')
            self.ui_t32.line_connect_status.setStyleSheet("color:white;font-weight:600;background-color: %s;border: 1px solid transparent;" % "rgba(255, 0, 0, 0.70)")
