import os
import csv
import pickle


def save_pkl_list(file_path: str, data: list):
    with open(file_path, 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


def load_csv_list(file_path: str) -> list:
    """
    :param file_path: file path to load
    :return: csv list
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            csv_lst = list(reader)
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='cp949') as f:
            reader = csv.reader(f)
            csv_lst = list(reader)
    return csv_lst


path = '../data/input/script'


for dir_path, dir_names, filenames in os.walk(path):
    for file in filenames:
        if '.csv' in file and 'Measure' not in dir_path:
            data = load_csv_list(os.path.join(dir_path, file))
            save_pkl_list(os.path.join(dir_path, file.replace('.csv', '.pkl')), data)
