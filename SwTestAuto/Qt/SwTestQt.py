import re
from PyQt5 import uic
from PyQt5.QtWidgets import *
from Lib.DataProcess.TestCaseProcess import *
from Lib.Inst.canLib import *

swtest_form = uic.loadUiType("./Qt/static/ui/SwTestQt.ui")[0]


class SwTestView(QWidget, swtest_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.project = Configure.set['system']['project']

        self.swTest = TestProcess(self.project)
        self.connectBtnInit()
        self.connectLineInit()

        self.testcase_num_str = []
        self.testcase_num_range_str = []
        self.dic_test_mode = dict()

        self.connectCBoxInit()  # dic_test_mode가 먼저 선언 필요

        self._update_map_script()
        self._update_map_mode()
        self._update_status(False)

    def connectBtnInit(self):
        self.btn_TESTCASE_Start.clicked.connect(self.func_btn_TESTCASE_Start)
        self.btn_TESTCASE_Start_range.clicked.connect(self.func_btn_TESTCASE_Start_range)
        self.btn_TESTMode_Start.clicked.connect(self.func_btn_TESTMode_Start)

        self.btn_Script_Folder.clicked.connect(self.func_btn_Script_Folder)
        self.btn_Result_Folder.clicked.connect(self.func_btn_Result_Folder)
        self.btn_Map_Mode.clicked.connect(self.func_btn_Map_Mode)
        self.btn_Project_CSV.clicked.connect(self.func_btn_Project_CSV)
        self.btn_apply.clicked.connect(self.func_btn_apply)

    def connectLineInit(self):
        self.line_Testcase_num.textChanged.connect(self.func_line_Testcase_num)
        self.line_Testcase_num.returnPressed.connect(self.func_line_Testcase_num)
        self.line_Testcase_num_range.returnPressed.connect(self.func_line_Testcase_num_range)

    def connectCBoxInit(self):
        self.cbox_project.currentIndexChanged.connect(self.func_cbox_project)

    def show_widget(self, main_geometry):
        self.move(main_geometry.topRight())
        self.show()
        self.activateWindow()

    def func_cbox_project(self):
        self.project = self.cbox_project.currentText().strip()
        self._update_map_script()
        self._update_map_mode()
        self.swTest.script_path = os.path.join(self.swTest.main_path, 'data', 'input', 'script', self.project)

    def func_btn_TESTCASE_Start(self):
        self._update_status(True)  # 테스트 시작
        if self.testcase_num_str:
            self.swTest.run(self.testcase_num_str)
        else:
            logging_print("Error: There is no Test Case")
        self._update_status(False)  # 테스트 종료

    def func_btn_TESTCASE_Start_range(self):
        self._update_status(True)  # 테스트 시작
        if self.testcase_num_range_str:
            self.swTest.run(self.testcase_num_range_str)
        else:
            logging_print("Error: There is no Test Case")
        self._update_status(False)  # 테스트 종료

    def func_btn_TESTMode_Start(self):
        self._update_map_mode()
        self._update_status(True)  # 테스트 시작
        test_mode = str(self.cbox_Test_mode.currentText().strip())
        test_cases = self.dic_test_mode[test_mode]
        test_cases = list(map(str, test_cases))
        self.swTest.run(test_cases)
        self._update_status(False)  # 테스트 종료

    # noinspection PyMethodMayBeStatic
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

    def func_line_Testcase_num(self):

        line_testcase_num_str = re.sub(r'[^0-9,~]', '', self.line_Testcase_num.text().replace(' ', ''))
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
        for v in testcase_lst:
            if v not in self.testcase_num_str and v != '':
                self.testcase_num_str.append(v)
        print(self.testcase_num_str)

        '''
        line_testcase_num_str = self.line_Testcase_num.text()
        self.testcase_num_str = line_testcase_num_str.split()
        print(self.testcase_num_str)
        '''

    def func_line_Testcase_num_range(self):
        line_testcase_num_range_str = self.line_Testcase_num_range.text()
        temp = line_testcase_num_range_str.split()
        self.testcase_num_range_str = []
        for i in range(int(temp[0]), int(temp[1]) + 1):
            self.testcase_num_range_str.append(str(i))
        print(self.testcase_num_range_str)

    def func_btn_apply(self):
        configure_str = self.pText_map_test.toPlainText()
        with open('./data/input/script/set/map_script_sw_test.yaml', 'w', encoding='utf-8') as f:
            f.write(configure_str)

        logging_print('[INFO] The map script is modified as seen in the display\n')

    def _update_map_script(self):
        self.swTest.map_script_path = './data/input/script/{}/set/map_script_sw_test.yaml'.format(self.project)
        with open(self.swTest.map_script_path, 'r', encoding='utf-8') as f:
            f_lines = f.readlines()
            map_test = "".join(f_lines)
        self.pText_map_test.setPlainText(map_test)

    def _update_map_mode(self):
        self.cbox_Test_mode.clear()
        self.swTest.map_mode_path = './data/input/script/{}/set/map_test_mode.yaml'.format(self.project)
        self.dic_test_mode = self.swTest.update_map_mode()
        self.cbox_Test_mode.addItems(list(self.dic_test_mode.keys()))

    def _update_status(self, status):
        if status is True:
            self.line_status.setText('RUNNING')
            self.line_status.setStyleSheet("background-color: %s;border: 1px solid transparent;" % "#42f566")
        else:
            self.line_status.setText('Not RUNNING')
            self.line_status.setStyleSheet(
                "background-color: %s;border: 1px solid transparent;" % "rgba(255, 0, 0, 0.70)")
