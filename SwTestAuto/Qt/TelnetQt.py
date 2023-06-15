from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from Lib.Inst.telnetLib import *

telnet_form = uic.loadUiType("./Qt/static/ui/TelnetQt.ui")[0]


class TelnetView(QWidget, telnet_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.connectBtnInit()
        self.connectLineInit()
        self.connectTextInit()
        self.connectToggleInit()

    def show_widget(self, main_geometry):
        self.move(main_geometry.topRight())
        self.show()
        self.activateWindow()

    def connectBtnInit(self):
        self.btn_Connect.clicked.connect(self.func_btn_Connect)
        self.btn_send.clicked.connect(self.func_btn_send)

    def connectLineInit(self):
        self._update_status()

    def connectTextInit(self):
        self.pText_cmd.textChanged.connect(self.func_pText_cmd)

    def connectToggleInit(self):
        self.btn_servo_on.toggled.connect(self.func_btn_servo_on_toggle)

    def func_btn_Connect(self):
        telnet.connect_dev(self.line_Host.text().strip(), self.line_Port.text().strip())
        self._update_status()

    def func_btn_send(self):
        try:
            lst_cmd_str = self.pText_cmd.toPlainText().split("\n")
            read_msg = ''
            for cmd_str in lst_cmd_str:
                cmd = cmd_str.strip()
                if 'W:' in cmd[:2]:
                    telnet.msg_write(cmd[2:].strip())
                    read_msg += 'Write Msg {}\n'.format(cmd[2:].strip())
                elif 'R:' in cmd[:2]:
                    read_msg += ('Read Msg: ' + str(telnet.query(cmd[2:].strip())))
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

    @pyqtSlot(bool)
    def func_btn_servo_on_toggle(self, state):
        if state:
            self.btn_servo_on.setStyleSheet("background-color: #42f566;border: 1px solid black;border-radius: 5px;")
            self.btn_servo_on.setText("SERVO_ON")
            self._stop_servo()
        else:
            self.btn_servo_on.setStyleSheet(
                "background-color: rgba(255, 0, 0, 0.70);border: 1px solid black;border-radius: 5px;")
            self.btn_servo_on.setText("SERVO_OFF")
            self._run_servo()

    def _update_status(self):
        if telnet.status is True:
            self.line_connect_status.setText('Connected')
            self.line_connect_status.setStyleSheet("background-color: %s;border: 1px solid transparent;" % "#42f566")
        else:
            self.line_connect_status.setText('Not Connected')
            self.line_connect_status.setStyleSheet(
                "background-color: %s;border: 1px solid transparent;" % "rgba(255, 0, 0, 0.70)")

    def _run_servo(self):
        serve_mode = str(self.cbox_servo_mode.currentText())
        telnet.set_servo_mode(serve_mode)

        if telnet.servo_ready is False:
            telnet.enable_servo(True)
            telnet.servo_ready = True

        if telnet.servo_mode == 'RPM':
            telnet.set_servo_speed(int(self.line_servo_value.text().strip()))
        else:
            telnet.set_servo_torque(float(self.line_servo_value.text().strip()))

    def _stop_servo(self):
        if telnet.servo_mode == 'RPM':
            telnet.set_servo_speed(0)
        else:
            telnet.set_servo_torque(0.0)
