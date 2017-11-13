import abc

class AbsStock(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def buy(self):
        pass
    
    @abc.abstractmethod
    def sell(self):
        pass

    
    @abc.abstractproperty   
    def stockType(self):
        pass
    
    @abc.abstractproperty
    def lastDividend(self):
        pass
    
    @abc.abstractproperty
    def fixedDividend(self):
        pass
    
    @abc.abstractproperty
    def parValue(self):
        pass
    """
    @abc.abstractmethod
    def calculateDividendYield(self):
        pass
    
    @abc.abstractmethod
    def calculatePriceToEarningsRatio(self):
        pass
    
    @abc.abstractmethod
    def calculateVolumeWeightedStockPrice(self):
        pass
"""