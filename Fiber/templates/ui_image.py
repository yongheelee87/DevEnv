# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *

class Ui_image(object):
    def setupUi(self, image):
        if not image.objectName():
            image.setObjectName(u"image")
        image.resize(1154, 919)
        image.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
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
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Label */\n"
"#label_open_f"
                        "ile { font: 63 12pt \"Segoe UI Semibold\";}\n"
"#label_fiber { font: 63 12pt \"Segoe UI Semibold\";}\n"
"#label_params { font: 63 12pt \"Segoe UI Semibold\";}\n"
"\n"
"/* Bottom Bar */\n"
"#frame_manip QLabel { font: 63 11pt \"Segoe UI Semibold\";}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
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
"    border-r"
                        "ight: 1px solid rgb(44, 49, 60);\n"
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
"    border: 1px solid rgb(44, 49, 60);\n"
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
"/* ////////////////////////////////////////////////////////////////////"
                        "/////////////////////////////\n"
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
"QPlainTextEdit:hover {\n"
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
"    b"
                        "order: none;\n"
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
"    border-bottom-left-radius: 4px;\n"
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
" QScrollBar::ad"
                        "d-line:vertical {\n"
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
"    background: rgb(44, 4"
                        "9, 60);\n"
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
"RadioButton */\n"
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
"	b"
                        "order: 2px solid rgb(33, 37, 43);\n"
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
"	border-bottom-right-radius: 3px;	\n"
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
"	background-color: rgb(52, 59"
                        ", 72);\n"
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
"QSlider::handle:horizontal:pressed {\n"
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
"QSlider::handle:vertical:pre"
                        "ssed {\n"
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
"	background-color: rgb(44, 49, 60);\n"
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
"/* /////////////////////////////////////////////////////////////////////////////"
                        "////////////////////\n"
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
"	border: 5px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(image)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.bgApp = QFrame(image)
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
        self.verticalLayout = QVBoxLayout(self.pagesContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
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
        sizePolicy.setHeightForWidth(self.frame_div_content_1.sizePolicy().hasHeightForWidth())
        self.frame_div_content_1.setSizePolicy(sizePolicy)
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
        self.label_open_file = QLabel(self.frame_title_wid_1)
        self.label_open_file.setObjectName(u"label_open_file")
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_open_file.setFont(font)
        self.label_open_file.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.label_open_file)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.line_file_path = QLineEdit(self.frame_content_wid_1)
        self.line_file_path.setObjectName(u"line_file_path")
        self.line_file_path.setMinimumSize(QSize(0, 30))
        self.line_file_path.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.line_file_path, 0, 0, 1, 1)

        self.btn_open_file = QPushButton(self.frame_content_wid_1)
        self.btn_open_file.setObjectName(u"btn_open_file")
        self.btn_open_file.setMinimumSize(QSize(150, 30))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.btn_open_file.setFont(font1)
        self.btn_open_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_file.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_file.setIcon(icon)

        self.gridLayout.addWidget(self.btn_open_file, 0, 1, 1, 1)

        self.label_open_descript = QLabel(self.frame_content_wid_1)
        self.label_open_descript.setObjectName(u"label_open_descript")
        self.label_open_descript.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_open_descript.setLineWidth(1)
        self.label_open_descript.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_open_descript, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.line_3 = QFrame(self.pagesContainer)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 20))
        self.line_3.setAutoFillBackground(False)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.row_2 = QFrame(self.pagesContainer)
        self.row_2.setObjectName(u"row_2")
        sizePolicy.setHeightForWidth(self.row_2.sizePolicy().hasHeightForWidth())
        self.row_2.setSizePolicy(sizePolicy)
        self.row_2.setMinimumSize(QSize(0, 0))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.row_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.row_2)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 200))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_4 = QFrame(self.frame)
        self.frame_title_wid_4.setObjectName(u"frame_title_wid_4")
        self.frame_title_wid_4.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_4.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_title_wid_4)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_params = QLabel(self.frame_title_wid_4)
        self.label_params.setObjectName(u"label_params")
        self.label_params.setFont(font)
        self.label_params.setStyleSheet(u"")

        self.verticalLayout_28.addWidget(self.label_params)


        self.verticalLayout_4.addWidget(self.frame_title_wid_4)

        self.frame_manip = QFrame(self.frame)
        self.frame_manip.setObjectName(u"frame_manip")
        self.frame_manip.setMouseTracking(False)
        self.verticalLayout_9 = QVBoxLayout(self.frame_manip)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(40, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 2, 1)

        self.verticalSpacer_2 = QSpacerItem(40, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 4, 2, 1)

        self.verticalSpacer_3 = QSpacerItem(40, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 0, 7, 2, 1)

        self.verticalSpacer_4 = QSpacerItem(40, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 0, 10, 2, 1)

        self.label_10 = QLabel(self.frame_manip)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 0, 11, 1, 2)

        self.verticalSpacer_5 = QSpacerItem(40, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 0, 13, 2, 1)

        self.label_14 = QLabel(self.frame_manip)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_14, 0, 14, 1, 1)

        self.label_5 = QLabel(self.frame_manip)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.label = QLabel(self.frame_manip)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 1, 2, 1, 1)

        self.label_2 = QLabel(self.frame_manip)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 3, 1, 1)

        self.label_4 = QLabel(self.frame_manip)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 1, 5, 1, 1)

        self.label_3 = QLabel(self.frame_manip)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 1, 6, 1, 1)

        self.label_11 = QLabel(self.frame_manip)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_11, 1, 8, 1, 1)

        self.label_13 = QLabel(self.frame_manip)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_13, 1, 9, 1, 1)

        self.label_8 = QLabel(self.frame_manip)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 1, 11, 1, 1)

        self.label_9 = QLabel(self.frame_manip)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_9, 1, 12, 1, 1)

        self.label_15 = QLabel(self.frame_manip)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_15, 1, 14, 1, 1)

        self.spBox_Percent = QSpinBox(self.frame_manip)
        self.spBox_Percent.setObjectName(u"spBox_Percent")
        sizePolicy.setHeightForWidth(self.spBox_Percent.sizePolicy().hasHeightForWidth())
        self.spBox_Percent.setSizePolicy(sizePolicy)
        self.spBox_Percent.setMinimumSize(QSize(0, 30))
        self.spBox_Percent.setStyleSheet(u"")
        self.spBox_Percent.setWrapping(False)
        self.spBox_Percent.setFrame(False)
        self.spBox_Percent.setAlignment(Qt.AlignCenter)
        self.spBox_Percent.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spBox_Percent.setMaximum(100)
        self.spBox_Percent.setValue(7)

        self.gridLayout_2.addWidget(self.spBox_Percent, 2, 0, 1, 1)

        self.spBox_colorThres = QSpinBox(self.frame_manip)
        self.spBox_colorThres.setObjectName(u"spBox_colorThres")
        sizePolicy.setHeightForWidth(self.spBox_colorThres.sizePolicy().hasHeightForWidth())
        self.spBox_colorThres.setSizePolicy(sizePolicy)
        self.spBox_colorThres.setMinimumSize(QSize(0, 30))
        self.spBox_colorThres.setMaximumSize(QSize(16777215, 16777215))
        self.spBox_colorThres.setFrame(False)
        self.spBox_colorThres.setAlignment(Qt.AlignCenter)
        self.spBox_colorThres.setMaximum(255)
        self.spBox_colorThres.setValue(250)

        self.gridLayout_2.addWidget(self.spBox_colorThres, 2, 2, 1, 1)

        self.spBox_areaThres = QSpinBox(self.frame_manip)
        self.spBox_areaThres.setObjectName(u"spBox_areaThres")
        sizePolicy.setHeightForWidth(self.spBox_areaThres.sizePolicy().hasHeightForWidth())
        self.spBox_areaThres.setSizePolicy(sizePolicy)
        self.spBox_areaThres.setMinimumSize(QSize(0, 30))
        self.spBox_areaThres.setFrame(False)
        self.spBox_areaThres.setAlignment(Qt.AlignCenter)
        self.spBox_areaThres.setMaximum(350)
        self.spBox_areaThres.setValue(10)

        self.gridLayout_2.addWidget(self.spBox_areaThres, 2, 3, 1, 1)

        self.spBox_colorVoidThres = QSpinBox(self.frame_manip)
        self.spBox_colorVoidThres.setObjectName(u"spBox_colorVoidThres")
        sizePolicy.setHeightForWidth(self.spBox_colorVoidThres.sizePolicy().hasHeightForWidth())
        self.spBox_colorVoidThres.setSizePolicy(sizePolicy)
        self.spBox_colorVoidThres.setMinimumSize(QSize(0, 30))
        self.spBox_colorVoidThres.setFrame(False)
        self.spBox_colorVoidThres.setAlignment(Qt.AlignCenter)
        self.spBox_colorVoidThres.setMaximum(255)
        self.spBox_colorVoidThres.setValue(210)

        self.gridLayout_2.addWidget(self.spBox_colorVoidThres, 2, 5, 1, 1)

        self.spBox_areaVoidThres = QSpinBox(self.frame_manip)
        self.spBox_areaVoidThres.setObjectName(u"spBox_areaVoidThres")
        sizePolicy.setHeightForWidth(self.spBox_areaVoidThres.sizePolicy().hasHeightForWidth())
        self.spBox_areaVoidThres.setSizePolicy(sizePolicy)
        self.spBox_areaVoidThres.setMinimumSize(QSize(0, 30))
        self.spBox_areaVoidThres.setFrame(False)
        self.spBox_areaVoidThres.setAlignment(Qt.AlignCenter)
        self.spBox_areaVoidThres.setMaximum(350)
        self.spBox_areaVoidThres.setValue(10)

        self.gridLayout_2.addWidget(self.spBox_areaVoidThres, 2, 6, 1, 1)

        self.spBox_dilateX = QSpinBox(self.frame_manip)
        self.spBox_dilateX.setObjectName(u"spBox_dilateX")
        sizePolicy.setHeightForWidth(self.spBox_dilateX.sizePolicy().hasHeightForWidth())
        self.spBox_dilateX.setSizePolicy(sizePolicy)
        self.spBox_dilateX.setMinimumSize(QSize(0, 30))
        self.spBox_dilateX.setFrame(False)
        self.spBox_dilateX.setAlignment(Qt.AlignCenter)
        self.spBox_dilateX.setMaximum(9)
        self.spBox_dilateX.setValue(1)

        self.gridLayout_2.addWidget(self.spBox_dilateX, 2, 8, 1, 1)

        self.spBox_dilateY = QSpinBox(self.frame_manip)
        self.spBox_dilateY.setObjectName(u"spBox_dilateY")
        sizePolicy.setHeightForWidth(self.spBox_dilateY.sizePolicy().hasHeightForWidth())
        self.spBox_dilateY.setSizePolicy(sizePolicy)
        self.spBox_dilateY.setMinimumSize(QSize(0, 30))
        self.spBox_dilateY.setFrame(False)
        self.spBox_dilateY.setAlignment(Qt.AlignCenter)
        self.spBox_dilateY.setMaximum(9)
        self.spBox_dilateY.setValue(1)

        self.gridLayout_2.addWidget(self.spBox_dilateY, 2, 9, 1, 1)

        self.spBox_ksizeX = QSpinBox(self.frame_manip)
        self.spBox_ksizeX.setObjectName(u"spBox_ksizeX")
        sizePolicy.setHeightForWidth(self.spBox_ksizeX.sizePolicy().hasHeightForWidth())
        self.spBox_ksizeX.setSizePolicy(sizePolicy)
        self.spBox_ksizeX.setMinimumSize(QSize(0, 30))
        self.spBox_ksizeX.setFrame(False)
        self.spBox_ksizeX.setAlignment(Qt.AlignCenter)
        self.spBox_ksizeX.setMaximum(30)
        self.spBox_ksizeX.setValue(6)

        self.gridLayout_2.addWidget(self.spBox_ksizeX, 2, 11, 1, 1)

        self.spBox_ksizeY = QSpinBox(self.frame_manip)
        self.spBox_ksizeY.setObjectName(u"spBox_ksizeY")
        sizePolicy.setHeightForWidth(self.spBox_ksizeY.sizePolicy().hasHeightForWidth())
        self.spBox_ksizeY.setSizePolicy(sizePolicy)
        self.spBox_ksizeY.setMinimumSize(QSize(0, 30))
        self.spBox_ksizeY.setFrame(False)
        self.spBox_ksizeY.setAlignment(Qt.AlignCenter)
        self.spBox_ksizeY.setMaximum(30)
        self.spBox_ksizeY.setValue(6)

        self.gridLayout_2.addWidget(self.spBox_ksizeY, 2, 12, 1, 1)

        self.spBox_white = QSpinBox(self.frame_manip)
        self.spBox_white.setObjectName(u"spBox_white")
        sizePolicy.setHeightForWidth(self.spBox_white.sizePolicy().hasHeightForWidth())
        self.spBox_white.setSizePolicy(sizePolicy)
        self.spBox_white.setMinimumSize(QSize(0, 30))
        self.spBox_white.setFrame(False)
        self.spBox_white.setAlignment(Qt.AlignCenter)
        self.spBox_white.setMaximum(250)
        self.spBox_white.setValue(100)

        self.gridLayout_2.addWidget(self.spBox_white, 2, 14, 1, 1)

        self.hSlider_Percent = QSlider(self.frame_manip)
        self.hSlider_Percent.setObjectName(u"hSlider_Percent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.hSlider_Percent.sizePolicy().hasHeightForWidth())
        self.hSlider_Percent.setSizePolicy(sizePolicy2)
        self.hSlider_Percent.setMaximum(100)
        self.hSlider_Percent.setValue(7)
        self.hSlider_Percent.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.hSlider_Percent, 3, 0, 1, 1)

        self.hSlider_colorThres = QSlider(self.frame_manip)
        self.hSlider_colorThres.setObjectName(u"hSlider_colorThres")
        sizePolicy2.setHeightForWidth(self.hSlider_colorThres.sizePolicy().hasHeightForWidth())
        self.hSlider_colorThres.setSizePolicy(sizePolicy2)
        self.hSlider_colorThres.setMaximum(255)
        self.hSlider_colorThres.setValue(250)
        self.hSlider_colorThres.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.hSlider_colorThres, 3, 2, 1, 1)

        self.hSlider_areaThres = QSlider(self.frame_manip)
        self.hSlider_areaThres.setObjectName(u"hSlider_areaThres")
        sizePolicy2.setHeightForWidth(self.hSlider_areaThres.sizePolicy().hasHeightForWidth())
        self.hSlider_areaThres.setSizePolicy(sizePolicy2)
        self.hSlider_areaThres.setMaximum(350)
        self.hSlider_areaThres.setValue(10)
        self.hSlider_areaThres.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.hSlider_areaThres, 3, 3, 1, 1)

        self.hSlider_colorVoidThres = QSlider(self.frame_manip)
        self.hSlider_colorVoidThres.setObjectName(u"hSlider_colorVoidThres")
        sizePolicy2.setHeightForWidth(self.hSlider_colorVoidThres.sizePolicy().hasHeightForWidth())
        self.hSlider_colorVoidThres.setSizePolicy(sizePolicy2)
        self.hSlider_colorVoidThres.setMaximum(255)
        self.hSlider_colorVoidThres.setValue(210)
        self.hSlider_colorVoidThres.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.hSlider_colorVoidThres, 3, 5, 1, 1)

        self.hSlider_areaVoidThres = QSlider(self.frame_manip)
        self.hSlider_areaVoidThres.setObjectName(u"hSlider_areaVoidThres")
        sizePolicy2.setHeightForWidth(self.hSlider_areaVoidThres.sizePolicy().hasHeightForWidth())
        self.hSlider_areaVoidThres.setSizePolicy(sizePolicy2)
        self.hSlider_areaVoidThres.setMaximum(350)
        self.hSlider_areaVoidThres.setValue(10)
        self.hSlider_areaVoidThres.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.hSlider_areaVoidThres, 3, 6, 1, 1)

        self.hSlider_dilateX = QSlider(self.frame_manip)
        self.hSlider_dilateX.setObjectName(u"hSlider_dilateX")
        sizePolicy2.setHeightForWidth(self.hSlider_dilateX.sizePolicy().hasHeightForWidth())
        self.hSlider_dilateX.setSizePolicy(sizePolicy2)
        self.hSlider_dilateX.setMaximum(9)
        self.hSlider_dilateX.setValue(1)
        self.hSlider_dilateX.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.hSlider_dilateX, 3, 8, 1, 1)

        self.hSlider_dilateY = QSlider(self.frame_manip)
        self.hSlider_dilateY.setObjectName(u"hSlider_dilateY")
        sizePolicy2.setHeightForWidth(self.hSlider_dilateY.sizePolicy().hasHeightForWidth())
        self.hSlider_dilateY.setSizePolicy(sizePolicy2)
        self.hSlider_dilateY.setMaximum(9)
        self.hSlider_dilateY.setValue(1)
        self.hSlider_dilateY.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.hSlider_dilateY, 3, 9, 1, 1)

        self.hSlider_ksizeX = QSlider(self.frame_manip)
        self.hSlider_ksizeX.setObjectName(u"hSlider_ksizeX")
        sizePolicy2.setHeightForWidth(self.hSlider_ksizeX.sizePolicy().hasHeightForWidth())
        self.hSlider_ksizeX.setSizePolicy(sizePolicy2)
        self.hSlider_ksizeX.setMaximum(30)
        self.hSlider_ksizeX.setValue(6)
        self.hSlider_ksizeX.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.hSlider_ksizeX, 3, 11, 1, 1)

        self.hSlider_ksizeY = QSlider(self.frame_manip)
        self.hSlider_ksizeY.setObjectName(u"hSlider_ksizeY")
        sizePolicy2.setHeightForWidth(self.hSlider_ksizeY.sizePolicy().hasHeightForWidth())
        self.hSlider_ksizeY.setSizePolicy(sizePolicy2)
        self.hSlider_ksizeY.setMaximum(30)
        self.hSlider_ksizeY.setValue(6)
        self.hSlider_ksizeY.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.hSlider_ksizeY, 3, 12, 1, 1)

        self.hSlider_white = QSlider(self.frame_manip)
        self.hSlider_white.setObjectName(u"hSlider_white")
        sizePolicy2.setHeightForWidth(self.hSlider_white.sizePolicy().hasHeightForWidth())
        self.hSlider_white.setSizePolicy(sizePolicy2)
        self.hSlider_white.setMaximum(250)
        self.hSlider_white.setValue(100)
        self.hSlider_white.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.hSlider_white, 3, 14, 1, 1)

        self.label_12 = QLabel(self.frame_manip)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_12, 0, 8, 1, 2)

        self.label_7 = QLabel(self.frame_manip)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 0, 5, 1, 2)

        self.label_6 = QLabel(self.frame_manip)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 2)


        self.verticalLayout_9.addLayout(self.gridLayout_2)


        self.verticalLayout_4.addWidget(self.frame_manip)


        self.verticalLayout_7.addWidget(self.frame)


        self.verticalLayout.addWidget(self.row_2)

        self.line_4 = QFrame(self.pagesContainer)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(0, 20))
        self.line_4.setStyleSheet(u"")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.row_3 = QFrame(self.pagesContainer)
        self.row_3.setObjectName(u"row_3")
        sizePolicy.setHeightForWidth(self.row_3.sizePolicy().hasHeightForWidth())
        self.row_3.setSizePolicy(sizePolicy)
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.row_3)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_2 = QFrame(self.row_3)
        self.frame_div_content_2.setObjectName(u"frame_div_content_2")
        self.frame_div_content_2.setMinimumSize(QSize(0, 0))
        self.frame_div_content_2.setMaximumSize(QSize(16777215, 160))
        self.frame_div_content_2.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_div_content_2)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_3 = QFrame(self.frame_div_content_2)
        self.frame_title_wid_3.setObjectName(u"frame_title_wid_3")
        self.frame_title_wid_3.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_3.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_title_wid_3)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_find_fiber = QLabel(self.frame_title_wid_3)
        self.label_find_fiber.setObjectName(u"label_find_fiber")
        self.label_find_fiber.setFont(font1)
        self.label_find_fiber.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.label_find_fiber)


        self.verticalLayout_22.addWidget(self.frame_title_wid_3)

        self.frame_content_wid_3 = QFrame(self.frame_div_content_2)
        self.frame_content_wid_3.setObjectName(u"frame_content_wid_3")
        sizePolicy.setHeightForWidth(self.frame_content_wid_3.sizePolicy().hasHeightForWidth())
        self.frame_content_wid_3.setSizePolicy(sizePolicy)
        self.frame_content_wid_3.setMinimumSize(QSize(0, 70))
        self.frame_content_wid_3.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_content_wid_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 2, 6, 1, 1)

        self.label_result = QLabel(self.frame_content_wid_3)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_result.setLineWidth(1)
        self.label_result.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_result, 2, 7, 1, 1)

        self.btn_start = QPushButton(self.frame_content_wid_3)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setMinimumSize(QSize(150, 30))
        self.btn_start.setFont(font1)
        self.btn_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_start.setIcon(icon1)

        self.gridLayout_3.addWidget(self.btn_start, 0, 8, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 2, 3, 1, 1)

        self.btn_result = QPushButton(self.frame_content_wid_3)
        self.btn_result.setObjectName(u"btn_result")
        self.btn_result.setMinimumSize(QSize(150, 30))
        self.btn_result.setFont(font1)
        self.btn_result.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_result.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_result.setIcon(icon)

        self.gridLayout_3.addWidget(self.btn_result, 2, 8, 1, 1)

        self.btn_display_image = QPushButton(self.frame_content_wid_3)
        self.btn_display_image.setObjectName(u"btn_display_image")
        self.btn_display_image.setMinimumSize(QSize(150, 30))
        self.btn_display_image.setFont(font1)
        self.btn_display_image.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_display_image.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil-browser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_display_image.setIcon(icon2)

        self.gridLayout_3.addWidget(self.btn_display_image, 2, 5, 1, 1)

        self.label_result_2 = QLabel(self.frame_content_wid_3)
        self.label_result_2.setObjectName(u"label_result_2")
        self.label_result_2.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_result_2.setLineWidth(1)
        self.label_result_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_result_2, 2, 4, 1, 1)

        self.label_start = QLabel(self.frame_content_wid_3)
        self.label_start.setObjectName(u"label_start")
        self.label_start.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_start.setLineWidth(1)
        self.label_start.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_start, 0, 0, 1, 1)

        self.label_state = QLabel(self.frame_content_wid_3)
        self.label_state.setObjectName(u"label_state")
        self.label_state.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_state.setLineWidth(1)
        self.label_state.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_state, 0, 7, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_3)


        self.verticalLayout_22.addWidget(self.frame_content_wid_3)


        self.verticalLayout_21.addWidget(self.frame_div_content_2)


        self.verticalLayout.addWidget(self.row_3)

        self.row_4 = QFrame(self.pagesContainer)
        self.row_4.setObjectName(u"row_4")
        self.row_4.setFrameShape(QFrame.StyledPanel)
        self.row_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.row_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pText_state = QTextEdit(self.row_4)
        self.pText_state.setObjectName(u"pText_state")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(40)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pText_state.sizePolicy().hasHeightForWidth())
        self.pText_state.setSizePolicy(sizePolicy3)
        self.pText_state.setMaximumSize(QSize(235, 16777215))

        self.horizontalLayout.addWidget(self.pText_state)

        self.label_origin = QLabel(self.row_4)
        self.label_origin.setObjectName(u"label_origin")
        self.label_origin.setScaledContents(True)
        self.label_origin.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_origin)

        self.label_fiber = QLabel(self.row_4)
        self.label_fiber.setObjectName(u"label_fiber")
        self.label_fiber.setScaledContents(True)
        self.label_fiber.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_fiber)


        self.verticalLayout.addWidget(self.row_4)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_3.addWidget(self.bgApp)


        self.retranslateUi(image)
        self.hSlider_areaVoidThres.valueChanged.connect(self.spBox_areaVoidThres.setValue)
        self.hSlider_colorThres.valueChanged.connect(self.spBox_colorThres.setValue)
        self.hSlider_colorVoidThres.valueChanged.connect(self.spBox_colorVoidThres.setValue)
        self.hSlider_Percent.valueChanged.connect(self.spBox_Percent.setValue)
        self.hSlider_areaThres.valueChanged.connect(self.spBox_areaThres.setValue)
        self.spBox_Percent.valueChanged.connect(self.hSlider_Percent.setValue)
        self.spBox_colorThres.valueChanged.connect(self.hSlider_colorThres.setValue)
        self.spBox_areaThres.valueChanged.connect(self.hSlider_areaThres.setValue)
        self.spBox_colorVoidThres.valueChanged.connect(self.hSlider_colorVoidThres.setValue)
        self.spBox_areaVoidThres.valueChanged.connect(self.hSlider_areaVoidThres.setValue)
        self.spBox_ksizeX.valueChanged.connect(self.hSlider_ksizeX.setValue)
        self.spBox_ksizeY.valueChanged.connect(self.hSlider_ksizeY.setValue)
        self.hSlider_ksizeX.valueChanged.connect(self.spBox_ksizeX.setValue)
        self.hSlider_ksizeY.valueChanged.connect(self.spBox_ksizeY.setValue)
        self.spBox_dilateX.valueChanged.connect(self.hSlider_dilateX.setValue)
        self.hSlider_dilateX.valueChanged.connect(self.spBox_dilateX.setValue)
        self.spBox_white.valueChanged.connect(self.hSlider_white.setValue)
        self.hSlider_white.valueChanged.connect(self.spBox_white.setValue)
        self.spBox_dilateY.valueChanged.connect(self.hSlider_dilateY.setValue)
        self.hSlider_dilateY.valueChanged.connect(self.spBox_dilateY.setValue)

        QMetaObject.connectSlotsByName(image)
    # setupUi

    def retranslateUi(self, image):
        image.setWindowTitle(QCoreApplication.translate("image", u"Image", None))
        self.label_open_file.setText(QCoreApplication.translate("image", u"LOAD IMAGE FILE", None))
        self.line_file_path.setText("")
        self.line_file_path.setPlaceholderText(QCoreApplication.translate("image", u"Type here", None))
        self.btn_open_file.setText(QCoreApplication.translate("image", u"Open", None))
        self.label_open_descript.setText(QCoreApplication.translate("image", u"It supports the following files; PNG( .png) JPEG(.jpg, .jpeg) TIF( .tif)", None))
        self.label_params.setText(QCoreApplication.translate("image", u"PARAMETERS", None))
        self.label_10.setText(QCoreApplication.translate("image", u"Kernel Size (Border)", None))
        self.label_14.setText(QCoreApplication.translate("image", u"White", None))
        self.label_5.setText(QCoreApplication.translate("image", u"Percent Crop", None))
        self.label.setText(QCoreApplication.translate("image", u"Color ThresHold", None))
        self.label_2.setText(QCoreApplication.translate("image", u"Area ThresHold", None))
        self.label_4.setText(QCoreApplication.translate("image", u"Color ThresHold", None))
        self.label_3.setText(QCoreApplication.translate("image", u"Area ThresHold", None))
        self.label_11.setText(QCoreApplication.translate("image", u"X", None))
        self.label_13.setText(QCoreApplication.translate("image", u"Y", None))
        self.label_8.setText(QCoreApplication.translate("image", u"X", None))
        self.label_9.setText(QCoreApplication.translate("image", u"Y", None))
        self.label_15.setText(QCoreApplication.translate("image", u"Sense", None))
        self.label_12.setText(QCoreApplication.translate("image", u"dilate (%)", None))
        self.label_7.setText(QCoreApplication.translate("image", u"Void (Black)", None))
        self.label_6.setText(QCoreApplication.translate("image", u"Fiber (white)", None))
        self.label_find_fiber.setText(QCoreApplication.translate("image", u"FIND THE FIBERS", None))
        self.label_result.setText(QCoreApplication.translate("image", u"Open the Result Folder   ", None))
        self.btn_start.setText(QCoreApplication.translate("image", u"START", None))
        self.btn_result.setText(QCoreApplication.translate("image", u"Result", None))
        self.btn_display_image.setText(QCoreApplication.translate("image", u"Display", None))
        self.label_result_2.setText(QCoreApplication.translate("image", u"Display Result   ", None))
        self.label_start.setText(QCoreApplication.translate("image", u"Start to find the fibers on the Image with above parameters   ", None))
        self.label_state.setText(QCoreApplication.translate("image", u"No Selected Files", None))
        self.label_origin.setText("")
        self.label_fiber.setText("")
    # retranslateUi

