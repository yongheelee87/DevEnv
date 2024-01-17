import pandas as pd
import yaml
import time
from Lib.Inst import *
from Lib.Common import *
from . updatePy import *

RESULT_FILE_PATH = os.path.join(os.getcwd(), 'data', 'result')
MODULES = ['CCW', 'CTCW', 'SWA', 'SDR', 'CDW', 'BSW']


class AutoTest:
    def __init__(self, test_yaml: str):
        self.swTest = None # TestProcess class 메모리
        self.df_inst = get_inst_status()  # Instruments status 가져오기
        self.test_map, self.total_map = self._update_test_map(path=test_yaml)  # update map file for test
        self.ui_ON = False
        self.script_path = None  # Test script path
        self.result_path = None  # Result Path to be exported
        self.version = None
        self.project = None
        self.tc_script = {}
        self.num_lines = 0
        self.test_case = []

    def run(self):
        print("************************************************************")
        print("*** SW TEST Automation Test Start!\n"
              "*** Please Do not try additional command until it completes")
        print("************************************************************\n")

        start_time = time.localtime(time.time())
        print('Starting at: {}'.format(time.strftime("%a, %d-%b-%Y %I:%M:%S", start_time)))
        self.result_path = os.path.join(RESULT_FILE_PATH, time.strftime('%Y%m%d_%H%M%S', start_time))
        isdir_and_make(self.result_path)

        self.version = self._get_sw_version()  # update current sw version
        print("SW version\n{}\n".format(self.version))

        total_res = {}
        if self.ui_ON is True:
            total_res[self.project] = self.test_module(self.project)
        else:
            for pjt in self.test_map.keys():
                total_res[pjt] = self.test_module(pjt)
        make_home_HTML(data=total_res, export_path=self.result_path, df_ver=self.version)
        self.stop()

    def stop(self):
        import shutil
        archive_path = Configure.set['system']['archive_path']
        zip_name = 'EILS_' + os.path.basename(self.result_path)
        if os.path.exists(archive_path):
            shutil.rmtree(archive_path)
        shutil.make_archive(os.path.join(archive_path, zip_name), 'zip', self.result_path)
        print('Ending at: {}'.format(time.strftime("%a, %d-%b-%Y %I:%M:%S", time.localtime(time.time()))))
        print("[INFO] {}.zip has been created\n".format(zip_name))
        print("************************************************************")
        print("*** SW TEST Automation Test completed")
        print("************************************************************\n")
        time.sleep(1)

    def test_module(self, project: str):
        self.script_path = os.path.join('data', 'input', 'script', project)

        project_tc = {}
        if self.ui_ON is True:
            for tc in self.test_case:
                project_tc[tc] = self.total_map[project][tc]
        else:
            project_tc = self.test_map[project]  # 모듈 별 테스트 케이스

        num_tc = len(project_tc.keys())  # TC 갯수
        print("************************************************************")
        print("*** Module: {}".format(project))
        print("*** Test Script: {}".format(', '.join(list(project_tc.keys()))))
        print("*** Number of Test: {}".format(num_tc))
        print("************************************************************\n")

        start_time = time.time()  # 시작 시간 저장

        export_path = os.path.join(self.result_path, project)
        isdir_and_make(export_path)

        res_tc = {}
        self.tc_script = {}  # Initialize for each module
        self.num_lines = 0
        for idx, test_script in enumerate(project_tc.keys()):
            print('Running {} ({}/{})'.format(test_script, idx+1, num_tc))
            res_tc[project_tc[test_script]] = self._run_test_case(test_script, export_path)
            if 'Fail' in res_tc[project_tc[test_script]]:
                print('Result: Fail')
            else:
                print('Result: {}'.format(res_tc[project_tc[test_script]]))
            print('{} has been Done ({}/{})\n'.format(test_script, idx+1, num_tc))

        self._export_test_sum(file_path=export_path, start_time=start_time,
                              elapsed_time=time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)),  # 경과 시간 저장
                              project=project, tc_dict=project_tc, res_dict=res_tc)
        return res_tc

    def _update_test_map(self, path: str) -> (dict, dict):
        # 지정된 장소에 파일이 없을 경우 remote에 설정된 파일 로드
        if not os.path.isfile(path):
            path = './data/config/remote/test_map.yaml'

        # Todo unicode 에러 발생
        with open(path, encoding="utf-8") as f:
            raw_lines = f.readlines()
            lines = raw_lines[2:] if '# Project' in raw_lines[0] else raw_lines
            lst_total = []
            lst_auto = []
            for line in lines:
                if line != '\n' or line != '#\n':
                    new_line = line.replace('#', '')
                    space = check_front_space(new_line)
                    if space < 2:
                        new_line = new_line.lstrip()
                    elif space < 5:
                        new_line = '  ' + new_line.lstrip()
                    else:
                        new_line = '    ' + new_line.lstrip()

                    if '#' not in line:
                        lst_auto.append(new_line)  # 주석 처리 적용된 yaml 적용
                    lst_total.append(new_line)  # 주석 처리 무시된 yaml 적용

            auto_dict = yaml.load(''.join(lst_auto), Loader=yaml.SafeLoader)
            total_dict = yaml.load(''.join(lst_total), Loader=yaml.SafeLoader)
        return auto_dict, total_dict

    def _run_test_case(self, test_script: str, export_path: str) -> str:
        '''
        :param test_script: Test Script
        :param export_path: path to export result
        :return: test result
        '''
        script_file = os.path.join(self.script_path, test_script + '.py')  # 실행할 테스트 python 코드
        csv_file = os.path.join(self.script_path, test_script + '.csv')  # 실행할 테스트 csv 파일
        csv_res_file = os.path.join(export_path, test_script + '.csv')  # 생성된 결과 파일

        if os.path.isfile(script_file) is False and os.path.isfile(csv_file) is False:  # py파일과 csv파일이 없을 경우
            ret = 'Skip'
        else:
            if os.path.isfile(csv_res_file) is False:
                py_lines, df_tc = update_py(py_path=script_file, output_path=export_path, title=test_script)  # python testcase code update
                if df_tc is not None:
                    self.tc_script[test_script] = df_tc
                    self.num_lines += len(df_tc)
                exec(py_lines)  # python TestCase Function 실행
            ret = self._check_tc_pass_state(tc_res_file=csv_res_file)
        return ret
    
    def _check_tc_pass_state(self, tc_res_file: str) -> str:
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

    def _export_test_sum(self, file_path: str, start_time: float, elapsed_time: str, project: str, tc_dict: dict, res_dict: dict):
        '''
        :param file_path:
        :param start_time:
        :param elapsed_time: elapsed time for test
        :param project: project name
        :param res_dict: a dict of test result
        '''

        time_start = time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime(start_time))
        time_end = time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime(time.time()))

        len_pass = 0
        len_skip = 0
        len_fail = 0
        lst_fail = []
        for tc_name in res_dict.keys():
            tc_res = res_dict[tc_name]
            if tc_res == 'Pass':
                len_pass += 1
            elif tc_res == 'Skip':
                len_skip += 1
            else:
                len_fail += 1
                lst_tc_res = tc_res.split(',')
                if len(lst_tc_res) == 1:
                    lst_fail.append(tc_name)
                else:
                    lst_fail.append('{} (Step {})'.format(tc_name, ','.join(lst_tc_res[1:])))

        if len_fail == 0:
            fail_case = 'Nothing'
        else:
            fail_case = ','.join(lst_fail)

        lst_tc = list(res_dict.keys())
        tc_names = ', '.join(lst_tc)  # 한글 버전
        ind = ["Date_Start", "Date_End", "Elapsed_Time", "TestCase_Names", "TestCase_Amt", "Pass_Amt", "Skip_Amt", "Fail_Amt", "Fail_Case", "Steps"]
        con = [time_start, time_end, elapsed_time, tc_names, len(lst_tc), len_pass, len_skip, len_fail, fail_case, self.num_lines]
        df_tc_sum = pd.DataFrame(con, columns=["Value"], index=ind)
        df_tc_sum.to_csv(file_path + "\\" + "Summary_{}.csv".format(os.path.basename(file_path)), encoding='utf-8-sig')
        df_ver = self.version.set_index(keys='Module')

        print("*** Number of Pass Test Case: {}/{}".format(len_pass, len(lst_tc)))
        print("*** Number of Fail Test Case: {}/{}".format(len_fail, len(lst_tc)))
        print("*** The Test for Module {} has been completed\n".format(os.path.basename(file_path)))
        make_pjt_HTML(df_sum=df_tc_sum, project=os.path.basename(file_path), version=df_ver.loc[project, 'Version'], dict_tc=tc_dict, tc_script=self.tc_script, export_path=file_path)  # 최종 결과물 HTML로 산출

    def _get_sw_version(self) -> pd.DataFrame:
        t32._wait_until_command_ends(timeout=5)
        lst_version = []
        for module in MODULES:
            if 'BSW' == module:
                var_basic = ['ubE_SoftwareVer1', 'ubE_SoftwareVer2', 'ubE_SoftwareVer3', 'ubE_SoftwareVer4', 'ubC_DraftReleaseCnt1']
                lst_basic = [chr(int(t32.read_symbol(symbol=b))) for b in var_basic[:-1]] + ['{0:02d}'.format(int(t32.read_symbol(symbol=var_basic[-1])))]
                lst_version.append([module, '{}.{}{}.{}.{}'.format(lst_basic[0], lst_basic[1], lst_basic[2], lst_basic[3], lst_basic[4])])
            else:
                ver = str(hex(int(t32.read_symbol(symbol='ASW_Version.{}'.format(module)))))[5:]
                lst_version.append([module, '{}_{}_{}_{}.{}'.format(ver[0], ver[1], ver[2], ver[3], ver[4])])
        return pd.DataFrame(lst_version, columns=['Module', 'Version'])

    def update_test_case(self, pjt: str, test_num: list):
        self.project = pjt
        with open(os.path.join('data', 'input', 'script', pjt, 'set', 'map_script_sw_test.yaml')) as f:
            temp = yaml.load(f, Loader=yaml.FullLoader)
        tc_dict = {str(oldv): oldk for oldk, oldv in temp.items()}
        self.test_case = [tc_dict[num] for num in test_num]

    def update_map_mode(self, pjt: str) -> dict:
        map_mode = os.path.join('data', 'input', 'script', pjt, 'set', 'map_test_mode.yaml')
        if os.path.isfile(map_mode):
            with open(map_mode) as f:
                temp = yaml.load(f, Loader=yaml.FullLoader)
        else:
            temp = {'N/A': '0'}
        return temp
