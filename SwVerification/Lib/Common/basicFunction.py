from logging.config import dictConfig
import logging
import pandas as pd
import pygetwindow as gw
import os  # module for paths and directories
import csv
import configparser
import struct


class SysConfig:
    def __init__(self, path):
        self.path = path
        self.set = configparser.ConfigParser()
        self.set.read(self.path, encoding='utf-8')

    def update(self):
        self.set.read(self.path, encoding='utf-8')


Configure = SysConfig(path='./data/config/config_sys.ini')  # Configuration 전역변수 선언


def to_raw(string: str):
    return r'{}'.format(string)


def to_hex_str(integerVariable: int):
    strHex = "0x%0.2X" % integerVariable
    return strHex


def float_to_hex(f: float):
    '''
    :param f: float input value
    :return: hex str
    '''
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])


def hex_to_float(h: str):
    '''
    :param h: hex str
    :return: float value
    '''
    return struct.unpack('<f', struct.pack('i', int(h, 16)))[0]


def to_hex_little_lst(in_val):
    str_val = in_val if isinstance(in_val, str) else str(in_val)
    if '.' in str_val:
        str_val = str(float_to_hex(float(str_val)))
    hex_str = to_hex_str(int(str_val, 0)).replace('0x', '')
    if (len(hex_str) % 2) != 0:
        hex_str = '0' + hex_str
    return list(bytes.fromhex(hex_str))[::-1]


def bytearray_to_hex(arr):
    return '0x' + ''.join('{:02x}'.format(x) for x in arr)


def isdir_and_make(dir_name: str):
    if not (os.path.isdir(dir_name)):
        os.mkdir(dir_name)
        print("Success: Create {}\n".format(dir_name))
    else:
        print("Success: Access {}\n".format(dir_name))


def check_process_open(keyword: str):
    to_do_process = gw.getWindowsWithTitle(keyword)
    # print(to_do_process)
    num_of_process = len(to_do_process)
    if num_of_process == 0:
        return False
    else:
        return True


def to_do_process_close(keyword: str):
    to_do_process = gw.getWindowsWithTitle(keyword)
    num_of_process = len(to_do_process)
    if num_of_process == 0:
        pass
    else:
        for i in range(num_of_process):
            to_do_process[i].close()


def isfile_and_pass(file_path: str, file_name: str):
    if not os.path.isfile(file_path + '\\' + file_name):
        print("Error: Access {}\n".format(file_name))
        pass
    else:
        print("Success: Access {}\n".format(file_name))


def isfile_and_remove(file: str):
    if not os.path.isfile(file):
        pass
    else:
        os.remove(file)


def open_path(path: str):
    path = os.path.realpath(path)
    os.startfile(path)
    print("Success: Open {}\n".format(path))


def load_csv_dataframe(file_path: str, filename: str):
    df = pd.read_csv(file_path + "\\" + filename + ".csv", dtype=object, encoding='cp1252')
    return df


def export_csv_dataframe(df, file_path: str, filename: str):
    df.to_csv(file_path + "\\" + filename + ".csv", index=False)


def load_csv_list(file_path: str):
    csv_lst = []
    with open(file_path, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            csv_lst.append(row)
    return csv_lst


def export_csv_list(file_path: str, filename: str, lists: list):
    with open(file_path + "\\" + filename + ".csv", 'w', newline='', encoding='utf-8') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerows(lists)


def update_script_py(py_path: str, output_path: str, title: str):
    new_lines = []
    with open(to_raw(py_path), "r+", encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if "OUTPUT_PATH = " in line:
                line = "OUTPUT_PATH = " + "r'{}'".format(output_path) + '\n'
            if 'title = [' in line:
                line = "title = [" + "r'{}'".format(title) + "]" + '\n'
            new_lines.append(line)
    new_line = ''.join(new_lines)
    return new_line


def check_same_value(var, value):
    ret = False
    if type(var) == type(value):
        check_available = True
    elif isinstance(var, (int, float)) and isinstance(value, (int, float)):
        check_available = True
    else:
        try:
            var = float(var)
            value = float(value)
            check_available = True
        except ValueError:
            print("Error: Data Type is NOT Compatible")
            check_available = False

    if check_available is True:
        if var == value:
            ret = True
    return ret


def check_value_in_margin(var, value, percentage: float):
    ret = False
    if abs(float(value) * (1 - percentage)) <= abs(float(var)) <= abs(float(value) * (1 + percentage)):
        ret = True
    return ret


def check_value_in_margin_value(input, expected_result, margin):
    ret = False
    if (expected_result - margin) <= float(input) <= (expected_result + margin):
        ret = True
    return ret


def column_naming(data):
    temp = pd.DataFrame(data)
    col_len = len(temp.columns)
    col_name = ['ret', 'Test_Result']

    if col_len == 2:
        ret = pd.DataFrame(data, columns=col_name)
    else:
        add_col = ['var' + str(i + 1) for i in range(col_len - 2)]
        col_name += add_col
        ret = pd.DataFrame(data, columns=col_name)
    return ret


def data_mean_std_min_max(data):
    mean = data.mean()
    std = data.std()
    minvalue = data.min()
    maxvalue = data.max()
    return mean, std, minvalue, maxvalue


def data_col_mean_std_min_max(data, col_name):
    mean = data[col_name].mean()
    std = data[col_name].std()
    minvalue = data[col_name].min()
    maxvalue = data[col_name].max()
    return mean, std, minvalue, maxvalue


def get_sqrt(df, col1, col2):
    return (df[col1] ** 2 + df[col2] ** 2) ** (1 / 2)


def get_window_with_loop(title, cnt_limit):
    cnt = 0
    win_temp = None
    while cnt < cnt_limit:
        titles = gw.getAllTitles()
        win_list = [ti for ti in titles if title in ti]
        if len(win_list) != 0:
            win_temp = gw.getWindowsWithTitle(win_list[0])[0]
            logging_print("Success: Get WINDOW {}\n".format(title))
            break
        cnt += 1
    return win_temp


def logging_initialize():
    if os.path.isfile("./data/result/Debug.log"):
        os.remove("./data/result/Debug.log")
    else:
        pass

    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(message)s',
            },
            'simple': {
                'format': '%(message)s',
            }
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "simple",
            },

            "info_file_handler": {
                "class": "logging.FileHandler",
                "level": "INFO",
                "formatter": "default",
                "encoding": "utf-8",
                "filename": "./data/result/Debug.log"
            }
        },

        'root': {
            'level': 'INFO',
            'handlers': ["console", "info_file_handler"]
        }
    })


def logging_print(text):
    logging.info(text)
# This is a new line that ends the file
