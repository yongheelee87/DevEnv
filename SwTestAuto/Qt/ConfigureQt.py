from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog
from Lib.Inst.canLib import *
from Lib.Inst.telnetLib import *
from Lib.Inst.Trace32Lib import *
from Lib.Inst.visaLib import *
from Lib.Common.basicFunction import *

configure_form = uic.loadUiType("./Qt/static/ui/ConfigureQt.ui")[0]


class ConfigureView(QWidget, configure_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.connectBtnInit()
        self.connectLineInit()
        self._update_config()

    def show_widget(self, main_geometry):
        self.move(main_geometry.topRight())
        self.show()
        self.activateWindow()

    def connectBtnInit(self):
        self.btn_apply.clicked.connect(self.func_btn_apply)
        self.btn_config_load.clicked.connect(self.func_btn_config_load)

    def connectLineInit(self):
        self.line_config_path.setText(Configure.path)

    def func_btn_config_load(self):
        config_name = QFileDialog.getOpenFileName(self, 'Open File', './data/config', 'ini File(*.ini);; All File(*)',
                                                  options=QFileDialog.DontUseNativeDialog)
        input_config_file = config_name[0]
        if input_config_file:
            Configure.path = input_config_file
            self.line_config_path.setText(input_config_file)
            self._update_config()

    def func_btn_apply(self):
        configure_str = self.pText_configuration.toPlainText()
        with open(Configure.path, 'w', encoding='utf-8') as f:
            f.write(configure_str)

        Configure.set = configparser.ConfigParser()
        Configure.set.read(Configure.path, encoding='utf-8')

        logging_print('[INFO] The configuration is being applied to all equipment. It may take some time.\n')

        # Initialization of All devices
        canBus.__init__(config_sys=Configure.set)
        telnet.__init__(config_sys=Configure.set)
        t32.__init__(config_sys=Configure.set)
        visa.__init__(config_sys=Configure.set)

    def _update_config(self):
        with open(Configure.path, 'r', encoding='utf-8') as f:
            f_lines = f.readlines()
            configuration = "".join(f_lines)
        self.pText_configuration.setPlainText(configuration)
