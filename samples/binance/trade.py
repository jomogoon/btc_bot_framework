from botfw.base.trade import test_trade
from botfw.binance.trade import BinanceTrade
test_trade(BinanceTrade('btcusdt', future=True))
