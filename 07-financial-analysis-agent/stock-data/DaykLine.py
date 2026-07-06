import pandas as pd
import akshare as ak

df = ak.stock_zh_a_hist(symbol="600600", 
                                        period="daily", 
                                        start_date="20240901", 
                                        end_date='20240930', 
                                        adjust="qfq")

print(df.dtypes)
df['日期'] = pd.to_datetime(df['日期'])
print(df.dtypes)

df.set_index('日期', inplace=True)
df.sort_index(ascending=True, inplace=True)

df.to_csv('600600.csv')
