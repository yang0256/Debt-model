import pandas as pd
import matplotlib.pyplot as plt
ddf = pd.DataFrame()
'''function to clean the dataset'''
def clean_df(df): 
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.drop(['20 YR', '30 YR', 'Extrapolation Factor',
       '8 WEEKS BANK DISCOUNT', '17 WEEKS BANK DISCOUNT','COUPON EQUIVALENT', '52 WEEKS BANK DISCOUNT',
       'COUPON EQUIVALENT.1','COUPON EQUIVALENT.2'],axis=1).set_index('Date')
    return df
'''gathering data and call clean function to transform dataset'''
for year in range(2022,2023):
    url = f"https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value={year}"
    table_list = pd.read_html(url)
    df = table_list[0]
    ddf = pd.concat([ddf,clean_df(df)]) 
df = ddf.sort_index()
print(df.head())
df.columns = [    "1M", "2M", "3M","4M", "6M",
                  "1Y","2Y","3Y","5Y","7Y","10Y","20Y","30Y'"]
###plotting the chart

plt.plot(df.index, df['1M'], color='grey')
plt.plot(df.index, df['2M'], color='grey')
plt.plot(df.index, df['3M'], color='grey')
plt.plot(df.index, df['4M'], color='red')
plt.plot(df.index, df['6M'], color='grey')
plt.plot(df.index, df['1Y'], color='grey')
plt.plot(df.index, df['2Y'], color='grey')
plt.plot(df.index, df['3Y'], color='red')
plt.plot(df.index, df['5Y'], color='grey')
plt.plot(df.index, df['7Y'], color='grey')
plt.plot(df.index, df['10Y'], color='black')
plt.plot(df.index, df['20Y'], color='red')
plt.plot(df.index, df['30Y'], color='grey')
# plt.plot(df['LOCAL_DATE'], df['MIN_TEMPERATURE'], color='blue')!!
# plt.title('Toronto Temperature in 2020', fontsize=18)
plt.xlabel('Date', fontsize=12)
# plt.ylabel('Temperature', fontsize=12)
plt.grid(True)
plt.show()