from Lib.DataProcess.code.codeWrap import *

OVER_COL = ['Description', 'Safety_Level']
DEF_COL = ['Definition', 'Description']
FUNC_COL = ['Name', 'Prototype', 'Description', 'Input', 'Output', 'Total_Description']
VAR_COL = ['Var_Type', 'Data Name', 'Data Type', 'Value Range', 'Description', 'Full_Name']


class CodeParser(CodeWrapper):
    def __init__(self):
        super().__init__()
        self.df_overview = None
        self.df_include = None
        self.df_define = None
        self.df_struct = None
        self.df_globalFunc = None
        self.df_staticFunc = None
        self.df_var = None
        self.df_extern = None
        isdir_and_make('./result/src')  # src 경로 생성
        isdir_and_make('./result/inc')  # inc 경로 생성

    def run(self, file):
        self.wrap(file)

        file_name = os.path.basename(file)
        if '.c' in file_name:
            path = './result/src/{}'.format(file_name.replace('.c', ''))
            isdir_and_make(path)  # path 경로 생성

            # Parse Overview
            self.df_overview = self.parse_overview(self.descript)
            export_csv_dataframe(self.df_overview, path, 'Overview')

            # Parse Include
            self.df_include = self.parse_include(self.include)
            export_csv_dataframe(self.df_include, path, 'Include')

            # Parse Define
            self.df_define = self.parse_define(self.define)
            export_csv_dataframe(self.df_define, path, 'Defines')

            # Parse Structure
            self.df_struct = self.parse_struct(self.structure)
            export_csv_dataframe(self.df_struct, path, 'Structure')

            # Parse Global Functions
            self.df_globalFunc = self.parse_func(self.globalFunc)
            export_csv_dataframe(self.df_globalFunc, path, 'Global_Function')

            # Parse Static Functions
            self.df_staticFunc = self.parse_func(self.staticFunc)
            export_csv_dataframe(self.df_staticFunc, path, 'Static_Function')

            # Parse Variables
            self.df_var = self.parse_var(self.globalVar, self.staticVar)
            export_csv_dataframe(self.df_var, path, 'Variables')
        else:
            path = './result/inc/{}'.format(file_name.replace('.h', ''))
            isdir_and_make(path)  # path 경로 생성
            # Parse Overview
            self.df_overview = self.parse_overview(self.descript)
            export_csv_dataframe(self.df_overview, path, 'Overview')

            # Parse Define
            self.df_define = self.parse_define(self.define)
            export_csv_dataframe(self.df_define, path, 'Defines')

            # Parse Structure
            self.df_struct = self.parse_struct(self.structure)
            export_csv_dataframe(self.df_struct, path, 'Structure')

            # Parse Extern
            self.df_extern = self.parse_extern(self.globalFunc)
            export_csv_dataframe(self.df_extern, path, 'Extern')

    def parse_overview(self, descript):
        data_overview = []
        if descript is not None:
            lst_overview = self._get_overview(descript)
            data_overview = [lst_overview]
        return pd.DataFrame(data_overview, columns=OVER_COL)

    def parse_include(self, include_lines):
        data_include = []
        if include_lines is not None:
            data_include = self._get_include(include_lines)
        return pd.DataFrame(data_include, columns=['include'])

    def parse_define(self, define_lines):
        data_def = []
        data_typedef = []
        if define_lines is not None:
            data_def = self._get_define(define_lines)
            data_typedef = [self._filter_typedef_data(typedef) for typedef in self._get_typedef(define_lines)]
        return pd.DataFrame(data_def + data_typedef, columns=DEF_COL)

    def parse_struct(self, typedef_line):
        data_typedef = []
        if typedef_line is not None:
            data_typedef = [self._filter_typedef_data(typedef) for typedef in self._get_typedef(typedef_line)]
        return pd.DataFrame(data_typedef, columns=DEF_COL)

    def parse_func(self, func_code):
        data_func = []
        if func_code is not None:
            lst_annotate, lst_func = self._split_funcs(func_code)
            data_func = []
            for annotate, func in zip(lst_annotate, lst_func):
                proto_type = func.replace('\n', '')
                name = [i for i in proto_type.split() if 'static' not in i and 'inline' not in i][
                    1]  # [0]: return type [1]: name
                func_name = name[:name.find('(')] if '(' in name else name
                descript = annotate[0][annotate[0].find(':') + 1:].replace('\n', '').replace('\t', '').lstrip()
                input_data, output_data = self._get_input_output(annotate)
                description = "".join([i[2:].lstrip() for i in annotate])[:-1].replace('\t', ' ')
                if description[-2:] == '*/':
                    description = description[:-2]
                data_func.append(
                    [func_name, proto_type, descript, input_data, output_data, description])
        return pd.DataFrame(data_func, columns=FUNC_COL)

    def parse_var(self, global_var, static_var):
        data_var = []
        if global_var is not None or static_var is not None:
            lst_global = self._get_variable(global_var[2:])
            lst_static = self._get_variable(static_var[2:])
            for global_var in lst_global:
                data_var.append(self._filter_var_data(global_var))
            for static_var in lst_static:
                data_var.append(self._filter_var_data(static_var))
        return pd.DataFrame(data_var, columns=VAR_COL)

    # noinspection PyMethodMayBeStatic
    def parse_extern(self, global_func):
        data_extern = []
        if global_func is not None:
            data_extern = self._get_extern(global_func)
        return pd.DataFrame(data_extern, columns=DEF_COL)

    # noinspection PyMethodMayBeStatic
    def _get_overview(self, descript_line):
        description = ''
        safety = ''
        for line in descript_line:
            if 'Description:' in line:
                description = line[line.find(':') + 1:].replace('\n', '').replace('\t', '').strip()
            elif 'Safety Level' in line:
                safety = line[line.find(':') + 1:].replace('\n', '').replace('\t', '').strip()
        if safety == '':
            safety = 'QM'
        lst_overview = [description, safety]
        return lst_overview

    # noinspection PyMethodMayBeStatic
    def _get_include(self, include_line):
        lst_include = []
        for line in include_line:
            if '#include' in line:
                line = line.replace('\n', '').replace('\t', '').replace('"', '').replace('<', '').replace('>',
                                                                                                          '').strip()
                lst_include.append(line)
        return lst_include

    # noinspection PyMethodMayBeStatic
    def _get_define(self, def_line):
        lst_def = []
        for line in def_line:
            if '#define' in line:
                line = line.replace('\n', '').replace('\t', '')
                if '/*' in line:
                    definition = line[:line.find('/*')].strip()
                    descript = line[line.find('/*') + 2:].replace('*/', '').strip()
                else:
                    definition = line.strip()
                    descript = ''
                lst_def.append([definition, descript])
        return lst_def

    # noinspection PyMethodMayBeStatic
    def _get_extern(self, global_line):
        lst_extern = []
        for line in global_line:
            if 'extern' in line:
                line = line.replace('\n', '').replace('\t', '')
                if '/*' in line:
                    definition = line[:line.find('/*')].strip()
                    descript = line[line.find('/*') + 2:].replace('*/', '').strip()
                else:
                    definition = line.strip()
                    descript = ''
                lst_extern.append([definition, descript])
        return lst_extern

    # noinspection PyMethodMayBeStatic
    def _split_funcs(self, code):
        lst_func = []
        lst_descript = []

        lst_idx_code = [index for index, line in enumerate(code) if line.count('Description') or line.count('Return')]

        for idx_des, idx_return in zip(lst_idx_code[::2], lst_idx_code[1::2]):
            idx_end = idx_return + 1
            lst_descript.append(code[idx_des:idx_end])
            while idx_end < len(code):
                if '{' in code[idx_end]:
                    break
                idx_end += 1
            lst_func.append(code[idx_end - 1])
        return lst_descript, lst_func

    # noinspection PyMethodMayBeStatic
    def _get_input_output(self, comment):
        lst_input = []
        output_str = 'void'
        for f in comment[1:]:
            if 'Param' in f:
                lst_input.append(f[f.find(':') + 1:].replace('\n', '').replace('\t', '').strip())
            elif 'Return' in f:
                output_str = f[f.find(':') + 1:].replace('\n', '').replace('\t', '').strip()
        input_str = "\n".join(lst_input)
        return input_str, output_str

    # noinspection PyMethodMayBeStatic
    def _get_variable(self, var_line):
        lst_var = []
        temp = []
        for line in var_line:
            if '=' in line and ';' in line:
                lst_var.append(line.replace('\n', ''))
            elif '=' in line:
                temp.append(line)
            elif ';' in line:
                temp.append(line.replace('\n', ''))
                lst_var.append(''.join(temp))
                temp = []
            elif len(temp) != 0:
                temp.append(line)
            else:
                pass
        return lst_var

    # noinspection PyMethodMayBeStatic
    def _get_typedef(self, type_line):
        lst_type = []
        temp = []
        bracket_cnt = 0
        for line in type_line:
            line = line.replace('\t', ' ')
            if 'typedef' in line:
                temp.append(line)
            elif '{' in line:
                temp.append(line)
                bracket_cnt += 1
            elif '}' in line:
                temp.append(line.replace('\n', ''))
                bracket_cnt -= 1

                if bracket_cnt == 0:
                    lst_type.append(''.join(temp))
                    temp = []
            elif len(temp) != 0:
                temp.append(line)
            else:
                pass
        return lst_type

    # noinspection PyMethodMayBeStatic
    def _filter_var_data(self, var_str):
        var_type = 'global'
        if 'static' in var_str:
            var_type = 'static'
            var_str = var_str.replace('static', '')
        var_str = var_str.replace('const', '')
        index_var = var_str.find(';')
        var = var_str[:index_var].replace('\n', '').replace('\t', '').lstrip()
        index_value = var.find('=')
        value = var[index_value:].replace('=', '').replace('\n', '').replace('\t',
                                                                             '').lstrip() if index_value != -1 else ''
        descript = var_str[index_var + 1:].replace('/*', '').replace('*/', '').replace('\n', '').replace('\t',
                                                                                                         '').strip()
        return [var_type, var.split()[1], var.split()[0], value, descript, var]

    # noinspection PyMethodMayBeStatic
    def _filter_typedef_data(self, typedef_str):
        index_typedef = typedef_str.rfind(';')
        typedef = typedef_str[:index_typedef].strip()
        descript = typedef_str[index_typedef + 1:].replace('/*', '').replace('*/', '').replace('\n', '').replace('\t',
                                                                                                                 '').strip()
        return [typedef, descript]

