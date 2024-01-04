import os.path

from Lib.Inst import *
from Lib.Common.basicFunction import *

tc_head_body = """
# USE CSV INTERFACE
from threading import Thread
import time
from Lib.Inst import *


OUTPUT_PATH = ''
title = []
outcome = [title]

# Data Begin
# Data End

# Dev signal List Begin
# Dev signal List End

out_col, lst_t32_out = find_out_signals_for_col(dev_out_sigs)
total_col = ['Step', 'Elapsed_Time'] + ['In: {}'.format(sig[2]) for sig in dev_in_sigs] + out_col
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

for i in input_data:
    if i[2] != 255:
{write_msg}
    else:
        canBus.stop_all_period_msg()
        i[2] = None
        log_th.in_data = i[2:]
        t32.re_init()
        time.sleep(1)

    log_th.step = int(i[0])
    log_th.in_data = i[2:]

    time.sleep(i[1])

log_th.log_state = False  # log stop

for log_lst in log_th.log_lst:
    outcome.append(log_lst)

df_log = pd.DataFrame(log_th.log_lst, columns=total_col)
signal_step_graph(df=df_log.copy(), x_col='Elapsed_Time', filepath=OUTPUT_PATH, filename=title[0])

# Result judgement logic
NUM_OF_MATCH = 0  # define criteria for matching rows
outcome = judge_final_result(df_result=df_log[['Step'] + out_col], expected_outs=expected_data, num_match=NUM_OF_MATCH, meas_log=outcome.copy(), out_col=out_col)

export_csv_list(OUTPUT_PATH, title[0], outcome)
"""


def update_py(py_path: str, output_path: str, title: str) -> (str, pd.DataFrame):
    codes, use_csv = parse_script_py(py_path, output_path, title)
    df_tc_raw = None
    if use_csv is True:
        lst_df = load_csv_list(file_path=py_path.replace('.py', '.csv'))
        sample_rate = lst_df[0][1]
        num_match = lst_df[1][1]
        df_tc_raw = pd.DataFrame(lst_df[4:], columns=lst_df[3])
        df_tc = df_tc_raw.drop(['Scenario'], axis=1).apply(pd.to_numeric)
        in_col, out_col, inputs, outputs = _get_msg_in_out(df=df_tc)
        in_data = str(df_tc[in_col].values.tolist()).replace('nan', 'None')
        out_data = str(df_tc[out_col].values.tolist()).replace('nan', 'None')
        lst_condition = [['# Data Begin', '# Data End', 'input_data = {}\nexpected_data = {}'.format(in_data, out_data)],
                         ['# Dev signal List Begin', '# Dev signal List End', 'dev_in_sigs = {}\ndev_out_sigs = {}'.format(str(inputs), str(outputs))],
                         ['# LogThread Begin', '# LogThread End', log_thread_body.format(len_in=len(in_col) - 2, sample_rate=sample_rate, read_msg=_get_msg_read(outputs))],
                         ['# Dev Input Begin', '# Dev Input End', _get_msg_write(inputs)],
                         ['# TC main Begin', '# TC main End', tc_main_body.format(write_msg=_get_msg_write(inputs))]]

        for con in lst_condition:
            codes = apply_csv_code(lines=codes, s_str=con[0], e_str=con[1], new_str=con[2])
        codes = codes.replace('NUM_OF_MATCH = 0', 'NUM_OF_MATCH = {}'.format(num_match))  # match 갯수 적용
        df_tc_raw.replace('', 'None').replace('255', 'Reset')
    return codes, df_tc_raw


def parse_script_py(py_path: str, output_path: str, title: str) -> (str, str):
    new_lines = []
    csv_interface = False
    if os.path.isfile(py_path) is True:
        with open(to_raw(py_path), "r+", encoding='utf-8') as file:
            lines = file.readlines()
    else:
        lines = tc_head_body.splitlines(True)[1:]

    if '# USE CSV INTERFACE' in lines[0]:
        csv_interface = True

    for line in lines:
        if "OUTPUT_PATH = " in line:
            line = "OUTPUT_PATH = " + "r'{}'".format(output_path) + '\n'
        if 'title = [' in line:
            line = "title = [" + "r'{}'".format(title) + "]" + '\n'
        new_lines.append(line)
    new_line = ''.join(new_lines)
    return new_line, csv_interface


def apply_csv_code(lines: str, s_str: str, e_str: str, new_str: str) -> str:
    if s_str in lines:
        s_inx, e_inx = find_str_inx(lines, start_str=s_str, end_str=e_str)
        lines = lines.replace(lines[s_inx:e_inx], new_str)
    return lines


def _get_msg_write(lst_input: list) -> str:
    lst_line = []
    idx = 2
    for str_in in lst_input:
        if str_in[0] != 'LIN' and str_in[0] != 'T32':  # Only for CAN message
            if 'Event' in str_in[4]:
                if 'Extended' in str_in[3]:
                    line = "        canBus.devs['{}'].msg_write('{}', '{}', i[{}], {}, is_extended=True)".format(str_in[0], str_in[1], str_in[2], idx, str_in[-1])
                else:
                    line = "        canBus.devs['{}'].msg_write('{}', '{}', i[{}], {})".format(str_in[0], str_in[1], str_in[2], idx, str_in[-1])
            else:
                if 'Extended' in str_in[3]:
                    line = "        canBus.devs['{}'].msg_period_write('{}', '{}', i[{}], {}, is_extended=True)".format(str_in[0], str_in[1], str_in[2], idx, str_in[-1])
                else:
                    line = "        canBus.devs['{}'].msg_period_write('{}', '{}', i[{}], {})".format(str_in[0], str_in[1], str_in[2], idx, str_in[-1])
        else:
            line = "        t32.write_symbol(symbol='{}', value=i[{}])".format(str_in[-1], idx)
        lst_line.append(line)
        idx += 1
    return '\n'.join(lst_line)


def _get_msg_in_out(df: pd.DataFrame) -> (list, list, list, list):
    cols = df.columns.tolist()
    col_in = cols[:2]  # Step, Time
    col_out = cols[:1]  # Step
    lst_in = []
    lst_out = []
    for col in cols[2:]:
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
            lst_in.append(temp)
    return col_in, col_out, lst_in, lst_out


def _get_msg_read(lst_output: list) -> str:
    idx = 0
    lst_line = []
    used_lines = {}
    for str_out in lst_output:
        if 'T32' in str_out[0]:
            line = "                out_data.append(t32.get_symbol_data(sym='{var}'))".format(var=str_out[-1])  # int형 return값 받기
        else:
            if 'Event' in str_out[-1]:
                dev_line = "self.can.devs['{dev}'].msg_read_event('{frame}', decode_on=False)".format(dev=str_out[0], frame=str_out[1])
            else:
                dev_line = "self.can.devs['{dev}'].msg_read_name('{frame}', decode_on=False)".format(dev=str_out[0], frame=str_out[1])

            used = False
            for used_line in used_lines.keys():
                if used_line == dev_line:
                    used = True

            if used is False:
                msg_var = 'msg_{}'.format(idx)
                used_lines[dev_line] = msg_var
                idx += 1
                if 'Event' in str_out[-1]:
                    line = (
                        "                {var} = self.can.devs['{dev}'].msg_read_event('{frame}', decode_on=False)\n"
                        "                out_data.append({var}['{sig}'] if {var} else None)").format(var=msg_var, dev=str_out[0], frame=str_out[1], sig=str_out[2])
                else:
                    line = ("                {var} = self.can.devs['{dev}'].msg_read_name('{frame}', decode_on=False)\n"
                            "                out_data.append({var}['{sig}'] if {var} else None)").format(var=msg_var, dev=str_out[0], frame=str_out[1], sig=str_out[2])
            else:
                msg_var = used_lines[dev_line]
                line = "                out_data.append({var}['{sig}'] if {var} else None)".format(var=msg_var, dev=str_out[0], frame=str_out[1], sig=str_out[2])

        lst_line.append(line)
    return '\n'.join(lst_line)
