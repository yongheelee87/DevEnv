import time
from Lib.Inst import *


OUTPUT_PATH = ''

title = ['SwTC_20']
field = ['Time Log', 'Input: ACSetTemp.phyVal', 'Input: CTCW_Internal_Var.ACSetTemp.phyVal', 'Input: ACSetTemp.isReserved', 'Input: ACSetTemp.isInvaild', 'Output: CTCW_InterModule_Var.isCCUChange']
outcome = [title, field]


intput_data = [[-15, -14, 0, 0], [-15, -15, 0, 0], [127, 127, 0, 0], [-128, -128, 0, 0], [254, 255, 0, 0], [30, 30, 1, 0], [254, 255, 0, 1]]
expected_result = [1, 0, 0, 0, 0, 0, 0]
final_result = 'Pass'

for i, res in zip(intput_data, expected_result):
    time_start = time.strftime('%Y-%m-%d, %H:%M:%S', time.localtime(time.time()))
    test_result = 'Pass'

    var1 = i[0]
    var2 = i[1]
    var3 = i[2]
    var4 = i[3]

    time.sleep(0.5)

    var5 = res

    if not check_same_value(var=var5, value=res):
        test_result = 'Fail'
        final_result = 'Fail'
    outcome.append([time_start, var1, var2, var3, var4, var5, test_result])

outcome.append(['Result', final_result])

export_csv_list(OUTPUT_PATH, title[0], outcome)



