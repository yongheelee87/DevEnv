import os
import pandas as pd
from logging.config import dictConfig
import logging


def to_raw(str_input):
    return r'{}'.format(str_input)


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


def open_path(dir_path):
    if os.path.isdir(dir_path):
        path = os.path.realpath(dir_path)
        os.startfile(path)
        print("Success: Access {}\n".format(dir_path))
    else:
        print("Error: Access {}\n".format(dir_path))


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
