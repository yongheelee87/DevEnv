import pandas as pd
import matplotlib
matplotlib.use('Agg')
import os
import matplotlib.pyplot as plt


def signal_step_graph(data, col, x_col, filepath, filename):
    plt.rcParams['axes.xmargin'] = 0

    df = pd.DataFrame(data, columns=col)
    df.fillna(0, inplace=True)
    df.set_index(x_col, drop=True, inplace=True)
    data_col = df.columns.tolist()

    # 그래프 코드
    colors = ['rosybrown', 'lightcoral', 'darkgreen', 'lime', 'lightseagreen', 'teal', 'aqua', 'cadetblue', 'steelblue', 'slategray', 'purple', 'magenta', 'crimson', 'navy', 'lightsteelblue',
              'salmon', 'peru', 'saddlebrown', 'sandybrown', 'red', 'olive', 'yellow', 'darkred', 'deeppink', 'indigo', 'mediumorchid', 'darkorange', 'tan', 'dodgerblue', 'cyan', 'forestgreen']
    fig = plt.figure(figsize=(24, 24))
    axs = fig.add_gridspec(len(data_col), hspace=0.1).subplots(sharex=True, sharey=False)

    for i in range(len(data_col)):
        sig_name = data_col[i].replace('In: ', '').replace('Out: ', '')
        axs[i].step(df.index.values, df[data_col[i]], c=colors[i], label=sig_name, where='post', linewidth=3.0)
        axs[i].set_ylabel(sig_name)
        min_val = df[data_col[i]].min()
        if min_val < 0:
            axs[i].set_ylim(bottom=min_val-1)
        else:
            axs[i].set_ylim(bottom=0)

    # Hide x labels and tick labels for all but bottom plot
    for ax in axs:
        ax.legend(loc='upper right')
        ax.label_outer()

    plt.locator_params(axis='x', nbins=5)
    plt.xlabel('Time[sec]')

    plt.savefig('{}/{}.png'.format(filepath, filename))


def make_pjt_HTML(df_sum, project: str, dict_tc: dict, export_path: str):
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
    {img_body}
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
        </body>
    </html>
    """

    export_file = os.path.join(export_path, 'Result_{}.html'.format(project))
    with open(export_file, 'w') as html_file:
        html_file.write(html_text.format(title=project, sum_body=_write_summary(df_sum), img_body=_write_img_body(dict_tc)))


def make_home_HTML(data: dict, export_path: str):
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
        lst_table.append('<td rowspan={} style="padding: 15px;border: 1px solid #54585d;">{}</td>'.format(len(pjt_data), pjt))
        module_tr_written = False
        for tc in pjt_data.keys():
            if module_tr_written:
                lst_table.append('<tr>')
            lst_table.append('<td rowspan=1 style="padding: 15px;border: 1px solid #54585d;">{}</td>'.format(tc))
            tc_result = pjt_data[tc]
            if tc_result == 'Fail':
                lst_table.append('<td rowspan=1 style="background-color: #F1948A;padding: 15px;border: 1px solid #54585d;">{}</td>'.format(pjt_data[tc]))
            elif tc_result == 'Pass':
                lst_table.append('<td rowspan=1 style="background-color: #ABEBC6;padding: 15px;border: 1px solid #54585d;">{}</td>'.format(pjt_data[tc]))
            else:
                lst_table.append('<td rowspan=1 style="padding: 15px;border: 1px solid #54585d;">{}</td>'.format(pjt_data[tc]))
            if module_tr_written is False:
                lst_table.append('<td rowspan={len_row} style="padding: 15px;border: 1px solid #54585d;text-align: center"><a href="{project}/Result_{project}.html">{project}<br>{date}</a></td>'.format(len_row=len(pjt_data), project=pjt, date=test_date))
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
            <h2 style="font-family: 'Jua', sans-serif;font-size: 1.0em;color: red;margin: 20px 0 10px 10px;>테스트 수행 날짜: {date}</h2>
            <table style="font-family: 'Nunito', sans-serif;border: none;border-collapse: collapse;font-size: 1.0em;color: black;margin-bottom: 40px;margin-left: 20px;padding: 20px;">
            {sum_body}
            </table>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
        </body>
    </html>
    """

    export_file = os.path.join(export_path, 'Result_{}.html'.format(test_date))
    with open(export_file, 'w') as html_file:
        html_file.write(html_text.format(title='EILS 테스트 결과', date=test_date, sum_body=sum_result))


def _write_summary(df_sum):
    lst_html = df_sum.to_html(border=None).split('\n')
    new_html = []
    for line in lst_html:
        if '<td' in line:
            if 'TestCase_Names' in new_html[-1]:
                test_Cases = df_sum.loc['TestCase_Names', 'Value'].split(', ')
                line = '<td style="text-align: right;padding-left: 30px;font-weight: 900;color: black;">{}</td>'.format('<br>'.join(test_Cases))
            elif 'Fail_Case' in new_html[-1]:
                fail_cases = df_sum.loc['Fail_Case', 'Value'].split(', ')
                if 'Nothing' != fail_cases[0]:
                    line = '<td style="text-align: right;padding-left: 30px;font-weight: 900;color: red;">{}</td>'.format('<br>'.join(test_Cases))
                else:
                    line = line.replace('<td>', '<td style="text-align: right;padding-left: 30px;">')
            else:
                line = line.replace('<td>', '<td style="text-align: right;padding-left: 30px;">')
        elif 'class=dataframe' in line:
            line = """<table class="dataframe" style="font-family: 'Nunito', sans-serif;border: none;border-collapse: collapse;font-size: 1.0em;color: black;margin-bottom: 40px;margin-left: 20px;padding: 20px;">"""
        new_html.append(line)
    sum_html = '\n'.join(new_html)
    return sum_html

def _write_img_body(dict_tc: dict):
    img_html = ''
    for lmg_src in dict_tc.keys():
        img_body = """
            <h3 style="font-family: 'Jua', sans-serif;font-size: 1em;color: red;margin: 0 0 0 10px;>{sub_title}</h3>
            <img src="{img_src}" width="1200" height="1200" style="width: 1200px; height: 950px; object-fit:cover;margin: 0 0 40px 0px;" alt="NOT FOUND"></img>
        """
        img_html += img_body.format(sub_title=dict_tc[lmg_src], img_src=lmg_src + '.png')
    return img_html
