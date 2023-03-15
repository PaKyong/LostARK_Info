# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'informationoqDzFb.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from functools import cached_property
import requests
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, Signal, QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTabWidget, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout)

from PySide6.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest

class Ui_MainWindow(object):
    def main_setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(MainWindow.main_window_w, MainWindow.main_window_h)
        self.win_w, self.win_h = MainWindow.main_window_w, MainWindow.main_window_h
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(5, 0, MainWindow.main_window_w-10, MainWindow.main_window_h-2))
        self.tab = self.my_character(MainWindow.API, MainWindow.hyp)
        self.tab.setObjectName(u"my_character")
        self.tabWidget.addTab(self.tab, "내 캐릭터")
        self.tab_2 = QWidget(self.search_character(MainWindow.API))
        self.tab_2.setObjectName(u"search_character")
        self.tabWidget.addTab(self.tab_2, "캐릭터 찾기")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"search_item")
        self.tabWidget.addTab(self.tab_3, "아이템 찾기")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, MainWindow.main_window_w, 35))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.main_retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def main_retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"내 캐릭터", None))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"캐릭터 찾기", None))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"아이템 찾기", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\uba54\ub274", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
    # retranslateUi

    def my_character(self, api, hyp):
        if len(hyp['my_character']) > 0:
            character_list = api.get_character_lists(hyp['my_character'])
            character_list = sorted(character_list, key=lambda a:  float(a['ItemAvgLevel'].replace(',', '')), reverse=True)

        else:
            character_list = None
        charater_tab = QTabWidget()
        charater_tab.setObjectName(u"charater_tab")
        charater_tab.setGeometry(QRect(10, 4, self.win_w - 20, self.win_h - 8))


        for i in range(len(character_list)):
            c_tab = self.character_widget(api.get_character_profiles(character_list[i]['CharacterName']))
            c_tab.setObjectName(f"chracter_tab_{i}")
            charater_tab.addTab(c_tab, character_list[i]['CharacterName'])
        return charater_tab

    def character_widget(self, character_info):
        tab_widget = QWidget()
        h_layout = QHBoxLayout(tab_widget)
        img_label = QLabel(tab_widget)
        img_label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap()
        request = requests.get(character_info['CharacterImage'])
        pixmap.loadFromData(request.content)
        img_label.setPixmap(pixmap)
        h_layout.addWidget(img_label)

        info_widget = QWidget(tab_widget)
        info_grid_layout_Widget = QWidget(info_widget)
        info_grid_layout_Widget.setGeometry(QRect(0, 0, int(self.win_w/2), int(self.win_h/2)))

        grid_layout = QGridLayout(info_grid_layout_Widget)
        grid_layout.setContentsMargins(0, 0, 0, 0)

        info_label_00 = QLabel(info_grid_layout_Widget)
        info_label_00.setText("닉네임")
        grid_layout.addWidget(info_label_00, 0, 0, 1, 1)

        info_label_01 = QLabel(info_grid_layout_Widget)
        info_label_01.setText("직업")
        grid_layout.addWidget(info_label_01, 0, 1, 1, 1)

        info_label_02 = QLabel(info_grid_layout_Widget)
        info_label_02.setText("아이템 레벨")
        grid_layout.addWidget(info_label_02, 0, 2, 1, 1)

        info_label_03 = QLabel(info_grid_layout_Widget)
        info_label_03.setText("원정대 레벨")
        grid_layout.addWidget(info_label_03, 0, 3, 1, 1)

        info_label_10 = QLabel(info_grid_layout_Widget)
        info_label_10.setText(character_info["CharacterName"])
        grid_layout.addWidget(info_label_10, 1, 0, 1, 1)

        info_label_11 = QLabel(info_grid_layout_Widget)
        info_label_11.setText(character_info["CharacterClassName"])
        grid_layout.addWidget(info_label_11, 1, 1, 1, 1)

        info_label_12 = QLabel(info_grid_layout_Widget)
        info_label_12.setText(character_info["ItemAvgLevel"])
        grid_layout.addWidget(info_label_12, 1, 2, 1, 1)

        info_label_13 = QLabel(info_grid_layout_Widget)
        info_label_13.setText(str(character_info["ExpeditionLevel"]))
        grid_layout.addWidget(info_label_13, 1, 3, 1, 1)

        info_label_20 = QLabel(info_grid_layout_Widget)
        info_label_20.setText("지성")
        grid_layout.addWidget(info_label_20, 2, 0, 1, 1)

        info_label_21 = QLabel(info_grid_layout_Widget)
        info_label_21.setText("담력")
        grid_layout.addWidget(info_label_21, 2, 1, 1, 1)

        info_label_22 = QLabel(info_grid_layout_Widget)
        info_label_22.setText("매력")
        grid_layout.addWidget(info_label_22, 2, 2, 1, 1)

        info_label_23 = QLabel(info_grid_layout_Widget)
        info_label_23.setText("친절")
        grid_layout.addWidget(info_label_23, 2, 3, 1, 1)

        info_label_30 = QLabel(info_grid_layout_Widget)
        info_label_30.setText(str(character_info["Tendencies"][0]["Point"]))
        grid_layout.addWidget(info_label_30, 3, 0, 1, 1)

        info_label_31 = QLabel(info_grid_layout_Widget)
        info_label_31.setText(str(character_info["Tendencies"][1]["Point"]))
        grid_layout.addWidget(info_label_31, 3, 1, 1, 1)

        info_label_32 = QLabel(info_grid_layout_Widget)
        info_label_32.setText(str(character_info["Tendencies"][2]["Point"]))
        grid_layout.addWidget(info_label_32, 3, 2, 1, 1)

        info_label_33 = QLabel(info_grid_layout_Widget)
        info_label_33.setText(str(character_info["Tendencies"][3]["Point"]))
        grid_layout.addWidget(info_label_33, 3, 3, 1, 1)

        h_layout.addWidget(info_widget)
        return tab_widget

    def search_character(self, api, name='댠닉'):
        character_list = api.get_character_lists(name)
        character_list = sorted(character_list, key=lambda a: float(a['ItemAvgLevel'].replace(',', '')), reverse=True)

