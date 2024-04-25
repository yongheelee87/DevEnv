import datetime
import time
from threading import Thread
from Lib.DataProcess import *
from Lib.TestProcess.updatePy import UpdatePy


class MeasRGW(UpdatePy):
    def __init__(self):
        UpdatePy.__init__(self)

        self.num_lines = 0
        self.df_tc = None
        self.rate = '0.1'
        self.judge = 'same'
        self.n_match = '1'
        self.fill_zero = True

    def run(self):
        print("************************************************************")
        print("*** Measurement Start!\n"
              "*** Please Do not try additional command until it completes")
        print("************************************************************\n")

        start_time = time.time()  # 시작 시간 저장
        start_time_str = time.strftime("%a, %d-%b-%Y %I:%M:%S", time.localtime(start_time))

        print(f'Starting at: {start_time_str}')
        self.py_title = 'RGW'
        self.py_output_path = os.path.join(os.path.join(os.getcwd(), 'data', 'result'), time.strftime('%Y%m%d_%H%M%S', time.localtime(start_time)))
        isdir_and_make(self.py_output_path)

        result = self._run_measure()
        print(f'Result: {result}')
        self._export_test_sum(start_time=start_time, res=result)

        self.stop()

    def stop(self):
        end_time_str = time.strftime("%a, %d-%b-%Y %I:%M:%S", time.localtime(time.time()))
        print(f'Ending at: {end_time_str}')
        print("************************************************************")
        print("*** Measurement completed")
        print("************************************************************\n")
        open_path(os.path.join(self.py_output_path, 'Result_RGW.html'))
        time.sleep(1)

    def _run_measure(self) -> str:
        '''
        :return: test result
        '''
        lines = self.tc_head_body.splitlines(True)[1:]
        py_lines, self.df_tc = self.fill_variables(df=self.df_tc, py_code=self._fill_header(lines), rate=self.rate, judge=self.judge, n_match=self.n_match, fill_zero=self.fill_zero)
        if self.df_tc is not None:
            self.num_lines = len(self.df_tc)
        exec(py_lines)  # python TestCase Function 실행
        csv_res_file = os.path.join(self.py_output_path, f'{self.py_title}.csv')  # 생성된 결과 파일
        return self._check_tc_pass_state(tc_res_file=csv_res_file)

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

    def _export_test_sum(self, start_time: float, res: str):
        '''
        :param start_time:
        :param res: test result
        '''
        end_time = time.time()
        str_end = time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime(end_time))
        elapsed_time = time.strftime("%H:%M:%S", time.gmtime(end_time - start_time))
        str_start = time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime(start_time))

        if 'Fail' in res:
            lst_res = res.split(',')
            fail_step_str = ','.join(lst_res[1:])
            res = f'Fail (Step {fail_step_str})'

        df_tc_sum = pd.DataFrame(np.array([str_start, str_end, elapsed_time, res, self.num_lines], dtype=object),
                                 columns=["Value"],
                                 index=["Date_Start", "Date_End", "Elapsed_Time", "Result", "Steps"])
        make_meas_HTML(df_sum=df_tc_sum, project='RGW', tc_script=self.df_tc, export_path=self.py_output_path)  # 최종 결과물 HTML로 산출
