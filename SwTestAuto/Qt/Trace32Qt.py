import time
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog
from Lib.Inst.Trace32Lib import *

Trace32_form = uic.loadUiType("./Qt/static/ui/Trace32Qt.ui")[0]


class Trace32View(QWidget, Trace32_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.backgroundInit()
        self.connectBtnInit()
        self.connectLineInit()
        self.connectTextInit()

    def __del__(self):
        print(".... TRACE32 QT CLOSE.....\n")

    def backgroundInit(self):
        t32.check_status()

    def connectBtnInit(self):
        self.btn_T32_Open.clicked.connect(self.func_btn_T32_Open)
        self.btn_Connect.clicked.connect(self.func_btn_Connect)
        self.btn_cmm_load.clicked.connect(self.func_btn_cmm_load)

        self.btn_T32_Go.clicked.connect(self.btn_T32_GO_button)
        self.btn_T32_Break.clicked.connect(self.btn_T32_Break_button)
        self.btn_T32_Exit.clicked.connect(self.btn_T32_Exit_button)
        self.btn_T32_RESET.clicked.connect(self.btn_T32_RESET_button)
        self.btn_T32_RESET_GO.clicked.connect(self.btn_T32_RESET_GO_button)
        self.btn_T32_Attach.clicked.connect(self.btn_T32_Attach_button)
        self.btn_T32_NoDebug.clicked.connect(self.btn_T32_NoDebug_button)
        self.btn_send.clicked.connect(self.func_btn_send)

    def connectLineInit(self):
        self._update_status()

    def connectTextInit(self):
        self.pText_cmd.textChanged.connect(self.func_pText_cmd)

    def show_widget(self, main_geometry):
        self.move(main_geometry.topRight())
        self.show()
        self.activateWindow()

    # noinspection PyMethodMayBeStatic
    def func_btn_T32_Open(self):
        t32.open_exe(Configure.set['TRACE32']['api_path'])

    # noinspection PyMethodMayBeStatic
    def func_btn_Connect(self):
        t32.connect_dev()
        self._update_status()

    def func_btn_cmm_load(self):
        cmm_name = QFileDialog.getOpenFileName(self, 'Open File', './data/input/script',
                                               'cmm File(*.cmm);; All File(*)', options=QFileDialog.DontUseNativeDialog)
        input_dbc_file = cmm_name[0]
        if input_dbc_file:
            self.line_cmm_path.setText(input_dbc_file)
            t32.cmd("CD.DO " + input_dbc_file)

    # noinspection PyMethodMayBeStatic
    def btn_T32_GO_button(self):
        t32.cmd('Go')

    # noinspection PyMethodMayBeStatic
    def btn_T32_Break_button(self):
        t32.cmd('Break')

    # noinspection PyMethodMayBeStatic
    def btn_T32_Exit_button(self):
        print("Nothing")

    # noinspection PyMethodMayBeStatic
    def btn_T32_RESET_button(self):
        t32.cmd('System.ResetTarget')

    # noinspection PyMethodMayBeStatic
    def btn_T32_RESET_GO_button(self):
        t32.reset_go()

    # noinspection PyMethodMayBeStatic
    def btn_T32_Attach_button(self):
        t32.cmd('SYStem.Mode.Attach')

    # noinspection PyMethodMayBeStatic
    def btn_T32_NoDebug_button(self):
        t32.cmd('SYStem.Mode.NoDebug')

    def func_btn_send(self):
        try:
            lst_cmd_str = self.pText_cmd.toPlainText().split("\n")
            read_msg = ''
            for cmd_str in lst_cmd_str:
                cmd = cmd_str.strip()
                if 'W:' in cmd[:2]:
                    lst_cmd = cmd[2:].strip().split(",")
                    str_value = lst_cmd[1].strip()
                    value = float(str_value) if '.' in str_value else int(str_value)
                    t32.write_symbol(symbol=lst_cmd[0].strip(), value=value)
                    read_msg += 'Write Msg {}\n'.format(lst_cmd)
                elif 'R:' in cmd[:2]:
                    val = t32.read_symbol(symbol=cmd[2:].strip())
                    if val is None:
                        val = 'None'
                    read_msg += ('Read Msg: {}\n'.format(str(val)))
                elif 'T:' in cmd[:2]:
                    time.sleep(float(cmd[2:].strip()))
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
        if t32.status is True:
            self.line_connect_status.setText('Connected')
            self.line_connect_status.setStyleSheet("background-color: %s;border: 1px solid transparent;" % "#42f566")
        else:
            self.line_connect_status.setText('Not Connected')
            self.line_connect_status.setStyleSheet(
                "background-color: %s;border: 1px solid transparent;" % "rgba(255, 0, 0, 0.70)")
