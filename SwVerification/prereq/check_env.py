import sys
import os
import shutil
from Lib.Inst import *


class CheckEnv:
    def __init__(self):
        self.inst_status = get_inst_status()['Connect'].values.tolist()
        self.path = Configure.set['system']['archive_path']
        self.file = os.path.join(self.path, 'env_available.txt')
        if os.path.isfile(self.file):  # 시작전 파일이 있다면 삭제
            os.remove(self.file)

    def run(self):
        print("************************************************************")
        print("*** Check Environment for Test")
        print("************************************************************\n")

        false_cnt = self.inst_status.count(False)
        if false_cnt == 0:
            isdir_and_make(self.path)
            with open(self.file, "w") as f:
                f.write('PASS')
            t32.flash_binary()  # 새로 flash