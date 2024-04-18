import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
from PyQt6 import uic

# Load both ui files
uifile_1 = 'splash_screen.ui'
form_1, base_1 = uic.loadUiType(uifile_1)

uifile_2 = 'dashboardx.ui'
form_2, base_2 = uic.loadUiType(uifile_2)


class Example(base_1, form_1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.startButton.clicked.connect(self.change)
        self.change()

        
    def change(self):
        self.main = MainPage()
        self.main.show()
        self.close()

class MainPage(base_2, form_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())