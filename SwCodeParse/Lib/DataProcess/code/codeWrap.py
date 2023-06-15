from Lib.Common.basicFunction import *


class CodeWrapper:
    def __init__(self):
        self.descript = None
        self.include = None
        self.define = None
        self.structure = None
        self.globalVar = None
        self.staticVar = None
        self.globalFunc = None
        self.staticFunc = None

    def wrap(self, file):
        self._initialization_var()
        file_name = os.path.basename(file)
        with open(file, 'r', encoding='utf-8') as f:
            logging_print("......... Parsing : {} .........".format(file_name))
            code = f.readlines()
            indexes = []
            for index, line in enumerate(code):
                if line.count('Includes') and line.count('**'):
                    self.include = self._cut_end(code[index:])
                    indexes.append(index)
                elif line.count('Define') and line.count('**'):
                    self.define = self._cut_end(code[index:])
                    indexes.append(index)
                elif line.count('Structure') and line.count('**'):
                    self.structure = self._cut_end(code[index:])
                    indexes.append(index)
                elif line.count('Global Variables') and line.count('**'):
                    self.globalVar = self._cut_end(code[index:])
                    indexes.append(index)
                elif line.count('Static Variables') and line.count('**'):
                    self.staticVar = self._cut_end(code[index:])
                    indexes.append(index)
                elif line.count('Global Function') or line.count('Global Functions') or line.count(
                        'Global Functions (Body)'):
                    self.globalFunc = self._cut_end(code[index:])
                    indexes.append(index)
                elif line.count('Static Functions (Body)'):
                    self.staticFunc = self._cut_end(code[index:])
                    indexes.append(index)
            self.descript = code[:min(indexes)]

    def _initialization_var(self):
        self.descript = None
        self.include = None
        self.define = None
        self.structure = None
        self.globalVar = None
        self.staticVar = None
        self.globalFunc = None
        self.staticFunc = None

    # noinspection PyMethodMayBeStatic
    def _cut_end(self, lines):
        ret_lines = []
        for index, line in enumerate(lines):
            if '/**********************************************************' in line: break
            ret_lines.append(line)
        return ret_lines
# This is a new line that ends the file
