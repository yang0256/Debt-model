# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 11:08:57 2022

@editor: Tao Yang 
modified from Jose Portilla's original code at https://pieriantraining.com/author/jportilla/
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


for year in range(2022,2023):
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
# ddf.tail()

df = ddf
print(df)

import plotly.graph_objects as go
import pandas as pd
import numpy as np

x = df.columns
y = df.index
z = df.to_numpy()

fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_layout(title='Yield Curves',
                  scene = {"aspectratio": {"x": 1, "y": 1, "z": 0.4}})
fig.show()
    



