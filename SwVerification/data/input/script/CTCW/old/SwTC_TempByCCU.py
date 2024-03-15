from threading import Thread
import time

from Lib.Inst import *
from Lib.Common import *

OUTPUT_PATH = ''

title = ['SwTC_101']
outcome = [title]

input_data = [[1, 3, 3, i, None, None, 1] for i in range(5, 31)]  # Set temp
dev_in_sigs = [['HS-RGW_T1', 'CC_01_200ms', 'ACSetSta', 0.2],
               ['HS-RGW_T1', 'CC_01_200ms', 'ACSetTemp', 0.2],
               ['HS-RGW_T1', 'CC_01_200ms', 'ACCurtemp_1', 0.2],
               ['HS_M', 'CCU_CCS_01_00ms_2', 'SetCargoWrngValue', 0.5],
               ['HS_M', 'IVI_USM_E_01', 'IVI_ACTempWrngValCtrl', 0.5],
               ['HS_M', 'IVI_USM_E_01', 'IVI_ACUSMReset', 0.5]]
dev_out_sigs = [['HS_M', 'PBVDC_04_200ms_1', 'ACTempWrngSta'],
               ['HS_M', 'PBVDC_04_200ms_1', 'ACTempWrngVal']]

in_col = [f'In: {sig[2]}' for sig in dev_in_sigs]
out_col = [f'Out: {sig[2]}' for sig in dev_out_sigs]
data_col = in_col + out_col
total_col = ['Elapsed_Time'] + data_col
outcome.append(total_col)

final_result = 'Pass'


class LogThread(Thread):
    def __init__(self, can_bus):
        super().__init__()
        self.can = can_bus
        self.in_data = [None for _ in range(6)]
        self.log_state = False
        self.log_lst = []
        self.sample_rate = 0.01
        self.start_test = time.time()

    def run(self):
        while True:
            if self.log_state:
                can_out = self.can.devs['HS_M'].msg_read_name('PBVDC_04_200ms_1', decode_on=False)
                if can_out:
                    wrngSta = can_out['ACTempWrngSta']
                    wrngVal = can_out['ACTempWrngVal']
                else:
                    wrngSta = None
                    wrngVal = None
                elapsed = round((time.time() - self.start_test), 2)
                self.log_lst.append([elapsed] + self.in_data + [wrngSta, wrngVal])
            time.sleep(self.sample_rate)


canBus.stop_all_period_msg()
t32.reset_go()
time.sleep(0.5)

# 초기화
canBus.devs['HS-RGW_T1'].msg_period_write('CC_01_200ms', 'ACSetSta', 1, 0.2)  # 냉동기 작동
canBus.devs['HS_M'].msg_write('CCU_CCS_01_00ms_2', 'SetCargoWrngValue', 3, 0.5, True)  # NVM 초기화 값
time.sleep(1)

# Measure Data Thread 설정
log_th = LogThread(can_bus=canBus)
log_th.start()
log_th.log_state = True

for i in input_data:
    if i[0] != 255:
        canBus.devs['HS-RGW_T1'].msg_period_write('CC_01_200ms', 'ACSetSta', i[0], 0.2)
        canBus.devs['HS-RGW_T1'].msg_period_write('CC_01_200ms', 'ACSetTemp', i[1], 0.2)
        canBus.devs['HS-RGW_T1'].msg_period_write('CC_01_200ms', 'ACCurtemp_1', i[2], 0.2)
        canBus.devs['HS_M'].msg_write('CCU_CCS_01_00ms_2', 'SetCargoWrngValue', i[3], 0.5, True)
        canBus.devs['HS_M'].msg_write('IVI_USM_E_01', 'IVI_ACTempWrngValCtrl', i[4], 0.5, True)
        canBus.devs['HS_M'].msg_write('IVI_USM_E_01', 'IVI_ACUSMReset', i[5], 0.5, True)
    else:
        canBus.stop_all_period_msg()
        log_th.in_data = [None for _ in range(6)]
        t32.reset_go()
        canBus.devs['HS-RGW_T1'].msg_period_write('CC_01_200ms', 'ACSetSta', 1, 0.2)  # 냉동기 작동
        time.sleep(4)
        i[0] = None

    log_th.in_data = i[:6]

    time.sleep(i[-1])

log_th.log_state = False

for log_lst in log_th.log_lst:
    outcome.append(log_lst)

signal_step_graph(data=log_th.log_lst, col=total_col, x_col='Elapsed_Time', filepath=OUTPUT_PATH, filename=title[0])

outcome.append(['Result', final_result])

export_csv_list(OUTPUT_PATH, title[0], outcome)
