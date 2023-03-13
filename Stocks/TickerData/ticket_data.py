# Importing the yfinance package
import yfinance as yf

# Set the start and end date
start_date = '2020-01-01'
end_date = '2022-01-01'

# Set the ticker
tickers = [
    'A',
    'GOOGL'
]

# Get the data
for ticker in tickers:
    data = yf.download(ticker, start_date, end_date)
    data["Date"] = data.index
    data.to_csv(ticker+".csv")
