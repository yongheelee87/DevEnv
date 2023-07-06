from templates import *
from Lib.ImageProcess.fiber_detect import *


class ImageWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # SET AS IMAGE WIDGETS
        self.ui_image = Ui_image()
        self.ui_image.setupUi(self)

        self.fiber = FiberDetection()

        self.request_display = False

        self.connectBtnInit()
        self.connectLineInit()

        self.open_file_path = './data'

        self.set_initial_parameters()

    def connectBtnInit(self):
        self.ui_image.btn_open_file.clicked.connect(self.func_btn_open_file)
        self.ui_image.btn_start.clicked.connect(self.func_btn_start)
        self.ui_image.btn_result.clicked.connect(self.func_btn_result)

    def connectLineInit(self):
        self.ui_image.line_file_path.textChanged.connect(self.func_line_file_path)

    def func_btn_open_file(self):
        script_name = QFileDialog.getOpenFileNames(self, 'Open File', self.open_file_path, 'Image File(*.jpg *.png *.tif);; All File(*)')[0]
        if script_name:
            self.ui_image.line_file_path.setText(',  '.join(script_name))
            self.fiber.img_names = script_name
            self.open_file_path = os.path.dirname(script_name[0])
            print("Current Image Files: {}\n".format(self.fiber.img_names))

    def func_btn_start(self):
        if self.fiber.img_names is not None:
            self.fiber.update_params(percent=self.ui_image.spBox_Percent.value(),
                                     colorThres=self.ui_image.spBox_colorThres.value(),
                                     areaThres=self.ui_image.spBox_areaThres.value(),
                                     colorVoidThres=self.ui_image.spBox_colorVoidThres.value(),
                                     areaVoidThres=self.ui_image.spBox_areaVoidThres.value(),
                                     dilateX=self.ui_image.spBox_dilateX.value(),
                                     dilateY=self.ui_image.spBox_dilateY.value(),
                                     ksizeX=self.ui_image.spBox_ksizeX.value(),
                                     ksizeY=self.ui_image.spBox_ksizeY.value(),
                                     white=self.ui_image.spBox_white.value())
            str_result = self.fiber.image_process()
            print(str_result)
            self.ui_image.pText_state.append(str_result)
            self.display_img()
            self.request_display = True
        else:
            print("There is No Loaded Image File\n")

    def func_btn_result(self):
        open_path(self.fiber.result_path)

    def func_line_file_path(self):
        if self.ui_image.line_file_path.text():
            self.ui_image.label_state.setText('Ready to Start')
        else:
            self.ui_image.label_state.setText('No Selected Files')

    def display_img(self):
        img_base_name = os.path.basename(self.fiber.result_path)

        origin_pix = QPixmap('{}/Origin_{}.jpg'.format(self.fiber.result_path, img_base_name))
        fiber_pix = QPixmap('{}/Fiber_{}.jpg'.format(self.fiber.result_path, img_base_name))

        self.ui_image.label_origin.setPixmap(origin_pix)
        self.ui_image.label_fiber.setPixmap(fiber_pix)

    def set_initial_parameters(self):
        self.ui_image.spBox_Percent.setValue(self.fiber.bottom_crop)
        self.ui_image.hSlider_Percent.setValue(self.fiber.bottom_crop)
        self.ui_image.spBox_colorThres.setValue(self.fiber.color_threshold)
        self.ui_image.hSlider_colorThres.setValue(self.fiber.color_threshold)
        self.ui_image.spBox_areaThres.setValue(self.fiber.area_threshold)
        self.ui_image.hSlider_areaThres.setValue(self.fiber.area_threshold)
        self.ui_image.spBox_colorVoidThres.setValue(self.fiber.void_color_threshold)
        self.ui_image.hSlider_colorVoidThres.setValue(self.fiber.void_color_threshold)
        self.ui_image.spBox_areaVoidThres.setValue(self.fiber.void_area_threshold)
        self.ui_image.hSlider_areaVoidThres.setValue(self.fiber.void_area_threshold)
        self.ui_image.spBox_dilateX.setValue(self.fiber.dilate_x)
        self.ui_image.hSlider_dilateX.setValue(self.fiber.dilate_x)
        self.ui_image.spBox_dilateY.setValue(self.fiber.dilate_y)
        self.ui_image.hSlider_dilateY.setValue(self.fiber.dilate_y)
        self.ui_image.spBox_ksizeX.setValue(self.fiber.ksize_x)
        self.ui_image.hSlider_ksizeX.setValue(self.fiber.ksize_x)
        self.ui_image.spBox_ksizeY.setValue(self.fiber.ksize_y)
        self.ui_image.hSlider_ksizeY.setValue(self.fiber.ksize_y)
        self.ui_image.spBox_white.setValue(self.fiber.white_sense)
        self.ui_image.hSlider_white.setValue(self.fiber.white_sense)
