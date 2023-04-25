import ccxt
import json
from types import SimpleNamespace
from .modelos.coinAskBid import CoinAskBid
import datetime


coins = [
    "BTC/BRL",
    "ETH/BRL",
    "XRP/BRL",
    "ADA/BRL",
    "DOT/BRL",
    "MATIC/BRL",
    "LINK/BRL"
  ]
class BotData:
    def __init__(self, exchange):
        self.exchange = exchange

    def getData(self):
        orderBook = []
        order = []
        connect = getattr(ccxt, self.exchange)
        for coin in coins:
            print(coin)
            orders_coin = connect().fetch_order_book(coin, limit=10)
            orders_coin = json.loads(json.dumps(orders_coin), object_hook=lambda d: SimpleNamespace(**d))
            orderBook.append(orders_coin)
        for ord in orderBook:
            name = ord.symbol
            asks = ord.asks
            bids = ord.bids
            order.append(CoinAskBid(name, asks, bids))
            
        return order
    



class Oportunity:

    def __init__(self, exchangeBid, exchangeAsk):
        self.exchangeBid = exchangeBid
        self.exchangeAsk = exchangeAsk

    def oportunity(self):
        arrayOportunity = []
        ordersBids = BotData(self.exchangeBid).getData()
        ordersAsks = BotData(self.exchangeAsk).getData()
        
        for i in range(len(ordersBids)):
            arrayOportunity.append((ordersBids[i].bids.price / ordersAsks[i].asks.price) - 1)
        
        max_index = arrayOportunity.index(max(arrayOportunity))

        opo = max(arrayOportunity)
        orderAsk = [ordersAsks[max_index].asks.price, ordersAsks[max_index].asks.qtity]
        orderBid = [ordersBids[max_index].bids.price, ordersBids[max_index].bids.qtity]
        buyIn = self.exchangeAsk
        coin = ordersAsks[max_index].name
        date = datetime.datetime.now()
        oportunity = {
            'oportunity': opo,
            'orderAsk': orderAsk,
            'orderBid': orderBid,
            'buyIn': buyIn,
            'coin': coin,
            'date': f'{date.day}/{date.month}/{date.year} -- {date.hour}:{date.minute}:{date.second}'
        }
        return oportunity