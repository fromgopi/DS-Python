import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

data_path = '../data/california_housing_train.csv'

training_df = pd.read_csv(filepath_or_buffer=data_path)

# print(training_df.head())

# print(training_df.describe())

model = tf.keras.Sequential()
print(model.name)

