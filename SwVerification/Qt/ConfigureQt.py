from templates import *
from Lib.Common import Configure, logging_print
from Lib.Inst import canBus, t32


class ConfigureWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # SET AS IMAGE WIDGETS
        self.ui_config = Ui_configure()
        self.ui_config.setupUi(self)

        self.backgroundInit()
        self.connectBtnInit()
        self.connectLineInit()

    def backgroundInit(self):
        self._update_config()

    def connectBtnInit(self):
        self.ui_config.btn_apply.clicked.connect(self.func_btn_apply)
        self.ui_config.btn_config_load.clicked.connect(self.func_btn_config_load)

    def connectLineInit(self):
        self.ui_config.line_config_path.setText(Configure.path)

    def func_btn_config_load(self):
        config_name = QFileDialog.getOpenFileName(self, 'Open File', './data/config', 'ini File(*.ini);; All File(*)')
        input_config_file = config_name[0]
        if input_config_file:
            Configure.path = input_config_file  # update configuration path
            Configure.update()  # update configuration set
            self.ui_config.line_config_path.setText(input_config_file)
            self._update_config()
            logging_print('[INFO] The configuration is loaded. \n')

    def func_btn_apply(self):
        configure_str = self.ui_config.pText_configuration.toPlainText()
        with open(Configure.path, 'w', encoding='utf-8') as f:
            f.write(configure_str)

        Configure.update()  # update configuration set
        logging_print('[INFO] The configuration is being applied to all equipment. It may take some time.\n')

        # Initialization of All devices
        canBus.__init__(config_sys=Configure.set)
        t32.__init__(config_sys=Configure.set)
        # visa.__init__(config_sys=Configure.set)

    def _update_config(self):
        with open(Configure.path, 'r', encoding='utf-8') as f:
            f_lines = f.readlines()
            configuration = "".join(f_lines)
        self.ui_config.pText_configuration.setPlainText(configuration)
