# from sklearn.datasets import load_digits
# from sklearn import datasets
# data = datasets.load_breast_cancer()
# wine = datasets.load_wine()
# from sklearn.datasets import fetch_olivetti_faces
# sklearn.datasets.load_digits
# sklearn.datasets.load_wine


# from yang0256_2101_Project import let_user_choose_next

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns




def load_dataset_cali():
    from sklearn.datasets import fetch_california_housing
    california = fetch_california_housing()
    pd.set_option('display.precision', 4)
    pd.set_option('display.max_columns', 12)
    pd.set_option('display.width' , None)
    california_df = pd.DataFrame(california.data, columns = california.feature_names)
    california_df['MedHouseValue'] = pd.Series(california.target)
    
    # print(california_df.head())
    # print(california_df.describe())
    
    sample_df = california_df.sample(frac=0.1, random_state=17)
    # print(sample_df)
    
    # import matplotlib.pyplot as plt
    # import seaborn as sns
    sns.set(font_scale=2)
    sns.set_style('whitegrid')
    
    
    # let_user_choose_next()

    print(sample_df.head())
    print(sample_df.tail())
    print('California_housing datdaset loaded:')

# '''

    for feature in california.feature_names:
        plt.figure(figsize=(16, 9))
        sns.scatterplot(data=sample_df, x=feature,
            y='MedHouseValue', hue='MedHouseValue',
            palette='cool', legend=False)
    
    ###Splitting the Data for Training and Testing
    
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
         california.data, california.target, random_state=11)
    
    X_train.shape
    (15480, 8)
    X_test.shape
    (5160, 8)


'''

##Training the Model
from sklearn.linear_model import LinearRegression
linear_regression = LinearRegression()
linear_regression.fit(X=X_train, y=y_train)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
         normalize=False)

for i, name in enumerate(california.feature_names):
      print(f'{name:>10}: {linear_regression.coef_[i]}')

###Testing the Model

predicted = linear_regression.predict(X_test)
expected = y_test
###first five predictions and their corresponding expected values:

predicted[:5]
# Out[32]: array([1.25396876, 2.34693107, 2.03794745, 1.8701254, 2.53608339])

expected[:5]
# Out[33]: array([0.762, 1.732, 1.125, 1.37 , 1.856])

df = pd.DataFrame()
df['Expected'] = pd.Series(expected)
df['Predicted'] = pd.Series(predicted)

##plot the data as a scatter plot with the expected (target) prices 
##along the x-axis and the predicted prices along the y-axis
figure = plt.figure(figsize=(9, 9))
axes = sns.scatterplot(data=df, x='Expected', y='Predicted',
         hue='Predicted', palette='cool', legend=False)
##set the x- and y-axes’ limits
start = min(expected.min(), predicted.min())
end = max(expected.max(), predicted.max())
axes.set_xlim(start, end)
axes.set_ylim(start, end)
##plot a line that represents perfect predictions 
line = plt.plot([start, end], [start, end], 'k--')


### Regression Model Metrics

from sklearn import metrics
metrics.r2_score(expected, predicted)
##call function mean_squared_error (from module sklearn.metrics) 
metrics.mean_squared_error(expected, predicted)


'''