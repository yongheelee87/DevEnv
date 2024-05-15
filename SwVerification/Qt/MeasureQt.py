import os
import pandas as pd
from sys import modules
from templates import *
from Lib.Common import Configure, open_path, load_csv_list, logging_print, export_csv_list
from measure import MeasRGW
from . _thread import TaskThread
from . _graph import GraphView


class MeasureWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # SET AS IMAGE WIDGETS
        self.ui_meas = Ui_measure()
        self.ui_meas.setupUi(self)
        self.script_path = os.path.join('./data/input/script/Measure', 'removed.csv')

        self.measure = None  # Measure Class 선언 및 설정
        self.measure_th = TaskThread(task_model=self.measure)  # Measure Class 선언 및 설정

        # self.backgroundInit()
        self.connectBtnInit()
        self.connectLineInit()
        self.connectCBoxInit()

        self.graph = GraphView(fig=self.measure.fig, title='Measurement Graph')

    def backgroundInit(self):
        print("N/A")

    def connectBtnInit(self):
        self.ui_meas.btn_script_load.clicked.connect(self.func_btn_script_load)
        self.ui_meas.btn_script_save.clicked.connect(self.func_btn_script_save)
        self.ui_meas.btn_Result_Folder.clicked.connect(self.func_btn_Result_Folder)
        self.ui_meas.btn_Run_Script.clicked.connect(self.func_btn_Run_Script)
        self.ui_meas.btn_show_graph.clicked.connect(self.func_btn_show_graph)

    def connectLineInit(self):
        self.ui_meas.line_sample_rate.textChanged.connect(self.func_line_sample_rate)
        self.ui_meas.line_num_match.textChanged.connect(self.func_line_num_match)

    def connectCBoxInit(self):
        self.ui_meas.cbox_project.clear()
        self.ui_meas.cbox_project.addItems(self._get_target())
        target = Configure.set['system']['project'].strip()
        self.ui_meas.cbox_project.setCurrentText(target)
        self.update_measure_target()
        self.ui_meas.cbox_project.currentIndexChanged.connect(self.update_measure_target)
        self.ui_meas.cbox_time_type.currentIndexChanged.connect(self.func_cbox_time_type)
        self.ui_meas.cbox_judge_type.currentIndexChanged.connect(self.func_cbox_judge_type)
        self.ui_meas.cbox_fill_zero.currentIndexChanged.connect(self.func_cbox_fill_zero)

    def func_btn_script_load(self):
        input_script_file = QFileDialog.getOpenFileName(self, 'Open File', os.path.dirname(self.script_path), 'csv File(*.csv);; All File(*)')[0]
        if 'csv' in input_script_file:
            self.ui_meas.line_script_path.setText(input_script_file)
            self._update_tbl_from_df()
            self.script_path = input_script_file

    # noinspection PyMethodMayBeStatic
    def func_btn_Result_Folder(self):
        open_path('./data/result/')

    # noinspection PyMethodMayBeStatic
    def func_btn_script_save(self):
        input_script_file = QFileDialog.getSaveFileName(self, 'Save File', os.path.dirname(self.script_path), 'csv File(*.csv);; All File(*)')[0]
        if 'csv' in input_script_file:
            self.ui_meas.line_script_path.setText(input_script_file)
            self.script_path = input_script_file
            self._generate_script_file()

    def func_btn_show_graph(self):
        self.measure.step_graph()
        main_geometry = self.frameGeometry()
        self.graph.show_widget(main_geometry)
        self.graph.canvas.draw()

    def func_line_sample_rate(self):
        str_sample_rate = self.ui_meas.line_sample_rate.text().strip()
        if str_sample_rate == '':
            str_sample_rate = '0.1'  # 초기 값
        self.measure.rate = str_sample_rate

    def func_line_num_match(self):
        str_num_match = self.ui_meas.line_num_match.text().strip()
        if str_num_match == '':
            str_num_match = '1'  # 초기 값
        self.measure.n_match = str_num_match

    def func_cbox_time_type(self):
        str_time_type = self.ui_meas.cbox_time_type.currentText().strip()
        if 'Total' in str_time_type:
            self.measure.time_type = 'Total Time'
        else:
            self.measure.time_type = 'Per step'

    def func_cbox_judge_type(self):
        str_judge_type = self.ui_meas.cbox_judge_type.currentText().strip()
        if 'same' in str_judge_type:
            self.measure.judge = 'same'
        else:
            self.measure.judge = 'independent'

    def func_cbox_fill_zero(self):
        str_fill_zero = self.ui_meas.cbox_fill_zero.currentText().strip()
        if 'True' in str_fill_zero:
            self.measure.fill_zero = True
        else:
            self.measure.fill_zero = False

    def func_btn_Run_Script(self):
        script_data = self._convert_data_from_tbl()
        self.measure.df_tc = pd.DataFrame(script_data[1:], columns=script_data[0])
        print("START: MEASUREMENT WITH SCRIPT\n")
        self.measure_th.start()

    def update_measure_target(self):
        self.measure = getattr(modules[__name__], 'Meas' + str(self.ui_meas.cbox_project.currentText().strip()))()  # Measure Class 선언 및 설정
        self.measure_th._task = self.measure

    def _get_target(self):
        return [t.strip().replace('.py', '').replace('meas', '') for t in os.listdir('./measure') if 'meas' in t.strip()]

    def _update_tbl_from_df(self):
        # 테이블 위젯 값 쓰기
        self.ui_meas.tbl_script.clear()
        # Select Dataframe
        lst_df = load_csv_list(file_path=self.ui_meas.line_script_path.text())
        self.ui_meas.cbox_judge_type.setCurrentIndex(1 if 'Total' in lst_df[1][1] else 0)
        self.ui_meas.cbox_judge_type.setCurrentIndex(0 if 'same' in lst_df[2][1] else 1)
        self.ui_meas.line_sample_rate.setText(lst_df[0][1])
        self.ui_meas.line_num_match.setText(lst_df[3][1])
        self.func_line_sample_rate()
        self.func_line_num_match()
        self.func_cbox_time_type()
        self.func_cbox_judge_type()

        df_testEnv = pd.DataFrame(lst_df[6:], columns=lst_df[5])
        logging_print(f"The test script has been loaded successfully\n")
        # Table Contents
        self.ui_meas.tbl_script.setColumnCount(len(df_testEnv.columns))
        self.ui_meas.tbl_script.setHorizontalHeaderLabels(df_testEnv.columns)
        rowCnt = int(len(df_testEnv.index) * 1.5) if len(df_testEnv.index) < 20 else len(df_testEnv.index) + 10
        self.ui_meas.tbl_script.setRowCount(rowCnt)

        for r in range(len(df_testEnv.index)):
            for c in range(len(df_testEnv.columns)):
                self.ui_meas.tbl_script.setItem(r, c, QTableWidgetItem(str(df_testEnv.iloc[r][c])))
        self.ui_meas.tbl_script.resizeColumnsToContents()

    # noinspection PyMethodMayBeStatic
    def _convert_data_from_tbl(self) -> list:
        """
        :return: dataframe table data
        """
        number_of_columns = self.ui_meas.tbl_script.columnCount()

        # df indexing is slow, so use lists
        lst_data = [[str(self.ui_meas.tbl_script.horizontalHeaderItem(i).text()) for i in range(number_of_columns)]]
        for row in range(self.ui_meas.tbl_script.rowCount()):
            lst_temp = []
            for col in range(number_of_columns):
                table_item = self.ui_meas.tbl_script.item(row, col)
                lst_temp.append('' if table_item is None else str(table_item.text()))
            if lst_temp[0] != '':
                lst_data.append(lst_temp)
        return lst_data

    def _generate_script_file(self):
        script_data = self._convert_data_from_tbl()
        empty_str = ['' for _ in range(len(script_data[0]) - 2)]
        header_data = [['Sample Rate', self.measure.rate] + empty_str,
                       ['Time Type', self.measure.time_type] + empty_str,
                       ['Judge Type', self.measure.judge] + empty_str,
                       ['Num of Match', self.measure.n_match] + empty_str,
                       ['' for _ in range(len(script_data[0]))]]
        export_csv_list(file_path=os.path.dirname(self.script_path), filename=os.path.basename(self.script_path).replace(".csv", ""), lists=header_data + script_data)
