import os

import yaml
import time
from Lib.Common.basicFunction import *

RESULT_FILE_PATH = os.path.join(os.getcwd(), 'data', 'result')


class AutoTest:
    def __init__(self):
        self.swTest = None # TestProcess class 메모리
        self.map_path = './data/config/auto_test.yaml'
        self.map_dict = dict()
        self.script_path = None  # Test script path
        self.result_path = None  # Result Path to be exported

    def test(self, project: str):
        self.script_path = os.path.join('data', 'input', 'script', project)
        print(".... Module: {} ....\n\nTest Script: {}\n".format(project, self.map_dict[project]))

        start_time = time.time()  # 시작 시간 저장
        time_start = time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime(time.time()))

        export_path = os.path.join(self.result_path, project)
        isdir_and_make(export_path)

        results = [self._run_test_case(test_script, export_path) for test_script in self.map_dict[project]]

        self._export_test_sum(file_path=export_path,
                              time_start=time_start,
                              elapsed_time=time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)),  # 경과 시간 저장
                              lst_tc=self.map_dict[project],
                              res=results)

    def run(self):
        print(".... SW TEST Automation Test Start! Please Do not try additional command until it completes ....\n")
        self.map_dict = self._update_test_map()
        self.result_path = os.path.join(RESULT_FILE_PATH, time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time())))
        isdir_and_make(self.result_path)

        for pjt in self.map_dict.keys():
            self.test(pjt)

        self.stop()

    def stop(self):
        print(".... SW TEST Automation Test completed ....\n")
        time.sleep(1)

    def _update_test_map(self):
        dict_auto = dict()
        if os.path.exists(self.map_path):
            with open(self.map_path) as f:
                dict_auto = yaml.load(f, Loader=yaml.FullLoader)
        return dict_auto

    def _run_test_case(self, test_script: str, export_path: str):
        '''
        :param test_script: Test Script
        :param export_path: path to export result
        :return: test result
        '''
        print("Start: {}\n".format(test_script))
        script_file = os.path.join(self.script_path, test_script + '.py')
        csv_tc_file = os.path.join(export_path, test_script + '.csv')

        if os.path.isfile(script_file) is True:
            if os.path.isfile(csv_tc_file) is False:
                exec(update_script_py(py_path=script_file, output_path=export_path, title=test_script))  # TestCase Function 실행
            ret = self._check_tc_pass_state(tc_res_file=csv_tc_file)
            if ret == 'Fail':  # Fail일 경우에는 Fail Test Script 반환
                ret = test_script
        else:
            ret = 'Skip'

        print("Done: {} Test with result of {}\n".format(test_script, ret))
        return ret
    
    def _check_tc_pass_state(self, tc_res_file: str):
        '''
        :param tc_res_file: test result individual csv file path 
        :return: tc_pass_state
        '''
        # csv가 생성 되었는지 확인
        tc_pass_state = 'Skip'
        if os.path.isfile(tc_res_file) is True:
            # 파일 Access가 가능한지 확인
            try:
                # Result 위치 변경(가장 아래)시 수정 필요
                tc_pass_state = load_csv_list(tc_res_file)[-1][-1].replace(' ', '')  # Pass Fail 받아오기 마지막 인덱스
            except PermissionError:
                pass
        return tc_pass_state

    def _export_test_sum(self, file_path: str, time_start: str, elapsed_time: str, lst_tc: list, res: list):
        '''
        :param file_path:
        :param time_start:
        :param elapsed_time: elapsed time for test
        :param lst_tc: a list of test cases
        :param res: a list of test result
        '''
        time_end = time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime(time.time()))
        len_pass = 0
        len_skip = 0
        len_fail = 0
        fail_case = ''
        for tc_result in res:
            if tc_result == 'Pass':
                len_pass += 1
            elif tc_result == 'Skip':
                len_skip += 1
            else:
                len_fail += 1
                fail_case = ', {}'.format(tc_result)

        if len_fail == 0:
            fail_case = 'Nothing'

        ind = ["Date_Start", "Date_End", "Elapsed_Time", "TestCase_Names", "TestCase_Amt", "Pass_Amt", "Skip_Amt", "Fail_Amt", "Fail_Case"]
        con = [[time_start], [time_end], [elapsed_time], [lst_tc], [len(lst_tc)], [len_pass], [len_skip], [len_fail], [fail_case]]
        df_tc_sum = pd.DataFrame(con, columns=["Value"], index=ind)
        df_tc_sum.to_csv(file_path + "\\" + "Summary_{}.csv".format(os.path.basename(file_path)), encoding='cp1252')
