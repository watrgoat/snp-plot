import yfinance as yf
import pandas as pd

# s&p 500 ticker symbol
snp = yf.Ticker('^GSPC')

df = snp.history(period='max', interval='1mo')
df = df.reset_index()['Close']

m_returns = []
# Monthly Return = (Closing Price on Month / Closing Price Previous Month) - 1
for i in range(1, len(df)-1):
    m_returns.append((df[i]/df[i-1])-1)

df = pd.DataFrame(m_returns, columns=['Returns'])
df.to_csv('returns.csv')