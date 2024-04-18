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



def run_flask():
    flask_app.run(port=8000)

class MyWindow(QMainWindow):
    endpoint_url = None
    
    global stock_lis  

    def __init__(self):
        self.reserve_value = None
        self.trade_value = None
        self.risk_value = None
        super().__init__()
        loadUi('dashboardx.ui', self)
        self.startButton.clicked.connect(self.run_functions)
        self.stopButton.clicked.connect(self.stop_functions)

    def run_functions(self):
        self.run_script()
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
        self.reserve_value = self.reserveText.toPlainText()
        self.trade_value = self.tradeText.toPlainText()
        self.risk_value = self.riskText.toPlainText()
        reserve_value = flask_app.config['reserve_value'] 
        print("Reserve value:", reserve_value)
        stock_lis.append(self.stockOneText.toPlainText())
        stock_lis.append(self.stockTwoText.toPlainText())
        stock_lis.append(self.stockThreeText.toPlainText())
        stock_lis.append(self.stockFourText.toPlainText())
        print("Button clicked!")
        print(stock_lis)

    def place_order_tradex(self):
        return "success"



flask_app = Flask(__name__)
stock_lis = []
@flask_app.route('/desktop_webhook', methods=['POST'])
async def handle_webhook():
    global stock_lis 
    data = request.json 
    print("Webhook received:", data)
    symbol = data.get('symbol')
    quantity = 1
    action = data.get('action')
    obj = MyWindow()
    value2 = obj.reserve_value
    print(value2)
    asyncio.create_task(place_order(ib, symbol, quantity, action))
    return 'Webhook received successfully', 200


if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
