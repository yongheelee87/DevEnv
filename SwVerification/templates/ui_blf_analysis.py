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
from PySide6.QtWidgets import QAbstractScrollArea, QCheckBox, QFrame, QGridLayout, QHBoxLayout, QHeaderView, QLabel, QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout, QWidget, QSpacerItem, QTableWidget

from . resources_rc import *


class Ui_blf_analysis(object):
    def setupUi(self, blf_analysis):
        if not blf_analysis.objectName():
            blf_analysis.setObjectName(u"blf_analysis")
        blf_analysis.resize(1168, 889)
        blf_analysis.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
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
"    border: 3px solid rgb(134, 149, 179);\n"
"	width: 20px;\n"
"	height: 18px;\n"
"	border-radius: 12px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(81, 176, 98);\n"
"}\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 3px solid rgb(81, 176, 98);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(134, 149, 179);\n"
"	width: 20px;\n"
"	height: 18px;\n"
"	border-radius: 12px;\n"
"	background-image: url(:/icons/icons/cil-check-alt.png) no-repeat;\n"
"	background-position: center center;\n"
"}\n"
"\n"
"/* //////////////////////////////////////////////////////////////////////////////"
                        "///////////////////\n"
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
""
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
"    background-color: rgb(147, 181, 249);"
                        "\n"
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
"	color: "
                        "rgb(113, 192, 217);\n"
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
"	background-color: rgb("
                        "35, 40, 49);\n"
"	border: 5px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(blf_analysis)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.bgApp = QFrame(blf_analysis)
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
        self.horizontalLayout = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(351, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.chk_show_graph = QCheckBox(self.frame_content_wid_1)
        self.chk_show_graph.setObjectName(u"chk_show_graph")
        icon = QIcon()
        icon.addFile(u":/icons/icons/cil-image-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chk_show_graph.setIcon(icon)
        self.chk_show_graph.setChecked(False)

        self.horizontalLayout.addWidget(self.chk_show_graph)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_Result_Folder = QPushButton(self.frame_content_wid_1)
        self.btn_Result_Folder.setObjectName(u"btn_Result_Folder")
        sizePolicy.setHeightForWidth(self.btn_Result_Folder.sizePolicy().hasHeightForWidth())
        self.btn_Result_Folder.setSizePolicy(sizePolicy)
        self.btn_Result_Folder.setMinimumSize(QSize(150, 40))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.btn_Result_Folder.setFont(font1)
        self.btn_Result_Folder.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Result_Folder.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Result_Folder.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_Result_Folder)

        self.btn_Run_Analysis = QPushButton(self.frame_content_wid_1)
        self.btn_Run_Analysis.setObjectName(u"btn_Run_Analysis")
        self.btn_Run_Analysis.setMinimumSize(QSize(150, 40))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        self.btn_Run_Analysis.setFont(font2)
        self.btn_Run_Analysis.setStyleSheet(u"QPushButton {\n"
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
        self.btn_Run_Analysis.setIcon(icon2)
        self.btn_Run_Analysis.setCheckable(True)
        self.btn_Run_Analysis.setChecked(True)

        self.horizontalLayout.addWidget(self.btn_Run_Analysis)


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
        self.verticalLayout = QVBoxLayout(self.frame_content_wid_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 0, 9, 9)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_path_descript_2 = QLabel(self.frame_content_wid_2)
        self.label_path_descript_2.setObjectName(u"label_path_descript_2")
        self.label_path_descript_2.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_path_descript_2.setLineWidth(1)
        self.label_path_descript_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_path_descript_2, 1, 0, 1, 2)

        self.line_cfg_path = QLineEdit(self.frame_content_wid_2)
        self.line_cfg_path.setObjectName(u"line_cfg_path")
        self.line_cfg_path.setMinimumSize(QSize(0, 40))
        self.line_cfg_path.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.line_cfg_path, 0, 0, 1, 1)

        self.btn_cfg_save = QPushButton(self.frame_content_wid_2)
        self.btn_cfg_save.setObjectName(u"btn_cfg_save")
        sizePolicy.setHeightForWidth(self.btn_cfg_save.sizePolicy().hasHeightForWidth())
        self.btn_cfg_save.setSizePolicy(sizePolicy)
        self.btn_cfg_save.setMinimumSize(QSize(150, 40))
        self.btn_cfg_save.setFont(font1)
        self.btn_cfg_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cfg_save.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cfg_save.setIcon(icon3)

        self.gridLayout_3.addWidget(self.btn_cfg_save, 0, 1, 1, 1)

        self.btn_cfg_load = QPushButton(self.frame_content_wid_2)
        self.btn_cfg_load.setObjectName(u"btn_cfg_load")
        sizePolicy.setHeightForWidth(self.btn_cfg_load.sizePolicy().hasHeightForWidth())
        self.btn_cfg_load.setSizePolicy(sizePolicy)
        self.btn_cfg_load.setMinimumSize(QSize(150, 40))
        self.btn_cfg_load.setFont(font1)
        self.btn_cfg_load.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cfg_load.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_cfg_load.setIcon(icon1)

        self.gridLayout_3.addWidget(self.btn_cfg_load, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_path_descript = QLabel(self.frame_content_wid_2)
        self.label_path_descript.setObjectName(u"label_path_descript")
        self.label_path_descript.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_path_descript.setLineWidth(1)
        self.label_path_descript.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_path_descript, 1, 0, 1, 2)

        self.line_blf_path = QLineEdit(self.frame_content_wid_2)
        self.line_blf_path.setObjectName(u"line_blf_path")
        self.line_blf_path.setMinimumSize(QSize(0, 40))
        self.line_blf_path.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_2.addWidget(self.line_blf_path, 0, 0, 1, 1)

        self.btn_blf_load = QPushButton(self.frame_content_wid_2)
        self.btn_blf_load.setObjectName(u"btn_blf_load")
        sizePolicy.setHeightForWidth(self.btn_blf_load.sizePolicy().hasHeightForWidth())
        self.btn_blf_load.setSizePolicy(sizePolicy)
        self.btn_blf_load.setMinimumSize(QSize(150, 40))
        self.btn_blf_load.setFont(font1)
        self.btn_blf_load.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_blf_load.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_blf_load.setIcon(icon1)

        self.gridLayout_2.addWidget(self.btn_blf_load, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.verticalLayout_5.addWidget(self.frame_content_wid_2)


        self.verticalLayout_4.addWidget(self.frame_div_content)


        self.verticalLayout_7.addWidget(self.row_2)

        self.row_3 = QFrame(self.pagesContainer)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.row_3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_2 = QFrame(self.row_3)
        self.frame_div_content_2.setObjectName(u"frame_div_content_2")
        self.frame_div_content_2.setFrameShape(QFrame.StyledPanel)
        self.frame_div_content_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_div_content_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_content_wid_5 = QFrame(self.frame_div_content_2)
        self.frame_content_wid_5.setObjectName(u"frame_content_wid_5")
        self.frame_content_wid_5.setFrameShape(QFrame.StyledPanel)
        self.frame_content_wid_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_content_wid_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_table_2 = QFrame(self.frame_content_wid_5)
        self.frame_table_2.setObjectName(u"frame_table_2")
        self.frame_table_2.setMaximumSize(QSize(220, 16777215))
        self.frame_table_2.setFrameShape(QFrame.StyledPanel)
        self.frame_table_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_table_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_channel = QLabel(self.frame_table_2)
        self.label_channel.setObjectName(u"label_channel")
        self.label_channel.setMinimumSize(QSize(0, 30))
        self.label_channel.setFont(font1)
        self.label_channel.setStyleSheet(u"")

        self.verticalLayout_14.addWidget(self.label_channel)

        self.tbl_ch_device = QTableWidget(self.frame_table_2)
        self.tbl_ch_device.setObjectName(u"tbl_ch_device")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tbl_ch_device.sizePolicy().hasHeightForWidth())
        self.tbl_ch_device.setSizePolicy(sizePolicy1)
        self.tbl_ch_device.setFont(font1)
        self.tbl_ch_device.setStyleSheet(u"QTableView\n"
"{\n"
"    border: 1px solid white;\n"
"    gridline-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: rgb(33, 37, 43);\n"
"}")
        self.tbl_ch_device.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tbl_ch_device.setDragEnabled(True)
        self.tbl_ch_device.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_ch_device.horizontalHeader().setMinimumSectionSize(38)
        self.tbl_ch_device.horizontalHeader().setProperty("showSortIndicator", False)
        self.tbl_ch_device.horizontalHeader().setStretchLastSection(True)
        self.tbl_ch_device.verticalHeader().setVisible(False)
        self.tbl_ch_device.verticalHeader().setMinimumSectionSize(28)
        self.tbl_ch_device.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_14.addWidget(self.tbl_ch_device)


        self.horizontalLayout_3.addWidget(self.frame_table_2)

        self.frame_signal = QFrame(self.frame_content_wid_5)
        self.frame_signal.setObjectName(u"frame_signal")
        self.frame_signal.setFrameShape(QFrame.StyledPanel)
        self.frame_signal.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_signal)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_signal = QLabel(self.frame_signal)
        self.label_signal.setObjectName(u"label_signal")
        self.label_signal.setMinimumSize(QSize(0, 30))
        self.label_signal.setFont(font1)
        self.label_signal.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_signal, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(431, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.line_Resample_Rate = QLineEdit(self.frame_signal)
        self.line_Resample_Rate.setObjectName(u"line_Resample_Rate")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_Resample_Rate.sizePolicy().hasHeightForWidth())
        self.line_Resample_Rate.setSizePolicy(sizePolicy2)
        self.line_Resample_Rate.setMinimumSize(QSize(150, 30))
        self.line_Resample_Rate.setFont(font1)
        self.line_Resample_Rate.setLayoutDirection(Qt.LeftToRight)
        self.line_Resample_Rate.setStyleSheet(u"qproperty-cursorPosition: 0;\n"
"border: 1px solid rgb(113, 126, 149);")
        self.line_Resample_Rate.setFrame(True)
        self.line_Resample_Rate.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.line_Resample_Rate, 0, 2, 1, 1)

        self.pText_signal = QPlainTextEdit(self.frame_signal)
        self.pText_signal.setObjectName(u"pText_signal")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pText_signal.sizePolicy().hasHeightForWidth())
        self.pText_signal.setSizePolicy(sizePolicy3)
        self.pText_signal.setFont(font1)

        self.gridLayout.addWidget(self.pText_signal, 1, 0, 1, 3)


        self.horizontalLayout_3.addWidget(self.frame_signal)


        self.verticalLayout_12.addWidget(self.frame_content_wid_5)


        self.verticalLayout_11.addWidget(self.frame_div_content_2)


        self.verticalLayout_7.addWidget(self.row_3)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_3.addWidget(self.bgApp)


        self.retranslateUi(blf_analysis)

        QMetaObject.connectSlotsByName(blf_analysis)
    # setupUi

    def retranslateUi(self, blf_analysis):
        blf_analysis.setWindowTitle(QCoreApplication.translate("blf_analysis", u"blf_analysis", None))
        self.label_title.setText(QCoreApplication.translate("blf_analysis", u"BLF ANALYSIS", None))
        self.chk_show_graph.setText(QCoreApplication.translate("blf_analysis", u"Show Interactive Graph", None))
        self.btn_Result_Folder.setText(QCoreApplication.translate("blf_analysis", u"Open Result", None))
        self.btn_Run_Analysis.setText(QCoreApplication.translate("blf_analysis", u"RUN ANALYSIS", None))
        self.label_path_descript_2.setText(QCoreApplication.translate("blf_analysis", u"Please Open and Load the Configuration with a path.", None))
        self.line_cfg_path.setText("")
        self.line_cfg_path.setPlaceholderText(QCoreApplication.translate("blf_analysis", u"Configuration File Path", None))
        self.btn_cfg_save.setText(QCoreApplication.translate("blf_analysis", u"Save Cfg", None))
        self.btn_cfg_load.setText(QCoreApplication.translate("blf_analysis", u"Load Cfg", None))
        self.label_path_descript.setText(QCoreApplication.translate("blf_analysis", u"Please Open and Load the BLF file with a path.", None))
        self.line_blf_path.setText("")
        self.line_blf_path.setPlaceholderText(QCoreApplication.translate("blf_analysis", u"BLF File Path", None))
        self.btn_blf_load.setText(QCoreApplication.translate("blf_analysis", u"Load BLF", None))
        self.label_channel.setText(QCoreApplication.translate("blf_analysis", u"CHANNEL", None))
        self.label_signal.setText(QCoreApplication.translate("blf_analysis", u"SIGNALS", None))
        self.line_Resample_Rate.setText(QCoreApplication.translate("blf_analysis", u"Resample Rate", None))
    # retranslateUi

