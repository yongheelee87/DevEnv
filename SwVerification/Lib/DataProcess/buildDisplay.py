import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import string
from Lib.Inst import canBus


def signal_step_graph(df: pd.DataFrame, sigs: list, x_col: str, filepath: str, filename: str, fill_zero: bool = True, step_debug: bool = True):
    plt.rcParams['axes.xmargin'] = 0

    # maxT = df[x_col].max()
    df.set_index(x_col, drop=True, inplace=True)
    data_col = df.columns
    # Step Column 제거
    step_dict = {}
    if data_col[0] == 'Step':
        for step, group in df.groupby('Step'):
            time_sec = group.index.to_numpy()  # 스텝 별 시간 데이터
            step_dict[step] = (time_sec[0], time_sec[-1])

        df.drop(labels='Step', axis=1, inplace=True)
        data_col = data_col[1:]

    if fill_zero is True:
        df.fillna(0, inplace=True)  # replace None with zero

    # 그래프 코드
    fig = plt.figure(figsize=(26, 26))
    axs = fig.add_gridspec(len(data_col), hspace=0.1).subplots(sharex=True, sharey=False)

    for i, signal in enumerate(data_col):
        sig_color_idx = i % 20
        sig_name = data_col[i].replace('In: ', '').replace('Out: ', '')
        df_signal = df[[signal]].dropna(axis=0)
        x_data = df_signal.index.to_numpy()
        y_data = df_signal.to_numpy()

        axs[i].step(x_data, y_data, 'o-', markersize=2, label=sig_name, c=plt.cm.tab20(sig_color_idx), where='post', linewidth=1.0)

        if y_data.size == 0:
            yticks_val = range(0, 2)
        else:
            min_y = int(min(y_data))
            max_y = int(max(y_data))
            if max_y == 0:
                yticks_val = range(min_y, max_y + 2)
            else:
                if max_y > 8:
                    yticks_val = list(range(min_y, max_y, int(max_y / 7)))
                    yticks_val[-1] = max_y
                else:
                    yticks_val = range(min_y, max_y + 1)
        axs[i].set_yticks(yticks_val)
        yticks_labels = []
        for y_val in yticks_val:
            if (sig_name == sigs[i][-1]) and (sigs[i][0] != 'T32') and (sigs[i][0] != 'LIN'):
                if (sig_name in canBus.devs[sigs[i][0]].sig_val) and (y_val in canBus.devs[sigs[i][0]].sig_val[sig_name]):
                    yticks_labels.append(canBus.devs[sigs[i][0]].sig_val[sig_name][y_val])
                else:
                    yticks_labels.append(f'{y_val}')
            else:
                yticks_labels.append(f'{y_val}')
        axs[i].set_yticklabels(yticks_labels)
        # axs[i].set_xlim(left=0, right=maxT)

        if step_debug is True:
            step_location = []
            for idx, step_time in enumerate(step_dict.values()):
                color_idx = idx % 20
                axs[i].axvspan(step_time[0], step_time[1], alpha=0.1, color=plt.cm.tab20(color_idx))
                step_location.append(np.mean(step_time))

            if i == 0:
                ax_twin = axs[i].twiny()
                ax_twin.set_xlim(axs[i].get_xlim())
                ax_twin.set_xticks(np.array(step_location))
                ax_twin.set_xticklabels(step_dict.keys())
                ax_twin.set_xlabel('Step')

        if i == len(data_col)-1:
            axs[i].set_xlabel('Time[sec]')

    # Hide x labels and tick labels for all but bottom plot
    for ax in axs:
        ax.legend(loc='upper right')
        ax.label_outer()

    # plt.tight_layout(pad=0)
    plt.savefig(f'{filepath}/{filename}.png', format='png', bbox_inches='tight')
    # plt.savefig(f'{filepath}/{filename}.svg', format='svg')
    plt.cla()  # clear the current axes
    plt.clf()  # clear the current figure
    plt.close()  # closes the current figure


def make_pjt_HTML(df_sum, project: str, version: str, dict_tc: dict, tc_script: dict, tc_in_out: dict, export_path: str):
    html_text = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="EUC-KR">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
            <link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap' type='text/css'>
            <link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Jua&display=swap' type='text/css'>
            <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Nunito:400,300' type='text/css'>
            <title>{title} Result</title>
        </head>
        <body>
            <h1 style="font-family: 'Black Han Sans', sans-serif;font-size: 2.5em;color: red;margin: 20px 0 10px 10px;>{title}</h1>
            <h2 style="font-family: 'Jua', sans-serif;font-size: 1.0em;color: black;margin: 20px 0 10px 40px;>* SW 버전: {ver}</h2>
    {sum_body}
    {res_body}
            <h2 style="font-family: 'Jua', sans-serif;font-size: 1.0em;color: black;margin: 0 0 10px 40px;><a href="./" style="text-decoration:none">테스트 원본 파일을 다운받으시려면 여기를 클릭해주세요</a></h2>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
        </body>
    </html>
    """

    export_file = os.path.join(export_path, f'Result_{project}.html')
    with open(export_file, 'w') as html_file:
        html_file.write(html_text.format(title=project, ver=version, sum_body=_write_summary(df_sum), res_body=_write_tc_res_body(dict_tc, tc_script, tc_in_out)))


def make_meas_HTML(df_sum, project: str, tc_script: pd.DataFrame, tc_in_out: list, export_path: str):
    html_text = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="EUC-KR">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
            <link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap' type='text/css'>
            <link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Jua&display=swap' type='text/css'>
            <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Nunito:400,300' type='text/css'>
            <title>{title} Result</title>
        </head>
        <body>
            <h1 style="font-family: 'Black Han Sans', sans-serif;font-size: 2.5em;color: red;margin: 20px 0 10px 10px;>{title}</h1>
    {sum_body}
    {res_body}
            <h2 style="font-family: 'Jua', sans-serif;font-size: 1.0em;color: black;margin: 0 0 10px 40px;><a href="./" style="text-decoration:none">테스트 원본 파일을 다운받으시려면 여기를 클릭해주세요</a></h2>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
        </body>
    </html>
    """

    export_file = os.path.join(export_path, f'Result_{project}.html')
    with open(export_file, 'w') as html_file:
        html_file.write(html_text.format(title=project, sum_body=_write_summary(df_sum), res_body=_write_meas_res(project, tc_script, tc_in_out)))


def make_home_HTML(data: dict, export_path: str, df_ver: pd.DataFrame):
    test_date = os.path.basename(export_path)

    lst_table = [
        '<tr style="background-color: #54585d;border: 1px solid #54585d;">',
        '<th style="padding: 15px;border-right: 1px solid #54585d;text-align: center;color: white;">모듈</th>',
        '<th style="padding: 15px;border-right: 1px solid #54585d;text-align: center;color: white;">기능</th>',
        '<th style="padding: 15px;border-right: 1px solid #54585d;text-align: center;color: white;">결과</th>',
        '<th style="padding: 15px;text-align: center;color: white;">상세 링크</th>',
        '</tr>']

    for pjt in data.keys():
        pjt_data = data[pjt]
        lst_table.append('<tr>')
        lst_table.append(f'<td rowspan={len(pjt_data)} style="padding: 15px;border: 1px solid #54585d;">{pjt}</td>')
        module_tr_written = False
        for tc in pjt_data.keys():
            if module_tr_written:
                lst_table.append('<tr>')
            lst_table.append(f'<td rowspan=1 style="padding: 15px;border: 1px solid #54585d;">{tc}</td>')
            tc_result = pjt_data[tc]
            if 'Fail' in tc_result:
                lst_table.append('<td rowspan=1 style="background-color: #F1948A;padding: 15px;border: 1px solid #54585d;">Fail</td>')
            elif 'Pass' in tc_result:
                lst_table.append('<td rowspan=1 style="background-color: #ABEBC6;padding: 15px;border: 1px solid #54585d;">Pass</td>')
            else:
                lst_table.append(f'<td rowspan=1 style="padding: 15px;border: 1px solid #54585d;">{pjt_data[tc]}</td>')
            if module_tr_written is False:
                lst_table.append(f'<td rowspan={len(pjt_data)} style="padding: 15px;border: 1px solid #54585d;text-align: center"><a href="{pjt}/Result_{pjt}.html">{pjt}<br>{test_date}</a></td>')
                module_tr_written = True
            lst_table.append('</tr>')
    sum_result = '\n'.join(lst_table)

    html_text = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="EUC-KR">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
            <link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap' type='text/css'>
            <link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Jua&display=swap' type='text/css'>
            <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Nunito:400,300' type='text/css'>
            <title>{title} Result</title>
        </head>
        <body>
            <h1 style="font-family: 'Black Han Sans', sans-serif;font-size: 2.5em;color: red;margin: 20px 0 10px 10px;>{title}</h1>
            <h2 style="font-family: 'Jua', sans-serif;font-size: 1.0em;color: red;margin: 20px 0 10px 10px;>* 테스트 수행 날짜: {date}<br>* 테스트 환경: 제어기 + CAN + T32<br>* 테스트 방법: CAN Bus와 T32 제어 가능한 프로그램을 이용하여 정해진 시나리오를 진행</h2>
            {ver_body}
            <table style="font-family: 'Nunito', sans-serif;border: none;border-collapse: collapse;font-size: 1.0em;color: black;margin-bottom: 40px;margin-left: 40px;padding: 20px;">
            {sum_body}
            </table>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
        </body>
    </html>
    """

    export_file = os.path.join(export_path, f'Result_{test_date}.html')
    with open(export_file, 'w') as html_file:
        html_file.write(html_text.format(title='EILS 테스트 결과', date=test_date, ver_body=_write_version(df_ver), sum_body=sum_result))


def _write_version(df_ver: pd.DataFrame) -> str:
    lst_html = df_ver.to_html(border=None, index=False).split('\n')
    new_html = []
    for line in lst_html:
        if 'class="dataframe"' in line:
            line = """<table class="dataframe" style="font-family: 'Nunito', sans-serif;border: none;border-collapse: collapse;font-size: 1.0em;color: black;margin: 0 0 40px 40px;padding: 20px;">"""
        elif '<td>' in line and '.' not in line:
            line = line.replace('<td>', '<td style="text-align: right;padding-left: 30px;color: black;">')
        new_html.append(line)
    ver_html = '\n'.join(new_html)
    return ver_html


def _write_summary(df_sum: pd.DataFrame) -> str:
    lst_html = df_sum.to_html(border=None).split('\n')
    new_html = []
    for line in lst_html:
        if '<td' in line:
            if 'TestCase_Names' in new_html[-1]:
                test_cases = df_sum.loc['TestCase_Names', 'Value'].split(', ')
                html_test_cases = '<br>'.join(test_cases)
                line = f'<td style="border-bottom: 2px solid #54585d;text-align: right;padding-left: 30px;font-weight: 900;color: black;">{html_test_cases}</td>'
            elif 'Fail_Case' in new_html[-1]:
                fail_cases = df_sum.loc['Fail_Case', 'Value'].split(', ')
                if 'Nothing' != fail_cases[0]:
                    html_fail_cases = '<br>'.join(fail_cases).replace(',', ', ')
                    line = f'<td style="border-bottom: 2px solid #54585d;text-align: right;padding-left: 30px;font-weight: 900;color: red;">{html_fail_cases}</td>'
                else:
                    line = line.replace('<td>', '<td style="text-align: right;padding-left: 30px;">')
            else:
                line = line.replace('<td>', '<td style="text-align: right;padding-left: 30px;">')
        elif '<th>' in line and 'Value' not in line:
            line = line.replace('<th>', '<th style="padding-right: 20px;">')
        elif 'class=dataframe' in line:
            line = """<table class="dataframe" style="font-family: 'Nunito', sans-serif;border: none;border-collapse: collapse;font-size: 1.0em;color: black;margin-bottom: 40px;margin-left: 40px;padding: 20px;">"""
        new_html.append(line)
    sum_html = '\n'.join(new_html)
    return sum_html


def _write_tc_res_body(dict_tc: dict, tc_script: dict, tc_in_out: dict) -> str:
    tc_res_html = ''
    for tc in dict_tc.keys():
        sub_title = dict_tc[tc]
        img_src = f'{tc}.png'
        if tc_script and tc_script[tc] is not None:
            str_tc_prefix, str_tc_script = _write_tc(tc_script[tc], tc_in_out[tc])
            tc_res_body = f"""
            <h3 style="font-family: 'Jua', sans-serif;font-size: 1em;color: black;margin: 0 0 0 40px;">{sub_title}</h3>
            {str_tc_prefix}
            {str_tc_script}
            <img src="{img_src}" width="1100" height="1100" style="width: 1100px; height: 850px; margin: 0 0 40px 20px;" alt="NOT FOUND"></img>
            """
        else:
            tc_res_body = f"""
            <h3 style="font-family: 'Jua', sans-serif;font-size: 1em;color: black;margin: 0 0 0 40px;">{sub_title}</h3>
            <img src="{img_src}" width="1100" height="1100" style="width: 1100px; height: 850px; margin: 0 0 40px 20px;" alt="NOT FOUND"></img>
            """
        tc_res_html += tc_res_body
    return tc_res_html


def _write_meas_res(project: str, tc_script: pd.DataFrame, tc_in_out: list) -> str:
    img_src = f'{project}.png'
    str_tc_prefix, str_tc_script = _write_tc(tc_script, tc_in_out)
    res_html = f"""
               <h3 style="font-family: 'Jua', sans-serif;font-size: 1em;color: black;margin: 0 0 0 40px;">Script and Result Graph</h3>
               {str_tc_prefix}
               {str_tc_script}
               <img src="{img_src}" width="1100" height="1100" style="width: 1100px; height: 850px; margin: 0 0 40px 20px;" alt="NOT FOUND"></img>
               """
    return res_html


def _write_tc(df_script: pd.DataFrame, in_out: list) -> (str, str):
    cols = ['#', 'Scenario', 'Time[s]']
    inputs = []
    for i, in_sig in zip(string.ascii_uppercase, in_out[0]):
        inputs.append(f'{i}. {in_sig.replace(", ", "/ ")}')
        cols.append(i)
    outs = []
    for i, in_sig in zip(string.ascii_uppercase, in_out[0]):
        inputs.append(f'A{i}. {in_sig.reaplace("[OUT]", "").replace(", ", "/ ")}')
        cols.append(f'A{i}')

    df_prefix = pd.DataFrame({'Input': ['spacing'.join(inputs)], 'Output': ['spacing'.join(outs)]})
    df_script.columns = cols
    pre_html = _table_tc_to_html(lst_html=df_prefix.to_html(border=None, index=False).split('\n'), scr=False).replace('spacing', '<br>')
    scr_html = _table_tc_to_html(lst_html=df_script.to_html(border=None, index=False).split('\n'), scr=True, max_length=df_script['Scenario'].str.len().max()).replace('spacing', '<br>')
    return pre_html, scr_html


def _table_tc_to_html(lst_html, scr: bool = False, max_length: int = 10):
    new_html = []
    col_td = 0
    for line in lst_html:
        if 'class="dataframe"' in line:
            line = """<table class="dataframe" style="font-family: 'Nunito', sans-serif;border: none;border-collapse: collapse;font-size: 0.8em;color: black;margin: 10px 0 20px 40px;padding: 20px;">"""
        elif '<th>' in line:
            if 'Scenario' in line:
                if max_length <= 8:
                    pixel_num = '10'
                elif max_length <= 15:
                    pixel_num = '60'
                elif max_length <= 20:
                    pixel_num = '90'
                else:
                    pixel_num = str(int(max_length*5.5))
                line = line.replace(', ', '<br>').replace('<th>', f'<td style="background-color: #FCF3F2;border: 1px solid #c1c4c7;text-align: center;padding: 0 {pixel_num}px 0 {pixel_num}px;">')
            else:
                line = line.replace(', ', '<br>').replace('<th>', '<td style="background-color: #FCF3F2;border: 1px solid #c1c4c7;text-align: center;padding: 0 10px 0 10px;">')
        elif '<td>' in line:
            if scr:
                if col_td != 1:
                    line = line.replace('<td>', '<td style="border: 1px solid #c1c4c7;text-align: center;padding: 0 10px 0 10px;">')
                else:
                    line = line.replace('<td>', '<td style="border: 1px solid #c1c4c7;text-align: left;padding: 0 10px 0 10px;">')
            else:
                line = line.replace('<td>', '<td style="border: 1px solid #c1c4c7;text-align: left;padding: 0 10px 0 10px;vertical-align: top;">')
            col_td += 1
        elif '<tr>' in line:
            col_td = 0
        new_html.append(line)
    return '\n'.join(new_html)
