from Lib.Common.basicFunction import *

MAIN_INFO = ['File name', 'Location', 'Description']
UNIT_ATTRIBUTE = ['Interface unit List', 'Internal unit List']
DEF_COL = ['Definition', 'Description']


class SwDdGenerator:
    def __init__(self, global_h):
        super().__init__()
        self.components = os.listdir('./result/src')
        self.header_files = os.listdir('./result/inc')
        self.dict_global_h = self.get_dict_header(global_h)
        self.dict_component = self.get_dict_comp()

    def get_dict_comp(self):
        dict_comp = dict()
        for component in self.components:
            dict_comp[component] = [self._get_main_info(component), self._get_header_file(component),
                                    self._get_global_var(component), self._get_unit_list(component),
                                    self._get_global_func(component), self._get_static_func(component)]
        return dict_comp

    def get_dict_header(self, global_header):
        dict_h = dict()
        for header_path in global_header:
            header = os.path.basename(header_path)
            dict_h[header] = self._get_header_file(header.replace('.h', ''))
        return dict_h

    # noinspection PyMethodMayBeStatic
    def _get_main_info(self, component):
        df_global = load_csv_dataframe('./result/src/{}'.format(component), 'Global_Function').fillna('')
        description = '\n'.join([i for i in df_global.loc[:, 'Description'].values if 'None' != i])
        return pd.DataFrame([['{}.c'.format(component), r'\Sourcecode in ALM', description]], columns=MAIN_INFO)

    # noinspection PyMethodMayBeStatic
    def _get_header_file(self, component):
        df_header = pd.DataFrame(columns=DEF_COL)
        if component in self.header_files:
            df_include = load_csv_dataframe('./result/inc/{}'.format(component), 'Defines').fillna('')
            df_structure = load_csv_dataframe('./result/inc/{}'.format(component), 'Structure').fillna('')
            df_extern = load_csv_dataframe('./result/inc/{}'.format(component), 'Extern').fillna('')
            df_header = pd.concat([df_include, df_structure, df_extern])
        return df_header

    # noinspection PyMethodMayBeStatic
    def _get_global_var(self, component):
        df_variable = load_csv_dataframe('./result/src/{}'.format(component), 'Variables')[
            ['Data Name', 'Data Type', 'Value Range', 'Description']].fillna('')
        return df_variable

    # noinspection PyMethodMayBeStatic
    def _get_unit_list(self, component):
        df_global = load_csv_dataframe('./result/src/{}'.format(component), 'Global_Function')
        df_static = load_csv_dataframe('./result/src/{}'.format(component), 'Static_Function')

        global_funcs = 'There is no interface unit name' if df_global.empty else '\n'.join(
            [i for i in df_global.loc[:, 'Name'].values if 'None' != i])
        static_funcs = 'There is no internal unit name' if df_static.empty else '\n'.join(
            [i for i in df_static.loc[:, 'Name'].values if 'None' != i])

        return pd.DataFrame({'Attribute': UNIT_ATTRIBUTE, 'Contents': [global_funcs, static_funcs]})

    # noinspection PyMethodMayBeStatic
    def _get_global_func(self, component):
        df_global = load_csv_dataframe('./result/src/{}'.format(component), 'Global_Function')[
            ['Name', 'Prototype', 'Input', 'Output', 'Description']]
        return df_global

    # noinspection PyMethodMayBeStatic
    def _get_static_func(self, component):
        df_static = load_csv_dataframe('./result/src/{}'.format(component), 'Static_Function')[
            ['Name', 'Prototype', 'Input', 'Output', 'Description']]
        return df_static
