#from .abs_stock import AbsStock
from .parentStockFunctions import ParentStockFunctions

class Tea(ParentStockFunctions):
    
    recordTrade = []
    
    def __init__(self):
        self.stockType = 'common'
        self.lastDividend = 0.0
        self.fixedDividend = 0.0
        self.parValue = 100.0
        #self.__totalQuantity = 0.0
        

        
              