import yfinance as yf
class StockRepository:
    def fetch(self, ticker):
        return yf.download(ticker)