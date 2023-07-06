from templates import *
from Lib.ImageProcess.fiber_detect import *


class DisplayWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # SET AS IMAGE WIDGETS
        self.ui_display = Ui_display()
        self.ui_display.setupUi(self)

        self.result_path = './data/result'

        self.connectBtnInit()
    def connectBtnInit(self):
        self.ui_display.btn_open_file.clicked.connect(self.func_btn_open_file)
        self.ui_display.btn_result.clicked.connect(self.func_btn_result)

    def display_img(self):
        self._update_file_path()

        img_base_name = os.path.basename(self.result_path)

        origin_pix = QPixmap('{}/Origin_{}.jpg'.format(self.result_path, img_base_name))
        fiber_pix = QPixmap('{}/Fiber_{}.jpg'.format(self.result_path, img_base_name))

        self.ui_display.label_origin.setPixmap(origin_pix)
        self.ui_display.label_fiber.setPixmap(fiber_pix)

        df_fiber = pd.read_csv('{}/Fiber_{}.csv'.format(self.result_path, img_base_name), dtype=object, encoding='utf-8', index_col=0)
        result_txt = "[{}]   Area for Fiber: {}%,   Area for Void: {}%"\
            .format(img_base_name, df_fiber.loc['Percentage of total area', 'Fiber'], df_fiber.loc['Percentage of total area', 'Void'])
        self.ui_display.label_csv.setText(result_txt)

    def func_btn_open_file(self):
        self.result_path = QFileDialog.getExistingDirectory(self, 'Select Directory', './data/result')
        if self.result_path:
            print("Selected Result Folder: {}\n".format(self.result_path))
            # Display Image based on the selected result folder
            self.display_img()

    def func_btn_result(self):
        open_path(self.result_path)

    def _update_file_path(self):
        self.ui_display.line_file_path.setText(self.result_path)
