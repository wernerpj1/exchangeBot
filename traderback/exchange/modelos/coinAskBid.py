import json
from types import SimpleNamespace
from .orders import Orders

class CoinAskBid:
    #constructor
    def __init__(self, name, asks, bids):
        orders_asks = Orders(asks[0][0], asks[0][1])
        orders_bids = Orders(bids[0][0], bids[0][1])
        self.name = name
        self.asks = orders_asks
        self.bids = orders_bids

    def getBestAsk(self):
        return self.asks
    
    def getBestBid(self):
        return self.bids