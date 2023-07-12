import pandas as pd

melbourne_housing_data_path = '../data/melb_data.csv'
melbourne_housing_data = pd.read_csv(melbourne_housing_data_path)

print(melbourne_housing_data.describe())
print(melbourne_housing_data.columns)


