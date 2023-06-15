import os  # module for paths and directories
import shutil
from logging.config import dictConfig
import logging
import pandas as pd


def isdir_and_make(dir_name):
    if not (os.path.isdir(dir_name)):
        os.mkdir(dir_name)
        logging_print("Success: Create {}\n".format(dir_name))
    else:
        logging_print("Success: Access {}\n".format(dir_name))


def isfile_and_copy(update_file_path, file_path, file):
    if not (os.path.isfile(update_file_path + '\\' + file)):
        shutil.copy2(file_path + '\\' + file, update_file_path + '\\' + file)
        logging_print("Success: Create {}\n".format(file))
    else:
        logging_print("Success: Access {}\n".format(file))


def remove_data_in_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)  # 지정된 폴더와 하위 디렉토리 폴더, 파일를 모두 삭제
    os.mkdir(path)


def load_csv_dataframe(file_path, filename):
    df = pd.read_csv(file_path + "\\" + filename + ".csv", dtype=object, encoding='cp1252')
    return df


def export_csv_dataframe(df, file_path, filename):
    df.to_csv(file_path + "\\" + filename + ".csv", index=False)


def to_inch_pixel(pixel):
    return pixel * 0.0104166667


def logging_initialize():
    if os.path.isfile("Debug.log"):
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
                "filename": "Debug.log"
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
