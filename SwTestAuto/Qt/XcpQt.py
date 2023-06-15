from PyQt5 import uic
from PyQt5.QtWidgets import *
from Lib.Inst.canLib import *

Xcp_form = uic.loadUiType("./Qt/static/ui/XcpQt.ui")[0]


class XcpView(QWidget, Xcp_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.connectBtnInit()
        self.connectLineInit()
        self.connectTextInit()

        self.xcp_variable = ''
        self.xcp_value = ''

    def __del__(self):
        print(".... XCP QT CLOSE.....\n")

    def connectBtnInit(self):
        self.btn_Connect.clicked.connect(self.func_btn_Connect)
        self.btn_XCP_Read.clicked.connect(self.func_btn_XCP_Read)
        self.btn_XCP_Write.clicked.connect(self.func_btn_XCP_Write)
        self.btn_send.clicked.connect(self.func_btn_send)

    def connectLineInit(self):
        self.line_XCP_Var.textChanged.connect(self.func_line_XCP_Var)
        self.line_XCP_Var.returnPressed.connect(self.func_line_XCP_Var)
        self.line_XCP_Value.textChanged.connect(self.func_line_XCP_Value)
        self.line_XCP_Value.returnPressed.connect(self.func_line_XCP_Value)

    def connectTextInit(self):
        self.pText_cmd.textChanged.connect(self.func_pText_cmd)

    def show_widget(self, main_geometry):
        self.move(main_geometry.topRight())
        self.show()
        self.activateWindow()

    def func_btn_Connect(self):
        canBus.xcp.connect(canBus.can_bus)
        time.sleep(0.01)
        if XcpVar.status is True:
            self.pText_monitor.setPlainText('Success: XCP protocol is operating correctly.')
        else:
            self.pText_monitor.setPlainText('Error: XCP protocol is NOT operating correctly.')
        self._update_status()

    def func_btn_XCP_Read(self):
        val = canBus.xcp_read_symbol(symbol=self.xcp_variable)
        time.sleep(0.01)
        self._update_status()
        if val is None:
            val = 'None'
        self.pText_monitor.setPlainText('Read Msg\nVariable: {}\nvalue: {}'.format(self.xcp_variable, val))

    def func_btn_XCP_Write(self):
        if self.xcp_value == '':
            self.xcp_value = 0
        canBus.xcp.send_msg_write(time_delay=0.05, addr_hex=self.xcp_variable, data=self.xcp_value)
        time.sleep(0.01)
        self._update_status()
        self.pText_monitor.setPlainText('Write Msg\nVariable: {}\nValue: {}'.format(self.xcp_variable, self.xcp_value))

    def func_line_XCP_Var(self):
        str_xcp_variable = self.line_XCP_Var.text()
        self.xcp_variable = str_xcp_variable.replace(' ', '')

    def func_line_XCP_Value(self):
        str_xcp_value = self.line_XCP_Value.text()
        self.xcp_value = str_xcp_value.replace(' ', '')

    def func_btn_send(self):
        try:
            lst_cmd_str = self.pText_cmd.toPlainText().split("\n")
            read_msg = ''
            for cmd_str in lst_cmd_str:
                cmd = cmd_str.strip()
                if 'W:' in cmd[:2]:
                    lst_cmd = cmd[2:].strip().split(",")
                    canBus.xcp.send_msg_write(time_delay=0.05, addr_hex=lst_cmd[0].strip(), data=lst_cmd[1].strip())
                    read_msg += 'Write Msg {}\n'.format(lst_cmd)
                elif 'R:' in cmd[:2]:
                    val = canBus.xcp_read_symbol(symbol=cmd[2:].strip())
                    if val is None:
                        val = 'None'
                    read_msg += ('Read Msg: {}\n'.format(str(val)))
                elif 'T:' in cmd[:2]:
                    time.sleep(float(cmd[2:].strip()))
            time.sleep(0.01)
            self._update_status()
            self.pText_monitor.setPlainText(read_msg)
        except ValueError:
            logging_print('Error: invalid literal in the box\n')

    def func_pText_cmd(self):
        if self.pText_cmd.toPlainText().replace('\n', '') == 'Option':
            self.pText_cmd.setPlainText('W: Write Msg (Symbol, Value)\n'
                                        'R: Read Msg (Symbol)\n'
                                        'T: Time Delay (ex. T: 0.2)\n'
                                        'Option: Display Option')

    def _update_status(self):
        if XcpVar.status is True:
            self.line_connect_status.setText('Connected')
            self.line_connect_status.setStyleSheet("background-color: %s;border: 1px solid transparent;" % "#42f566")
        else:
            self.line_connect_status.setText('Not Connected')
            self.line_connect_status.setStyleSheet(
                "background-color: %s;border: 1px solid transparent;" % "rgba(255, 0, 0, 0.70)")
