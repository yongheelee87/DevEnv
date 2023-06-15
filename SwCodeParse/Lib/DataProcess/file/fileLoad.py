from Lib.Common.basicFunction import *


class FileLoader:
    def __init__(self, config):
        super().__init__()
        self.file_root_path = config['system']['file_root_path']
        self.compile_code(config['system']['compile'])
        self.all_c, self.all_h = self.get_all_code()
        self.add_c = []
        self.global_h = []
        self.tcee_lib = []
        self.c_lst, self.h_lst = self.get_source_file()
        self.flash_usage = self.get_program_code()

    def compile_code(self, cmd):
        root = os.getcwd()  # 작업 후 원래 경로로 회귀
        os.chdir(os.path.join(self.file_root_path, 'Appl'))  # build를 위한 작업 경로 변경
        if 'build' in cmd:
            os.system(cmd)  # build 실행
        os.chdir(root)  # 작업 후 원래 경로로 회귀

    def get_source_file(self):
        c_lst = []
        h_lst = []

        for fp in self._get_sw_file_directory():
            for (root, directories, files) in os.walk(fp):
                for file in files:
                    file_path = os.path.join(root, file)
                    if '.c' in file[-2:]:
                        c_lst.append(file_path)
                    elif '.h' in file[-2:]:
                        h_lst.append(file_path)
        # 모든 파일 리스트 업데이트
        c_lst += self.add_c
        h_lst += self.global_h
        # 반복 되는 데이터 제거
        return list(set(c_lst)), list(set(h_lst))

    def get_program_code(self):
        obj_lst = []
        fp = os.path.join(self.file_root_path, 'Appl', 'BuildTempFiles', 'CMakeFiles')
        for (root, directories, files) in os.walk(fp):
            for file in files:
                file_path = os.path.join(root, file)
                if '.obj' in file:
                    obj_lst.append([file.replace('.obj', ''), os.path.getsize(file_path)])
        flash_usage = pd.DataFrame(obj_lst, columns=['Component', 'Program_Code'])
        isdir_and_make('./result/usage')
        export_csv_dataframe(flash_usage, './result/usage', 'program_code')
        return flash_usage

    def get_all_code(self):
        all_c_lst = []
        all_h_lst = []
        for (root, directories, files) in os.walk(self.file_root_path):
            for file in files:
                file_path = os.path.join(root, file)
                if '.c' in file[-2:]:
                    all_c_lst.append(file_path)
                elif '.h' in file[-2:]:
                    all_h_lst.append(file_path)
        return all_c_lst, all_h_lst

    def _get_sw_file_directory(self):
        with open('./config/code_list.txt', 'r', encoding='utf-8') as file:
            lines = "".join(file.readlines())
        paths = []
        tcee_tree = False
        for path in lines.split('\n'):
            if path != '' and '##' not in path:
                if not tcee_tree:
                    if '.c' in path[-2:]:
                        self.add_c.append(self.all_c[self._get_index(self.all_c, path)])
                    elif '.h' in path[-2:]:
                        self.global_h.append(self.all_h[self._get_index(self.all_h, path)])
                    else:
                        paths.append(os.path.join(self.file_root_path, path))
                else:
                    self.tcee_lib += [c_file for c_file in self.all_c if path in c_file]

            if '## tceetree' in path:
                tcee_tree = True
        return paths

    # noinspection PyMethodMayBeStatic
    def _get_index(self, lst_str, sub_str):
        idx = 0
        for idx, string in enumerate(lst_str):
            if sub_str in string:
                break
        return idx
# This is a new line that ends the file
