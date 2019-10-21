## 2. Introduction To The Data ##

import pandas as pd

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])

unrate.head(12)

## 6. Introduction to Matplotlib ##

import matplotlib.pyplot as plt

plt.plot()
plt.show()

## 7. Adding Data ##

import matplotlib.pyplot as plt

plt.plot(unrate.head(12)['DATE'], unrate.head(12)['VALUE'])
plt.show()

## 8. Fixing Axis Ticks ##

import matplotlib.pyplot as plt

plt.xticks(rotation=90)
plt.plot(unrate.head(12)['DATE'], unrate.head(12)['VALUE'])
plt.show()

## 9. Adding Axis Labels And A Title ##

import matplotlib.pyplot as plt

plt.xticks(rotation=90)
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')

plt.plot(unrate.head(12)['DATE'], unrate.head(12)['VALUE'])
plt.show()