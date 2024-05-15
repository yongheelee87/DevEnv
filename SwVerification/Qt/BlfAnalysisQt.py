import os
import yaml
from templates import *
from sys import modules
from Lib.Common import open_path
from App.blf import BlfAnalysis
from . _graph import GraphView


class BlfAnalysisWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # SET AS IMAGE WIDGETS
        self.ui_blf = Ui_blf_analysis()
        self.ui_blf.setupUi(self)

        self.blf = BlfAnalysis()
        self.graph = GraphView(fig=self.blf.fig, title='BLF Analysis Graph')

        self.backgroundInit()
        self.connectBtnInit()
        self.connectChkInit()

        self.blf_path = os.path.join(os.getcwd(), 'removed.blf')
        self.cfg_path = os.path.join('./data/config/blf', 'removed.yaml')

    def backgroundInit(self):
        self._update_ch_tbl(dict_ch_dev=self.blf.get_ch_dev())

    def connectBtnInit(self):
        self.ui_blf.btn_Result_Folder.clicked.connect(self.func_btn_Result_Folder)
        self.ui_blf.btn_Run_Analysis.clicked.connect(self.func_btn_Run_Analysis)
        self.ui_blf.btn_cfg_save.clicked.connect(self.func_btn_cfg_save)
        self.ui_blf.btn_cfg_load.clicked.connect(self.func_btn_cfg_load)
        self.ui_blf.btn_blf_load.clicked.connect(self.func_btn_blf_load)

    def connectChkInit(self):
        self.ui_blf.chk_show_graph.stateChanged.connect(self.func_chk_show_graph)

    def func_btn_cfg_save(self):
        input_cfg_file = QFileDialog.getSaveFileName(self, 'Save File', os.path.dirname(self.cfg_path), 'cfg File(*.yaml);; All File(*)')[0]
        if input_cfg_file:
            self.ui_blf.line_cfg_path.setText(input_cfg_file)
            cfg = {'CHANNEL': self._extract_channel(), 'SIGNALS': self._read_signals()}
            with open(self.ui_blf.line_cfg_path.text(), 'w', encoding="utf-8-sig") as f:
                yaml.dump(cfg, f, default_flow_style=None)
            self.cfg_path = input_cfg_file

    def func_btn_cfg_load(self):
        input_cfg_file = QFileDialog.getOpenFileName(self, 'Open File', os.path.dirname(self.cfg_path), 'cfg File(*.yaml);; All File(*)')[0]
        if input_cfg_file:
            self.ui_blf.line_cfg_path.setText(input_cfg_file)
            with open(input_cfg_file, encoding="utf-8-sig") as f:
                cfg_yaml = yaml.load(f, Loader=yaml.SafeLoader)
                self._update_ch_tbl(dict_ch_dev=cfg_yaml['CHANNEL'])
                self._update_signal_txt(lst_sigs=cfg_yaml['SIGNALS'])
            self.cfg_path = input_cfg_file

    def func_btn_blf_load(self):
        input_blf_file = QFileDialog.getOpenFileName(self, 'Open File', os.path.dirname(self.blf_path), 'blf File(*.blf);; All File(*)')[0]
        if input_blf_file:
            self.ui_blf.line_blf_path.setText(input_blf_file)
            self.blf_path = input_blf_file

    def func_btn_Run_Analysis(self):
        self.blf.update_param(blf_path=self.blf_path, dic_channel=self._extract_channel(), sigs=self._read_signals(), rate=self._read_rate())
        self.blf.run()
        if self.blf.inter_graph is True:
            main_geometry = self.frameGeometry()
            self.graph.show_widget(main_geometry)
            self.graph.canvas.draw()

    # noinspection PyMethodMayBeStatic
    def func_btn_Result_Folder(self):
        open_path('./data/result/')

    def func_chk_show_graph(self):
        if self.ui_blf.chk_show_graph.isChecked():
            self.blf.inter_graph = True
        else:
            self.blf.inter_graph = False

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

    def _read_rate(self) -> str:
        str_line_Resample_Rate = self.ui_blf.line_Resample_Rate.text().strip()
        if str_line_Resample_Rate == '' or str_line_Resample_Rate == 'Resample Rate':
            str_line_Resample_Rate = '200ms'
        return str_line_Resample_Rate
