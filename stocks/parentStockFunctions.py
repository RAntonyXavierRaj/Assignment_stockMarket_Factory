# -*- coding: utf-8 -*-
from .abs_stock import AbsStock
import datetime

class ParentStockFunctions(AbsStock):
    
    def stockType(self):
        return self.stockType
    def lastDividend(self):
        return self.lastDividend
    def fixedDividend(self):
        return self.fixedDividend
    def parValue(self):
        return self.parValue
          
    def buy(self, quantity, price):
        #self.__totalQuantity += quantity
        self.recordTrade.append([datetime.datetime.now(), 'buy', quantity, price])
    

    def sell(self,quantity, price):
        #quantity = -quantity
        #self.__totalQuantity += quantity
        self.recordTrade.append([datetime.datetime.now(), 'sell', quantity, price])

    
    # Function to calculate Dividend Yield
    def calculateDividendYield(self, price):
        if self.stockType == 'common':
            return (self.lastDividend / price)
        elif self.stockType == 'preferred':
            return (self.fixedDividend * self.parValue / price)
    
    # Function to calculate PE ratio
    def calculatePriceToEarningsRatio(self, price):
        dividend = self.lastDividend
        if (dividend) == 0:
            return (0)
        else:
            return (price/dividend)
        
    # function to calculate Volume weighted stock price
    # recorded trades under the stocks are used to find the volume weights.  
    def calculateVolumeWeightedStockPrice(self):
        cutOffTime = datetime.datetime.now() - datetime.timedelta(minutes=15)
        x = 0
        y = 0
        for i in range(len(self.recordTrade),0,-1):
            temp = self.recordTrade[i-1]
            if temp[0] > cutOffTime:
                y = y + (temp[2] * temp[3])             # numerator  = quantity x price
                x = x + temp[2]                         # denominator = sum of quantities
            else:
                return 0
        return (y/x)
    
    