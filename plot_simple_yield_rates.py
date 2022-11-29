# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

ddf = pd.DataFrame()


def clean_df(df):
    df['Date'] = pd.to_datetime(df['Date'])
    # df = df.set_index('Date')
    df = df.drop(['20 YR', '30 YR', 'Extrapolation Factor',
       '8 WEEKS BANK DISCOUNT', '17 WEEKS BANK DISCOUNT','COUPON EQUIVALENT', '52 WEEKS BANK DISCOUNT',
       'COUPON EQUIVALENT.1','COUPON EQUIVALENT.2'],axis=1).set_index('Date')
    return df


# for year in range(2022,2023):
for year in range(1990,1991):
    url = f"https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value={year}"
    table_list = pd.read_html(url)
    
    df = table_list[0]
    # df.head()
    # print(df)
    
    ddf = pd.concat([ddf,clean_df(df)]) 
    
    # ddf += clean_df(df)

    
# df = clean_df(df)
# print(ddf)   
ddf = ddf.sort_index()
# ddf.head()
# print(ddf.tail())
print(ddf) 
df = ddf




# df.to_csv('cleaned_yields_2022.csv') 

##### load csv files and combine to table

print(df.head())
df.columns = [    "1M",
                  "2M",
                  "3M",
                  "4M",
                  "6M",
                  "1Y","2Y","3Y","5Y","7Y","10Y","20Y",
                  "30Y"]

# print(df)
import matplotlib.pyplot as plt
plt.plot(df.index, df['1M'], color='grey')
plt.plot(df.index, df['2M'], color='grey')
plt.plot(df.index, df['3M'], color='grey')
plt.plot(df.index, df['4M'], color='grey')
plt.plot(df.index, df['6M'], color='grey')
plt.plot(df.index, df['1Y'], color='grey')
plt.plot(df.index, df['2Y'], color='grey')
plt.plot(df.index, df['3Y'], color='grey')
plt.plot(df.index, df['5Y'], color='grey')
plt.plot(df.index, df['7Y'], color='grey')
plt.plot(df.index, df['10Y'], color='grey')
plt.plot(df.index, df['20Y'], color='grey')
plt.plot(df.index, df['30Y'], color='grey')
# plt.plot(df['LOCAL_DATE'], df['MIN_TEMPERATURE'], color='blue')!!
# plt.title('Toronto Temperature in 2020', fontsize=18)
plt.xlabel('Date', fontsize=12)
# plt.ylabel('Temperature', fontsize=12)
plt.grid(True)
plt.show()
# print(df)
# import plotly.graph_objects as go
# import pandas as pd
# import numpy as np

# x = df.columns
# y = df.index
# z = df.to_numpy()

# fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
# fig.update_layout(title='Yield Curves',
#                   scene = {"aspectratio": {"x": 1, "y": 1, "z": 0.4}})
# fig.show()

