# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QRadioButton, QSizePolicy, QTextEdit, QLineEdit,
    QWidget)

import json
import os
import sys

class Ui_Dialog(object):
    def dialog_setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        self.hyp_json = Dialog.hyp

        Dialog.resize(Dialog.main_window_w/5, Dialog.main_window_h/5)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, Dialog.main_window_w/5, (Dialog.main_window_h/5)/4))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, ((Dialog.main_window_h/5)/4)+20, Dialog.main_window_w/5-20, (Dialog.main_window_h/5)/4))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(0, (Dialog.main_window_h/5)/2+40, Dialog.main_window_w/5-10, (Dialog.main_window_h/5)/4))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QFont()
        if (Dialog.main_window_h/5)/4 > 100:
            font.setPointSize(25)
        elif 100 > (Dialog.main_window_h/5)/4 > 50:
            font.setPointSize(20)
        else:
            font.setPointSize(15)

        self.lineEdit.setFont(font)

        self.dialog_retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

        self.buttonBox.accepted.connect(self.ok)
        self.buttonBox.rejected.connect(QCoreApplication.instance().quit)
    # setupUi

    def dialog_retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt;\">Your main Character name</span></p></body></html>", None))

    # retranslateUi


    def ok(self):
        character_name = self.lineEdit.text()
        self.hyp_json['my_character'] = character_name
        with open('./resource/config.json', 'w', encoding='utf-8') as f:
            json.dump(self.hyp_json, f, indent=2, ensure_ascii=False)
        os.execl(sys.executable, sys.executable, *sys.argv)
