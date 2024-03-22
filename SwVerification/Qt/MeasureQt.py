from templates import *
from sys import modules
from PyQt5.QtCore import pyqtSlot

from measure import *


class MeasureWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # SET AS IMAGE WIDGETS
        self.ui_meas = Ui_measure()
        self.ui_meas.setupUi(self)

        self.datetime = QDateTime.currentDateTime()
        self.df_testEnv = None  # script에 적힌 시험 환경

        self.measure = None  # Measure Class 선언 및 설정
        self.measure_thread = MeasureThread(self.measure)

        # self.backgroundInit()
        self.connectBtnInit()
        self.connectToggleInit()
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

    def connectToggleInit(self):
        self.ui_meas.btn_Run_Script.toggled.connect(self.func_btn_Run_Script_toggle)

    def connectCBoxInit(self):
        self.ui_meas.cbox_project.clear()
        self.ui_meas.cbox_project.addItems(self._get_target())
        target = Configure.set['system']['project'].strip()
        self.ui_meas.cbox_project.setCurrentText(target)
        self.update_measure_target()
        self.ui_meas.cbox_project.currentIndexChanged.connect(self.update_measure_target)

    def run_finish(self):
        if self.measure.is_stop_btn is True or self.measure_thread.isFinished() is True:
            self.ui_meas.btn_Run_Script.click()
            self.measure_watch_dog.stop()

    def func_btn_script_load(self):
        script_name = QFileDialog.getOpenFileName(self, 'Open File', './data/input/script/cmd', 'csv File(*.csv);; All File(*)')
        input_script_file = script_name[0]
        if input_script_file:
            self.ui_meas.line_script_path.setText(input_script_file)
            self._update_tbl_from_df()

    # noinspection PyMethodMayBeStatic
    def func_btn_Result_Folder(self):
        open_path('./data/result/')

    # noinspection PyMethodMayBeStatic
    def func_btn_script_save(self):
        print("TEST")

    def _update_tbl_from_df(self):
        # 테이블 위젯 값 쓰기
        self.ui_meas.tbl_script.clear()
        # Select Dataframe
        self.df_testEnv = pd.read_csv(self.ui_meas.line_script_path.text(), dtype=object, encoding='cp1252')
        logging_print(f"Current Test Environment\n{self.df_testEnv}\n")
        # Table Contents
        self.ui_meas.tbl_script.setColumnCount(len(self.df_testEnv.columns))
        self.ui_meas.tbl_script.setHorizontalHeaderLabels(self.df_testEnv.columns.tolist())
        rowCnt = int(len(self.df_testEnv.index) * 1.5) if len(self.df_testEnv.index) < 20 else len(
            self.df_testEnv.index) + 10
        self.ui_meas.tbl_script.setRowCount(rowCnt)

        for r in range(len(self.df_testEnv.index)):
            for c in range(len(self.df_testEnv.columns)):
                self.ui_meas.tbl_script.setItem(r, c, QTableWidgetItem(str(self.df_testEnv.iloc[r][c])))
        self.ui_meas.tbl_script.resizeColumnsToContents()

    # noinspection PyMethodMayBeStatic
    def _convert_df_from_tbl(self, table):
        '''
        :param table: data in the QtableWidget defined in the ui
        :return: dataframe table data
        '''
        number_of_rows = table.rowCount()
        number_of_columns = table.columnCount()

        # df indexing is slow, so use lists
        lst_data = []
        for row in range(number_of_rows):
            lst_temp = []
            for col in range(number_of_columns):
                table_item = table.item(row, col)
                lst_temp.append('' if table_item is None else str(table_item.text()))
            lst_data.append(lst_temp)
        print(lst_data)
        # TODO
        # 데이터 'nan' to 0으로 변환
        return pd.DataFrame(lst_data, columns=[str(table.horizontalHeaderItem(i).text()) for i in range(number_of_columns)])

    @pyqtSlot(bool)
    def func_btn_Run_Script_toggle(self, state):
        '''
        :param state: True = thread.stop, False = thread.start
        '''
        if state is True:
            self.ui_meas.btn_Run_Script.setStyleSheet("font-weight:500;color:black;background-color: #c8f7c8;border: 1px solid black;")
            self.ui_meas.btn_Run_Script.setText("RUN SCRIPT")
            print("STOP: MEASUREMENT WITH SCRIPT\n")
            if not self.measure_thread.isFinished():
                self.measure_thread.stop()
        else:
            self.ui_meas.btn_Run_Script.setStyleSheet("font-weight:500;color:black;background-color: rgba(255, 0, 0, 0.70);border: 1px solid black;")
            self.ui_meas.btn_Run_Script.setText("STOP SCRIPT")
            self.measure.load_script(self.df_testEnv)
            print("START: MEASUREMENT WITH SCRIPT\n")
            self.measure_thread.start()
            self.measure_watch_dog.start()

    def update_measure_target(self):
        self.measure = getattr(modules[__name__], 'Meas' + str(self.ui_meas.cbox_project.currentText().strip()))()  # Measure Class 선언 및 설정
        self.measure_thread.meas_model = self.measure

    def _get_target(self):
        return [t.strip().replace('.py', '').replace('meas', '') for t in os.listdir('./measure') if 'meas' in t.strip()]


class MeasureThread(QThread):
    """ MeasurementProcessThread(parent:QThread) """

    def __init__(self, meas_model):
        super().__init__()
        self.meas_model = meas_model

    def run(self):
        self.meas_model.start()

    def stop(self):
        self.meas_model.stop()
        self.terminate()
        self.wait(100)

