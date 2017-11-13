#from .abs_stock import AbsStock
from .parentStockFunctions import ParentStockFunctions

class Gin(ParentStockFunctions):
    
    recordTrade = []
    
    def __init__(self):
        self.stockType = 'preferred'
        self.lastDividend = 8.0
        self.fixedDividend = 2.0
        self.parValue = 100.0
      

        
              