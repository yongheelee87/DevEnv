import os
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mplcursors import cursor
from Lib.Common import isdir_and_make, open_path, load_csv_list
from Lib.Inst import canBus
from Lib.DataProcess import make_meas_HTML
from Lib.TestProcess.updatePy import UpdatePy


class MeasRGW(UpdatePy):
    def __init__(self):
        UpdatePy.__init__(self)

        self.num_lines = 0
        self.df_tc = None
        self.rate = '0.1'
        self.time_type = 'Per step'
        self.judge = 'same'
        self.n_match = '1'
        self.fill_zero = True
        self.df_log = None
        self.sig = []
        self.fig = plt.figure(figsize=(26, 26))

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
        """
        :return: test result
        """
        lines = self.tc_head_body.splitlines(True)[1:]
        py_lines, self.df_tc = self.fill_variables(df=self.df_tc, py_code=self._fill_header(lines), rate=self.rate, time_type=self.time_type, judge=self.judge, n_match=self.n_match, fill_zero=self.fill_zero)
        if self.df_tc is not None:
            self.num_lines = len(self.df_tc)
        data = {}
        exec(py_lines, data)  # python TestCase Function 실행
        self.df_log = data['df_log']
        self.sig = data['dev_all_sigs']
        csv_res_file = os.path.join(self.py_output_path, f'{self.py_title}.csv')  # 생성된 결과 파일
        return self._check_tc_pass_state(tc_res_file=csv_res_file)

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

    def _export_test_sum(self, start_time: float, res: str):
        """
        :param start_time:
        :param res: test result
        """
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
        make_meas_HTML(df_sum=df_tc_sum, project='RGW', tc_script=self.df_tc, tc_in_out=self.in_out_sigs, export_path=self.py_output_path)  # 최종 결과물 HTML로 산출

    def step_graph(self, step_debug: bool = True):
        self.fig.clf()  # figure 초기화
        self.fig.set_size_inches(26, 26)

        plt.rcParams['axes.xmargin'] = 0

        df = self.df_log.copy()
        df.set_index('Elapsed_Time', drop=True, inplace=True)
        data_col = df.columns
        # Step Column 제거
        step_dict = {}
        if data_col[0] == 'Step':
            for step, group in df.groupby('Step'):
                time_sec = group.index.to_numpy()  # 스텝 별 시간 데이터
                step_dict[step] = (time_sec[0], time_sec[-1])

            df.drop(labels='Step', axis=1, inplace=True)
            data_col = data_col[1:]

        if self.fill_zero is True:
            df.fillna(0, inplace=True)  # replace None with zero

        # 그래프 코드
        fig = plt.figure(figsize=(26, 26))
        axs = fig.add_gridspec(len(data_col), hspace=0.1).subplots(sharex=True, sharey=False)

        for i, signal in enumerate(data_col):
            sig_color_idx = i % 20
            sig_name = data_col[i].replace('In: ', '').replace('Out: ', '')
            df_signal = df[[signal]].dropna(axis=0)
            x_data = df_signal.index.to_numpy()
            y_data = df_signal.to_numpy()

            axs[i].step(x_data, y_data, 'o-', markersize=2, label=sig_name, c=plt.cm.tab20(sig_color_idx), where='post',
                        linewidth=1.0)

            if y_data.size == 0:
                yticks_val = range(0, 2)
            else:
                min_y = int(min(y_data))
                max_y = int(max(y_data))
                if max_y == 0:
                    yticks_val = range(min_y, max_y + 2)
                else:
                    if max_y > 8:
                        yticks_val = list(range(min_y, max_y, int(max_y / 7)))
                        yticks_val[-1] = max_y
                    else:
                        yticks_val = range(min_y, max_y + 1)
            axs[i].set_yticks(yticks_val)
            yticks_labels = []
            for y_val in yticks_val:
                if (sig_name == self.sig[i][-1]) and (self.sig[i][0] != 'T32') and (self.sig[i][0] != 'LIN'):
                    if (sig_name in canBus.devs[self.sig[i][0]].sig_val) and (
                            y_val in canBus.devs[self.sig[i][0]].sig_val[sig_name]):
                        yticks_labels.append(canBus.devs[self.sig[i][0]].sig_val[sig_name][y_val])
                    else:
                        yticks_labels.append(f'{y_val}')
                else:
                    yticks_labels.append(f'{y_val}')
            axs[i].set_yticklabels(yticks_labels, fontsize=6)

            if step_debug is True:
                step_location = []
                for idx, step_time in enumerate(step_dict.values()):
                    color_idx = idx % 20
                    axs[i].axvspan(step_time[0], step_time[1], alpha=0.1, color=plt.cm.tab20(color_idx))
                    step_location.append(np.mean(step_time))

                if i == 0:
                    ax_twin = axs[i].twiny()
                    ax_twin.set_xlim(axs[i].get_xlim())
                    ax_twin.set_xticks(np.array(step_location))
                    ax_twin.set_xticklabels(step_dict.keys())
                    ax_twin.set_xlabel('Step')

            if i == len(data_col) - 1:
                axs[i].set_xlabel('Time[sec]')

        # Hide x labels and tick labels for all but bottom plot
        for ax in axs:
            ax.legend(loc='upper right', fontsize=7)
            # ax.label_outer()

        cursor(hover=True, highlight=False)
