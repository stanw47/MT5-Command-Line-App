from datetime import datetime
import MetaTrader5 as mt5
import sys
import time

# Initializing MT5 connection 
if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()

print(mt5.terminal_info())
print(mt5.version())

now = datetime.now()

gbpusd_ticks = mt5.copy_ticks_from("GBPUSD", now, 1, mt5.COPY_TICKS_ALL)
eurusd_ticks = mt5.copy_ticks_from("EURUSD", now, 1, mt5.COPY_TICKS_ALL)
audusd_ticks = mt5.copy_ticks_from("AUDUSD", now, 1, mt5.COPY_TICKS_ALL)
usdjpy_ticks = mt5.copy_ticks_from("USDJPY", now, 1, mt5.COPY_TICKS_ALL)



start = input("What do you want to do? For FX quotes, type 'quotes', or to place a trade, type 'trade' ")
if start == "quotes":
    print(gbpusd_ticks, eurusd_ticks, audusd_ticks, usdjpy_ticks)

if start == "trade":
    print("Which currency pair?")