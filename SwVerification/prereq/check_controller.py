import sys
import os
import shutil
from Lib.Inst import *

if __name__ == "__main__":
    inst_status = get_inst_status()['Connect'].values.tolist()
    false_cnt = inst_status.count(False)
    path = Configure.set['system']['archive_path']
    file = os.path.join(path, 'env_available.txt')
    if os.path.isfile(file):  # 시작전 파일이 있다면 삭제
        os.remove(file)

    if false_cnt == 0:
        isdir_and_make(path)
        with open(file, "w") as f:
            f.write('PASS')
        t32.flash_binary()  # Flash

    # 프로그램 동작이 끌날시 시스템 종료 코드
    os._exit(0)
