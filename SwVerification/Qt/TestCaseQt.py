import os
import re
import yaml
from templates import *
from Lib.Common import Configure, logging_print, open_path
from Lib.TestProcess import AutoTest
from . _thread import TaskThread


class TestCaseWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # SET AS IMAGE WIDGETS
        self.ui_tc = Ui_testcase()
        self.ui_tc.setupUi(self)
        self.project = Configure.set['system']['project'].strip()

        self.swTest = AutoTest(test_yaml='./data/config/test_map.yaml')
        self.connectBtnInit()

        self.testcase_num_str = []
        self.dic_test_mode = {}
        self.single_mode = False
        self.connectCBoxInit()  # dic_test_mode가 먼저 선언 필요

        self._update_map_script()
        self._update_map_mode()

        self.test_th = TaskThread(task_model=self.swTest)  # Test Class 선언 및 설정

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
        self.single_mode = True if self.project != Configure.set['system']['project'].strip() else False
        self._update_map_script()
        self._update_map_mode()

    def func_btn_apply(self):
        configure_str = self.ui_tc.pText_map_test.toPlainText()
        if self.single_mode is True:
            with open(f'./data/input/script/{self.project}/set/map_script_sw_test.yaml', 'w', encoding='utf-8') as f:
                f.write(configure_str)
        logging_print('[INFO] The map script is modified as seen in the display\n')

    def func_btn_Script_Folder(self):
        if self.single_mode is True:
            open_path(f'./data/input/script/{self.project}')
        else:
            open_path('./data/config')

    # noinspection PyMethodMayBeStatic
    def func_btn_Result_Folder(self):
        open_path('./data/result/')

    # noinspection PyMethodMayBeStatic
    def func_btn_Project_CSV(self):
        open_path('Deleted Function')

    def func_btn_Map_Mode(self):
        if self.single_mode is True:
            open_path(os.path.join('data', 'input', 'script', self.project, 'set', 'map_test_mode.yaml'))

    def func_btn_testcase(self):
        if self.single_mode is True:
            self._update_testcase()  # Line에 기입된 Case Number 정렬하기
            if self.testcase_num_str:
                self.swTest.update_test_case(pjt=self.project, test_num=self.testcase_num_str)
                self.test_th.start()
        else:
            self.swTest.test_map = yaml.load(self.ui_tc.pText_map_test.toPlainText(), Loader=yaml.SafeLoader)
            self.test_th.start()

    def func_btn_testmode(self):
        self._update_map_mode()
        test_mode = str(self.ui_tc.cbox_Test_mode.currentText().strip())
        test_cases = self.dic_test_mode[test_mode]
        self.test_th.start()

    def _get_project(self):
        project_lst = os.listdir('./data/input/script')
        project_lst.remove('Measure')
        project_lst.append(self.project)  # 전체 기능 실행
        return project_lst

    def _update_testcase(self):
        line_testcase_num_str = re.sub(r'[^0-9,~]', '', self.ui_tc.line_testcase_num.text().strip())
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
        if self.single_mode is True:
            self.swTest.script_path = os.path.join('data', 'input', 'script', self.project)
            path = f'{self.swTest.script_path}/set/map_script_sw_test.yaml'
        else:
            path = self.swTest.yaml_path

        with open(path, 'r', encoding='utf-8') as f:
            f_lines = f.readlines()
            map_test = "".join(f_lines)
        self.ui_tc.pText_map_test.setPlainText(map_test)

    def _update_map_mode(self):
        self.ui_tc.cbox_Test_mode.clear()
        self.dic_test_mode = self.swTest.update_map_mode(self.project)
        self.ui_tc.cbox_Test_mode.addItems(list(self.dic_test_mode.keys()))
