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
from PySide6.QtWidgets import QFrame, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout, QWidget, QSpacerItem

from . resources_rc import *


class Ui_trace32(object):
    def setupUi(self, trace32):
        if not trace32.objectName():
            trace32.setObjectName(u"trace32")
        trace32.resize(783, 926)
        trace32.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
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
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Label */\n"
"#label_title { font: 63 12pt \"Segoe UI Semibold\";}\n"
"#label_taget_title { font: 63 12pt \"Segoe UI Semibold\";}\n"
"#label_command { font: 63 12pt \"Segoe UI Semibold\";}\n"
"#label_monitor { font: 63 12pt \"Segoe UI Semibold\";}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	bord"
                        "er-radius: 5px;\n"
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
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* //////////////////"
                        "///////////////////////////////////////////////////////////////////////////////\n"
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
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88)"
                        ";\n"
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
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subco"
                        "ntrol-origin: margin;\n"
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
"    border-top-right-radius: 4px;\n"
"     subcont"
                        "rol-position: top;\n"
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
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px"
                        " solid rgb(52, 59, 72);\n"
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
"	border-bottom-right-radius: 3px;	\n"
"	background-"
                        "image: url(:/icons/icons/cil-arrow-bottom.png);\n"
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
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(113, 192"
                        ", 217);\n"
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
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButt"
                        "on:pressed {	\n"
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
"	border: 5px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(trace32)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(trace32)
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
        self.verticalLayout_12 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.row_1 = QFrame(self.pagesContainer)
        self.row_1.setObjectName(u"row_1")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.row_1.sizePolicy().hasHeightForWidth())
        self.row_1.setSizePolicy(sizePolicy)
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.row_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
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


        self.verticalLayout_13.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_content_wid_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_taget_title = QLabel(self.frame_content_wid_1)
        self.label_taget_title.setObjectName(u"label_taget_title")
        self.label_taget_title.setMinimumSize(QSize(65, 0))
        self.label_taget_title.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_taget_title.setLineWidth(1)
        self.label_taget_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_taget_title, 0, 0, 1, 1)

        self.btn_Connect = QPushButton(self.frame_content_wid_1)
        self.btn_Connect.setObjectName(u"btn_Connect")
        sizePolicy.setHeightForWidth(self.btn_Connect.sizePolicy().hasHeightForWidth())
        self.btn_Connect.setSizePolicy(sizePolicy)
        self.btn_Connect.setMinimumSize(QSize(130, 40))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.btn_Connect.setFont(font1)
        self.btn_Connect.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	background-color: rgba(245, 188, 66, 150);\n"
"	border-radius: 5px;\n"
"	border: 1px solid transparent;\n"
"}\n"
"QPushButton::pressed{\n"
"background-color : blue; color: blue\n"
"}\n"
"QPushButton::hover{\n"
"background-color: lightblue;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/images/usb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Connect.setIcon(icon)
        self.btn_Connect.setIconSize(QSize(21, 21))

        self.gridLayout_3.addWidget(self.btn_Connect, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(504, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.line_connect_status = QLineEdit(self.frame_content_wid_1)
        self.line_connect_status.setObjectName(u"line_connect_status")
        sizePolicy.setHeightForWidth(self.line_connect_status.sizePolicy().hasHeightForWidth())
        self.line_connect_status.setSizePolicy(sizePolicy)
        self.line_connect_status.setMinimumSize(QSize(125, 40))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        self.line_connect_status.setFont(font2)
        self.line_connect_status.setLayoutDirection(Qt.LeftToRight)
        self.line_connect_status.setStyleSheet(u"font-weight:600;\n"
"qproperty-cursorPosition: 0;\n"
"border: 1px solid transparent;\n"
"background-color: rgba(255, 0, 0, 0.70)")
        self.line_connect_status.setFrame(True)
        self.line_connect_status.setAlignment(Qt.AlignCenter)
        self.line_connect_status.setReadOnly(True)

        self.gridLayout_3.addWidget(self.line_connect_status, 0, 1, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_content_wid_1)


        self.verticalLayout_7.addWidget(self.frame_div_content_1)

        self.frame_content_wid_3 = QFrame(self.row_1)
        self.frame_content_wid_3.setObjectName(u"frame_content_wid_3")
        self.frame_content_wid_3.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content_wid_3)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.line_cmm_path = QLineEdit(self.frame_content_wid_3)
        self.line_cmm_path.setObjectName(u"line_cmm_path")
        self.line_cmm_path.setMinimumSize(QSize(0, 40))
        self.line_cmm_path.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.line_cmm_path, 0, 0, 1, 1)

        self.btn_cmm_load = QPushButton(self.frame_content_wid_3)
        self.btn_cmm_load.setObjectName(u"btn_cmm_load")
        sizePolicy.setHeightForWidth(self.btn_cmm_load.sizePolicy().hasHeightForWidth())
        self.btn_cmm_load.setSizePolicy(sizePolicy)
        self.btn_cmm_load.setMinimumSize(QSize(150, 30))
        self.btn_cmm_load.setFont(font1)
        self.btn_cmm_load.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cmm_load.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cmm_load.setIcon(icon1)

        self.gridLayout_4.addWidget(self.btn_cmm_load, 0, 2, 1, 1)

        self.label_path_descript_3 = QLabel(self.frame_content_wid_3)
        self.label_path_descript_3.setObjectName(u"label_path_descript_3")
        self.label_path_descript_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_path_descript_3.setLineWidth(1)
        self.label_path_descript_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_path_descript_3, 1, 0, 1, 2)


        self.verticalLayout_9.addLayout(self.gridLayout_4)


        self.verticalLayout_7.addWidget(self.frame_content_wid_3)

        self.frame_content_wid_3.raise_()
        self.frame_div_content_1.raise_()

        self.verticalLayout_12.addWidget(self.row_1)

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
        self.frame_2 = QFrame(self.frame_div_content)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_command = QLabel(self.frame_2)
        self.label_command.setObjectName(u"label_command")
        self.label_command.setFont(font)
        self.label_command.setStyleSheet(u"color: rgb(113, 126, 149);")

        self.gridLayout_2.addWidget(self.label_command, 0, 0, 1, 1)

        self.btn_send = QPushButton(self.frame_2)
        self.btn_send.setObjectName(u"btn_send")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_send.sizePolicy().hasHeightForWidth())
        self.btn_send.setSizePolicy(sizePolicy1)
        self.btn_send.setMinimumSize(QSize(150, 30))
        self.btn_send.setFont(font2)
        self.btn_send.setStyleSheet(u"font-weight:600;\n"
"background-color: rgb(52, 59, 72);")

        self.gridLayout_2.addWidget(self.btn_send, 0, 2, 1, 1)

        self.pText_cmd = QPlainTextEdit(self.frame_2)
        self.pText_cmd.setObjectName(u"pText_cmd")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pText_cmd.sizePolicy().hasHeightForWidth())
        self.pText_cmd.setSizePolicy(sizePolicy2)
        self.pText_cmd.setMaximumSize(QSize(16777215, 130))
        self.pText_cmd.setFont(font1)

        self.gridLayout_2.addWidget(self.pText_cmd, 1, 0, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)


        self.verticalLayout_14.addLayout(self.gridLayout_2)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.verticalLayout_4.addWidget(self.frame_div_content)


        self.verticalLayout_12.addWidget(self.row_2)

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
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(9)
        self.pText_monitor = QPlainTextEdit(self.frame)
        self.pText_monitor.setObjectName(u"pText_monitor")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pText_monitor.sizePolicy().hasHeightForWidth())
        self.pText_monitor.setSizePolicy(sizePolicy3)
        self.pText_monitor.setFont(font1)

        self.gridLayout.addWidget(self.pText_monitor, 1, 0, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.label_monitor = QLabel(self.frame)
        self.label_monitor.setObjectName(u"label_monitor")
        self.label_monitor.setFont(font)
        self.label_monitor.setStyleSheet(u"color: rgb(113, 126, 149);")

        self.gridLayout.addWidget(self.label_monitor, 0, 0, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout)


        self.verticalLayout_11.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_div_content_2)


        self.verticalLayout_12.addWidget(self.row_3)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_3.addWidget(self.bgApp)


        self.retranslateUi(trace32)

        QMetaObject.connectSlotsByName(trace32)
    # setupUi

    def retranslateUi(self, trace32):
        trace32.setWindowTitle(QCoreApplication.translate("trace32", u"trace32", None))
        self.label_title.setText(QCoreApplication.translate("trace32", u"TRACE32", None))
        self.label_taget_title.setText(QCoreApplication.translate("trace32", u"Status : ", None))
        self.btn_Connect.setText(QCoreApplication.translate("trace32", u"CONNECT", None))
        self.line_connect_status.setText(QCoreApplication.translate("trace32", u"Not Connected", None))
        self.line_cmm_path.setText("")
        self.line_cmm_path.setPlaceholderText(QCoreApplication.translate("trace32", u"Cmm Path", None))
        self.btn_cmm_load.setText(QCoreApplication.translate("trace32", u"Load", None))
        self.label_path_descript_3.setText(QCoreApplication.translate("trace32", u"Please Open and Load the cmm with a path.", None))
        self.label_command.setText(QCoreApplication.translate("trace32", u"COMMAND", None))
        self.btn_send.setText(QCoreApplication.translate("trace32", u"SEND", None))
        self.pText_cmd.setPlainText(QCoreApplication.translate("trace32", u"W: Write Msg (Symbol, Value)\n"
"R: Read Msg (Symbol)\n"
"T: Time Delay (ex. T: 0.2)\n"
"Option: Display Option", None))
        self.label_monitor.setText(QCoreApplication.translate("trace32", u"Monitor", None))
    # retranslateUi

