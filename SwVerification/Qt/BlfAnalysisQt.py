from templates import *
from sys import modules
from PyQt5.QtCore import QDateTime, QThread, pyqtSlot, QTimer
from App.blf import *


class BlfAnalysisWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # SET AS IMAGE WIDGETS
        self.ui_blf = Ui_blf_analysis()
        self.ui_blf.setupUi(self)

        self.blf = BlfAnalysis()

        self.backgroundInit()
        self.connectBtnInit()

        self.blf_path = ''

    def backgroundInit(self):
        self._update_tbl_from_df()

    def connectBtnInit(self):
        self.ui_blf.btn_blf_load.clicked.connect(self.func_btn_blf_load)
        self.ui_blf.btn_Result_Folder.clicked.connect(self.func_btn_Result_Folder)
        self.ui_blf.btn_Run_Analysis.clicked.connect(self.func_btn_Run_Analysis)

    def func_btn_blf_load(self):
        blf_name = QFileDialog.getOpenFileName(self, 'Open File', './', 'blf File(*.blf);; All File(*)')
        input_blf_file = blf_name[0]
        if input_blf_file:
            self.ui_blf.line_blf_path.setText(input_blf_file)
            self.blf_path = input_blf_file

    def func_btn_Run_Analysis(self):
        self.blf.read_blf(blf_path=self.blf_path, dic_channel=self._extract_channel(), sigs=self._read_signals())
        self.blf.display_graph()

    # noinspection PyMethodMayBeStatic
    def func_btn_Result_Folder(self):
        open_path('./data/result/')

    def _update_tbl_from_df(self):
        # 테이블 위젯 값 쓰기
        self.ui_blf.tbl_ch_device.clear()
        # Select Dataframe
        df_ch_dev = self.blf.get_ch_dev()
        # Table Contents
        self.ui_blf.tbl_ch_device.setColumnCount(len(df_ch_dev.columns))
        self.ui_blf.tbl_ch_device.setHorizontalHeaderLabels(df_ch_dev.columns.tolist())
        self.ui_blf.tbl_ch_device.setRowCount(len(df_ch_dev.index))

        for r in range(len(df_ch_dev.index)):
            for c in range(len(df_ch_dev.columns)):
                self.ui_blf.tbl_ch_device.setItem(r, c, QTableWidgetItem(str(df_ch_dev.iloc[r][c])))
        self.ui_blf.tbl_ch_device.resizeColumnsToContents()

    def _read_signals(self):
        lst_sigs_str = self.ui_blf.pText_signal.toPlainText().split("\n")
        lst_sigs = []
        for sig_str in lst_sigs_str:
            temp = []
            for sig in sig_str.strip().replace("'", '').split(","):
                if sig != '':
                    temp.append(sig.strip())
            lst_sigs.append(temp)
        return lst_sigs

    def _extract_channel(self):
        dict_ch_dev = {}
        for r in range(self.ui_blf.tbl_ch_device.rowCount()):
            if self.ui_blf.tbl_ch_device.item(r, 0).text() != '':
                dict_ch_dev[int(self.ui_blf.tbl_ch_device.item(r, 0).text())] = str(self.ui_blf.tbl_ch_device.item(r, 1).text())
        return dict_ch_dev
