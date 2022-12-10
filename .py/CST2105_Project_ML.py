import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\solvm\OneDrive\Documents\Python Scripts\yield_data_Daily.csv", index_col=0, parse_dates=['DATE'])

print(df.info())
print(df.head())
print(df.tail())

plt.plot(df.index, df['DGS10'], color='grey')
plt.plot(df.index, df['DGS20'], color='grey')
plt.plot(df.index, df['DGS5'], color='grey')
plt.plot(df.index, df['DGS2'], color='red')
plt.plot(df.index, df['DGS30'], color='grey')
plt.plot(df.index, df['DGS3'], color='grey')
plt.plot(df.index, df['DGS1'], color='grey')
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

df_training = df.drop(["DGS20","DGS5","DGS2","DGS30","DGS3",
"DGS1","CPI","DX"],axis=1)
plt.plot(df_training.index, df_training['DGS10'])
# plt.show()
df_training['ds'] = df_training.index
df_training = df_training.rename(columns={"DGS10":"y"})
# print(df.head())
df_training.index = df_training.index.rename('ds')
# print(df.head())
# print(df.dtypes)

from prophet import Prophet
# initialiazing the model with 95% confidence interval
model = Prophet(interval_width= 0.95)
model.fit(df_training)

# forecasting for future
future = model.make_future_dataframe(periods=80, freq='D')
print(future.tail())
# print(df_training.tail())
# forecast predictions
forecast = model.predict(future)
# Prophet's prediction 
forecast.head()
forecast.tail()

# showing the predictions
forecast[['ds', 'yhat']].tail()
# visualizing the forecat predictions
fig1 = model.plot(forecast)
# weekly seasonality and yearly seasonality
fig2 = model.plot_components(forecast)


