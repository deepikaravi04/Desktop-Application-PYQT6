import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
from PyQt6 import uic

# Load both ui files
uifile_1 = 'splash_screen.ui'
form_1, base_1 = uic.loadUiType(uifile_1)

uifile_2 = 'dashboardx.ui'
form_2, base_2 = uic.loadUiType(uifile_2)


class SplashScreen(base_1, form_1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Connect the button click to the method that switches to the main page
        # self.startButton.clicked.connect(self.change)
        self.change()

    def change(self):
        self.main = MainPage()  # Instantiate MainPage
        self.main.show()  # Show MainPage
        self.close()  # Close SplashScreen


class MainPage(base_2, form_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.center()

    def center(self):
        # Get the desktop's geometry
        desktop_geometry = QApplication.primaryScreen().geometry()

        # Calculate the center position
        x = (desktop_geometry.width() - self.width()) // 2
        y = (desktop_geometry.height() - self.height()) // 2

        # Move the window to the center
        self.move(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SplashScreen()
    ex.show()
    sys.exit(app.exec())
