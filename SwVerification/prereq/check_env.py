import os
from Lib.Common import isdir_and_make, Configure
from Lib.Inst import t32, get_inst_status


class CheckEnv:
    def __init__(self):
        self.inst_status = get_inst_status()['Connect'].to_numpy().tolist()
        self.path = Configure.set['system']['archive_path']
        self.file = os.path.join(self.path, 'env_available.txt')
        if os.path.isfile(self.file):  # 시작전 파일이 있다면 삭제
            os.remove(self.file)

    def run(self):
        print("************************************************************")
        print("*** Check Environment for Test")
        print("************************************************************\n")

        false_cnt = self.inst_status.count('Not Connected')
        if false_cnt == 0:
            isdir_and_make(self.path)
            with open(self.file, "w") as f:
                f.write('PASS')
            t32.flash_binary(run_cmd=Configure.set['TRACE32']['flash_cmm'])  # 새로 flash
        else:
            print("Error: Device Connect is not completed. Please check the connection with devices")
            # 에러로 인한 프로그램 종료
            os._exit(0)
