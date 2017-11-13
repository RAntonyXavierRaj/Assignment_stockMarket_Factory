#from .abs_stock import AbsStock
from .parentStockFunctions import ParentStockFunctions

class Pop(ParentStockFunctions):
    
    recordTrade = []
    
    def __init__(self):
        self.stockType = 'common'
        self.lastDividend = 8.0
        self.fixedDividend = 0.0
        self.parValue = 100.0
        #self.__totalQuantity = 0.0
        
     
              