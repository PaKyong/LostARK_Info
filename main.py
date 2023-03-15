from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QScreen
from information import Ui_MainWindow
from dialog import Ui_Dialog
import json
from api_test import LostArkAPI
import screeninfo

class MainWindow(QMainWindow, Ui_MainWindow, Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        with open('./resource/config.json', 'r') as j:
            self.hyp = json.load(j)
        self.API = LostArkAPI()
        monitor_info = screeninfo.get_monitors()[0]
        monitor_height = monitor_info.height
        monitor_width = monitor_info.width
        self.main_window_w = int(monitor_width/2)
        self.main_window_h = int(monitor_height/2)
        if self.hyp.get("my_character") is None:
            self.dialog_setupUi(self)
        else:
            self.main_setupUi(self)




if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    geo = window.frameGeometry()
    geo.moveCenter(center)
    window.move(geo.topLeft())
    app.exec()