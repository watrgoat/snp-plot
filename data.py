import yfinance as yf
import pandas as pd

# ticker symbol
tickers = ['^IXIC', '^GSPC', '^DJI']
for ticker in tickers:
    snp = yf.Ticker(ticker)

    df = snp.history(period='max', interval='1mo')
    df = df.reset_index()['Close']

    m_returns = []
    # Monthly Return = (Closing Price on Month / Closing Price Previous Month) - 1
    for i in range(1, len(df)-1):
        m_returns.append((df[i]/df[i-1])-1)

    df = pd.DataFrame(m_returns, columns=['Returns'])
    file = f'C:\\Users\\olive\\snp-plot\\historic data\\{ticker}.csv'
    df.to_csv(file, index=False)