import sys
from PyQt6.QtWidgets import QApplication, QWidget, QProgressBar
from PyQt6 import uic, QtCore

# Load both ui files
uifile_splash = 'splash_screen.ui'
form_splash, base_splash = uic.loadUiType(uifile_splash)

uifile_main = 'dashboardx.ui'
form_main, base_main = uic.loadUiType(uifile_main)

class MainPage(base_main, form_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.center()

    def center(self):
        desktop_geometry = QApplication.primaryScreen().geometry()
        x = (desktop_geometry.width() - self.width()) // 2
        y = (desktop_geometry.height() - self.height()) // 2
        self.move(x, y)

class SplashScreen(base_splash, form_splash):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.progress)
        self.counter = 0
        self.timer.start(35)
        self.label_description.setText("<strong>WELCOME</strong> TO MMP")
        QtCore.QTimer.singleShot(1500, lambda: self.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))

    def progress(self):
        self.progressBar.setValue(self.counter)
        if self.counter > 100:
            self.timer.stop()
            self.show_main_window()
            self.close()
        self.counter += 1

    def show_main_window(self):
        self.main = MainPage()
        self.main.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SplashScreen()
    ex.show()
    sys.exit(app.exec())
