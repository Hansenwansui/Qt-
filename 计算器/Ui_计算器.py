# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '计算器.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QVBoxLayout,
    QWidget)

from qfluentwidgets import (LineEdit, PushButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(468, 625)
        font = QFont()
        font.setFamilies([u"Cascadia Code"])
        font.setPointSize(20)
        font.setBold(False)
        Form.setFont(font)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LineEdit = LineEdit(Form)
        self.LineEdit.setObjectName(u"LineEdit")
        self.LineEdit.setMinimumSize(QSize(0, 200))
        self.LineEdit.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(36)
        font1.setBold(False)
        self.LineEdit.setFont(font1)

        self.verticalLayout.addWidget(self.LineEdit)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.PushButton_back = PushButton(Form)
        self.PushButton_back.setObjectName(u"PushButton_back")
        self.PushButton_back.setMinimumSize(QSize(0, 75))

        self.gridLayout.addWidget(self.PushButton_back, 0, 2, 1, 1)

        self.PushButton_clean = PushButton(Form)
        self.PushButton_clean.setObjectName(u"PushButton_clean")
        self.PushButton_clean.setMinimumSize(QSize(0, 75))

        self.gridLayout.addWidget(self.PushButton_clean, 0, 1, 1, 1)

        self.PushButton_n7 = PushButton(Form)
        self.PushButton_n7.setObjectName(u"PushButton_n7")
        self.PushButton_n7.setMinimumSize(QSize(0, 75))

        self.gridLayout.addWidget(self.PushButton_n7, 1, 0, 1, 1)

        self.PushButton_quit = PushButton(Form)
        self.PushButton_quit.setObjectName(u"PushButton_quit")
        self.PushButton_quit.setMinimumSize(QSize(0, 75))

        self.gridLayout.addWidget(self.PushButton_quit, 0, 0, 1, 1)

        self.PushButton_n8 = PushButton(Form)
        self.PushButton_n8.setObjectName(u"PushButton_n8")
        self.PushButton_n8.setMinimumSize(QSize(0, 75))

        self.gridLayout.addWidget(self.PushButton_n8, 1, 1, 1, 1)

        self.PushButton_div = PushButton(Form)
        self.PushButton_div.setObjectName(u"PushButton_div")
        self.PushButton_div.setMinimumSize(QSize(0, 75))

        self.gridLayout.addWidget(self.PushButton_div, 0, 3, 1, 1)

        self.PushButton_n6 = PushButton(Form)
        self.PushButton_n6.setObjectName(u"PushButton_n6")
        self.PushButton_n6.setMinimumSize(QSize(0, 75))

        self.gridLayout.addWidget(self.PushButton_n6, 2, 2, 1, 1)

        self.PushButton_n1 = PushButton(Form)
        self.PushButton_n1.setObjectName(u"PushButton_n1")
        self.PushButton_n1.setMinimumSize(QSize(0, 75))

        self.gridLayout.addWidget(self.PushButton_n1, 3, 0, 1, 1)

        self.PushButton_point = PushButton(Form)
        self.PushButton_point.setObjectName(u"PushButton_point")
        self.PushButton_point.setMinimumSize(QSize(0, 75))

        self.gridLayout.addWidget(self.PushButton_point, 4, 0, 1, 1)

        self.PushButton_n4 = PushButton(Form)
        self.PushButton_n4.setObjectName(u"PushButton_n4")
        self.PushButton_n4.setMinimumSize(QSize(0, 75))

        self.gridLayout.addWidget(self.PushButton_n4, 2, 0, 1, 1)

        self.PushButton_n3 = PushButton(Form)
        self.PushButton_n3.setObjectName(u"PushButton_n3")
        self.PushButton_n3.setMinimumSize(QSize(0, 75))

        self.gridLayout.addWidget(self.PushButton_n3, 3, 2, 1, 1)

        self.PushButton_sub = PushButton(Form)
        self.PushButton_sub.setObjectName(u"PushButton_sub")
        self.PushButton_sub.setMinimumSize(QSize(0, 75))

        self.gridLayout.addWidget(self.PushButton_sub, 2, 3, 1, 1)

        self.PushButton_n9 = PushButton(Form)
        self.PushButton_n9.setObjectName(u"PushButton_n9")
        self.PushButton_n9.setMinimumSize(QSize(0, 75))

        self.gridLayout.addWidget(self.PushButton_n9, 1, 2, 1, 1)

        self.PushButton_n0 = PushButton(Form)
        self.PushButton_n0.setObjectName(u"PushButton_n0")
        self.PushButton_n0.setMinimumSize(QSize(0, 75))

        self.gridLayout.addWidget(self.PushButton_n0, 4, 1, 1, 1)

        self.PushButton_mul = PushButton(Form)
        self.PushButton_mul.setObjectName(u"PushButton_mul")
        self.PushButton_mul.setMinimumSize(QSize(0, 75))

        self.gridLayout.addWidget(self.PushButton_mul, 1, 3, 1, 1)

        self.PushButton_add = PushButton(Form)
        self.PushButton_add.setObjectName(u"PushButton_add")
        self.PushButton_add.setMinimumSize(QSize(0, 150))

        self.gridLayout.addWidget(self.PushButton_add, 3, 3, 2, 1)

        self.PushButton_n2 = PushButton(Form)
        self.PushButton_n2.setObjectName(u"PushButton_n2")
        self.PushButton_n2.setMinimumSize(QSize(0, 75))

        self.gridLayout.addWidget(self.PushButton_n2, 3, 1, 1, 1)

        self.PushButton_n5 = PushButton(Form)
        self.PushButton_n5.setObjectName(u"PushButton_n5")
        self.PushButton_n5.setMinimumSize(QSize(0, 75))

        self.gridLayout.addWidget(self.PushButton_n5, 2, 1, 1, 1)

        self.PushButton_equal = PushButton(Form)
        self.PushButton_equal.setObjectName(u"PushButton_equal")
        self.PushButton_equal.setMinimumSize(QSize(0, 75))

        self.gridLayout.addWidget(self.PushButton_equal, 4, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u5668", None))
        self.PushButton_back.setText(QCoreApplication.translate("Form", u"\u9000\u683c", None))
        self.PushButton_clean.setText(QCoreApplication.translate("Form", u"\u6e05\u9664", None))
        self.PushButton_n7.setText(QCoreApplication.translate("Form", u"7", None))
        self.PushButton_quit.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.PushButton_n8.setText(QCoreApplication.translate("Form", u"8", None))
        self.PushButton_div.setText(QCoreApplication.translate("Form", u"/", None))
        self.PushButton_n6.setText(QCoreApplication.translate("Form", u"6", None))
        self.PushButton_n1.setText(QCoreApplication.translate("Form", u"1", None))
        self.PushButton_point.setText(QCoreApplication.translate("Form", u".", None))
        self.PushButton_n4.setText(QCoreApplication.translate("Form", u"4", None))
        self.PushButton_n3.setText(QCoreApplication.translate("Form", u"3", None))
        self.PushButton_sub.setText(QCoreApplication.translate("Form", u"-", None))
        self.PushButton_n9.setText(QCoreApplication.translate("Form", u"9", None))
        self.PushButton_n0.setText(QCoreApplication.translate("Form", u"0", None))
        self.PushButton_mul.setText(QCoreApplication.translate("Form", u"X", None))
        self.PushButton_add.setText(QCoreApplication.translate("Form", u"+", None))
        self.PushButton_n2.setText(QCoreApplication.translate("Form", u"2", None))
        self.PushButton_n5.setText(QCoreApplication.translate("Form", u"5", None))
        self.PushButton_equal.setText(QCoreApplication.translate("Form", u"=", None))
    # retranslateUi

