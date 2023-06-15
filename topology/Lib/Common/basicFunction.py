import os
import subprocess as sp
import pandas as pd
import pygetwindow as gw
from logging.config import dictConfig
import logging


def to_raw(str_input):
    return r'{}'.format(str_input)


def run_command_os(file_path, cmd):
    current_path = os.getcwd()
    os.chdir(file_path)
    os.system(cmd)
    os.chdir(current_path)


def run_command_by_sp(file_path, command):
    current_path = os.getcwd()
    os.chdir(file_path)
    sp.call(command)
    os.chdir(current_path)


def load_csv_dataframe(filepath, filename):
    df = pd.read_csv(filepath + '\\' + filename + '.csv', dtype=object, encoding='utf-8')
    df = df.apply(pd.to_numeric)
    return df


def export_csv_dataframe(df, file_path: str, filename: str):
    df.to_csv(file_path + "\\" + filename + ".csv", index=False)


def isdir_and_make(dir_name):
    if not (os.path.isdir(dir_name)):
        os.mkdir(dir_name)
        print("Success: Create {}\n".format(dir_name))
    else:
        print("Success: Access {}\n".format(dir_name))


def to_do_process_close(keyword_str):
    to_do_process = gw.getWindowsWithTitle(keyword_str)
    num_of_process = len(to_do_process)
    if num_of_process == 0:
        pass
    else:
        for i in range(num_of_process):
            to_do_process[i].close()


def convert_list_str_py(list_str):
    str_list = '['
    for i in list_str:
        str_list += "'" + i + "'" + ', '
    str_list = str_list[:-2]
    str_list += ']'
    return str_list


def logging_initialize():
    if os. path.isfile("Debug.log"):
        os.remove("Debug.log")
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

        'handlers': {
            'console': {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "simple",
             },

            'file': {
                "class": "logging.FileHandler",
                "level": "INFO",
                "formatter": "default",
                "filename": "Debug.log"
            }
        },

        'root': {
            'level': 'INFO',
            'handlers': ["console", "file"]
        }
    })


def logging_print(text):
    logging.info(text)
