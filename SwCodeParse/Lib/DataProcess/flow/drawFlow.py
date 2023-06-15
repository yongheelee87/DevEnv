from Lib.Common.basicFunction import *


class DrawFlow:
    def __init__(self, c_files, tcee_lib):
        super().__init__()
        self.c_files = c_files
        self.tceetree_lib = tcee_lib

    def run_flow(self):
        self._copy_source_code()  # 소스 코드 복사
        self._tceetree()  # run tceetree

        # Draw Flow diagram via valve for SW UDS
        for c_file in self.c_files:
            self._valve(c_file)

    def _tceetree(self):
        root = os.getcwd()  # 작업 후 원래 경로로 회귀
        os.chdir('./tool/tceetree')  # Tceetree작업을 위한 경로 변경
        os.system("DrawArchitectures_external.bat")  # Draw External 실행
        '''
        os.system("DrawArchitectures_internal.bat")  # Draw Internal 실행
        '''
        isdir_and_make(os.path.join(root, 'result/pngTceeTree'))
        self._move_png('./', os.path.join(root, 'result/pngTceeTree'))
        os.chdir(root)  # 작업 후 원래 경로로 회귀
        logging_print("DONE: draw tceetree call flow relationship\n")

    def _valve(self, c_file):
        root = os.getcwd()  # 작업 후 원래 경로로 회귀
        os.chdir('./tool/valve')  # Tceetree작업을 위한 경로 변경

        c_file_name = os.path.basename(c_file)
        logging_print("......... Draw Valve : {} .........".format(c_file_name))
        with open('./list.txt', 'w') as f:
            c_file += '\n'
            f.write(c_file)
        os.system("valve list.txt")
        isdir_and_make(os.path.join(root, 'result/pngValve'))
        self._move_png('./result', os.path.join(root, 'result/pngValve/{}'.format(c_file_name.replace('.c', ''))))
        os.chdir(root)  # 작업 후 원래 경로로 회귀

    def _copy_source_code(self):
        root = os.getcwd()  # 작업 후 원래 경로로 회귀
        os.chdir('./tool/tceetree')  # Tceetree작업을 위한 경로 변경
        logging_print('Current Dir: {}'.format(os.getcwd()))
        des = './src'
        if os.path.exists(des):
            shutil.rmtree(des)  # 지정된 폴더와 하위 디렉토리 폴더, 파일를 모두 삭제
        isdir_and_make(des)

        for c_file in list(set(self.c_files + self.tceetree_lib)):
            shutil.copy2(c_file, des)
        os.chdir(root)  # 작업 후 원래 경로로 회귀
        logging_print("DONE: copy source codes\n")

    # noinspection PyMethodMayBeStatic
    def _move_png(self, src, des):
        png_list = [os.path.join(src, i) for i in os.listdir(src) if '.png' in i]
        isdir_and_make(des)
        for png in png_list:
            shutil.move(png, des)
# This is a new line that ends the file
