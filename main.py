```python
# Basic Data Processing in Python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load a sample dataset
data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# Display the first 5 rows of the dataset
print(data.head())

# Display the shape of the dataset
print('Shape of the dataset:', data.shape)

# Checking for missing values
print('Missing values:', data.isnull().sum())

# Basic statistics of the dataset
print('Basic statistics of the dataset:')
print(data.describe())

# Checking the datatype of each column
print('Datatypes of each column:')
print(data.dtypes)

# Converting a column datatype from one type to another
data['sepal_length'] = data['sepal_length'].astype(int)
print('Updated Datatypes of each column:')
print(data.dtypes)

# Creating a new column
data['sepal_length_cm'] = data['sepal_length'] * 2.54
print('Data after adding a new column:')
print(data.head())

# Dropping a column
data = data.drop('sepal_length', axis = 1)
print('Data after dropping a column:')
print(data.head())

# Renaming a column
data = data.rename(columns={'sepal_length_cm': 'sepal_length_in_cm'})
print('Data after renaming a column:')
print(data.head())

# Applying a function on a column
data['sepal_length_in_cm'] = data['sepal_length_in_cm'].apply(np.sqrt)
print('Data after applying function on a column:')
print(data.head())

# Groupby operation
grouped_data = data.groupby('species').mean()
print('Grouped data:')
print(grouped_data)

# Sorting the data
sorted_data = data.sort_values('sepal_length_in_cm')
print('Sorted data:')
print(sorted_data.head())

# Filtering the data
filtered_data = data[data['sepal_length_in_cm'] > 2.5]
print('Filtered data:')
print(filtered_data.head())

# Saving the processed data
data.to_csv('processed_data.csv', index=False)

# Plotting the data
plt.scatter(data['sepal_width'], data['sepal_length_in_cm'])
plt.xlabel('Sepal Width')
plt.ylabel('Sepal Length')
plt.title('Iris dataset - Sepal Length vs Sepal Width')
plt.show()
```
Цей код - це приклад основної обробки даних у Python за допомогою pandas. Він включає завантаження набору даних, перегляд основних статистичних даних, перевірку відсутніх значень, конвертацію типів даних, створення та видалення стовпців, перейменування стовпців, застосування функції до стовпця, операції групування, сортування та фільтрації даних, а також збереження оброблених даних і візуалізацію даних за допомогою matplotlib.