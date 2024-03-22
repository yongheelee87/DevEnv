from templates import *
from sys import modules
from App.blf import *
from . _thread import TaskThread


class BlfAnalysisWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # SET AS IMAGE WIDGETS
        self.ui_blf = Ui_blf_analysis()
        self.ui_blf.setupUi(self)

        self.blf = BlfAnalysis()

        self.backgroundInit()
        self.connectBtnInit()

        self.blf_path = './'
        self.cfg_path = './'

        self.blf_th = TaskThread(task_model=self.blf)  # BLF Task Class 선언 및 설정

    def backgroundInit(self):
        self._update_ch_tbl(dict_ch_dev=self.blf.get_ch_dev())

    def connectBtnInit(self):
        self.ui_blf.btn_Result_Folder.clicked.connect(self.func_btn_Result_Folder)
        self.ui_blf.btn_Run_Analysis.clicked.connect(self.func_btn_Run_Analysis)
        self.ui_blf.btn_cfg_save.clicked.connect(self.func_btn_cfg_save)
        self.ui_blf.btn_cfg_load.clicked.connect(self.func_btn_cfg_load)
        self.ui_blf.btn_blf_load.clicked.connect(self.func_btn_blf_load)

    def func_btn_cfg_save(self):
        cfg = {'CHANNEL': self._extract_channel(), 'SIGNALS': self._read_signals()}
        with open(self.ui_blf.line_cfg_path.text(), 'w', encoding="utf-8-sig") as f:
            yaml.dump(cfg, f, default_flow_style=None)

    def func_btn_cfg_load(self):
        cfg_name = QFileDialog.getOpenFileName(self, 'Open File', './data/config/blf', 'cfg File(*.yaml);; All File(*)')
        input_cfg_file = cfg_name[0]
        if input_cfg_file:
            self.ui_blf.line_cfg_path.setText(input_cfg_file)
            self.cfg_path = input_cfg_file
            with open(self.cfg_path, encoding="utf-8-sig") as f:
                cfg_yaml = yaml.load(f, Loader=yaml.SafeLoader)
                self._update_ch_tbl(dict_ch_dev=cfg_yaml['CHANNEL'])
                self._update_signal_txt(lst_sigs=cfg_yaml['SIGNALS'])

    def func_btn_blf_load(self):
        blf_name = QFileDialog.getOpenFileName(self, 'Open File', './', 'blf File(*.blf);; All File(*)')
        input_blf_file = blf_name[0]
        if input_blf_file:
            self.ui_blf.line_blf_path.setText(input_blf_file)
            self.blf_path = input_blf_file

    def func_btn_Run_Analysis(self):
        self.blf.update_param(blf_path=self.blf_path, dic_channel=self._extract_channel(), sigs=self._read_signals())
        self.blf_th.update_model(model=self.blf)
        self.blf_th.start()  # BLF Analysis 실행

    # noinspection PyMethodMayBeStatic
    def func_btn_Result_Folder(self):
        open_path('./data/result/')

    def _update_ch_tbl(self, dict_ch_dev: dict):
        # 테이블 위젯 값 쓰기
        self.ui_blf.tbl_ch_device.clear()
        # Table Contents
        self.ui_blf.tbl_ch_device.setColumnCount(2)
        self.ui_blf.tbl_ch_device.setHorizontalHeaderLabels(['CH', 'DEV'])
        self.ui_blf.tbl_ch_device.setRowCount(len(dict_ch_dev))

        for r, (k, v) in enumerate(dict_ch_dev.items()):
            self.ui_blf.tbl_ch_device.setItem(r, 0, QTableWidgetItem(str(k)))
            self.ui_blf.tbl_ch_device.setItem(r, 1, QTableWidgetItem(str(v)))
        self.ui_blf.tbl_ch_device.resizeColumnsToContents()

    def _update_signal_txt(self, lst_sigs: list):
        # 테이블 위젯 값 쓰기
        self.ui_blf.pText_signal.clear()
        # Text Contents
        self.ui_blf.pText_signal.setPlainText('\n'.join(', '.join(map(str, i)) for i in lst_sigs))

    def _read_signals(self) -> list:
        lst_sigs_str = self.ui_blf.pText_signal.toPlainText().split("\n")
        lst_sigs = []
        for sig_str in lst_sigs_str:
            temp = []
            for sig in sig_str.strip().replace("'", '').split(","):
                if sig != '':
                    temp.append(sig.strip())
            lst_sigs.append(temp)
        return lst_sigs

    def _extract_channel(self) -> dict:
        dict_ch_dev = {}
        for r in range(self.ui_blf.tbl_ch_device.rowCount()):
            if self.ui_blf.tbl_ch_device.item(r, 0).text() != '':
                dict_ch_dev[int(self.ui_blf.tbl_ch_device.item(r, 0).text())] = str(self.ui_blf.tbl_ch_device.item(r, 1).text())
        return dict_ch_dev
