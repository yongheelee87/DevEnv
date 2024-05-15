import os
from ctypes import *  # module for C data types
import enum  # module for C data types
import subprocess  # module to create an additional process
import time  # time module
from Lib.Common import check_process_open

# file path
t32api_path = ''
t32api = cdll.LoadLibrary(t32api_path)

T32_DEV = 1
OK = 0
NOT_OK = 1


class InterpreterState(enum.IntEnum):
    UNKNOWN = -1
    NOT_RUNNING = 0
    RUNNING = 1


def t32_open_exe():
    t32api_path_lst = t32api_path.split(os.path.sep)
    t32_exe = os.path.join('C:' + os.sep, t32api_path_lst[1], 'bin', 'windows64', 't32mtc.exe')
    config_file = os.path.join('C:' + os.sep, t32api_path_lst[1], 'config.t32')
    command = [t32_exe, '-c', config_file]
    if not check_process_open('TRACE32 PowerView'):
        subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        # Wait until the TRACE32 instance is started
        time.sleep(3)
    # Configure communication channel
    t32api.T32_Config(b"PORT=", b"20001")
    t32api.T32_Config(b"PACKLEN=", b"1024")
    # Establish communication channel
    # rc = t32api.T32_Cmd(b"SYStem.Mode.Attach")
    if t32api.T32_Init() == OK:
        t32api.T32_Attach(T32_DEV)
        print('Success: Trace32 Init\n')
    else:
        print("ERR: Trace32 NOT Init\n")
        t32api.T32_Exit()
    print('Success: OPEN Trace32\n')


def t32_initialization():
    t32api.T32_Config(b"PORT=", b"20001")
    t32api.T32_Config(b"PACKLEN=", b"1024")
    ret = NOT_OK
    if t32api.T32_Init() == OK:
        t32api.T32_Attach(T32_DEV)
        ret = OK
    return ret


def t32_run_cmd(run_cmd):
    cmd_in = f"CD.DO {run_cmd}"
    if t32_initialization() == OK:
        t32api.T32_Cmd(cmd_in.encode())
        wait_until_command_ends()
        print(f'Success: Run Cmd {run_cmd}\n')
    else:
        t32api.T32_Stop()
        print(f'ERR: Run Cmd {run_cmd}\n')


def t32_go():
    if t32_initialization() == OK:
        t32api.T32_Cmd(b'Go')
        wait_until_command_ends()
        time.sleep(2)
        print('Success: Trace32 Go\n')
    else:
        t32api.T32_Stop()
        print('ERR: Trace32 NOT Go\n')


def t32_break():
    if t32_initialization() == OK:
        t32api.T32_Cmd(b'Break')
        wait_until_command_ends()
        print('Success: Trace32 Break\n')
    else:
        t32api.T32_Stop()
        print('ERR: Trace32 NOT Break\n')


def t32_exit():
    t32api.T32_Stop()
    wait_until_command_ends()
    ret = t32api.T32_Exit()
    if ret == 0:
        time.sleep(0.5)
        print('Success: Trace32 Connection End\n')
    else:
        time.sleep(0.5)
        print("ERR: Trace32 Connection NOT End\n")


def t32_reset():
    if t32_initialization() == OK:
        t32api.T32_Cmd(b'System.ResetTarget')
        wait_until_command_ends()
        print('Success: Trace32 Reset\n')
    else:
        t32api.T32_Stop()
        print('ERR: Trace32 NOT Reset\n')


def t32_reset_go():
    if t32_initialization() == OK:
        t32api.T32_Cmd(b'System.ResetTarget')
        wait_until_command_ends()
        time.sleep(0.2)
        t32api.T32_Cmd(b'Go')
        time.sleep(0.2)
        print('Success: Trace32 Reset_GO\n')
    else:
        t32api.T32_Stop()
        print('ERR: Trace32 NOT Reset_GO\n')


def t32_attach():
    if t32_initialization() == OK:
        t32api.T32_Cmd(b'SYStem.Mode.Attach')
        wait_until_command_ends()
        print('Success: Trace32 Attach\n')
    else:
        t32api.T32_Stop()
        print('ERR: Trace32 NOT Attach\n')


def t32_no_debug():
    if t32_initialization() == OK:
        t32api.T32_Cmd(b'SYStem.Mode.NoDebug')
        wait_until_command_ends()
        print('Success: Trace32 NoDebug\n')
    else:
        t32api.T32_Stop()
        print('ERR: Trace32 NOT NoDebug\n')


def wait_until_command_ends():
    state = c_int(InterpreterState.UNKNOWN)
    rc = 0
    while rc == 0 and not state.value == InterpreterState.NOT_RUNNING:
        rc = t32api.T32_GetPracticeState(byref(state))


def write_value_via_cmd(symbol, value):
    command_in = f"v.set.{str(symbol)}={str(value)}"
    if t32api.T32_Attach(T32_DEV) == OK:
        t32api.T32_Cmd(command_in.encode())
        wait_until_command_ends()


def read_value_string_via_symbol_name(symbol):
    message_ret = create_string_buffer(128)
    if t32api.T32_Attach(T32_DEV) == OK:
        t32api.T32_ReadVariableString(symbol.encode(), message_ret, 128)
        wait_until_command_ends()
    return message_ret.value.decode()
# This is a new line that ends the file
