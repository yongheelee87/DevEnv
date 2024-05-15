import logging
from templates import *
from Lib.Common import logging_print
# Qt Window
from . ConfigureQt import ConfigureWindow
from . InstQt import InstWindow
from . MeasureQt import MeasureWindow
from . TestCaseQt import TestCaseWindow
from . BlfAnalysisQt import BlfAnalysisWindow


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


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        logTextBox = QTextEditLogger(self.ui.pText_log)
        logTextBox.setFormatter(logging.Formatter('[%(asctime)s] %(message)s', "%Y-%m-%d %H:%M:%S"))
        logging.getLogger().addHandler(logTextBox)
        logging.getLogger().setLevel(logging.INFO)

        # SET AS IMAGE AND DISPLAY WIDGETS
        self.testcase = TestCaseWindow()
        self.measure = MeasureWindow()
        self.blf = BlfAnalysisWindow()
        self.inst = InstWindow()
        self.config = ConfigureWindow()

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # SET HOME PAGE AND SELECT MENU
        self.ui.stackedWidget.addWidget(self.measure)
        self.ui.stackedWidget.addWidget(self.testcase)
        self.ui.stackedWidget.addWidget(self.inst)
        self.ui.stackedWidget.addWidget(self.blf)
        self.ui.stackedWidget.addWidget(self.config)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.btn_home.setStyleSheet(UIFunctions.selectMenu(self.ui.btn_home.styleSheet()))

        # QTableWidget PARAMETERS
        # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # TOGGLE MENU
        self.ui.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # LEFT MENUS
        self.ui.btn_home.clicked.connect(self.func_btn_home)
        self.ui.btn_testcase.clicked.connect(self.func_btn_testcase)
        self.ui.btn_measure.clicked.connect(self.func_btn_measure)
        self.ui.btn_blf_analysis.clicked.connect(self.func_btn_blf_analysis)
        self.ui.btn_instrument.clicked.connect(self.func_btn_instrument)

        # EXTRA LEFT BOX
        self.ui.toggleLeftBox.clicked.connect(lambda: UIFunctions.toggleLeftBox(self, True))
        self.ui.extraCloseColumnBtn.clicked.connect(lambda: UIFunctions.toggleLeftBox(self, True))
        self.ui.btn_configure.clicked.connect(self.func_btn_configure)

        # EXTRA RIGHT BOX
        self.ui.settingsTopBtn.clicked.connect(lambda: UIFunctions.toggleRightBox(self, True))

        # SHOW APP
        self.show()

        # SET CUSTOM THEME
        self._set_custom_theme(False)

        logging_print(".... SW TEST Automation Initialization Completed.....\n")

    def _set_custom_theme(self, useCustomTheme: bool):
        # SET CUSTOM THEME
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

    def func_btn_home(self):
        # SHOW HOME PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        UIFunctions.resetStyle(self, "btn_home")
        self.sender().setStyleSheet(UIFunctions.selectMenu(self.sender().styleSheet()))

    def func_btn_testcase(self):
        # SHOW WIDGETS PAGE
        self.ui.stackedWidget.setCurrentWidget(self.testcase)
        UIFunctions.resetStyle(self, "btn_testcase")
        self.sender().setStyleSheet(UIFunctions.selectMenu(self.sender().styleSheet()))

    def func_btn_measure(self):
        # SHOW NEW PAGE
        self.ui.stackedWidget.setCurrentWidget(self.measure)  # SET PAGE
        UIFunctions.resetStyle(self, "btn_measure")  # RESET ANOTHERS BUTTONS SELECTED
        self.sender().setStyleSheet(UIFunctions.selectMenu(self.sender().styleSheet()))  # SELECT MENU

    def func_btn_blf_analysis(self):
        # SHOW NEW PAGE
        self.ui.stackedWidget.setCurrentWidget(self.blf)  # SET PAGE
        UIFunctions.resetStyle(self, "btn_blf_analysis")  # RESET ANOTHERS BUTTONS SELECTED
        self.sender().setStyleSheet(UIFunctions.selectMenu(self.sender().styleSheet()))  # SELECT MENU

    def func_btn_instrument(self):
        self.ui.stackedWidget.setCurrentWidget(self.inst)  # SET PAGE
        UIFunctions.resetStyle(self, "btn_instrument")  # RESET ANOTHERS BUTTONS SELECTED
        self.sender().setStyleSheet(UIFunctions.selectMenu(self.sender().styleSheet()))  # SELECT MENU

    def func_btn_configure(self):
        self.ui.stackedWidget.setCurrentWidget(self.config)  # SET PAGE

    # RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

        # PRINT MOUSE EVENTS
        '''
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        '''

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
