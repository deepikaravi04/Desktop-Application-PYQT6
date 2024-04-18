from ib_insync import *
import datetime

# Connect to TWS or IB Gateway
util.startLoop()
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)  # Adjust host and port accordingly

# Get previous day's date
prev_day = datetime.date.today() - datetime.timedelta(days=1)

# Request trades for the previous day
# trades = ib.trades()

# for trade in trades:
#     print(trade)
# # Filter trades for the previous day
# prev_day_trades = [trade for trade in trades if trade.execution.time.date() == prev_day]

# # Calculate P&L
# realized_pnl = sum(trade.realizedPNL for trade in prev_day_trades)
# unrealized_pnl = sum(trade.unrealizedPNL for trade in prev_day_trades)

# print("Realized P&L for", prev_day, ":", realized_pnl)
# print("Unrealized P&L for", prev_day, ":", unrealized_pnl)

# # Disconnect from IB
# ib.disconnect()
completed_orders = ib.reqCompletedOrders(apiOnly=True)
for i in completed_orders:
    print(i)
    print()