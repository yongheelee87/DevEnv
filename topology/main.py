import sys
from Lib.DataProcess.topopt_SOMP import *


if __name__ == "__main__":
    logging_initialize()
    somp = SOMP()

    print('[INFO]\n#1.Mode: Topology Optimization\n#2.Mode: Modify plt pause time\n#Else. System Exit\n')

    mode = input('Please Press the Mode to Execute (모드 입력): ')

    while mode != '99':
        if mode == '1':
            str_params = input('Enter Parameters (nelx nely volfrac penal rmin ft): ').strip().split()
            somp.update_params(str_params)
            somp.start()

        elif mode == '2':
            str_time = input('Enter plt pause time (그림 생성 딜레이 시간): ').strip()
            somp.plt_pause = float(str_time)
            logging_print("Success: plt pause time is modified to {}\n".format(somp.plt_pause))
        else:
            logging_print('EXIT: Topology Optimization\n')
            sys.exit(0)

        mode = input('Please Press the Mode to Execute (모드 입력): ')
