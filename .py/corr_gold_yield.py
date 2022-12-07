# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:13:30 2022

@author: solvm
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
df = pd.read_csv(r"C:\Users\solvm\Downloads\usd_vs_yield.csv", index_col=0, parse_dates=['DATE'])

print(df.info())
print(df.head())
print(df.tail())

plt.plot(df.index, df['DGS3'], color='grey')
plt.plot(df.index, df['DGS5'], color='grey')
plt.plot(df.index, df['DGS10'], color='grey')
plt.plot(df.index, df['DX'], color='red')
# plt.plot(df.index, df['DGS30'], color='grey')
# plt.plot(df.index, df['DGS3'], color='grey')
# plt.plot(df.index, df['DGS1'], color='grey')
# plt.plot(df.index, df['CPI'], color='grey')
# plt.plot(df.index, df['DX'], color='grey')

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

# print(df.head())

print(df.corr())
dataplot = sb.heatmap(df.corr(), cmap = "YlGnBu", annot = False)
plt.show()
