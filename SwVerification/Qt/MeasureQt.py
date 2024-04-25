from templates import *
from sys import modules
from measure import *
from . _thread import TaskThread


class MeasureWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # SET AS IMAGE WIDGETS
        self.ui_meas = Ui_measure()
        self.ui_meas.setupUi(self)

        self.measure = None  # Measure Class 선언 및 설정
        self.measure_th = TaskThread(task_model=self.measure)  # Measure Class 선언 및 설정

        # self.backgroundInit()
        self.connectBtnInit()
        self.connectLineInit()
        self.connectCBoxInit()

        self.measure_watch_dog = QTimer()
        self.measure_watch_dog.setInterval(500)
        self.measure_watch_dog.timeout.connect(self.run_finish)

    def backgroundInit(self):
        print("N/A")

    def connectBtnInit(self):
        self.ui_meas.btn_script_load.clicked.connect(self.func_btn_script_load)
        self.ui_meas.btn_script_save.clicked.connect(self.func_btn_script_save)
        self.ui_meas.btn_Result_Folder.clicked.connect(self.func_btn_Result_Folder)
        self.ui_meas.btn_Run_Script.clicked.connect(self.func_btn_Run_Script)

    def connectLineInit(self):
        self.ui_meas.line_sample_rate.returnPressed.connect(self.func_line_sample_rate)
        self.ui_meas.line_num_match.returnPressed.connect(self.func_line_num_match)

    def connectCBoxInit(self):
        self.ui_meas.cbox_project.clear()
        self.ui_meas.cbox_project.addItems(self._get_target())
        target = Configure.set['system']['project'].strip()
        self.ui_meas.cbox_project.setCurrentText(target)
        self.update_measure_target()
        self.ui_meas.cbox_project.currentIndexChanged.connect(self.update_measure_target)
        self.ui_meas.cbox_judge_type.currentIndexChanged.connect(self.func_cbox_judge_type)
        self.ui_meas.cbox_fill_zero.currentIndexChanged.connect(self.func_cbox_fill_zero)

    def run_finish(self):
        if self.measure_th.isFinished() is True:
            self.measure_watch_dog.stop()

    def func_btn_script_load(self):
        input_script_file = QFileDialog.getOpenFileName(self, 'Open File', './data/input/script/Measure', 'csv File(*.csv);; All File(*)')[0]
        if input_script_file:
            self.ui_meas.line_script_path.setText(input_script_file)
            self._update_tbl_from_df()

    # noinspection PyMethodMayBeStatic
    def func_btn_Result_Folder(self):
        open_path('./data/result/')

    # noinspection PyMethodMayBeStatic
    def func_btn_script_save(self):
        print("TEST")

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
        self.measure.df_tc = self._convert_df_from_tbl()
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
        judge_type = 'same time' if 'same' in lst_df[1][1] else 'independent'
        self.ui_meas.cbox_judge_type.setCurrentText(judge_type)
        self.ui_meas.line_sample_rate.setText(lst_df[0][1])
        self.ui_meas.line_num_match.setText(lst_df[2][1])
        self.func_line_sample_rate()
        self.func_line_num_match()
        self.func_cbox_judge_type()

        df_testEnv = pd.DataFrame(lst_df[5:], columns=lst_df[4])
        logging_print(f"The test script has been loaded successfully\n")
        # Table Contents
        self.ui_meas.tbl_script.setColumnCount(len(df_testEnv.columns))
        self.ui_meas.tbl_script.setHorizontalHeaderLabels(df_testEnv.columns.tolist())
        rowCnt = int(len(df_testEnv.index) * 1.5) if len(df_testEnv.index) < 20 else len(df_testEnv.index) + 10
        self.ui_meas.tbl_script.setRowCount(rowCnt)

        for r in range(len(df_testEnv.index)):
            for c in range(len(df_testEnv.columns)):
                self.ui_meas.tbl_script.setItem(r, c, QTableWidgetItem(str(df_testEnv.iloc[r][c])))
        self.ui_meas.tbl_script.resizeColumnsToContents()

    # noinspection PyMethodMayBeStatic
    def _convert_df_from_tbl(self) -> pd.DataFrame:
        '''
        :return: dataframe table data
        '''
        number_of_rows = self.ui_meas.tbl_script.rowCount()
        number_of_columns = self.ui_meas.tbl_script.columnCount()

        # df indexing is slow, so use lists
        lst_data = []
        for row in range(number_of_rows):
            lst_temp = []
            for col in range(number_of_columns):
                table_item = self.ui_meas.tbl_script.item(row, col)
                lst_temp.append('' if table_item is None else str(table_item.text()))
            if lst_temp[0] != '':
                lst_data.append(lst_temp)
        return pd.DataFrame(lst_data, columns=[str(self.ui_meas.tbl_script.horizontalHeaderItem(i).text()) for i in range(number_of_columns)])
