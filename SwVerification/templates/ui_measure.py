# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QCursor, QFont, QIcon
from PySide6.QtWidgets import QAbstractScrollArea, QComboBox, QFrame, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QTableWidget, QPushButton, QSizePolicy, QVBoxLayout, QWidget, QSpacerItem

from . resources_rc import *


class Ui_measure(object):
    def setupUi(self, measure):
        if not measure.objectName():
            measure.setObjectName(u"measure")
        measure.resize(1361, 1043)
        measure.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
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
"#label_taget_title { font: 63 12pt \"Segoe UI Semibold\";}\n"
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
"QTableWidget"
                        "::item{\n"
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
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	backgr"
                        "ound-color: rgb(33, 37, 43);\n"
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
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* ////////////////////////////"
                        "/////////////////////////////////////////////////////////////////////\n"
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
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     backgroun"
                        "d: none;\n"
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
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:ve"
                        "rtical {\n"
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
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);"
                        "\n"
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
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
" }"
                        "\n"
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
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(113, 192, 217);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
""
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
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(147, 207, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"/* /////////////////////////"
                        "////////////////////////////////////////////////////////////////////////\n"
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
"	border: 5px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(measure)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.bgApp = QFrame(measure)
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
        self.horizontalLayout_3 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_taget_title = QLabel(self.frame_content_wid_1)
        self.label_taget_title.setObjectName(u"label_taget_title")
        self.label_taget_title.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_taget_title.setLineWidth(1)
        self.label_taget_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_taget_title)

        self.cbox_project = QComboBox(self.frame_content_wid_1)
        self.cbox_project.addItem("")
        self.cbox_project.setObjectName(u"cbox_project")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cbox_project.sizePolicy().hasHeightForWidth())
        self.cbox_project.setSizePolicy(sizePolicy1)
        self.cbox_project.setMinimumSize(QSize(80, 0))
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
        sizePolicy.setHeightForWidth(self.btn_Result_Folder.sizePolicy().hasHeightForWidth())
        self.btn_Result_Folder.setSizePolicy(sizePolicy)
        self.btn_Result_Folder.setMinimumSize(QSize(150, 40))
        self.btn_Result_Folder.setFont(font1)
        self.btn_Result_Folder.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Result_Folder.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Result_Folder.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_Result_Folder)

        self.btn_show_graph = QPushButton(self.frame_content_wid_1)
        self.btn_show_graph.setObjectName(u"btn_show_graph")
        sizePolicy.setHeightForWidth(self.btn_show_graph.sizePolicy().hasHeightForWidth())
        self.btn_show_graph.setSizePolicy(sizePolicy)
        self.btn_show_graph.setMinimumSize(QSize(150, 40))
        self.btn_show_graph.setFont(font1)
        self.btn_show_graph.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_show_graph.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-chart-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_show_graph.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_show_graph)

        self.btn_Run_Script = QPushButton(self.frame_content_wid_1)
        self.btn_Run_Script.setObjectName(u"btn_Run_Script")
        self.btn_Run_Script.setMinimumSize(QSize(150, 40))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        self.btn_Run_Script.setFont(font2)
        self.btn_Run_Script.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/images/images/start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Run_Script.setIcon(icon2)
        self.btn_Run_Script.setCheckable(True)
        self.btn_Run_Script.setChecked(True)

        self.horizontalLayout.addWidget(self.btn_Run_Script)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

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
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_path_descript = QLabel(self.frame_content_wid_2)
        self.label_path_descript.setObjectName(u"label_path_descript")
        self.label_path_descript.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_path_descript.setLineWidth(1)
        self.label_path_descript.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_path_descript, 1, 0, 1, 2)

        self.line_script_path = QLineEdit(self.frame_content_wid_2)
        self.line_script_path.setObjectName(u"line_script_path")
        self.line_script_path.setMinimumSize(QSize(0, 40))
        self.line_script_path.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_2.addWidget(self.line_script_path, 0, 0, 1, 1)

        self.btn_script_save = QPushButton(self.frame_content_wid_2)
        self.btn_script_save.setObjectName(u"btn_script_save")
        sizePolicy.setHeightForWidth(self.btn_script_save.sizePolicy().hasHeightForWidth())
        self.btn_script_save.setSizePolicy(sizePolicy)
        self.btn_script_save.setMinimumSize(QSize(150, 40))
        self.btn_script_save.setFont(font1)
        self.btn_script_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_script_save.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_script_save.setIcon(icon3)

        self.gridLayout_2.addWidget(self.btn_script_save, 0, 1, 1, 1)

        self.btn_script_load = QPushButton(self.frame_content_wid_2)
        self.btn_script_load.setObjectName(u"btn_script_load")
        sizePolicy.setHeightForWidth(self.btn_script_load.sizePolicy().hasHeightForWidth())
        self.btn_script_load.setSizePolicy(sizePolicy)
        self.btn_script_load.setMinimumSize(QSize(150, 40))
        self.btn_script_load.setFont(font1)
        self.btn_script_load.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_script_load.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_script_load.setIcon(icon)

        self.gridLayout_2.addWidget(self.btn_script_load, 0, 2, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_2)


        self.verticalLayout_5.addWidget(self.frame_content_wid_2)

        self.frame_content_wid_3 = QFrame(self.frame_div_content)
        self.frame_content_wid_3.setObjectName(u"frame_content_wid_3")
        self.frame_content_wid_3.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_content_wid_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(281, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_fill_zero = QLabel(self.frame_content_wid_3)
        self.label_fill_zero.setObjectName(u"label_fill_zero")
        self.label_fill_zero.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_fill_zero.setLineWidth(1)
        self.label_fill_zero.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_fill_zero)

        self.cbox_fill_zero = QComboBox(self.frame_content_wid_3)
        self.cbox_fill_zero.addItem("")
        self.cbox_fill_zero.addItem("")
        self.cbox_fill_zero.setObjectName(u"cbox_fill_zero")
        sizePolicy1.setHeightForWidth(self.cbox_fill_zero.sizePolicy().hasHeightForWidth())
        self.cbox_fill_zero.setSizePolicy(sizePolicy1)
        self.cbox_fill_zero.setMinimumSize(QSize(80, 0))
        self.cbox_fill_zero.setFont(font1)
        self.cbox_fill_zero.setLayoutDirection(Qt.LeftToRight)
        self.cbox_fill_zero.setStyleSheet(u"QComboBox\n"
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
        self.cbox_fill_zero.setFrame(True)

        self.horizontalLayout_2.addWidget(self.cbox_fill_zero)

        self.label_judge_type = QLabel(self.frame_content_wid_3)
        self.label_judge_type.setObjectName(u"label_judge_type")
        self.label_judge_type.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_judge_type.setLineWidth(1)
        self.label_judge_type.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_judge_type)

        self.cbox_judge_type = QComboBox(self.frame_content_wid_3)
        self.cbox_judge_type.addItem("")
        self.cbox_judge_type.addItem("")
        self.cbox_judge_type.setObjectName(u"cbox_judge_type")
        sizePolicy1.setHeightForWidth(self.cbox_judge_type.sizePolicy().hasHeightForWidth())
        self.cbox_judge_type.setSizePolicy(sizePolicy1)
        self.cbox_judge_type.setMinimumSize(QSize(150, 0))
        self.cbox_judge_type.setFont(font1)
        self.cbox_judge_type.setLayoutDirection(Qt.LeftToRight)
        self.cbox_judge_type.setStyleSheet(u"QComboBox\n"
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
        self.cbox_judge_type.setFrame(True)

        self.horizontalLayout_2.addWidget(self.cbox_judge_type)

        self.label_time_type = QLabel(self.frame_content_wid_3)
        self.label_time_type.setObjectName(u"label_time_type")
        self.label_time_type.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_time_type.setLineWidth(1)
        self.label_time_type.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_time_type)

        self.cbox_time_type = QComboBox(self.frame_content_wid_3)
        self.cbox_time_type.addItem("")
        self.cbox_time_type.addItem("")
        self.cbox_time_type.setObjectName(u"cbox_time_type")
        sizePolicy1.setHeightForWidth(self.cbox_time_type.sizePolicy().hasHeightForWidth())
        self.cbox_time_type.setSizePolicy(sizePolicy1)
        self.cbox_time_type.setMinimumSize(QSize(110, 0))
        self.cbox_time_type.setFont(font1)
        self.cbox_time_type.setLayoutDirection(Qt.LeftToRight)
        self.cbox_time_type.setStyleSheet(u"QComboBox\n"
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
        self.cbox_time_type.setFrame(True)

        self.horizontalLayout_2.addWidget(self.cbox_time_type)

        self.label_num_match = QLabel(self.frame_content_wid_3)
        self.label_num_match.setObjectName(u"label_num_match")
        self.label_num_match.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_num_match.setLineWidth(1)
        self.label_num_match.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_num_match)

        self.line_sample_rate = QLineEdit(self.frame_content_wid_3)
        self.line_sample_rate.setObjectName(u"line_sample_rate")
        sizePolicy.setHeightForWidth(self.line_sample_rate.sizePolicy().hasHeightForWidth())
        self.line_sample_rate.setSizePolicy(sizePolicy)
        self.line_sample_rate.setMinimumSize(QSize(0, 40))
        self.line_sample_rate.setFocusPolicy(Qt.WheelFocus)
        self.line_sample_rate.setToolTipDuration(2)
        self.line_sample_rate.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.line_sample_rate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.line_sample_rate)

        self.label_path_descript_3 = QLabel(self.frame_content_wid_3)
        self.label_path_descript_3.setObjectName(u"label_path_descript_3")
        self.label_path_descript_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_path_descript_3.setLineWidth(1)
        self.label_path_descript_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_path_descript_3)

        self.line_num_match = QLineEdit(self.frame_content_wid_3)
        self.line_num_match.setObjectName(u"line_num_match")
        sizePolicy.setHeightForWidth(self.line_num_match.sizePolicy().hasHeightForWidth())
        self.line_num_match.setSizePolicy(sizePolicy)
        self.line_num_match.setMinimumSize(QSize(0, 40))
        self.line_num_match.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.line_num_match.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.line_num_match)


        self.verticalLayout_5.addWidget(self.frame_content_wid_3)

        self.frame_table = QFrame(self.frame_div_content)
        self.frame_table.setObjectName(u"frame_table")
        self.frame_table.setFrameShape(QFrame.StyledPanel)
        self.frame_table.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_table)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tbl_script = QTableWidget(self.frame_table)
        self.tbl_script.setObjectName(u"tbl_script")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        self.tbl_script.setFont(font3)
        self.tbl_script.setStyleSheet(u"QTableView\n"
"{\n"
"	font: 9pt \"Segoe UI\";\n"
"    border: 1px solid white;\n"
"    gridline-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: rgb(33, 37, 43);\n"
"}")
        self.tbl_script.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tbl_script.setDragEnabled(True)
        self.tbl_script.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_script.horizontalHeader().setProperty("showSortIndicator", False)
        self.tbl_script.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_7.addWidget(self.tbl_script)


        self.verticalLayout_5.addWidget(self.frame_table)


        self.verticalLayout_4.addWidget(self.frame_div_content)


        self.verticalLayout.addWidget(self.row_2)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_3.addWidget(self.bgApp)


        self.retranslateUi(measure)

        QMetaObject.connectSlotsByName(measure)
    # setupUi

    def retranslateUi(self, measure):
        measure.setWindowTitle(QCoreApplication.translate("measure", u"measure", None))
        self.label_title.setText(QCoreApplication.translate("measure", u"MEASUREMENT", None))
        self.label_taget_title.setText(QCoreApplication.translate("measure", u"Measure Target : ", None))
        self.cbox_project.setItemText(0, QCoreApplication.translate("measure", u"  RGW", None))

        self.btn_Result_Folder.setText(QCoreApplication.translate("measure", u"Open Result", None))
        self.btn_show_graph.setText(QCoreApplication.translate("measure", u"Show Graph", None))
        self.btn_Run_Script.setText(QCoreApplication.translate("measure", u"RUN SCRIPT", None))
        self.label_path_descript.setText(QCoreApplication.translate("measure", u"Please Open and Load the script with a path.", None))
        self.line_script_path.setText("")
        self.line_script_path.setPlaceholderText(QCoreApplication.translate("measure", u"Script Path", None))
        self.btn_script_save.setText(QCoreApplication.translate("measure", u"Save", None))
        self.btn_script_load.setText(QCoreApplication.translate("measure", u"Load", None))
        self.label_fill_zero.setText(QCoreApplication.translate("measure", u"Fill Zero: ", None))
        self.cbox_fill_zero.setItemText(0, QCoreApplication.translate("measure", u"True", None))
        self.cbox_fill_zero.setItemText(1, QCoreApplication.translate("measure", u"False", None))

        self.label_judge_type.setText(QCoreApplication.translate("measure", u"Judge Type: ", None))
        self.cbox_judge_type.setItemText(0, QCoreApplication.translate("measure", u"same time", None))
        self.cbox_judge_type.setItemText(1, QCoreApplication.translate("measure", u"independent", None))

        self.label_time_type.setText(QCoreApplication.translate("measure", u"Time Type: ", None))
        self.cbox_time_type.setItemText(0, QCoreApplication.translate("measure", u"Per step", None))
        self.cbox_time_type.setItemText(1, QCoreApplication.translate("measure", u"Total", None))

        self.label_num_match.setText(QCoreApplication.translate("measure", u"Sample Rate (sec): ", None))
        self.line_sample_rate.setText(QCoreApplication.translate("measure", u"0.1", None))
        self.line_sample_rate.setPlaceholderText(QCoreApplication.translate("measure", u"0.1", None))
        self.label_path_descript_3.setText(QCoreApplication.translate("measure", u"Num Of Match: ", None))
        self.line_num_match.setText(QCoreApplication.translate("measure", u"1", None))
        self.line_num_match.setPlaceholderText(QCoreApplication.translate("measure", u"1", None))
    # retranslateUi

