# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QComboBox, QFrame, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout, QWidget, QSpacerItem

from . resources_rc import *


class Ui_testcase(object):
    def setupUi(self, testcase):
        if not testcase.objectName():
            testcase.setObjectName(u"testcase")
        testcase.resize(961, 926)
        testcase.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 11pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(113, 192, 217);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Label */\n"
"#label_title { font: 63 12pt \"Segoe UI Semibold\";}\n"
"#label_project { font: 63 12pt \"Segoe UI Semibold\";}\n"
"#label_testcase { font: 63 11pt \"Segoe UI Semibold\";}\n"
"#label_testmode { font: 63 11pt \"Segoe UI Semibold\";}\n"
"#label_mapscript { font: 63 11pt \"Segoe UI Semibold\";}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	backgr"
                        "ound-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(147, 207, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid"
                        " rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(113, 192, 217);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(113, 192, 217);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainT"
                        "extEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(147, 207, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius:"
                        " 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(147, 207, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
""
                        "    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */"
                        "\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	"
                        "border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(113, 192, 217);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(147, 207, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(147, 181, 249);\n"
"}\n"
"QSlider::handle:horizonta"
                        "l:pressed {\n"
"    background-color: rgb(113, 192, 217);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(147, 207, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(147, 181, 249);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(113, 192, 217);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(113, 192, 217);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(113, 192, 217);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(113, 192, 217);\n"
"	background-"
                        "color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(147, 207, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"SpinBox */\n"
"QSpinBox {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QSpinBox:hover {	\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(81, 176, 98);\n"
"}\n"
"\n"
"QSpinBox::up-button { width: 32px; }\n"
"QSpinBox::down-button { width: 32px; }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 5px solid rgb(81, 176, 98);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 5px solid "
                        "rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(testcase)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.bgApp = QFrame(testcase)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QWidget(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.row_1 = QFrame(self.pagesContainer)
        self.row_1.setObjectName(u"row_1")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.row_1.sizePolicy().hasHeightForWidth())
        self.row_1.setSizePolicy(sizePolicy)
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_title = QLabel(self.frame_title_wid_1)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.label_title)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content_wid_1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_project = QLabel(self.frame_content_wid_1)
        self.label_project.setObjectName(u"label_project")
        self.label_project.setMinimumSize(QSize(65, 0))
        self.label_project.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_project.setLineWidth(1)
        self.label_project.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_project)

        self.cbox_project = QComboBox(self.frame_content_wid_1)
        self.cbox_project.addItem("")
        self.cbox_project.addItem("")
        self.cbox_project.setObjectName(u"cbox_project")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cbox_project.sizePolicy().hasHeightForWidth())
        self.cbox_project.setSizePolicy(sizePolicy1)
        self.cbox_project.setMinimumSize(QSize(120, 30))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.cbox_project.setFont(font1)
        self.cbox_project.setLayoutDirection(Qt.LeftToRight)
        self.cbox_project.setStyleSheet(u"QComboBox\n"
"{\n"
"background-color: rgb(40, 44, 52);\n"
"selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px solid transparent;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"selection-background-color: rgb(170, 170, 255);\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:hover\n"
"{\n"
"border: 4px solid green;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"border-width: 0px;\n"
"}\n"
"")
        self.cbox_project.setFrame(True)

        self.horizontalLayout.addWidget(self.cbox_project)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_Result_Folder = QPushButton(self.frame_content_wid_1)
        self.btn_Result_Folder.setObjectName(u"btn_Result_Folder")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_Result_Folder.sizePolicy().hasHeightForWidth())
        self.btn_Result_Folder.setSizePolicy(sizePolicy2)
        self.btn_Result_Folder.setMinimumSize(QSize(150, 40))
        self.btn_Result_Folder.setFont(font1)
        self.btn_Result_Folder.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_Result_Folder.setCheckable(False)
        self.btn_Result_Folder.setChecked(False)

        self.horizontalLayout.addWidget(self.btn_Result_Folder)

        self.btn_Map_Mode = QPushButton(self.frame_content_wid_1)
        self.btn_Map_Mode.setObjectName(u"btn_Map_Mode")
        sizePolicy2.setHeightForWidth(self.btn_Map_Mode.sizePolicy().hasHeightForWidth())
        self.btn_Map_Mode.setSizePolicy(sizePolicy2)
        self.btn_Map_Mode.setMinimumSize(QSize(150, 40))
        self.btn_Map_Mode.setFont(font1)
        self.btn_Map_Mode.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_Map_Mode.setCheckable(False)
        self.btn_Map_Mode.setChecked(False)

        self.horizontalLayout.addWidget(self.btn_Map_Mode)

        self.btn_Project_CSV = QPushButton(self.frame_content_wid_1)
        self.btn_Project_CSV.setObjectName(u"btn_Project_CSV")
        sizePolicy2.setHeightForWidth(self.btn_Project_CSV.sizePolicy().hasHeightForWidth())
        self.btn_Project_CSV.setSizePolicy(sizePolicy2)
        self.btn_Project_CSV.setMinimumSize(QSize(150, 40))
        self.btn_Project_CSV.setFont(font1)
        self.btn_Project_CSV.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_Project_CSV.setCheckable(False)
        self.btn_Project_CSV.setChecked(False)

        self.horizontalLayout.addWidget(self.btn_Project_CSV)


        self.verticalLayout_9.addLayout(self.horizontalLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout_7.addWidget(self.row_1)

        self.row_2 = QFrame(self.pagesContainer)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.row_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content = QFrame(self.row_2)
        self.frame_div_content.setObjectName(u"frame_div_content")
        self.frame_div_content.setFrameShape(QFrame.StyledPanel)
        self.frame_div_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_div_content)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_content_wid_2 = QFrame(self.frame_div_content)
        self.frame_content_wid_2.setObjectName(u"frame_content_wid_2")
        self.frame_content_wid_2.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_content_wid_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_testcase_num = QLineEdit(self.frame_content_wid_2)
        self.line_testcase_num.setObjectName(u"line_testcase_num")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line_testcase_num.sizePolicy().hasHeightForWidth())
        self.line_testcase_num.setSizePolicy(sizePolicy3)
        self.line_testcase_num.setMinimumSize(QSize(150, 40))
        self.line_testcase_num.setFont(font1)
        self.line_testcase_num.setLayoutDirection(Qt.LeftToRight)
        self.line_testcase_num.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.line_testcase_num.setFrame(True)
        self.line_testcase_num.setAlignment(Qt.AlignCenter)
        self.line_testcase_num.setReadOnly(False)

        self.gridLayout_2.addWidget(self.line_testcase_num, 1, 0, 1, 1)

        self.label_testmode = QLabel(self.frame_content_wid_2)
        self.label_testmode.setObjectName(u"label_testmode")
        self.label_testmode.setStyleSheet(u"")
        self.label_testmode.setLineWidth(1)
        self.label_testmode.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_testmode, 0, 4, 1, 3)

        self.cbox_Test_mode = QComboBox(self.frame_content_wid_2)
        self.cbox_Test_mode.setObjectName(u"cbox_Test_mode")
        sizePolicy3.setHeightForWidth(self.cbox_Test_mode.sizePolicy().hasHeightForWidth())
        self.cbox_Test_mode.setSizePolicy(sizePolicy3)
        self.cbox_Test_mode.setMinimumSize(QSize(150, 40))
        self.cbox_Test_mode.setFont(font1)
        self.cbox_Test_mode.setStyleSheet(u"border: 1px solid transparent;\n"
"background-color: rgb(33, 37, 43);")

        self.gridLayout_2.addWidget(self.cbox_Test_mode, 1, 4, 1, 1)

        self.btn_testcase = QPushButton(self.frame_content_wid_2)
        self.btn_testcase.setObjectName(u"btn_testcase")
        self.btn_testcase.setMinimumSize(QSize(150, 40))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        self.btn_testcase.setFont(font2)
        self.btn_testcase.setStyleSheet(u"QPushButton {\n"
"	font-weight:500;\n"
"	color:black;\n"
"	border: 1px solid black;\n"
"	background-color: #c8f7c8;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #42f566;\n"
"	border: 2px solid #c8f7c8;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 5px solid transparent;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/images/start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_testcase.setIcon(icon)
        self.btn_testcase.setCheckable(True)
        self.btn_testcase.setChecked(True)

        self.gridLayout_2.addWidget(self.btn_testcase, 1, 1, 1, 1)

        self.label_testcase = QLabel(self.frame_content_wid_2)
        self.label_testcase.setObjectName(u"label_testcase")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Semibold"])
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        self.label_testcase.setFont(font3)
        self.label_testcase.setStyleSheet(u"")
        self.label_testcase.setLineWidth(1)
        self.label_testcase.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_testcase, 0, 0, 1, 3)

        self.btn_testmode = QPushButton(self.frame_content_wid_2)
        self.btn_testmode.setObjectName(u"btn_testmode")
        self.btn_testmode.setMinimumSize(QSize(150, 40))
        self.btn_testmode.setFont(font2)
        self.btn_testmode.setStyleSheet(u"QPushButton {\n"
"	font-weight:500;\n"
"	color:black;\n"
"	border: 1px solid black;\n"
"	background-color: #c8f7c8;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #42f566;\n"
"	border: 2px solid #c8f7c8;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 5px solid transparent;\n"
"}")
        self.btn_testmode.setIcon(icon)
        self.btn_testmode.setCheckable(True)
        self.btn_testmode.setChecked(True)

        self.gridLayout_2.addWidget(self.btn_testmode, 1, 5, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(70, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_2)


        self.verticalLayout_5.addWidget(self.frame_content_wid_2)


        self.verticalLayout_4.addWidget(self.frame_div_content)


        self.verticalLayout_7.addWidget(self.row_2)

        self.row_3 = QFrame(self.pagesContainer)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.row_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_2 = QFrame(self.row_3)
        self.frame_div_content_2.setObjectName(u"frame_div_content_2")
        self.frame_div_content_2.setFrameShape(QFrame.StyledPanel)
        self.frame_div_content_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_div_content_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_div_content_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_name_2 = QLabel(self.frame)
        self.label_name_2.setObjectName(u"label_name_2")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(True)
        self.label_name_2.setFont(font4)
        self.label_name_2.setStyleSheet(u"color: red;")

        self.gridLayout.addWidget(self.label_name_2, 0, 0, 1, 3)

        self.label_mapscript = QLabel(self.frame)
        self.label_mapscript.setObjectName(u"label_mapscript")
        self.label_mapscript.setFont(font3)
        self.label_mapscript.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_mapscript, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.btn_Script_Folder = QPushButton(self.frame)
        self.btn_Script_Folder.setObjectName(u"btn_Script_Folder")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_Script_Folder.sizePolicy().hasHeightForWidth())
        self.btn_Script_Folder.setSizePolicy(sizePolicy4)
        self.btn_Script_Folder.setMinimumSize(QSize(150, 40))
        self.btn_Script_Folder.setFont(font1)
        self.btn_Script_Folder.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout.addWidget(self.btn_Script_Folder, 1, 2, 1, 1)

        self.btn_apply = QPushButton(self.frame)
        self.btn_apply.setObjectName(u"btn_apply")
        sizePolicy4.setHeightForWidth(self.btn_apply.sizePolicy().hasHeightForWidth())
        self.btn_apply.setSizePolicy(sizePolicy4)
        self.btn_apply.setMinimumSize(QSize(150, 40))
        self.btn_apply.setFont(font1)
        self.btn_apply.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout.addWidget(self.btn_apply, 1, 3, 1, 1)

        self.pText_map_test = QPlainTextEdit(self.frame)
        self.pText_map_test.setObjectName(u"pText_map_test")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pText_map_test.sizePolicy().hasHeightForWidth())
        self.pText_map_test.setSizePolicy(sizePolicy5)
        self.pText_map_test.setFont(font1)

        self.gridLayout.addWidget(self.pText_map_test, 2, 0, 1, 4)


        self.verticalLayout_10.addLayout(self.gridLayout)


        self.verticalLayout_11.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_div_content_2)


        self.verticalLayout_7.addWidget(self.row_3)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_3.addWidget(self.bgApp)


        self.retranslateUi(testcase)

        QMetaObject.connectSlotsByName(testcase)
    # setupUi

    def retranslateUi(self, testcase):
        testcase.setWindowTitle(QCoreApplication.translate("testcase", u"testcase", None))
        self.label_title.setText(QCoreApplication.translate("testcase", u"TEST CASE", None))
        self.label_project.setText(QCoreApplication.translate("testcase", u"Project : ", None))
        self.cbox_project.setItemText(0, QCoreApplication.translate("testcase", u"CTCW", None))
        self.cbox_project.setItemText(1, QCoreApplication.translate("testcase", u"SWA", None))

        self.btn_Result_Folder.setText(QCoreApplication.translate("testcase", u"Result", None))
        self.btn_Map_Mode.setText(QCoreApplication.translate("testcase", u"Map Mode", None))
        self.btn_Project_CSV.setText(QCoreApplication.translate("testcase", u"Project CSV", None))
        self.line_testcase_num.setText("")
        self.label_testmode.setText(QCoreApplication.translate("testcase", u"TEST MODE", None))
        self.btn_testcase.setText(QCoreApplication.translate("testcase", u"RUN", None))
        self.label_testcase.setText(QCoreApplication.translate("testcase", u"CASE NUMBER", None))
        self.btn_testmode.setText(QCoreApplication.translate("testcase", u"RUN", None))
        self.label_name_2.setText(QCoreApplication.translate("testcase", u"Note: It can NOT be applied unless the apply button is pressed", None))
        self.label_mapscript.setText(QCoreApplication.translate("testcase", u"MAP SCRIPT", None))
        self.btn_Script_Folder.setText(QCoreApplication.translate("testcase", u"Script", None))
        self.btn_apply.setText(QCoreApplication.translate("testcase", u"Apply", None))
    # retranslateUi

