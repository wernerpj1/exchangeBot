import ccxt
import numpy as np
from .modelos.orders import Orders


priceDollar = 0


class DollarToReal:
    def __init__(self, coin):
        self.coin = coin
        self.qtity = coin[0]
        self.coinQtity = coin[1]
        self.price = float(0)


    def fetchQtity(self):
        limitOrder = 1  
        qtityFetch = self.getDollarPrice(limitOrder)[0][1]
        arrayOrders = self.getDollarPrice(limitOrder)[0]
       
        if float(self.qtity) < float(qtityFetch):
            qtityFetch = self.qtity
            arrayOrders = [[arrayOrders[0], qtityFetch]]
        else:
            while (float(self.qtity) > float(qtityFetch)):
                limitOrder = limitOrder + 1
                asks = np.array(self.getDollarPrice(limitOrder))

                qtityFetch = np.sum(asks, axis=0)[1]

            else:
                    
                arrayOrders = self.getDollarPrice(limitOrder)
               
                qtityFetch = np.sum(np.array(arrayOrders), axis=0)[1]
                rest = qtityFetch - self.qtity
                
                arrayOrders[len(arrayOrders) - 1][1] = arrayOrders[len(arrayOrders) - 1][1] - rest
                #print(arrayOrders[len(arrayOrders) - 1])
                

        return arrayOrders


    def getDollarPrice(self, limitOrder):
        exchange = getattr(ccxt, 'binance')
        priceDollar = exchange().fetch_order_book('USDT/BRL', limit=limitOrder)
        
        return priceDollar['asks']
    
    def convert(self):
        arrayOrders = self.fetchQtity()
        
        parcial = 0
        for i in range(len(arrayOrders)):
            parcial += float(arrayOrders[i][0]) * float(arrayOrders[i][1])
        self.price = parcial * 1.01

        orderThreat = [self.price, self.coinQtity]

        return orderThreat
