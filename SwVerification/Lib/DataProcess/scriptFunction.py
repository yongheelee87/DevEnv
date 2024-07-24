import pandas as pd


def find_out_signals_for_col(out_sigs: list) -> (list, list):
    cols = []
    t32_out = []
    for sig in out_sigs:
        cols.append(f'Out: {sig[2]}')
        if 'T32' in sig[0]:
            t32_out.append(sig[-1])
    return cols, t32_out


def judge_final_result(df_result: pd.DataFrame, expected_outs: list, num_match: int, meas_log: list, out_col: list, judge: str = "same"):
    final_result = 'Pass'  # Final result to be recorded
    fail_cases = []

    # Result judgement logic
    if "same" in judge:
        for expected in expected_outs:  # Step increment
            df_match = df_result.copy()  # define the dataframe to store matching rows, memory protection
            for ex_value, col in zip(expected, df_match.columns):  # find matching rows by columns
                if ex_value is not None:
                    df_match = df_match[df_match[col] == ex_value]  # Overwrite matching rows

            if len(df_match) < num_match:  # If length of matching rows is less than the number to be configured, it leads to fail
                fail_step = str(int(expected[0]))
                fail_cases.append([fail_step, 'Fail Case', f'Step_{fail_step}', 'Expected Output'] + [f'{var}={val}' for var, val in zip(out_col, expected[1:])])
    else:
        for expected in expected_outs:  # Step increment
            df_res = df_result.copy()  # define the dataframe to store matching rows, memory protection
            df_step = df_res[df_res['Step'] == expected[0]]  # step dataframe
            step_pass = True
            for ex_value, col in zip(expected[1:], df_res.columns[1:]):  # find matching rows by columns
                if ex_value is not None:
                    df_match = df_step[df_step[col] == ex_value]  # Find matching rows
                    if len(df_match) < num_match:  # If length of matching rows is less than the number to be configured, it leads to fail
                        step_pass = False
            if step_pass is False:
                fail_step = str(int(expected[0]))
                fail_cases.append([fail_step, 'Fail Case', f'Step_{fail_step}', 'Expected Output'] + [f'{var}={val}' for var, val in zip(out_col, expected[1:])])

    if fail_cases:
        final_result = 'Fail'  # Final result would be fail
        for idx, fail_case in enumerate(fail_cases):
            meas_log.insert(idx+1, fail_case[1:])
            final_result += f',{fail_case[0]}'  # the final result should be written with fail steps
        final_result_str = final_result.replace(',', ', ').replace('Fail', 'Fail Step:')
        print(f'*** {final_result_str}')

    meas_log.append(['Result', final_result])
    return meas_log
