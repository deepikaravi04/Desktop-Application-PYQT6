import sys
import threading
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
from flask import Flask, request
from PyQt6.QtCore import QProcess
from pyngrok import ngrok
import requests
from ib_insync import *
import asyncio


ib = IB()
ib.connect('127.0.0.1', 7497, clientId=2)
async def place_order(ib, symbol, quantity, action):
    if ib.isConnected():
        contract = Stock(symbol, 'SMART', 'USD')  
        order = MarketOrder(action, quantity)
        trade = ib.placeOrder(contract, order)
        print("Order placed:", trade)
    else:
        print("Not connected to IB API. Cannot place order.")


flask_app = Flask(__name__)
stock_lis = []
reserve_value = []
trade_value = []
risk_value = []
@flask_app.route('/desktop_webhook', methods=['POST'])
async def handle_webhook():
    global stock_lis, reserve_value, trade_value, risk_value
    data = request.json 
    print("Webhook received:", data)
    risk_value = int(risk_value[0])
    reserve_value = int(reserve_value[0])
    symbol = data.get('symbol')
    price = data.get('price')
    # print(reserve_value, risk_value)
    trade_capital = reserve_value * (risk_value * 0.01)
    stoploss_percentage = (risk_value/price) * 100
    quantity = int(trade_capital / stoploss_percentage)
    # print(trade_capital , stoploss_percentage, risk_value, risk_value* 0.1, quantity)
    action = data.get('action')
    if symbol in stock_lis:
        asyncio.create_task(place_order(ib, symbol, quantity, action))
    return 'Webhook received successfully', 200
 
def run_flask():
    flask_app.run(port=8000)

class MyWindow(QMainWindow):
    endpoint_url = None
    
    global stock_lis, reserve_value, trade_value, risk_value

    def __init__(self):
        super().__init__()
        loadUi('dashboardx.ui', self)
        self.startButton.clicked.connect(self.run_functions)
        self.stopButton.clicked.connect(self.stop_functions)

    def run_functions(self):
        # self.run_script()
        self.button_clicked()
        self.place_order_tradex()


    def stop_functions(self):
        ngrok.disconnect(self.endpoint_url)
        ib.disconnect()
        # flask_thread.stop()

    def run_script(self):
        tunnel = ngrok.connect(8000, "http")
        self.endpoint_url = tunnel.public_url
        print()
        webhook_url = "http://3.87.76.198/endpoint_webhook"  
        data = {
            "username": "TEST", "desktop_url": self.endpoint_url
        }
        response = requests.post(webhook_url, json=data)
        if response.status_code == 200:
            print("Public URL sent to webhook successfully")
        else:
            print("Failed to send public URL to webhook")
        print(self.endpoint_url)

    def button_clicked(self):
        # print("Button clicked")
        reserve_value.append(self.reserveText.toPlainText())
        trade_value.append(self.tradeText.toPlainText())
        risk_value.append(self.riskText.toPlainText())
        print("Reserve value:", reserve_value)
        stock_lis.append(self.stockOneText.toPlainText())
        stock_lis.append(self.stockTwoText.toPlainText())
        stock_lis.append(self.stockThreeText.toPlainText())
        stock_lis.append(self.stockFourText.toPlainText())
        # Make sure to replace the IP and port with your TWS or Gateway settings
        print("Button clicked!")
        print(stock_lis)

    def place_order_tradex(self):
        return "success"







if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
