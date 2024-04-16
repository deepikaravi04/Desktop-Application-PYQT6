from flask import Flask, request
from ib_insync import *
import asyncio

app = Flask(__name__)
ib = IB()

# Connect to the IB API
ib.connect('127.0.0.1', 7497, clientId=1)  # Adjust host, port, and clientId as needed

# Function to place an order
async def place_order(ib, symbol, quantity, action):
    print("#################")
    if ib.isConnected():
        contract = Stock(symbol, 'SMART', 'USD')  
        order = MarketOrder(action, quantity)
        trade = ib.placeOrder(contract, order)
        print("Order placed:", trade)
    else:
        print("Not connected to IB API. Cannot place order.")

# Route to receive webhook
@app.route('/desktop_webhook', methods=['POST'])
def webhook():
    data = request.json  # Get JSON data from the request
    print("Webhook received:", data)  # Print the received data
    # Extract order information from the received data
    symbol = data.get('symbol')
    quantity = 1
    action = data.get('action')
    asyncio.run(place_order(ib, symbol, quantity, action))
    return 'Webhook received successfully', 200  # Return a response to the sender

if __name__ == '__main__':
    # util.startLoop()
    app.run(debug=True)  # Run the Flask app in debug mode
