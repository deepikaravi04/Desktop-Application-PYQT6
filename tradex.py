import sys
from PyQt6.QtWidgets import QApplication, QWidget, QProgressBar, QGraphicsScene, QLabel, QScrollArea
from PyQt6 import uic, QtCore
import requests
from pyngrok import ngrok
import threading
import time
from flask import Flask, request
from werkzeug.serving import make_server
from ib_insync import *
import asyncio

# Load both ui files
uifile_splash = 'splash_screen.ui'
form_splash, base_splash = uic.loadUiType(uifile_splash)

uifile_main = 'dashboardx.ui'
form_main, base_main = uic.loadUiType(uifile_main)

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


class ServerThread(threading.Thread):

    def __init__(self, app):
        threading.Thread.__init__(self)
        self.server = make_server('127.0.0.1', 8000, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        # log.info('starting server')
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()


class MainPage(base_main, form_main):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.center()
        self.endpoint_url = None
        self.reserve_value = None
        self.trade_value = None
        self.risk_value = None
        self.stock_one = None
        self.stock_two = None
        self.stock_three = None
        self.stock_four = None
        self.startButton.clicked.connect(self.start_functions)
        self.stopButton.clicked.connect(self.stop_functions)

    def start_functions(self):
        self.get_trade_values()
        self.start_flask_server()
        self.scroll_area_content = self.findChild(QScrollArea, "scrollArea")
        self.ngrok_connect_endpoint()
        # self.place_order_tradex()
        pass

    def stop_functions(self):
        self.stop_flask_server()
        ngrok.disconnect(self.endpoint_url)
        self.scroll_area_content.setWidget(QLabel(' ##################### closed connection ngrok ##################### '))
        # ib.disconnect()
        # flask_thread.stop()
        pass
    
    def ngrok_connect_endpoint(self):
        tunnel = ngrok.connect(8000, "http")
        self.endpoint_url = tunnel.public_url
        print()
        webhook_url = "http://3.87.76.198/endpoint_webhook"  
        data = {
            "username": "TEST", "desktop_url": self.endpoint_url
        }
        response = requests.post(webhook_url, json=data)
        if response.status_code == 200:
            self.scroll_area_content.setWidget(QLabel(' ##################### connected ngrok #####################'))
            print("Public URL sent to webhook successfully")
        else:
            print("Failed to send public URL to webhook")
        print(self.endpoint_url)



    def start_flask_server(self):
        print("start")
        global server
        app = Flask('myapp')
        # App routes defined here
        @app.route('/')
        def hello():
            return 'Hello, World!'
        
        @app.route('/desktop_webhook', methods=['POST'])
        async def handle_webhook():
            data = request.json 
            print("Webhook received:", data)
            symbol = data.get('symbol')
            price = data.get('price')
            trade_capital = self.reserve_value * (self.risk_value * 0.01)
            stoploss_percentage = (self.risk_value/price) * 100
            quantity = int(trade_capital / stoploss_percentage)
            # print(trade_capital , stoploss_percentage, risk_value, risk_value* 0.1, quantity)
            action = data.get('action')
            if symbol == self.stock_one or symbol == self.stock_two or symbol == self.stock_three or symbol == self.stock_four:
                asyncio.create_task(place_order(ib, symbol, quantity, action))
            return 'Webhook received successfully', 200


        server = ServerThread(app)
        server.start()
        # log.info('server started')
        print('server started')

        
    def stop_flask_server(self):
        global server
        print("Hello")
        server.shutdown()
        print('stop')

    def get_trade_values(self):
        self.reserve_value = int(self.reserveText.toPlainText())
        self.trade_value = int(self.tradeText.toPlainText())
        self.risk_value = int(self.riskText.toPlainText())
        self.stock_one = (self.stockOneText.toPlainText())
        self.stock_two = (self.stockTwoText.toPlainText())
        self.stock_three = (self.stockThreeText.toPlainText())
        self.stock_four = (self.stockFourText.toPlainText())
        

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


