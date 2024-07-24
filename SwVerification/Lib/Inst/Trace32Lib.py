import os
import time  # time module
from threading import Thread
import lauterbach.trace32.rcl as trace32
from lauterbach.trace32.rcl import CommandError
from Lib.Common import check_task_open

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

        if 'TRACE32' in self.config:
            self.connect_dev()  # 연결 시도
            if self.config['TRACE32']['auto_open'] is True:  # Auto Start 설정시
                if check_task_open(name="t32mppc.exe") is False:  # Trace32 Process 현재 작동 되지 않을 경우
                    self.open_exe()  # T32 exe 실행
                    '''
                    SubProcess에서 이전 작업으로 Trace32가 작동되어 있을 경우 Trace32 already is occupied by other GUI
                    config.t32에서 CONNECTIONMODE=AUTOCONNECT 설정 확인 후 CPU상태에 따라 4~7초의 Auto Connection 시간 필요
                    '''
                    self.wait_until_connect(timeout=12)  # Auto copnnectin 7초를 넘는 충분한 시간 할당
                    
            # Measure Data Thread 설정
            self.rx = T32RXThread(dev=self.device)  # TRACE32 RX 시그널 Thread 설정
            self.rx.start()  # TRACE32 RX 시그널 THREAD 동작

    def connect_dev(self):
        """
        Connect Device based on configuration written in config.t32 file
        """
        try:
            self.device = trace32.connect(node='localhost', port=20001, protocol="TCP", packlen=1024, timeout=10.0)
            self.status = True
        except ConnectionRefusedError:
            self.status = False
            print('Error: TRACE32 CONNECTION\nCHECK IF TRACE32 POWERVIEW IS OPENED AND RETRY THE CONNECTION\n')

    def check_status(self):
        if self.status:
            print('Success: TRACE32 CONNECTION\n')
        else:
            print('[INFO] TRACE32 is NOT CONNECTED with HOST\nIF YOU WANT TO USE TRACE32, CHECK IF TRACE32 POWERVIEW IS OPENED AND RETRY THE CONNECTION\n')

    def open_exe(self):
        t32_exe = os.path.join(self.config['TRACE32']['api_path'], 'bin', 'windows64', 't32mppc.exe')
        os.startfile(t32_exe)
        # Wait until the TRACE32 instance is started
        time.sleep(3)
        print('Success: OPEN Trace32\n')

    def flash_binary(self, run_cmd):
        if os.path.exists(run_cmd.split()[0]):
            try:
                self.device.cmd(f"CD.DO {run_cmd}")
                print(f'Flash: CD.DO {run_cmd}')
            except:
                self.wait_until_connect(timeout=10)
                self.device.cmd(f"CD.DO {run_cmd}")
        else:
            print(f'Error: No file {run_cmd}\n')

        start = time.time()
        elapse_time = 0
        ready_cnt = 0
        while elapse_time < 10:  # 10초 초과시
            if self._get_state() == SYSTEM_READY:
                ready_cnt += 1
                if ready_cnt >= 10:
                    break
            elapse_time = time.time() - start
            time.sleep(0.5)
        self.cmd('Go')

    def wait_until_connect(self, timeout: int):
        """
        :param timeout: integer number of time out
        """
        start = time.time()
        elapsed_time = 0
        while elapsed_time < timeout:  # Timeout
            self.connect_dev()  # 연결
            if self.status is True:
                break
            elapsed_time = time.time() - start

    def cmd(self, str_cmd: str, time_out: int = 10):
        """
        :param str_cmd: refer to Trace32 general_ref.pdf
        :param time_out: integer number of time out
        """
        try:
            self.device.cmd(str_cmd)
            self._wait_until_command_ends(timeout=time_out)
        except CommandError:
            print(f'Error: Run Cmd {str_cmd}\n')

    def cd_do(self, run_cmd: str):
        """
        :param run_cmd: commands including path
        """
        if os.path.exists(run_cmd.split()[0]):
            self.cmd(f"CD.DO {run_cmd}")
        else:
            print(f'Error: No file {run_cmd}\n')

    def write_symbol(self, symbol: str, value: int or float):
        """
        :param symbol: variable name loaded by elf
        :param value: input value
        """
        if value is not None:
            self.device.variable.write(symbol, value)

    def read_symbol(self, symbol: str):
        """
        :param symbol: variable name loaded by elf
        :return: only value, not array and structure
        """
        variable = self.device.variable.read(symbol)
        return str(variable.value)

    def read_symbol_arr(self, symbol: str):
        """
        return raw value with structure and array
        :param symbol: variable name loaded by elf
        :return: raw value with structure and array
        """
        return self.device.library.t32_readvariablestring(symbol)[:-1]

    def reset(self):
        self.cmd('System.ResetTarget')

    def reset_go(self):
        self.cmd('System.ResetTarget')
        start = time.time()
        elapse_time = 0
        while elapse_time < 5:  # 5초 초과시
            self.cmd('Go')
            if self._get_state() == RUNNING:
                break
            elapse_time = time.time() - start

    def _wait_until_command_ends(self, timeout: int):
        start = time.time()
        elapse_time = 0
        while elapse_time < timeout:  # Timeout
            rc = self.device.library.t32_getpracticestate()  # _get_practice_state()
            if rc == 0: break
            elapse_time = time.time() - start

    def _get_state(self):
        return int.from_bytes(self.device.get_state(), "big")

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

    def msg_init(self):
        self.rx.msg_dict.clear()  # 메세지 초기화

    def get_symbol_data(self, sym: str) -> int:
        """
        :param sym: symbol variable
        :return: t32 symbol data from dict
        """
        ret_data = None
        if sym in self.rx.msg_dict:  # 데이터 저장이 되어 있을 경우
            ret_data = int(self.rx.msg_dict[sym])
        return ret_data

    def re_init(self):
        self.rx.stop_log()
        time.sleep(0.5)
        self.reset_go()
        self.rx.msg_dict = {}  # 메세지 초기화
        self.rx.resume()


class T32RXThread(Thread):
    """ T32RXThread(parent: Thread) """

    def __init__(self, dev):
        super().__init__()
        self.dev = dev
        self.vars = []
        self.update_flag = False
        self.msg_dict = {}

    def run(self):
        while True:
            if self.update_flag is True:
                for var in self.vars:  # for문이 비워 있을때는 실행 안함
                    try:
                        self.msg_dict[var] = self.dev.variable.read(var).value
                    except ConnectionError:
                        pass
            time.sleep(0.0008)

    def stop_log(self):
        self.update_flag = False

    def resume(self):
        self.update_flag = True

# This is a new line that ends the file
