from templates import *
from Qt.ImageQt import *
from Qt.DisplayQt import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # SET AS IMAGE AND DISPLAY WIDGETS
        self.image = ImageWindow()
        self.display = DisplayWindow()

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # SET HOME PAGE AND SELECT MENU
        self.ui.stackedWidget.addWidget(self.image)
        self.ui.stackedWidget.addWidget(self.display)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.btn_home.setStyleSheet(UIFunctions.selectMenu(self.ui.btn_home.styleSheet()))

        # QTableWidget PARAMETERS
        # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # TOGGLE MENU
        self.ui.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # LEFT MENUS
        self.ui.btn_home.clicked.connect(self.func_btn_home)
        self.ui.btn_image.clicked.connect(self.func_btn_image)
        self.ui.btn_display.clicked.connect(self.func_btn_display)
        self.ui.btn_save.clicked.connect(self.func_btn_save)

        # EXTRA LEFT BOX
        self.ui.toggleLeftBox.clicked.connect(lambda: UIFunctions.toggleLeftBox(self, True))
        self.ui.extraCloseColumnBtn.clicked.connect(lambda: UIFunctions.toggleLeftBox(self, True))

        # EXTRA RIGHT BOX
        self.ui.settingsTopBtn.clicked.connect(lambda: UIFunctions.toggleRightBox(self, True))

        # WINDOW CHANGE BUTTON
        self.image.ui_image.btn_display_image.clicked.connect(self.func_btn_display_image)
        self.display.ui_display.btn_image_process.clicked.connect(self.func_btn_image_process)

        # SHOW APP
        self.show()

        # SET CUSTOM THEME
        self._set_custom_theme(False)

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

    def func_btn_image(self):
        # SHOW WIDGETS PAGE
        self.ui.stackedWidget.setCurrentWidget(self.image)
        UIFunctions.resetStyle(self, "btn_image")
        self.sender().setStyleSheet(UIFunctions.selectMenu(self.sender().styleSheet()))

    def func_btn_display(self):
        # SHOW NEW PAGE
        self.ui.stackedWidget.setCurrentWidget(self.display)  # SET PAGE

        UIFunctions.resetStyle(self, "btn_display")  # RESET ANOTHERS BUTTONS SELECTED
        self.sender().setStyleSheet(UIFunctions.selectMenu(self.sender().styleSheet()))  # SELECT MENU

        if self.image.request_display is True:
            self.display.result_path = self.image.fiber.result_path
            self.display.display_img()
            self.image.request_display = False

    def func_btn_display_image(self):
        self.ui.btn_display.click()

    def func_btn_image_process(self):
        self.ui.btn_image.click()

    def func_btn_save(self):
        print("Save BTN clicked!")

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