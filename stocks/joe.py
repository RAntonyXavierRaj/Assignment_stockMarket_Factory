#from .abs_stock import AbsStock
from .parentStockFunctions import ParentStockFunctions

class Joe(ParentStockFunctions):
    
    recordTrade = []
    
    def __init__(self):
        self.stockType = 'common'
        self.lastDividend = 13.0
        self.fixedDividend = 0.0
        self.parValue = 250.0
      

        
              