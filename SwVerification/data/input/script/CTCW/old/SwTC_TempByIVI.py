# USE DB INTERFACE
from threading import Thread
import time
from Lib.Inst import *


OUTPUT_PATH = ''
title = []
outcome = [title]

# Data Begin
input_data = []
expected_data = []
# Data End

# Dev signal List Begin
dev_in_sigs = []
dev_out_sigs = []
# Dev signal List End

out_col, lst_t32_out = find_out_signals_for_col(dev_out_sigs)
total_col = ['Step', 'Elapsed_Time'] + [f'In: {sig[2]}' for sig in dev_in_sigs] + out_col
outcome.append(total_col)

final_result = 'Pass'  # Final result to be recorded


# LogThread Begin
class LogThread(Thread):
    def __init__(self, can_bus):
        super().__init__()
        self.can = can_bus
        self.log_lst = []
# LogThread End


# Initialize all variables
canBus.stop_all_period_msg()
t32.re_init()
time.sleep(0.5)

if lst_t32_out:   # T32 Output 있다면
    t32.rx.vars = lst_t32_out  # define T32 rx variable

canBus.devs['HS-RGW_T1'].msg_period_write('CC_01_200ms', 'CC_ACSetSta', 1, 0.2)  # 냉동기 작동
canBus.devs['FD_C'].msg_write('CCU_CCS_01_00ms', 'SetCargoWrngValue', 3, 0.2)  # NVM 초기화 값
time.sleep(1)

# Measure Data Thread 설정
log_th = LogThread(can_bus=canBus)
log_th.start()
log_th.log_state = True  # log start

for i in input_data:
    if i[2] != 255:
# Dev Input Begin
        print("Please enter Input Variables")
# Dev Input End
    else:
        canBus.stop_all_period_msg()
        i[2] = None
        log_th.in_data = i[2:]
        t32.re_init()
        canBus.devs['HS-RGW_T1'].msg_period_write('CC_01_200ms', 'CC_ACSetSta', 1, 0.2)  # 냉동기 작동
        time.sleep(1)

    log_th.step = int(i[0])
    log_th.in_data = i[2:]

    time.sleep(i[1])

log_th.log_state = False  # log stop

for log_lst in log_th.log_lst:
    outcome.append(log_lst)

df_log = pd.DataFrame(np.array(log_th.log_lst, dtype=np.float32), columns=total_col)
signal_step_graph(df=df_log.copy(), x_col='Elapsed_Time', filepath=OUTPUT_PATH, filename=title[0])

# Result judgement logic
JUDGE_TYPE = "same"  # define type to judge data
NUM_OF_MATCH = 0  # define criteria for matching rows
outcome = judge_final_result(df_result=df_log[['Step'] + out_col], expected_outs=expected_data, num_match=NUM_OF_MATCH, meas_log=outcome.copy(), out_col=out_col, judge=JUDGE_TYPE)

export_csv_list(OUTPUT_PATH, title[0], outcome)
