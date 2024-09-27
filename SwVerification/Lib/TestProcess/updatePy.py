from itertools import groupby
import os
import pandas as pd
import numpy as np
from Lib.Inst import canBus
from Lib.Common import load_csv_list, to_raw, find_str_inx, load_pkl_list


MASK_FIRST_BIT = 1
MASK_SECOND_BIT = 2
T32_USE_ALL_lINE = 3


class UpdatePy:
    tc_head_body = """
# USE DB INTERFACE
import pandas as pd
import numpy as np
from threading import Thread
from tqdm import tqdm
import time
from Lib.Common import export_csv_list, to_hex_big_lst
from Lib.Inst import canBus, t32
from Lib.DataProcess import signal_step_graph, judge_final_result, find_out_signals_for_col


OUTPUT_PATH = ''
title = []
outcome = [title]

# Data Begin
# Data End

# Dev signal List Begin
# Dev signal List End

out_col, lst_t32_out = find_out_signals_for_col(dev_out_sigs)
total_col = ['Step', 'Elapsed_Time'] + [f'In: {sig[2]}' for sig in dev_in_sigs] + out_col
outcome.append(total_col)

# LogThread Begin
# LogThread End

# TC main Begin
# TC main End
"""

    log_thread_body = """
class LogThread(Thread):
    def __init__(self, can_bus):
        super().__init__()
        self.can = can_bus
        self.in_data = [None for _ in range({len_in})]
        self.log_state = False
        self.log_lst = []
        self.step = 0
        self.sample_rate = {sample_rate}
        self.start_test = time.time()

    def run(self):
        while True:
            if self.log_state:
                out_data = []
{read_msg}
                elapsed = round((time.time() - self.start_test), 2)
                self.log_lst.append([self.step, elapsed] + self.in_data + out_data)
            time.sleep(self.sample_rate)
"""

    tc_main_body = """
# Initialize all variables
canBus.stop_all_period_msg()

t32.rx.vars = lst_t32_out  # define T32 rx variable

t32.re_init()
time.sleep(0.5)

# Measure Data Thread 설정
log_th = LogThread(can_bus=canBus)
log_th.start()
log_th.log_state = True  # log start

start_time = log_th.start_test
elapsed_time = 0
for i in tqdm(input_data,
              total=len(input_data),  # 전체 진행수
              desc='Running',  # 진행률 앞쪽 출력 문장
              ncols=100,  # 진행률 출력 폭 조절
              leave=True,  # True 반복문 완료시 진행률 출력 남김. False 남기지 않음.
              colour='green'  # Bar 색
              ):
    # T32 Stop if use
    if i[2] == 255:
        log_th.step = int(i[0])
        i[2] = None
        log_th.in_data = i[2:]

        canBus.stop_all_period_msg()
        t32.re_init()
    elif i[2] == 254:
        log_th.step = int(i[0])
        i[2] = None
        log_th.in_data = i[2:]

        canBus.stop_all_period_msg()
    elif i[2] == 253:
        log_th.step = int(i[0])
        i[2] = None
        log_th.in_data = i[2:]

        canBus.stop_all_period_msg()
        t32.flash_binary(run_cmd=Configure.set['TRACE32']['flash_all_cmm'])
    else:
{write_msg}

    # T32 Resume if use
    log_th.step = int(i[0])
    log_th.in_data = i[2:]

    time.sleep(i[1])

log_th.log_state = False  # log stop

for log_lst in log_th.log_lst:
    outcome.append(log_lst)

df_log = pd.DataFrame(np.array(log_th.log_lst, dtype=np.float32), columns=total_col)
signal_step_graph(df=df_log.copy(), sigs=dev_all_sigs, x_col='Elapsed_Time', filepath=OUTPUT_PATH, filename=title[0], fill_zero=True)

# Result judgement logic
JUDGE_TYPE = "same"  # define type to judge data
NUM_OF_MATCH = 0  # define criteria for matching rows
outcome = judge_final_result(df_result=df_log[['Step'] + out_col], expected_outs=expected_data, num_match=NUM_OF_MATCH, meas_log=outcome.copy(), out_col=out_col, judge=JUDGE_TYPE)

export_csv_list(OUTPUT_PATH, title[0], outcome)
"""

    def __init__(self):
        self.py_path = ''
        self.py_title = ''
        self.py_sub_title = ''
        self.py_output_path = ''
        self.db_interface = False
        self.in_out_sigs = []

    def update_py(self) -> (str, pd.DataFrame):
        codes = self._parse_script_py()
        df_tc_raw = None
        if self.db_interface is True:
            lst_df = load_csv_list(file_path=self.py_path.replace('.py', '.csv'))
            self.py_sub_title = lst_df[0][1]  # 기존 csv파일 이름 제외 별도 이름
            # lst_df = load_pkl_list(file_path=self.py_path.replace('.py', '.pkl'))
            codes, df_tc_raw = self.fill_variables(df=pd.DataFrame(lst_df[7:], columns=lst_df[6]), py_code=codes, rate=lst_df[1][1], time_type=lst_df[2][1], judge=lst_df[3][1], n_match=lst_df[4][1])
        else:
            self.py_sub_title = os.path.basename(self.py_path).replace('.py', '')
        return codes, df_tc_raw

    def fill_variables(self, df: pd.DataFrame, py_code: str, rate: str, time_type: str, judge: str, n_match: str, fill_zero: bool = True) -> (str, pd.DataFrame):
        df_tc = df.drop(['Scenario'], axis=1).apply(pd.to_numeric) if 'Scenario' in df.columns else df.apply(pd.to_numeric)
        in_col, out_col, inputs, outputs, total, t32_usage = self._get_msg_in_out(cols=df_tc.columns)
        self.in_out_sigs = [in_col[2:], out_col[1:]]
        in_data = str(df_tc[in_col].to_numpy().tolist()).replace('nan', 'None')
        out_data = str(df_tc[out_col].to_numpy().tolist()).replace('nan', 'None')
        lst_condition = [['# Data Begin', '# Data End', f'input_data = {in_data}\nexpected_data = {out_data}'],
                         ['# Dev signal List Begin', '# Dev signal List End',
                          f'dev_in_sigs = {str(inputs)}\ndev_out_sigs = {str(outputs)}\ndev_all_sigs = {str(total)}'],
                         ['# LogThread Begin', '# LogThread End',
                          self.log_thread_body.format(len_in=len(in_col) - 2, sample_rate=rate, read_msg=self._get_msg_read(outputs))]]
        if '# Dev Input Begin' in py_code:
            lst_condition.append(['# Dev Input Begin', '# Dev Input End', self._get_msg_write(inputs)])
        else:
            lst_condition.append(['# TC main Begin', '# TC main End', self.tc_main_body.format(write_msg=self._get_msg_write_frame(inputs))])

        py_code = self._apply_db_to_code(lines=py_code, conditions=lst_condition)

        if 'Total' in time_type:
            py_code = py_code.replace('time.sleep(i[1])',
                                      'while elapsed_time < i[1]:  # Timeout\n         elapsed_time = time.time() - start_time  # Total Time 방식')  # Total time 방식 적용

        if t32_usage == T32_USE_ALL_lINE:
            py_code = py_code.replace('# T32 Stop if use', 't32.rx.stop_log()\n    time.sleep(0.003)')  # t32 logging stop
            py_code = py_code.replace('# T32 Resume if use', 't32.rx.resume()')  # t32 logging resume

        if fill_zero is False:
            py_code = py_code.replace('fill_zero=True', 'fill_zero=False')  # No Fill Zero 적용
        py_code = py_code.replace('JUDGE_TYPE = "same"', f'JUDGE_TYPE = "{judge}"')  # judge type 적용
        py_code = py_code.replace('NUM_OF_MATCH = 0', f'NUM_OF_MATCH = {n_match}')  # match 갯수 적용
        df = df.replace('254', 'CAN Stop').replace('255', 'Reset')
        return py_code, df

    def _parse_script_py(self) -> str:
        self.db_interface = False
        if os.path.isfile(self.py_path) is True:
            with open(to_raw(self.py_path), "r+", encoding='utf-8') as file:
                lines = file.readlines()
        else:
            lines = self.tc_head_body.splitlines(True)[1:]

        if '# USE DB INTERFACE' in lines[0]:
            self.db_interface = True

        return self._fill_header(lines)

    def _apply_db_to_code(self, lines: str, conditions: list) -> str:
        for str_con in conditions:
            if str_con[0] in lines:
                s_inx, e_inx = find_str_inx(lines, start_str=str_con[0], end_str=str_con[1])
                lines = lines.replace(lines[s_inx:e_inx], str_con[2])
        return lines

    def _fill_header(self, lines: list) -> str:
        new_lines = []
        for line in lines:
            if "OUTPUT_PATH = " in line:
                line = f"OUTPUT_PATH = r'{self.py_output_path}'\n"
            elif 'title = [' in line:
                line = f"title = [r'{self.py_title}']\n"
            new_lines.append(line)
        return ''.join(new_lines)

    def _get_msg_write(self, lst_input: list) -> str:
        lst_line = []
        idx = 2
        for str_in in lst_input:
            if str_in[0] != 'LIN' and str_in[0] != 'T32':  # Only for CAN message
                if 'Event' in str_in[4]:
                    if 'Extended' in str_in[3]:
                        line = f"        canBus.devs['{str_in[0]}'].msg_write('{str_in[1]}', '{str_in[2]}', i[{idx}], {str_in[-1]}, is_extended=True)"
                    else:
                        line = f"        canBus.devs['{str_in[0]}'].msg_write('{str_in[1]}', '{str_in[2]}', i[{idx}], {str_in[-1]})"
                else:
                    if 'Extended' in str_in[3]:
                        line = f"        canBus.devs['{str_in[0]}'].msg_period_write('{str_in[1]}', '{str_in[2]}', i[{idx}], {str_in[-1]}, is_extended=True)"
                    else:
                        line = f"        canBus.devs['{str_in[0]}'].msg_period_write('{str_in[1]}', '{str_in[2]}', i[{idx}], {str_in[-1]})"
            else:
                line = f"        t32.write_symbol(symbol='{str_in[-1]}', value=i[{idx}])"
            lst_line.append(line)
            idx += 1
        return '\n'.join(lst_line)

    def _get_msg_write_frame(self, lst_input: list) -> str:
        lst_line = []
        idx = 2

        sorted_sigs = (list(sig) for grp, sig in groupby(lst_input, lambda x: x[1]))
        for str_in in sorted_sigs:
            sig = []
            val = []
            for lst_in in str_in:
                sig.append(lst_in[2])
                val.append(f"i[{idx}]")
                idx += 1

            if str_in[0][0] != 'LIN' and str_in[0][0] != 'T32':  # Only for CAN message
                if 'Event' in str_in[0][4]:
                    if 'Extended' in str_in[0][3]:
                        line = f'''        canBus.devs['{str_in[0][0]}'].msg_write_by_frame('{str_in[0][1]}', {str(sig)}, {str(val).replace("'", "")}, {str_in[0][-1]}, is_extended=True)'''
                    else:
                        line = f'''        canBus.devs['{str_in[0][0]}'].msg_write_by_frame('{str_in[0][1]}', {str(sig)}, {str(val).replace("'", "")}, {str_in[0][-1]})'''
                else:
                    if 'Extended' in str_in[3]:
                        line = f'''        canBus.devs['{str_in[0][0]}'].msg_period_write_by_frame('{str_in[0][1]}', {str(sig)}, {str(val).replace("'", "")}, {str_in[0][-1]}, is_extended=True)'''
                    else:
                        line = f'''        canBus.devs['{str_in[0][0]}'].msg_period_write_by_frame('{str_in[0][1]}', {str(sig)}, {str(val).replace("'", "")}, {str_in[0][-1]})'''
            else:
                line = f"        t32.write_symbol(symbol='{str_in[0][-1]}', value=i[{idx-1}])"
            lst_line.append(line)
        return '\n'.join(lst_line)

    def _get_msg_in_out(self, cols: np.array) -> (list, list, list, list, list, int):
        col_in = cols[:2].tolist()  # Step, Time
        col_out = cols[:1].tolist()  # Step
        lst_in = []
        lst_out = []
        t32_usage = 0  # Not Used
        for col in cols[2:]:  # Signals except step,time
            temp = [t.strip() for t in col.split(', ')]  # get dev, signal
            if '[OUT]' in temp[0]:  # In case of Output
                col_out.append(col)  # Insert Output variable
                temp[0] = temp[0].replace('[OUT]', '')
                if temp[0] != 'T32':  # Only for CAN message
                    temp.append('Period')  # Default periodic message
                    for i in temp[1].split('_'):
                        if 'ms' in i:
                            if int(i.replace('ms', '')) <= 0:
                                temp[-1] = 'Event'
                else:  # In case of Trace32
                    temp = [temp[0], '', temp[-1]]  # Index 2를 변수로 설정 - Dev, '', symbol
                    t32_usage |= MASK_FIRST_BIT
                lst_out.append(temp)
            else:  # In case of Input
                col_in.append(col)  # Insert Input variable
                if temp[0] != 'LIN' and temp[0] != 'T32':  # Only for CAN message
                    id = canBus.devs[temp[0]].get_msg_id(temp[1])  # get the id to find whether it is extended or not
                    if id > 0xFFFF:
                        temp.append('Extended')
                    else:
                        temp.append('Normal')

                    if '_E_' in temp[1]:
                        temp += ['Event', '0.2']
                    else:
                        for i in temp[1].split('_'):
                            if 'ms' in i:
                                if int(i.replace('ms', '')) <= 0:
                                    temp += ['Event', '0.2']
                                else:
                                    temp += ['Period', str(float(i.replace('ms', '')) / 1000)]
                else:  # In Case of Trace32
                    t32_usage |= MASK_SECOND_BIT
                lst_in.append(temp)
        lst_total = [msg[:3] for msg in lst_in + lst_out]  # combine all msg
        return col_in, col_out, lst_in, lst_out, lst_total, t32_usage

    def _get_msg_read(self, lst_output: list) -> str:
        idx = 0
        lst_line = []
        used_lines = {}
        for str_out in lst_output:
            if 'T32' in str_out[0]:
                line = f"                out_data.append(t32.get_symbol_data(sym='{str_out[-1]}'))"  # int형 return값 받기
            else:
                if 'Event' in str_out[-1]:
                    dev_line = f"self.can.devs['{str_out[0]}'].msg_read_event('{str_out[1]}', decode_on=False)"
                else:
                    dev_line = f"self.can.devs['{str_out[0]}'].msg_read_name('{str_out[1]}', decode_on=False)"

                if dev_line in used_lines:
                    msg_var = used_lines[dev_line]
                    line = f"                out_data.append({msg_var}['{str_out[2]}'] if {msg_var} else None)"
                else:
                    msg_var = f'msg_{idx}'
                    used_lines[dev_line] = msg_var
                    idx += 1
                    if 'Event' in str_out[-1]:
                        line = (
                            f"                {msg_var} = self.can.devs['{str_out[0]}'].msg_read_event('{str_out[1]}', decode_on=False)\n"
                            f"                out_data.append({msg_var}['{str_out[2]}'] if {msg_var} else None)")
                    else:
                        line = (
                            f"                {msg_var} = self.can.devs['{str_out[0]}'].msg_read_name('{str_out[1]}', decode_on=False)\n"
                            f"                out_data.append({msg_var}['{str_out[2]}'] if {msg_var} else None)")

            lst_line.append(line)
        return '\n'.join(lst_line)
