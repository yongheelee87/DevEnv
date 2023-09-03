import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from Qt.measureQt import *
from Qt.instQt import *
from Qt.ConfigureQt import *
from Qt.SwTestQt import *
from Lib.Common.basicFunction import *

form_class = uic.loadUiType("./Qt/static/ui/Main.ui")[0]


class QTextEditLogger(logging.Handler):
    def __init__(self, textWidget):
        super().__init__()
        self.widget = textWidget
        self.widget.setReadOnly(True)
        self.widget.verticalScrollBar().setValue(self.widget.verticalScrollBar().maximum())

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)
        self.widget.ensureCursorVisible()
        self.widget.viewport().update()


class WindowClass(QMainWindow, form_class):
    def __init__(self, version):
        super().__init__()
        self.setupUi(self)

        logTextBox = QTextEditLogger(self.pText_Log)
        logTextBox.setFormatter(logging.Formatter('%(asctime)s %(message)s', "%Y-%m-%d %H:%M:%S"))
        logging.getLogger().addHandler(logTextBox)
        logging.getLogger().setLevel(logging.INFO)
        self.version = version

        # QWidget 선언
        self.measureWidget = MeasureView()
        self.instWidget = InstView()
        self.configureWidget = ConfigureView()
        self.swTestWidget = SwTestView()

        self.backgroundInit()
        self.connectBtnInit()
        self.triggerActInit()
        self.connectClass()

        logging_print(".... SW TEST Automation Initialization Completed.....\n")

    def closeEvent(self, event):
        self.activateWindow()
        quit_msg = "프로그램을 종료하시겠습니까?  "
        reply = QMessageBox.question(self, "종료 확인", quit_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            '''
            # Pyqt App 종료
            self.close()
            self.swTestWidget.close()
            self.measureWidget.close()
            self.instWidget.close()
            self.configureWidget.close()
            '''
            QCoreApplication.instance().quit()
            logging_print(".... End SW TEST Automation.....\n")
        else:
            event.ignore()

    def backgroundInit(self):
        title = "SW TEST Automation {} for SDV".format(self.version)
        self.setWindowTitle(title)

    def connectBtnInit(self):
        self.btn_swTest.clicked.connect(self.func_btn_swTest)
        self.btn_Measurement.clicked.connect(self.func_btn_Measurement)
        self.btn_Instrument.clicked.connect(self.func_btn_Instrument)
        self.btn_configuration.clicked.connect(self.func_btn_configuration)

        self.btn_Consol.clicked.connect(self.func_btn_Consol)

    def triggerActInit(self):
        self.act_swTest.triggered.connect(self.func_btn_swTest)
        self.act_measurement.triggered.connect(self.func_btn_Measurement)
        self.act_instrument.triggered.connect(self.func_btn_Instrument)
        self.act_configuration.triggered.connect(self.func_btn_configuration)
        self.act_Exit.triggered.connect(QCoreApplication.instance().quit)
        self.act_info.triggered.connect(self.Information_event)

    def connectClass(self):
        # self.configureWidget.btn_apply.clicked.connect(self.measureWidget.load_measure_target)
        self.configureWidget.btn_apply.clicked.connect(self.measureWidget.update_measure_target)
        self.configureWidget.btn_apply.clicked.connect(self.instWidget.update_tbl_from_df)

    def func_btn_swTest(self):
        main_geometry = self.frameGeometry()
        self.swTestWidget.show_widget(main_geometry)

    def func_btn_Measurement(self):
        main_geometry = self.frameGeometry()
        self.measureWidget.show_widget(main_geometry)

    def func_btn_Instrument(self):
        main_geometry = self.frameGeometry()
        self.instWidget.show_widget(main_geometry)

    def func_btn_configuration(self):
        main_geometry = self.frameGeometry()
        self.configureWidget.show_widget(main_geometry)

    # noinspection PyMethodMayBeStatic
    def func_btn_Config_Folder(self):
        open_path('./data/config/')

    # noinspection PyMethodMayBeStatic
    def func_btn_Input_Folder(self):
        open_path('./data/input/')

    # noinspection PyMethodMayBeStatic
    def func_btn_Result_Folder(self):
        open_path('./data/result/')

    # noinspection PyMethodMayBeStatic
    def func_btn_Consol(self):
        # Consol창 연결
        main_win = get_window_with_loop("SW TEST Automation {} for Control TASK".format(self.version), 5000)
        consol_cmd = get_window_with_loop('cmd.exe', 5000)
        main_win.activate()
        if main_win is not None and consol_cmd is not None:
            consol_cmd.resizeTo(int(main_win.width * 1.3), main_win.height)
            consol_cmd.moveTo(main_win.left - int(consol_cmd.width * 0.985), main_win.top)
            consol_cmd.activate()

    def Information_event(self):
        qmsgBox = QMessageBox()
        qmsgBox.information(self, 'Software Information',
                            'Title: SW TEST Automation \n\nSoftware Version: {}\n\nDate of Release: 04/13/2023\n\nCopyright (c) Control Task\n'.format(
                                self.version))
