import os
import time
import yaml
import pandas as pd
import numpy as np
from Lib.Common import isdir_and_make, Configure, check_front_space, load_csv_list
from Lib.DataProcess import make_home_HTML, make_pjt_HTML
from Lib.Inst import get_inst_status, t32
from . updatePy import UpdatePy

RESULT_FILE_PATH = os.path.join(os.getcwd(), 'data', 'result')
MODULES = ['CCW', 'CTCW', 'SWA', 'SDR', 'CDW', 'BSW']


class AutoTest(UpdatePy):
    def __init__(self, test_yaml: str):
        """
        :param test_yaml: test yaml file including list of functions corresponding to test cases
        """
        UpdatePy.__init__(self)

        self.df_inst = get_inst_status()  # Instruments status 가져오기
        self.yaml_path = test_yaml if os.path.isfile(test_yaml) else './data/config/remote/test_map.yaml'  # 지정된 장소에 파일이 없을 경우 remote에 설정된 파일 로드
        self.test_map, self.total_map = self._update_test_map()  # update map file for test
        self.script_path = ''  # Test script path
        self.result_path = ''  # Result Path to be exported
        self.version = None
        self.project = ''
        self.tc_script = {}
        self.tc_in_out = {}
        self.project_tc = {}
        self.tc_res = {}
        self.num_lines = 0
        self.test_case = []

    def run(self):
        print("************************************************************")
        print("*** SW TEST Automation Test Start!\n"
              "*** Please Do not try additional command until it completes")
        print("************************************************************\n")

        start_time = time.localtime(time.time())
        start_time_str = time.strftime("%a, %d-%b-%Y %I:%M:%S", start_time)
        print(f'Starting at: {start_time_str}')
        self.result_path = os.path.join(RESULT_FILE_PATH, time.strftime('%Y%m%d_%H%M%S', start_time))
        isdir_and_make(self.result_path)

        self.version = self._get_sw_version()  # update current sw version
        print(f"SW version\n{self.version}\n")

        # Single mode (Per project) or Total Mode
        if self.project:
            self.test_module()
            total_res = {self.project: self.tc_res}
        else:
            total_res = {}
            for pjt in self.test_map.keys():
                self.project = pjt
                self.test_module()
                total_res[self.project] = self.tc_res
        make_home_HTML(data=total_res, export_path=self.result_path, df_ver=self.version)
        self.stop()

    def stop(self):
        self.project = ''  # single mode를 위한 초기화
        
        import shutil
        archive_path = Configure.set['system']['archive_path']
        zip_name = f'EILS_{os.path.basename(self.result_path)}'
        if os.path.exists(archive_path):
            shutil.rmtree(archive_path)
        shutil.make_archive(os.path.join(archive_path, zip_name), 'zip', self.result_path)
        print(f'Ending at: {time.strftime("%a, %d-%b-%Y %I:%M:%S", time.localtime(time.time()))}')
        print(f"[INFO] {zip_name}.zip has been created\n")
        print("************************************************************")
        print("*** SW TEST Automation Test completed")
        print("************************************************************\n")
        time.sleep(1)

    def test_module(self) -> None:
        self.script_path = os.path.join('data', 'input', 'script', self.project)

        num_tc = len(self.test_map[self.project])  # TC 갯수
        print("************************************************************")
        print(f"*** Module: {self.project}")
        print(f"*** Test Script: {', '.join(list(self.test_map[self.project]))}")
        print(f"*** Number of Test: {num_tc}")
        print("************************************************************\n")

        start_time = time.time()  # 시작 시간 저장

        self.py_output_path = os.path.join(self.result_path, self.project)
        isdir_and_make(self.py_output_path)

        self.project_tc, self.tc_res, self.tc_script, self.tc_in_out, self.num_lines = {}, {}, {}, {}, 0  # Initialize for each module
        for idx, test_script in enumerate(self.test_map[self.project]):
            print(f'Starting on: {test_script} ({idx+1}/{num_tc})')
            self.tc_res[self.py_sub_title] = self._run_test_case(test_script)
            self.project_tc[test_script] = self.py_sub_title  # sub title 저장
            if 'Fail' in self.tc_res[self.py_sub_title]:
                print('Result: Fail')
            else:
                print(f'Result: {self.tc_res[self.py_sub_title]}')
            print(f'{test_script} has been Done ({idx+1}/{num_tc})\n')

        self._export_test_sum(start_time=start_time)

    def _update_test_map(self) -> (dict, dict):
        with open(self.yaml_path, encoding="utf-8") as f:
            auto_dict = yaml.load(f, Loader=yaml.SafeLoader)
            total_dict = yaml.load(f, Loader=yaml.SafeLoader)
        return auto_dict, total_dict

    def _run_test_case(self, test_script: str) -> str:
        """
        :param test_script: Test Script
        :return: test result
        """
        self.py_title = test_script
        self.py_path = os.path.join(self.script_path, f'{self.py_title}.py')  # 실행할 테스트 python 코드
        csv_file = os.path.join(self.script_path, f'{self.py_title}.csv')  # 실행할 테스트 csv 파일
        csv_res_file = os.path.join(self.py_output_path, f'{self.py_title}.csv')  # 생성된 결과 파일
        if os.path.isfile(self.py_path) is False and os.path.isfile(csv_file) is False:  # py파일과 csv파일이 없을 경우
            ret = 'Skip'
        else:
            if os.path.isfile(csv_res_file) is False:
                py_lines, df_tc = self.update_py()  # python testcase code update
                if df_tc is not None:
                    self.tc_script[test_script] = df_tc
                    self.tc_in_out[test_script] = self.in_out_sigs
                    self.num_lines += len(df_tc)
                exec(py_lines)  # python TestCase Function 실행
            ret = self._check_tc_pass_state(tc_res_file=csv_res_file)
        return ret
    
    def _check_tc_pass_state(self, tc_res_file: str) -> str:
        """
        :param tc_res_file: test result individual csv file path
        :return: tc_pass_state
        """
        # csv가 생성 되었는지 확인
        tc_pass_state = 'Skip'
        if os.path.isfile(tc_res_file) is True:
            # 파일 Access가 가능한지 확인
            try:
                # Result 위치 변경(가장 아래)시 수정 필요
                tc_pass_state = load_csv_list(tc_res_file)[-1][-1].strip()  # Pass Fail 받아오기 마지막 인덱스
            except PermissionError:
                pass
        return tc_pass_state

    def _export_test_sum(self, start_time: float):
        """
        :param start_time:
        """
        end_time = time.time()
        str_end = time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime(end_time))
        elapsed_time = time.strftime("%H:%M:%S", time.gmtime(end_time - start_time))
        str_start = time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime(start_time))

        len_pass = 0
        len_skip = 0
        len_fail = 0
        lst_fail = []
        for tc_name in self.tc_res.keys():
            tc_res = self.tc_res[tc_name]
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
                    step_str = ','.join(lst_tc_res[1:])
                    lst_fail.append(f'{tc_name} (Step {step_str})')

        if len_fail == 0:
            fail_case = 'Nothing'
        else:
            fail_case = ','.join(lst_fail)

        lst_tc = list(self.tc_res.keys())
        tc_names = ', '.join(lst_tc)  # 한글 버전
        df_tc_sum = pd.DataFrame(np.array([str_start, str_end, elapsed_time, tc_names, len(lst_tc), len_pass, len_skip, len_fail, fail_case, self.num_lines], dtype=object),
                                 columns=["Value"],
                                 index=["Date_Start", "Date_End", "Elapsed_Time", "TestCase_Names", "TestCase_Amt", "Pass_Amt", "Skip_Amt", "Fail_Amt", "Fail_Case", "Steps"])
        df_tc_sum.to_csv(self.py_output_path + "\\" + f"Summary_{os.path.basename(self.py_output_path)}.csv", encoding='utf-8-sig')
        df_ver = self.version.set_index(keys='Module')

        print(f"*** Number of Pass Test Case: {len_pass}/{len(lst_tc)}")
        print(f"*** Number of Fail Test Case: {len_fail}/{len(lst_tc)}")
        print(f"*** The Test for Module {os.path.basename(self.py_output_path)} has been completed\n")
        make_pjt_HTML(df_sum=df_tc_sum, project=os.path.basename(self.py_output_path), version=df_ver.loc[self.project, 'Version'], dict_tc=self.project_tc, tc_script=self.tc_script, tc_in_out=self.tc_in_out, export_path=self.py_output_path)  # 최종 결과물 HTML로 산출

    def _get_sw_version(self) -> pd.DataFrame:
        t32._wait_until_command_ends(timeout=5)
        lst_version = []
        for module in MODULES:
            if 'BSW' == module:
                var_basic = ['ubE_SoftwareVer1', 'ubE_SoftwareVer2', 'ubE_SoftwareVer3', 'ubE_SoftwareVer4', 'ubC_DraftReleaseCnt1']
                lst_basic = [chr(int(t32.read_symbol(symbol=b))) for b in var_basic[:-1]] + ['{0:02d}'.format(int(t32.read_symbol(symbol=var_basic[-1])))]
                lst_version.append([module, f'{lst_basic[0]}.{lst_basic[1]}{lst_basic[2]}.{lst_basic[3]}.{lst_basic[4]}'])
            else:
                ver = str(hex(int(t32.read_symbol(symbol=f'ASW_Version.{module}'))))[5:]
                lst_version.append([module, f'{ver[0]}_{ver[1]}_{ver[2]}_{ver[3]}.{ver[4]}'])
        return pd.DataFrame(np.array(lst_version, dtype=object), columns=['Module', 'Version'])

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
