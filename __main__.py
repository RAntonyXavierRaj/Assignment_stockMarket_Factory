from stockfactory import StockFactory
import pandas as pd

stockNames = pd.read_csv("StocksList.csv", header = None)

factory = StockFactory()

market = {}
for i in stockNames[0]:
    market.update([[i, factory.create_instance(i)]])

    
    
# trades for ale
market['Ale'].buy(200, 1000)
market['Ale'].sell(100, 1200)
market['Ale'].buy(20, 1100)

# trades for gin
market['Gin'].buy(500, 900)
market['Gin'].sell(300, 800)
market['Gin'].sell(200, 1000)

# trades for joe
market['Joe'].buy(20, 700)
market['Joe'].sell(100, 800)
market['Joe'].buy(50, 900)

# trades for pop
market['Pop'].buy(20, 1200)
market['Pop'].sell(500, 1300)
market['Pop'].buy(200, 1500)

# trades for tea
market['Tea'].sell(200, 1200)
market['Tea'].sell(200, 1300)
market['Tea'].buy(100, 1400)

# Samplestock functions
print(market['Ale'].calculateDividendYield(150))
print(market['Ale'].calculatePriceToEarningsRatio(150))
print(market['Ale'].calculateVolumeWeightedStockPrice())

