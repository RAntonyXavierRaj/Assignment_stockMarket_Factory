# This class will work on passing new name
from .parentStockFunctions import ParentStockFunctions

class NullCar(ParentStockFunctions):
    
    recordTrade = []    
    
    def __init__(self, carname):
        self._carname = carname
        self.stockType = 'common'
        self.lastDividend = 0.0
        self.fixedDividend = 0.0
        self.parValue = 100.0
