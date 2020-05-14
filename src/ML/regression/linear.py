import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df_train = pd.read_csv('../data/random-linear-regression/train.csv')
df_test = pd.read_csv('../data/random-linear-regression/test.csv')

x_train = df_train['x']
y_train = df_train['y']
x_test = df_test['x']
y_test = df_test['y']

x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)

x_train = x_train.reshape(-1, 1)
x_test = x_test.reshape(-1, 1)

if __name__ == '__main__':
    print(np.zeros((700, 1)))
