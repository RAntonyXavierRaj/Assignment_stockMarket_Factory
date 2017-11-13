from inspect import getmembers,  isclass, isabstract
import stocks

class StockFactory(object):
    stocks = {}  # Key = stock model name, Value = class for the stock

    
    def __init__(self):
        self.load_stocks()

    def load_stocks(self):
        classes = getmembers(stocks, lambda m: isclass(m) and not isabstract(m))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, stocks.AbsStock):
                self.stocks.update([[name, _type]])

    def create_instance(self, stockname):
        if stockname in self.stocks:
            return self.stocks[stockname]()
        else:
            return stocks.NullStock(stockname) 

