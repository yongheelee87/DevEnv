import yaml
import sys
import time
from Lib.Inst.Trace32Lib import *
from Lib.Common.basicFunction import *

TOTAL_RESULT_FILE = 'Total_TESTCASE'
SW_TC_NAME = r'SwTC_'
SW_TC_SUM_NAME = r"SwTC_Sum_"
SW_TC_RES_NAME = r"SwTC_Res_"
RESULT_FILE_PATH = os.path.join(os.getcwd(), 'data', 'result')


class TestProcess:
    """
    main test class for process
    """

    def __init__(self, project):
        self.main_path = os.getcwd()
        self.map_dict = dict()
        self.script_path = os.path.join(self.main_path, 'data', 'input', 'script', project)
        self.map_script_path = ''
        self.map_mode_path = ''

    def update_map_mode(self):
        if os.path.isfile(self.map_mode_path):
            with open(self.map_mode_path) as f:
                temp = yaml.load(f, Loader=yaml.FullLoader)
        else:
            temp = {'N/A': '0'}
        return temp

    def run(self, tc_num: list):
        logging_print(
            ".... SW TEST Automation Test Start! Please Do not try additional command until it completes ....\n")
        self.map_dict = self._update_map_script()  # Update Map Script for Test Case Function
        testcase_input = sorted(tc_num, key=int)
        logging_print("TestCase Number = {}\n".format(testcase_input))

        start_time = time.time()  # 시작 시간 저장
        time_start = time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime(time.time()))
        time_var = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
        df_result = load_csv_dataframe(RESULT_FILE_PATH, TOTAL_RESULT_FILE)

        results = [self._run_test_case(tc_num, df_result, time_var) for tc_num in testcase_input]
        print(df_result)
        # Total_TESTCASE 파일이 열러 있는지 확인 후 열려 있다면 덮어쓰기 금지
        if check_process_open(TOTAL_RESULT_FILE) is True:
            logging_print("Error: {} can not be available. The csv file is open\n".format(TOTAL_RESULT_FILE))
        else:  # Total_TESTCASE 덮어쓰기 가능
            export_csv_dataframe(df_result, RESULT_FILE_PATH, TOTAL_RESULT_FILE)  # Total_TESTCASE.csv 업데이트

        elapsed_time = time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))  # 시작 시간 저장
        time_end = time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime(time.time()))
        self._export_test_sum(time_var, time_start, time_end, elapsed_time, testcase_input, results)
        logging_print(".... SW TEST Automation Test completed ....\n")

    # noinspection PyMethodMayBeStatic
    def _run_test_case(self, tc_num: str, result, time_var: str):
        '''
        :param tc_num: Test case number
        :param result: dataframe result for Total_TESTCASE.csv
        :param time_var: time when it starts
        :return: test result
        '''
        func_name = SW_TC_NAME + tc_num
        export_path = os.path.join(RESULT_FILE_PATH, time_var)
        csv_tc_file = os.path.join(export_path, func_name + '.csv')

        data_testcase = result[result["TestCase"] == tc_num]
        data_index = int(data_testcase.index.values)

        isdir_and_make(export_path)

        if os.path.isfile(csv_tc_file) is False:
            for _ in range(int(data_testcase.iloc[0, 1])):
                self._exec_test_script(export_path, tc_num)  # TestCase Function 실행

        # csv가 생성 되었는지 확인
        start = time.time_ns()
        elapse_time = 0
        lst_tc = None

        # 3자리 숫자 인식 코드 추가
        func_name_3digit = SW_TC_NAME + tc_num.zfill(3)
        csv_tc_file_3digit = os.path.join(export_path, func_name_3digit + '.csv')

        while elapse_time < 60:  # 60초 초과시
            if os.path.isfile(csv_tc_file) is True:
                # 파일 Access가 가능한지 확인
                try:
                    # Result 위치 변경(가장 아래)시 수정 필요
                    lst_tc = load_csv_list(export_path, func_name)
                except PermissionError:
                    pass
            elif os.path.isfile(csv_tc_file_3digit) is True:
                # 파일 Access가 가능한지 확인
                try:
                    # Result 위치 변경(가장 아래)시 수정 필요
                    lst_tc = load_csv_list(export_path, func_name_3digit)
                except PermissionError:
                    pass

            # 파일을 정상적으로 읽을 경우 탈출
            if lst_tc is not None:
                break

            elapse_time = int((time.time_ns() - start) * 0.000000001)
            if elapse_time > 60:
                sys.exit('NO CSV File')

        tc_pass_state = lst_tc[-1][-1].replace(' ', '')  # Pass Fail 받아오기
        ret = tc_pass_state

        # Fail일 경우에는 Fail Test Case Number 반환
        if 'Fail' == ret:
            ret = tc_num

        result.loc[data_index]['Test_Result'] = tc_pass_state
        result.loc[data_index]['Output'] = ''
        result.loc[data_index]['Last_Run_Time'] = time_var

        logging_print("Success: {} Test Done\n".format(func_name))

        return ret

    def _export_test_sum(self, time_var: str, date_before: str, date_after: str, elapsed_time: str, tc_num: list,
                         res: list):
        '''
        :param time_var:
        :param date_before:
        :param date_after:
        :param elapsed_time: elapsed time for test
        :param tc_num: a list of test numbers
        :param res: a list of test result
        '''
        path_file = os.path.join(RESULT_FILE_PATH, time_var)
        isdir_and_make(path_file)
        result_col = pd.DataFrame(res, columns=['Result'])
        result_pass = result_col[result_col['Result'] == 'Pass']
        result_removed = result_col[result_col['Result'] == 'Removed']
        result_skip = result_col[result_col['Result'] == 'Skip']
        result_fail = result_col[
            (result_col['Result'] != 'Pass') & (result_col['Result'] != 'Removed') & (result_col['Result'] != 'Skip')]
        fail_amt = len(result_fail)

        if fail_amt != 0:
            fail_case = []
            for i in range(fail_amt):
                test = result_fail.iloc[i, 0]
                fail_case.append(str(test))
            logging_print("Test Result Fail Case: {}\n".format(fail_case))
        else:
            fail_case = 'Nothing'

        ind = ["Date_Start", "Date_End", "Elapsed_Time", "TestCase_Num", "TestCase_Amt", "Pass_Amt", "Removed_Amt",
               "Skip_Amt", "Fail_Amt", "Fail_Case"]
        con = [[date_before], [date_after], [elapsed_time], [tc_num], [len(result_col)], [len(result_pass)],
               [len(result_removed)],
               [len(result_skip)], [fail_amt], [fail_case]]
        df_tc_sum = pd.DataFrame(con, columns=["Value"], index=ind)
        df_tc_sum.to_csv(path_file + "\\" + SW_TC_SUM_NAME + time_var + ".csv", encoding='cp1252')

        res_total = [[str(num), result] for num, result in zip(tc_num, res)]
        df_res_total = pd.DataFrame(res_total, columns=["Test_Case", "Result"])
        df_res_total.to_csv(path_file + "\\" + SW_TC_RES_NAME + time_var + ".csv", index=False)

    # noinspection PyMethodMayBeStatic
    def _update_map_script(self):
        with open(self.map_script_path) as f:
            temp = yaml.load(f, Loader=yaml.FullLoader)
        return {str(k): oldk for oldk, oldv in temp.items() for k in oldv}

    # noinspection PyMethodMayBeStatic
    def _exec_test_script(self, export_path, test_num):
        lst_swTest_num = list(self.map_dict.keys())
        script_name = self.map_dict[test_num] if test_num in lst_swTest_num else "Empty"

        if '.cmm' in script_name:  # cmm 파일일 경우
            cmm_path = os.path.join(self.script_path, script_name)
            t32.cd_do(cmm_path + ' ' + str(export_path))
        elif '.py' in script_name:  # python 파일일 경우
            exec(update_path_py(os.path.join(self.script_path, script_name), export_path))
        else:  # 파일이 없을 경우
            df_empty = pd.DataFrame([['Result', 'Skip']], columns=[SW_TC_NAME + test_num, ''])
            export_csv_dataframe(df_empty, export_path, SW_TC_NAME + test_num)
# This is a new line that ends the file
