class Stock:
    def __init__(self, tickle, stock_price, country):
        self.tickle = tickle
        self.stock_price = stock_price
        self.country = country


aStock = Stock("IBM", "90", "USA")
print(aStock.tickle, aStock.stock_price, aStock.country)
