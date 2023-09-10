from templates import *
import re
from PyQt5.QtCore import QThread
from Lib.DataProcess.TestCaseProcess import *
from Lib.Inst.canLib import *


class TestCaseWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # SET AS IMAGE WIDGETS
        self.ui_tc = Ui_testcase()
        self.ui_tc.setupUi(self)
        self.project = Configure.set['system']['project'].strip()

        self.swTest = TestProcess(self.project)
        self.connectBtnInit()

        self.testcase_num_str = []
        self.dic_test_mode = dict()

        self.connectCBoxInit()  # dic_test_mode가 먼저 선언 필요

        self._update_map_script()
        self._update_map_mode()

        self.test_th = TestThread(self.swTest)  # Test Class 선언 및 설정

        # self.test_watch_dog = QTimer()
        # self.test_watch_dog.setInterval(50)
        # self.test_watch_dog.timeout.connect(self.run_finish)

    def connectBtnInit(self):
        self.ui_tc.btn_testcase.clicked.connect(self.func_btn_testcase)
        self.ui_tc.btn_testmode.clicked.connect(self.func_btn_testmode)

        self.ui_tc.btn_Script_Folder.clicked.connect(self.func_btn_Script_Folder)
        self.ui_tc.btn_Result_Folder.clicked.connect(self.func_btn_Result_Folder)
        self.ui_tc.btn_Map_Mode.clicked.connect(self.func_btn_Map_Mode)
        self.ui_tc.btn_Project_CSV.clicked.connect(self.func_btn_Project_CSV)
        self.ui_tc.btn_apply.clicked.connect(self.func_btn_apply)

    def connectCBoxInit(self):
        self.ui_tc.cbox_project.clear()
        self.ui_tc.cbox_project.addItems(self._get_project())
        self.ui_tc.cbox_project.setCurrentText(self.project)
        self.ui_tc.cbox_project.currentIndexChanged.connect(self.func_cbox_project)

    def func_cbox_project(self):
        self.project = self.ui_tc.cbox_project.currentText().strip()
        self._update_map_script()
        self._update_map_mode()
        self.test_th.test_model = self.swTest

    def func_btn_apply(self):
        configure_str = self.ui_tc.pText_map_test.toPlainText()
        with open('./data/input/script/{}/set/map_script_sw_test.yaml'.format(self.project), 'w', encoding='utf-8') as f:
            f.write(configure_str)

        logging_print('[INFO] The map script is modified as seen in the display\n')

    def func_btn_Script_Folder(self):
        open_path('./data/input/script/{}'.format(self.project))

    # noinspection PyMethodMayBeStatic
    def func_btn_Result_Folder(self):
        open_path('./data/result/')

    # noinspection PyMethodMayBeStatic
    def func_btn_Project_CSV(self):
        open_path('./data/result/Total_TESTCASE.csv')

    def func_btn_Map_Mode(self):
        open_path(self.swTest.map_mode_path)

    def func_btn_testcase(self):
        self._update_testcase()  # Line에 기입된 Case Number 정렬하기
        if self.testcase_num_str:
            self.test_th.tc_num = self.testcase_num_str
            self.test_th.start()

    def func_btn_testmode(self):
        self._update_map_mode()
        test_mode = str(self.ui_tc.cbox_Test_mode.currentText().strip())
        test_cases = self.dic_test_mode[test_mode]
        self.test_th.tc_num = list(map(str, test_cases))
        self.test_th.start()

    def _get_project(self):
        project_lst = os.listdir('./data/input/script')
        project_lst.remove('cmd')
        return project_lst

    def _update_testcase(self):
        line_testcase_num_str = re.sub(r'[^0-9,~]', '', self.ui_tc.line_testcase_num.text().replace(' ', ''))
        testcase_lst = []
        for num_str in line_testcase_num_str.split(','):
            if '~' in num_str:
                temp = num_str.split('~')
                if temp[1] != '':
                    for i in range(int(temp[0]), int(temp[1]) + 1):
                        testcase_lst.append(str(i))
                else:
                    testcase_lst.append(temp[0])
            else:
                testcase_lst.append(num_str)

        self.testcase_num_str = []
        # 중복 및 Null 제거
        for v in testcase_lst:
            if v not in self.testcase_num_str and v != '':
                self.testcase_num_str.append(v)

    def _update_map_script(self):
        self.swTest.script_path = os.path.join(self.swTest.main_path, 'data', 'input', 'script', self.project)
        self.swTest.map_script_path = '{}/set/map_script_sw_test.yaml'.format(self.swTest.script_path)
        with open(self.swTest.map_script_path, 'r', encoding='utf-8') as f:
            f_lines = f.readlines()
            map_test = "".join(f_lines)
        self.ui_tc.pText_map_test.setPlainText(map_test)

    def _update_map_mode(self):
        self.ui_tc.cbox_Test_mode.clear()
        self.swTest.map_mode_path = '{}/set/map_test_mode.yaml'.format(self.swTest.script_path)
        self.dic_test_mode = self.swTest.update_map_mode()
        self.ui_tc.cbox_Test_mode.addItems(list(self.dic_test_mode.keys()))


class TestThread(QThread):
    """ MeasurementProcessThread(parent:QThread) """

    def __init__(self, test_model):
        super().__init__()
        self.test_model = test_model
        self.tc_num = None

    def run(self):
        self.test_model.start(self.tc_num)

    def stop(self):
        self.test_model.stop()
        self.terminate()
        self.wait(2)
