from sys import modules
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QDateTime, QThread, pyqtSlot, QTimer

from measure.measureOPU import MeasureOPU

from Lib.Common.basicFunction import *

measure_form = uic.loadUiType("./Qt/static/ui/MeasureQt.ui")[0]


class MeasureView(QWidget, measure_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.datetime = QDateTime.currentDateTime()
        self.df_testEnv = None  # script에 적힌 시험 환경

        self.backgroundInit()
        self.connectBtnInit()
        self.connectToggleInit()
        self.connectCBoxInit()

        self.measure = getattr(modules[__name__],
                               str(self.cbox_project.currentText().strip()))()  # Measure Class 선언 및 설정
        self.measure_thread = MeasureThread(self.measure)

        self.measure_watch_dog = QTimer()
        self.measure_watch_dog.setInterval(500)
        self.measure_watch_dog.timeout.connect(self.run_finish)

        # self.measure_thread.finished.connect(self.run_finish)

    def __del__(self):
        print(".... MEASURE QT CLOSE.....\n")

    def backgroundInit(self):
        self.load_measure_target()

    def show_widget(self, main_geometry):
        self.move(main_geometry.topRight())
        self.show()
        self.activateWindow()

    def connectBtnInit(self):
        self.btn_script_load.clicked.connect(self.func_btn_script_load)
        self.btn_script_update.clicked.connect(self.func_btn_script_update)
        self.btn_Result_Folder.clicked.connect(self.func_btn_Result_Folder)

    def connectToggleInit(self):
        self.btn_Run_Script.toggled.connect(self.func_btn_Run_Script_toggle)

    def connectCBoxInit(self):
        self.cbox_project.currentIndexChanged.connect(self.update_measure_target)

    def run_finish(self):
        if self.measure.is_stop_btn is True or self.measure_thread.isFinished() is True:
            self.btn_Run_Script.click()
            self.measure_watch_dog.stop()

    def func_btn_script_load(self):
        script_name = QFileDialog.getOpenFileName(self, 'Open File', './data/input/script/cmd',
                                                  'csv File(*.csv);; All File(*)',
                                                  options=QFileDialog.DontUseNativeDialog)
        input_script_file = script_name[0]
        if input_script_file:
            self.line_script_path.setText(input_script_file)
            self._update_tbl_from_df()

    # noinspection PyMethodMayBeStatic
    def func_btn_Result_Folder(self):
        open_path('./data/result/')

    # noinspection PyMethodMayBeStatic
    def func_btn_script_update(self):
        self.df_testEnv = self._convert_df_from_tbl(self.tbl_script)
        logging_print("Current Test Environment\n{}\n".format(self.df_testEnv))

    def _update_tbl_from_df(self):
        # 테이블 위젯 값 쓰기
        self.tbl_script.clear()
        # Select Dataframe
        self.df_testEnv = pd.read_csv(self.line_script_path.text(), dtype=object, encoding='cp1252')
        logging_print("Current Test Environment\n{}\n".format(self.df_testEnv))
        # Table Contents
        self.tbl_script.setColumnCount(len(self.df_testEnv.columns))
        self.tbl_script.setHorizontalHeaderLabels(self.df_testEnv.columns.tolist())
        rowCnt = int(len(self.df_testEnv.index) * 1.5) if len(self.df_testEnv.index) < 20 else len(
            self.df_testEnv.index) + 10
        self.tbl_script.setRowCount(rowCnt)

        for r in range(len(self.df_testEnv.index)):
            for c in range(len(self.df_testEnv.columns)):
                self.tbl_script.setItem(r, c, QTableWidgetItem(str(self.df_testEnv.iloc[r][c])))
        self.tbl_script.resizeColumnsToContents()

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
            self.btn_Run_Script.setStyleSheet("background-color: #42f566;border: 1px solid black;")
            self.btn_Run_Script.setText("RUN SCRIPT")
            print("STOP: MEASUREMENT WITH SCRIPT\n")
            if not self.measure_thread.isFinished():
                self.measure_thread.stop()
        else:
            self.btn_Run_Script.setStyleSheet("background-color: rgba(255, 0, 0, 0.70);border: 1px solid black;")
            self.btn_Run_Script.setText("STOP SCRIPT")
            self.measure.load_script(self.df_testEnv)
            print("START: MEASUREMENT WITH SCRIPT\n")
            self.measure_thread.start()
            self.measure_watch_dog.start()

    def load_measure_target(self):
        self.cbox_project.clear()
        lst_target = ['   ' + tar for tar in Configure.set['system']['measure'].split(', ')]
        self.cbox_project.addItems(lst_target)

    def update_measure_target(self):
        self.measure = getattr(modules[__name__],
                               str(self.cbox_project.currentText().strip()))()  # Measure Class 선언 및 설정
        self.measure_thread.meas_model = self.measure


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
