# USE CSV INTERFACE
from threading import Thread
import time
from Lib.Inst import *
from Lib.DataProcess import *

OUTPUT_PATH = ''
title = []
outcome = [title]

# Data Begin
input_data = []
expected_data = []
# Data End

# Dev signal List Begin
dev_in_sigs = []
dev_out_sigs = []
dev_all_sigs = []
# Dev signal List End

out_col, lst_t32_out = find_out_signals_for_col(dev_out_sigs)
total_col = ['Step', 'Elapsed_Time'] + [f'In: {sig[2]}' for sig in dev_in_sigs] + out_col
outcome.append(total_col)

final_result = 'Pass'  # Final result to be recorded


# LogThread Begin
class LogThread(Thread):
    def __init__(self, can_bus):
        super().__init__()
        self.can = can_bus
        self.log_lst = []
# LogThread End

# TC main Begin
# TC main End
