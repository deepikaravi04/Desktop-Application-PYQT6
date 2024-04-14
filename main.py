import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the .ui file
        loadUi('dashboardx.ui', self)
        # Connect the button's clicked signal to a slot
        self.startButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        # This method will be called when the button is clicked
        reserve_value = self.reserveText.toPlainText()
        trade_value = self.tradeText.toPlainText()
        risk_value = self.riskText.toPlainText()
        # print(reserve_value, trade_value, risk_value)
        stock_one_value = self.stockOneText.toPlainText()
        stock_two_value = self.stockTwoText.toPlainText()
        stock_three_value = self.stockThreeText.toPlainText()
        stock_four_value = self.stockFourText.toPlainText()
        # print(stock_one_value, stock_two_value, stock_three_value, stock_four_value)
        print("Button clicked!")
        # Perform your desired process here

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
