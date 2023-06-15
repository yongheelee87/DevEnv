import time
from functools import partial
from PyQt5 import uic
from PyQt5.QtWidgets import *
from Lib.Inst.visaLib import *
from Lib.Common.basicFunction import *

visa_widget = uic.loadUiType("./Qt/static/ui/VisaWidget.ui")[0]


class VisaWidget(QWidget, visa_widget):
    def __init__(self, dev):
        super().__init__()
        self.setupUi(self)
        self.dev = dev
        self.connectBtnInit()
        self.connectLineInit()
        self.connectTextInit()

    def connectBtnInit(self):
        self.btn_Connect.clicked.connect(partial(self.func_btn_Connect, self.dev))
        self.btn_send.clicked.connect(partial(self.func_btn_send, self.dev))

    def connectLineInit(self):
        self.label_name.setText(self.dev)
        self.line_ID.setText(Configure.set[self.dev]['ID'])
        self._update_status()

    def connectTextInit(self):
        self.pText_cmd.textChanged.connect(self.func_pText_cmd)

    def func_btn_Connect(self, dev):
        visa.connect_dev(dev)
        self._update_status()

    def func_btn_send(self, dev):
        try:
            lst_cmd_str = self.pText_cmd.toPlainText().split("\n")
            read_msg = ''
            for cmd_str in lst_cmd_str:
                cmd = cmd_str.strip()
                if 'W:' in cmd[:2]:
                    visa.write(dev, cmd[2:].strip())
                    read_msg += 'Write Msg {}\n'.format(cmd[2:].strip())
                elif 'R:' in cmd[:2]:
                    read_msg += ('Read Msg: {}\n'.format(str(visa.read(dev, cmd[2:].strip()))))
                elif 'T:' in cmd[:2]:
                    time.sleep(float(cmd[2:].strip()))
            self.pText_monitor.setPlainText(read_msg)
        except ValueError:
            logging_print('Error: invalid literal in the box\n')

    def func_pText_cmd(self):
        if self.pText_cmd.toPlainText().replace('\n', '') == 'Option':
            self.pText_cmd.setPlainText('W: Write Command\n'
                                        'R: Read Command\n'
                                        'T: Time Delay (ex. T: 0.2)\n'
                                        'Option: Display Option')

    def _update_status(self):
        if visa.status[self.dev] is True:
            self.line_connect_status.setText('Connected')
            self.line_connect_status.setStyleSheet("background-color: %s;border: 1px solid transparent;" % "#42f566")
        else:
            self.line_connect_status.setText('Not Connected')
            self.line_connect_status.setStyleSheet(
                "background-color: %s;border: 1px solid transparent;" % "rgba(255, 0, 0, 0.70)")
