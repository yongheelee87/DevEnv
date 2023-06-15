from Lib.Common.basicFunction import *

COMPONENT_DEV_TYPE = ['No.', 'Component Name', 'Development Type', 'Program Code(byte)', 'Description']
COMPONENT_DES = ['Component ID', 'Component Name', 'Component Design', 'Input Information', 'Output Information',
                 'ASIL', 'CAL', 'TDL', 'Related ID', 'Quality Attribute', 'Alternative solution']


class SwDsGenerator:
    def __init__(self, usage, doc_type):
        super().__init__()
        self.usage = usage.set_index(keys='Component', drop=True)
        self.components = os.listdir('./result/src')
        self.component_dev = self._get_com_dev()
        self.component_des = self._get_com_descript(doc_type)

    def _get_com_descript(self, output_type):
        component_des = dict()
        for component in self.components:
            if output_type == 'Word':
                lst_com_des = ['']  # Component ID

                df_global = load_csv_dataframe('./result/src/{}'.format(component), 'Global_Function')
                df_overview = load_csv_dataframe('./result/src/{}'.format(component), 'Overview')

                lst_com_des.append(component)  # Component Name
                func_description = '\n'.join(
                    ['- ' + i for i in df_global.loc[:, 'Description'].values if 'None' != i]) + '\n\n'
                lst_com_des.append(func_description)  # Component Design
                inputs = []
                for param_in in df_global.loc[:, 'Input'].values:
                    if ',' in param_in:
                        inputs += param_in.split(', ')
                    elif '\n' in param_in:
                        inputs += param_in.split('\n')
                    else:
                        inputs.append(param_in)

                inputs = '\n'.join(list(set([i for i in inputs if 'None' != i])))
                outputs = '\n'.join(list(set([i for i in df_global.loc[:, 'Output'].values if 'None' != i])))

                lst_com_des.append(inputs)  # Input Information
                lst_com_des.append(outputs)  # Output Information
                lst_com_des.append(df_overview.loc[0, 'Safety_Level'])  # ASIL
                lst_com_des.append('')  # CAL
                lst_com_des.append('')  # TDL
                lst_com_des.append('')  # Related ID
                lst_com_des.append('')  # Quality Attribute
                lst_com_des.append('')  # Alternative solution

                component_des[component] = pd.DataFrame({'Attribute': COMPONENT_DES, 'Contents': lst_com_des})
            else:
                lst_com_des = []  # Component data

                df_global = load_csv_dataframe('./result/src/{}'.format(component), 'Global_Function')
                df_overview = load_csv_dataframe('./result/src/{}'.format(component), 'Overview')

                lst_com_des.append(component)  # Component Name
                func_description = '\n'.join(['- ' + i for i in df_global.loc[:, 'Description'].values if 'None' != i])
                description = df_overview.loc[0, 'Description'] + '\n' + func_description
                lst_com_des.append(description)  # Component Design
                inputs = []
                for param_in in df_global.loc[:, 'Input'].values:
                    if ',' in param_in:
                        inputs += param_in.split(', ')
                    elif '\n' in param_in:
                        inputs += param_in.split('\n')
                    else:
                        inputs.append(param_in)

                inputs = '\n' + '\n'.join(list(set(['- ' + i for i in inputs if 'None' != i])))
                outputs = '\n' + '\n'.join(
                    list(set(['- ' + i for i in df_global.loc[:, 'Output'].values if 'None' != i])))

                lst_com_des.append(inputs)  # Input Information
                lst_com_des.append(outputs)  # Output Information
                component_des[component] = lst_com_des
        return component_des

    def _get_com_dev(self):
        lst_com_dev = []
        number = 1
        for component in self.components:
            usage = self.usage.loc[component].values[0]
            description = load_csv_dataframe('./result/src/{}'.format(component), 'Overview').loc[0, 'Description']
            df_global = load_csv_dataframe('./result/src/{}'.format(component), 'Global_Function').fillna('')
            func_description = '\n'.join(['- ' + i for i in df_global.loc[:, 'Description'].values if 'None' != i])
            description = description + '\n' + func_description
            lst_com_dev.append([number, component, '', usage, description])
            number += 1
        return pd.DataFrame(lst_com_dev, columns=COMPONENT_DEV_TYPE)
