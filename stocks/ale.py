
#from .abs_stock import AbsStock
#import datetime
from .parentStockFunctions import ParentStockFunctions

class Ale(ParentStockFunctions):

    recordTrade = []
    
    def __init__(self):
        self.stockType = 'common'
        self.lastDividend = 23.0
        self.fixedDividend = 0.0
        self.parValue = 60.0
  

  