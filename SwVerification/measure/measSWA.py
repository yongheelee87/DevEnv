import datetime

from Lib.Inst.visaLib import *
from Lib.Inst.telnetLib import *
from Lib.Inst import *


class MeasSWA:
    def __init__(self):
        super().__init__()
        self.testEnv = None
        self.meas_input = []
        self.start_time = None

        self.env_servo = 'RPM'
        self.env_osc = 'MAX'
        self.sample_rate = 0.01
        self.servo_val = ''
        self.can_val = ''
        self.can_col = []

        self.osc_state = False
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
        print("Load Test Environment:\n{}".format(self.testEnv))

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
        export_csv_dataframe(df_log, './data/result',
                             'result_{}'.format(datetime.datetime.now().strftime("%Y%m%d_%H%M%S")))
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
        elif cmd == 'ENV_SERVO':
            if telnet.status is True:
                self.env_servo = self.testEnv.loc[index, 'Env_Val']
                telnet.set_servo_mode(self.env_servo)
        elif cmd == 'ENV_OSC':
            self.env_osc = self.testEnv.loc[index, 'Env_Val']
        elif cmd == 'SET_SERVO':
            if telnet.status is True:
                if telnet.servo_ready is False:
                    telnet.servo_ready = True
                    telnet.enable_servo(True)
                if self.env_servo == 'RPM':
                    telnet.set_servo_speed(int(self.testEnv.loc[index, 'Servo_Val']))
                else:
                    telnet.set_servo_torque(float(self.testEnv.loc[index, 'Servo_Val']))
            self.servo_val = int(self.testEnv.loc[index, 'Servo_Val'])
        elif cmd == 'STOP_SERVO':
            if telnet.status is True:
                if self.env_servo == 'RPM':
                    telnet.set_servo_speed(0)
                else:
                    telnet.set_servo_torque(0)
            self.servo_val = 0
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
        elif cmd == 'POWER_ON':
            if visa.status['POWER'] is True:
                visa.output('POWER', self.testEnv.loc[index, 'Env_Val'].strip())
        elif cmd == 'SET_POWER':
            if visa.status['POWER'] is True:
                Power_Input = self.testEnv.loc[index, 'Power_Val'].split(',')
                visa.set_volt_curr(Power_Input[0].strip(), Power_Input[1].strip())
        elif cmd == 'SAMPLE_RATE':
            self.sample_rate = float(self.testEnv.loc[index, 'Env_Val'])

    def meas_thread(self):
        while True:
            if self.meas_state is True:
                # 변수 선언 및 초기화
                # From CAN
                can_0x14A = None  # OPU CAN msg
                can_0x14A_values = []

                # From Oscilloscope
                current_p1 = 0
                current_p2 = 0
                current_p3 = 0

                # From Power Supply
                dc_voltage = None
                dc_current = None

                if canBus.status != CAN_ERR:
                    can_0x14A = canBus.msg_read_id(can_id=0x14A)
                    can_0x14A_values = list(can_0x14A.values())
                    if not self.can_col:
                        self.can_col = list(can_0x14A.keys())

                if self.osc_state:
                    if self.env_osc == 'MAX':
                        current_p1 = visa.read('OSCILLOSCOPE', "C1:PAVA? MAX")
                        current_p2 = visa.read('OSCILLOSCOPE', "C2:PAVA? MAX")
                        current_p3 = visa.read('OSCILLOSCOPE', "C3:PAVA? MAX")
                    elif self.env_osc == 'RMS':
                        current_p1 = visa.read('OSCILLOSCOPE', "C1:PAVA? RMS")
                        current_p2 = visa.read('OSCILLOSCOPE', "C2:PAVA? RMS")
                        current_p3 = visa.read('OSCILLOSCOPE', "C3:PAVA? RMS")

                    if current_p1 != 'Error - timeout':
                        # TBD
                        # 장비마다 output 형식이 다를 수 있어 코딩 필요 여부
                        # or 몇 번째 ~ 몇 번째 지정하여 슬라이싱
                        # ~~~~ 30 ~~~
                        # 30 ~~~~~~~~
                        # start: 0
                        # end: 2 + 1
                        # 단위: ma or A -> scale
                        current_p1 = float(current_p1.split(',')[-2].split()[0]) * 1000
                        current_p2 = float(current_p2.split(',')[-2].split()[0]) * 1000
                        current_p3 = float(current_p3.split(',')[-2].split()[0]) * 1000

                if visa.status['POWER'] is True:
                    dc_voltage, dc_current = visa.meas_volt_curr('POWER')

                self.time = datetime.datetime.now()
                self.data = [dc_current, dc_voltage, current_p1, current_p2, current_p3] + can_0x14A_values

                if self.log_state:
                    elapse_time = (self.time - self.start_time).total_seconds()
                    self.meas_input = [self.servo_val, self.can_val]
                    self.log_lst.append(
                        [self.time.strftime('%Y-%m-%d %H:%M:%S'), round(elapse_time, 3)] + self.meas_input + self.data)
                    self.can_val = ''
            time.sleep(self.sample_rate)
