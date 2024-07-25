from stock import Stock
from stockparser import addStocks

stockfile = "data/NASDAQ.txt"
marketsize = 20


class StockMarket:
    BLUE = "\033[94m"
    END_COLOR = "\033[0m"

    def __init__(self):
        self.stocks: list[Stock] = []
        self.stockandtickers = {}

    def initialize_stocks(self):
        addStocks(self.stocks, self.stockandtickers, stockfile, marketsize)

    def fluctuate_market(self):
        for stock in self.stocks:
            stock.fluctuate()

    def print_market_status(self, initial):
        if (initial):
            print("Initial Stock Prices:")
        else:
            print("Current Stock Prices:")
        for stock in self.stocks:
            print(f"{stock.ticker}: {stock.name}, ${stock.price:.2f}")
        print("")

    def get_stock(self, ticker):
        return self.stockandtickers.get(ticker)
        
