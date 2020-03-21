from datetime import datetime
import MetaTrader5 as mt5
import sys
import time
import socket, numpy as np
from sklearn.linear_model import LinearRegression

# Initializing MT5 connection 
if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()

class socketserver:
    def __init__(self, address = '', port = 9090):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address
        self.port = port
        self.sock.bind((self.address, self.port))
        self.cummdata = ''
    def recvmsg(self) :
        self.sock.listen(1)
        self.conn, self.addr = self.sock.accept()
        print('connected to', self.addr)
        self.cummdata = ''
        while True:
            data = self.conn.recv(10000)
            self.cummdata+=data.decode("utf-8")
            if not data:
                break
            self.conn.send(bytes(calcregr(self.cummdata), "utf-8"))
            return self.cummdata
    def __del__(self):
        self.sock.close()

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