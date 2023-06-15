import os
import subprocess  # module to create an additional process
import time  # time module
import lauterbach.trace32.rcl as trace32
from lauterbach.trace32.rcl import CommandError
from Lib.Common.basicFunction import *

SYSTEM_DOWN = 0
SYSTEM_READY = 2
RUNNING = 3


class Trace32:
    """
    main Trace32 class for bus and debugging
    """

    def __init__(self, config_sys):
        self.config = config_sys  # Config 파일 Set

        self.device = None  # Trace device 선언
        self.status = False  # status 선언

        if 'TRACE32' in self.config.sections():
            self.connect_dev()  # 연결

    def connect_dev(self):
        '''
        Connect Device based on configuration written in config.t32 file
        '''
        try:
            self.device = trace32.connect(node='localhost', port=20001, protocol="TCP", packlen=1024, timeout=10.0)
            self.status = True
            logging_print('Success: TRACE32 CONNECTION\n')
        except ConnectionRefusedError:
            self.status = False
            logging_print('Error: TRACE32 CONNECTION\nCHECK IF TRACE32 POWERVIEW IS OPENED AND RETRY THE CONNECTION\n')

    def check_status(self):
        if self.status:
            logging_print('Success: TRACE32 CONNECTION\n')
        else:
            logging_print(
                '[INFO] TRACE32 is NOT CONNECTED with HOST\nIF YOU WANT TO USE TRACE32, CHECK IF TRACE32 POWERVIEW IS OPENED AND RETRY THE CONNECTION\n')

    # noinspection PyMethodMayBeStatic
    def open_exe(self, t32api_path: str):
        '''
        :param t32api_path: Paths currently installed
        '''
        t32api_path_lst = t32api_path.split(os.path.sep)
        t32_exe = os.path.join('C:' + os.sep, t32api_path_lst[1], 'bin', 'windows64', 't32mtc.exe')
        config_file = os.path.join('C:' + os.sep, t32api_path_lst[1], 'config.t32')
        command = [t32_exe, '-c', config_file]
        if not check_process_open('TRACE32 PowerView'):
            subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            # Wait until the TRACE32 instance is started
            time.sleep(3)
        logging_print('Success: OPEN Trace32\n')

    # noinspection PyMethodMayBeStatic
    def cmd(self, str_cmd: str):
        '''
        :param str_cmd: refer to Trace32 general_ref.pdf
        '''
        try:
            self.device.cmd(str_cmd)
        except CommandError:
            print('Error: Run Cmd {}\n'.format(str_cmd))

    # noinspection PyMethodMayBeStatic
    def cd_do(self, run_cmd: str):
        '''
        :param run_cmd: commands including path
        '''
        cmd_in = "CD.DO " + run_cmd
        self.device.cmd(cmd_in)
        start = time.time_ns()
        elapse_time = 0
        while elapse_time < 180:  # 180초 초과시
            prac_state = self.device._get_practice_state()
            if prac_state == 0:
                break
            elapse_time = int((time.time_ns() - start) * 0.000000001)

    # noinspection PyMethodMayBeStatic
    def cmm_do(self, cmm_file: str):
        '''
        :param cmm_file: cmm file to be executed
        '''
        # script 경로 고정 data/input/script
        self.cd_do(os.path.join(os.getcwd(), 'data/input/script/swTC/{}'.format(cmm_file)))

    def write_symbol(self, symbol: str, value: int or float):
        '''
        :param symbol: variable name loaded by elf
        :param value: input value
        '''
        self.device.variable.write(symbol, value)

    def read_symbol(self, symbol: str):
        '''
        :param symbol: variable name loaded by elf
        :return: only value, not array and structure
        '''
        variable = self.device.variable.read(symbol)
        return str(variable.value)

    def read_symbol_arr(self, symbol: str):
        '''
        return raw value with structure and array
        :param symbol: variable name loaded by elf
        :return: raw value with structure and array
        '''
        return self.device.library.t32_readvariablestring(symbol)[:-1]

    def reset_go(self):
        t32.cmd('System.ResetTarget')
        time.sleep(0.2)
        start = time.time_ns()
        elapse_time = 0
        while elapse_time < 5:  # 5초 초과시
            t32.cmd('Go')
            time.sleep(0.2)
            if self.get_state() == RUNNING:
                break
            elapse_time = int((time.time_ns() - start) * 0.000000001)

    def get_state(self):
        return int.from_bytes(self.device.get_state(), "big")


t32 = Trace32(config_sys=Configure.set)  # TRACE32 연결; 전역 변수로 사용
# This is a new line that ends the file
