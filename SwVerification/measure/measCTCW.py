import datetime
from threading import Thread

from Lib.Inst.visaLib import *
from Lib.Inst.telnetLib import *
from Lib.Inst.canLib import *


class MeasCTCW:
    def __init__(self):
        super().__init__()
        self.testEnv = None
        self.meas_input = []
        self.start_time = None

        self.sample_rate = 0.01
        self.can_val = ''
        self.can_col = []

        self.time = datetime.datetime.now()
        self.data = []

        self.meas_state = False
        self.log_state = False
        self.log_lst = []
        self.is_stop_btn = False

        # Measure Data THREAD 설정
        self.meas_th = Thread(target=self.meas_thread)
        self.meas_th.daemon = True
        self.meas_th.start()

    def load_script(self, testEnv):
        self.testEnv = testEnv
        logging_print("Load Test Environment:\n{}".format(self.testEnv))

    def stop(self):
        self.meas_state = False
        self.save_data()
        time.sleep(1)

    def start(self):
        self.log_lst = []  # 로그 변수 초기화
        self.start_time = datetime.datetime.now()  # 측정 시작 시간 저장

        # Command Line 수행
        for i in range(len(self.testEnv)):
            executeTime = self.testEnv.loc[i, 'Time[sec]']
            executeTime = 0.0 if executeTime is None else float(executeTime)
            start = time.time_ns()
            elapse_time = 0.0

            self.run_cmd_process(i)
            # 기록된 수행시간이 만족될때까지 준비
            while executeTime > elapse_time:
                elapse_time = (time.time_ns() - start) * 0.000000001
                time.sleep(0.005)
        self.stop()

    def save_data(self):
        data_col = ['Time', 'Elapsed Time', 'Servo_Val', 'CAN_Val', 'dc_current', 'dc_voltage', 'current_p1',
                    'current_p2', 'current_p3']
        df_log = pd.DataFrame(self.log_lst, columns=data_col + self.can_col)
        export_csv_dataframe(df_log, './data/result', 'result_{}'.format(datetime.datetime.now().strftime("%Y%m%d_%H%M%S")))
        print("Success: Save Result Data\n")

    def run_cmd_process(self, index):
        cmd = self.testEnv.loc[index, 'CMD']
        """
        시퀀스에 따라 동작하는 함수
        """
        if cmd == 'MEASURE_START':
            self.log_state = True
        elif cmd == 'MEASURE_END':
            self.log_state = False
        elif cmd == 'READY':
            self.meas_state = True
        elif cmd == 'WAIT':
            pass
        elif cmd == 'GET_DATA':
            elapse_time = (self.time - self.start_time).total_seconds()
            self.meas_input = [self.servo_val, self.can_val]
            self.log_lst.append([self.time.strftime('%Y-%m-%d %H:%M:%S'), round(elapse_time, 2)] + self.meas_input + self.data)
            self.can_val = ''
        elif cmd == 'CAN_WRITE':
            if canBus.status != CAN_ERR:
                self.can_val = self.testEnv.loc[index, 'CAN_Val']
                CAN_Input = self.can_val.split(',')
                canBus.msg_write(CAN_Input[0].strip(), CAN_Input[1].strip(), float(CAN_Input[2].strip()),
                                 float(CAN_Input[3].strip()))
        elif cmd == 'CAN_WRITE_P':
            if canBus.status != CAN_ERR:
                self.can_val = self.testEnv.loc[index, 'CAN_Val'].split(',')
                CAN_Input = self.can_val.split(',')
                canBus.msg_period_write(CAN_Input[0].strip(), CAN_Input[1].strip(), float(CAN_Input[2].strip()),
                                        float(CAN_Input[3].strip()))
        elif cmd == 'SAMPLE_RATE':
            self.sample_rate = float(self.testEnv.loc[index, 'Env_Val'])

    def meas_thread(self):
        while True:
            if self.meas_state is True:
                # 변수 선언 및 초기화
                # From CAN
                can_0x14A = None  # OPU CAN msg
                can_0x14A_values = []

                if canBus.status != CAN_ERR:
                    can_0x14A = canBus.msg_read_id(can_id=0x14A)
                    can_0x14A_values = list(can_0x14A.values())
                    if not self.can_col:
                        self.can_col = list(can_0x14A.keys())

                self.time = datetime.datetime.now()
                self.data = can_0x14A_values

                if self.log_state:
                    elapse_time = (self.time - self.start_time).total_seconds()
                    self.meas_input = [self.servo_val, self.can_val]
                    self.log_lst.append([self.time.strftime('%Y-%m-%d %H:%M:%S'), round(elapse_time, 3)] + self.meas_input + self.data)
                    self.can_val = ''
            time.sleep(self.sample_rate)
