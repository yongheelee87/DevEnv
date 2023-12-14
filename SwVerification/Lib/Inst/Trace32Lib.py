import os
import subprocess  # module to create an additional process
import time  # time module
import lauterbach.trace32.rcl as trace32
from lauterbach.trace32.rcl import CommandError
from Lib.Common import *

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

        if 'TRACE32' in self.config.keys():
            self.connect_dev()  # 연결 시도
            if self.config['TRACE32']['auto_start'] is True:  # Auto Start 설정시
                if check_task_open(name="t32mppc.exe") is False:  # Trace32 Process 현재 작동 되지 않을 경우
                    self.open_exe(t32api_path=self.config['TRACE32']['api_path'])  # T32 exe 실행
                    '''
                    SubProcess에서 이전 작업으로 Trace32가 작동되어 있을 경우 Trace32 already is occupied by other GUI
                    config.t32에서 CONNECTIONMODE=AUTOCONNECT 설정 확인 후 CPU상태에 따라 4~7초의 Auto Connection 시간 필요
                    '''
                    self.wait_until_connect(timeout=12)

    def connect_dev(self):
        '''
        Connect Device based on configuration written in config.t32 file
        '''
        try:
            self.device = trace32.connect(node='localhost', port=20001, protocol="TCP", packlen=1024, timeout=10.0)
            self.status = True
            print('Success: TRACE32 CONNECTION\n')
        except ConnectionRefusedError:
            self.status = False
            print('Error: TRACE32 CONNECTION\nCHECK IF TRACE32 POWERVIEW IS OPENED AND RETRY THE CONNECTION\n')

    def check_status(self):
        if self.status:
            print('Success: TRACE32 CONNECTION\n')
        else:
            print('[INFO] TRACE32 is NOT CONNECTED with HOST\nIF YOU WANT TO USE TRACE32, CHECK IF TRACE32 POWERVIEW IS OPENED AND RETRY THE CONNECTION\n')

    def open_exe(self, t32api_path: str):
        '''
        :param t32api_path: Paths currently installed
        '''
        t32_exe = os.path.join(t32api_path, 'bin', 'windows64', 't32mppc.exe')
        os.startfile(t32_exe)
        # Wait until the TRACE32 instance is started
        time.sleep(3)
        print('Success: OPEN Trace32\n')

    def flash_binary(self):
        self.cd_do(self.config['TRACE32']['flash_cmm'])
        time.sleep(2)
        self.cmd('Go')
        time.sleep(3)

    def wait_until_connect(self, timeout: int):
        start = time.time_ns()
        elapsed_time = 0
        while elapsed_time < timeout:  # Timeout
            self.connect_dev()  # 연결
            if self.status is True:
                break
            elapsed_time = int((time.time_ns() - start) * 0.000000001)

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
        if os.path.exists(run_cmd.split()[0]):
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


# This is a new line that ends the file
