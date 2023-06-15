import pandas as pd
import xlsxwriter
import time
from win32com.client import Dispatch
from Lib.Common.basicFunction import *

COMPONENT_EXCEL_DES = ['Component Name', 'Component Design', 'Input Information', 'Output Information',
                       'Related Quality Attribute', 'Alternative solution']


class ExcelWrapper:
    def __init__(self):
        super().__init__()
        isdir_and_make('./result/doc')

    def set_ds(self, component_dev, component_des):
        # Create a new Excel document
        time_var = time.strftime('%Y%m%d', time.localtime(time.time()))
        f_comp_dev = './result/doc/Confidential_SwDS_Component_Develop_{}.xlsx'.format(time_var)
        f_comp_des = './result/doc/Confidential_SwDS_Component_Descript_{}.xlsx'.format(time_var)
        wr_component_dev = pd.ExcelWriter(f_comp_dev, engine='xlsxwriter')
        wr_component_des = pd.ExcelWriter(f_comp_des, engine='xlsxwriter')
        component_dev.to_excel(wr_component_dev, sheet_name="sheet0", index=False)

        lst_text = []
        for comp, comp_des in component_des.items():
            text = ''
            num = 1
            for col, content in zip(COMPONENT_EXCEL_DES, comp_des):
                text += '{}) {}: {}\n'.format(num, col, content)
                num += 1
            text += '{}) Related Quality Attribute:\n{}) Alternative solution:'.format(num, num + 1)
            lst_text.append([text])
        df_comp_des = pd.DataFrame(lst_text, columns=['text'])
        df_comp_des.to_excel(wr_component_des, sheet_name="sheet0", index=False)

        wr_component_dev.close()
        wr_component_des.close()

        self.convert_xls(f_comp_dev)
        self.convert_xls(f_comp_des)

    def set_dd(self, header_dict, component_dict):
        time_var = time.strftime('%Y%m%d', time.localtime(time.time()))
        for comp, comp_data in component_dict.items():
            f_comp = './result/doc/Confidential_SwDD_Component_{}_{}.xlsx'.format(comp, time_var)
            wr_component = pd.ExcelWriter(f_comp, engine='xlsxwriter')

            lst_intro = self._convert_lst_str_horizontal_df(comp_data[0])
            df_comp_intro = pd.DataFrame(lst_intro, columns=['text'])
            df_comp_intro.to_excel(wr_component, sheet_name="Intro", index=False)

            lst_header = []
            if not comp_data[1].empty:
                lst_header = self._convert_lst_str_horizontal_df(comp_data[1])
            df_comp_header = pd.DataFrame(lst_header, columns=['text'])
            df_comp_header.to_excel(wr_component, sheet_name="Header", index=False)

            lst_global_var = self._convert_lst_str_horizontal_df(comp_data[2])
            df_comp_global_var = pd.DataFrame(lst_global_var, columns=['text'])
            df_comp_global_var.to_excel(wr_component, sheet_name="Global Variable", index=False)

            lst_unit_list = self._convert_lst_str_vertical_df(comp_data[3])
            df_comp_unit_list = pd.DataFrame(lst_unit_list, columns=['text'])
            df_comp_unit_list.to_excel(wr_component, sheet_name="Interface Internal Unit List", index=False)

            lst_interface = self._convert_lst_str_horizontal_df(comp_data[4])
            df_comp_interface = pd.DataFrame(lst_interface, columns=['text'])
            df_comp_interface.to_excel(wr_component, sheet_name="Interface Unit", index=False)

            lst_internal = self._convert_lst_str_horizontal_df(comp_data[5])
            df_comp_internal = pd.DataFrame(lst_internal, columns=['text'])
            df_comp_internal.to_excel(wr_component, sheet_name="Internal Unit", index=False)

            wr_component.close()

    # noinspection PyMethodMayBeStatic
    def worksheet_configure(self, writer, workbook, sheet, func_table):
        worksheet = writer.sheets[sheet]
        for idx, col in enumerate(func_table):  # loop through all columns
            series = func_table[col]
            max_len = max((series.astype(str).map(len).max(), len(str(series.name)))) + 1  # adding
            worksheet.set_column(idx, idx, max_len)  # set column width

        border_fmt = workbook.add_format({'bottom': 1, 'top': 1, 'left': 1, 'right': 1})
        worksheet.conditional_format(
            xlsxwriter.utility.xl_range(0, 0, len(func_table), len(func_table.columns) - 1),
            {'type': 'no_errors', 'format': border_fmt})

    def convert_xls(self, xlsx_file):
        # xlsx to xls
        xl = Dispatch('Excel.Application')
        file_name = os.path.join(os.getcwd(), xlsx_file)
        wb = xl.Workbooks.Add(file_name)
        isdir_and_make('./result/ptc')
        wb.SaveAs(file_name[:-1].replace('doc/', 'ptc/'), FileFormat=56)
        xl.Quit()

    # noinspection PyMethodMayBeStatic
    def _convert_lst_str_horizontal_df(self, df):
        lst_text = []
        cols = df.columns.tolist()
        for i in range(df.shape[0]):
            text = ''
            for j in range(df.shape[1]):
                text += '{}: {}\n'.format(cols[j], df.iloc[i, j])
            lst_text.append([text[:-1]])
        return lst_text

    # noinspection PyMethodMayBeStatic
    def _convert_lst_str_vertical_df(self, df):
        lst_text = []
        text = ''
        for i in range(df.shape[0]):
            text += '{}: {}\n\n'.format(df.iloc[i, 0], df.iloc[i, 1].replace('\n', ', '))
        lst_text.append([text[:-2]])
        return lst_text
