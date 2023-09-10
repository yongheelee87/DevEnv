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
            if self.config['TRACE32']['auto_start'] == 'True':
                self.open_exe(t32api_path=self.config['TRACE32']['api_path'])  # T32 exe 실행

            self.connect_dev()  # 연결

            if self.config['TRACE32']['auto_start'] == 'True':
                self.cd_do(self.config['TRACE32']['window_cmm'])

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
            logging_print('[INFO] TRACE32 is NOT CONNECTED with HOST\nIF YOU WANT TO USE TRACE32, CHECK IF TRACE32 POWERVIEW IS OPENED AND RETRY THE CONNECTION\n')

    def open_exe(self, t32api_path: str):
        '''
        :param t32api_path: Paths currently installed
        '''
        t32api_path_lst = t32api_path.split(os.path.sep)
        t32_exe = os.path.join('C:' + os.sep, t32api_path_lst[1], 'bin', 'windows64', 't32mppc.exe')
        config_file = os.path.join('C:' + os.sep, t32api_path_lst[1], 'config.t32')
        command = [t32_exe, '-c', config_file]
        if not check_process_open('TRACE32 PowerView'):
            subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            # Wait until the TRACE32 instance is started
            time.sleep(3)
        logging_print('Success: OPEN Trace32\n')

    def cmd(self, str_cmd: str, time_out: int = 2):
        '''
        :param str_cmd: refer to Trace32 general_ref.pdf
        :param time_out: integer number of time out
        '''
        try:
            self.device.cmd(str_cmd)
            self._wait_until_command_ends(timeout=time_out)
        except CommandError:
            print('Error: Run Cmd {}\n'.format(str_cmd))

    def cd_do(self, run_cmd: str):
        '''
        :param run_cmd: commands including path
        '''
        if os.path.exists(run_cmd):
            self.cmd("CD.DO " + run_cmd)
        else:
            print('Error: No file {}\n'.format(run_cmd))

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

    def reset(self):
        self.cmd('System.ResetTarget')

    def reset_go(self):
        self.cmd('System.ResetTarget')
        start = time.time_ns()
        elapse_time = 0
        while elapse_time < 5:  # 5초 초과시
            self.cmd('Go')
            if self._get_state() == RUNNING:
                break
            elapse_time = int((time.time_ns() - start) * 0.000000001)

    def _get_state(self):
        return int.from_bytes(self.device.get_state(), "big")

    def _wait_until_command_ends(self, timeout: int):
        start = time.time_ns()
        elapse_time = 0
        while elapse_time < timeout:  # Timeout
            rc = self.device.library.t32_getpracticestate()  # _get_practice_state()
            if rc == 0: break
            elapse_time = int((time.time_ns() - start) * 0.000000001)

    def get_break_lst(self):
        return [self.device.symbol.query_by_address(address=i.address).name for i in self.device.breakpoint.list()]

    def set_break(self, name):
        return self.device.breakpoint.set(address=self.device.symbol.query_by_name(name=name).address)

    def delete_break(self, name):
        return self.device.breakpoint.delete(address=self.device.symbol.query_by_name(name=name).address)

    def disable_break(self, name):
        return self.device.breakpoint.disable(address=self.device.symbol.query_by_name(name=name).address)

    def enable_break(self, name):
        return self.device.breakpoint.enable(address=self.device.symbol.query_by_name(name=name).address)


t32 = Trace32(config_sys=Configure.set)  # TRACE32 연결; 전역 변수로 사용
# This is a new line that ends the file
