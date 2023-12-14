# ///////////////////////////////////////////////////////////////
#
# BY: YONGHEE LEE
# PROJECT MADE WITH: measurement with script command
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# ///////////////////////////////////////////////////////////////
import pandas as pd

# basic library
from . canLib import *
from . Trace32Lib import *
# from . visaLib import *
# from . xcpLib import *
# from . telnetLib import *
# from . serialLib import *

canBus = CANBus(config_sys=Configure.set)  # CAN BUS 연결; 전역 변수로 사용
t32 = Trace32(config_sys=Configure.set)  # TRACE32 연결; 전역 변수로 사용


def get_inst_status() -> pd.DataFrame:
    lst_inst_data = []
    lst_inst = [i for i in Configure.set.keys() if 'system' not in i and 'XCP' not in i]
    for inst in lst_inst:
        if Configure.set[inst]['type'] == 'T32':
            lst_inst_data.append([inst, t32.status])
        elif Configure.set[inst]['type'] == 'can':
            lst_inst_data.append([inst, False if canBus.devs[inst].status == CAN_ERR else True])
        else:
            lst_inst_data.append([inst, visa.status[inst]])
    return pd.DataFrame(lst_inst_data, columns=['Name', 'Connect'])