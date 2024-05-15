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
import numpy as np
import pandas as pd
from Lib.Common import Configure

# basic library
from . canLib import CANBus
from . trace32Lib import Trace32
# from . visaLib import *
# from . xcpLib import *
# from . telnetLib import *
# from . serialLib import *

canBus = CANBus(config_sys=Configure.set)  # CAN BUS 연결; 전역 변수로 사용
t32 = Trace32(config_sys=Configure.set)  # TRACE32 연결; 전역 변수로 사용

'''
visa = VisaDev(config_sys=Configure.set)  # ViSA 연결; 전역 변수로 사용
telnet = TelnetClient(config_sys=Configure.set)  # Telnet 연결; 전역 변수로 사용
'''


def get_inst_status() -> pd.DataFrame:
    lst_inst_data = []
    lst_inst = [i for i in Configure.set.keys() if 'system' not in i and 'XCP' not in i]
    for inst in lst_inst:
        if Configure.set[inst]['type'] == 'T32':
            lst_inst_data.append([inst, 'Not Connected' if t32.status is False else 'Connected'])
        elif Configure.set[inst]['type'] == 'can':
            lst_inst_data.append([inst, 'Not Connected' if canBus.devs[inst].status is False else 'Connected'])
        else:
            lst_inst_data.append([inst, 'Not Connected' if visa.status[inst] is False else 'Connected'])
    return pd.DataFrame(np.array(lst_inst_data, dtype=object), columns=['Name', 'Connect'])
