from PySide6.QtWidgets import QApplication, QMainWindow
# from PySide6.QtWidgets import *
from information import Ui_MainWindow
import json
from api_test import GetData
import screeninfo

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        with open('./hyp.json', 'r') as j:
            self.hyp = json.load(j)
        self.API = GetData()
        monitor_info = screeninfo.get_monitors()[0]
        monitor_height = monitor_info.height
        monitor_width = monitor_info.width
        self.main_window_w = int(monitor_width/2)
        self.main_window_h = int(monitor_height/2)
        self.setupUi(self)


app = QApplication()
window = MainWindow()
window.show()
app.exec_()