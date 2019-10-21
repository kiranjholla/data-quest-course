## 1. Recap ##

import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])

unrate1948 = unrate.head(12)

plt.xticks(rotation=90)
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')

plt.plot(unrate1948['DATE'], unrate1948['VALUE'])
plt.show()

## 3. Matplotlib Classes ##

import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
# ax3 = fig.add_subplot(2, 1, 3) # As expected this throws an error

plt.show()

## 5. Adding Data ##

import matplotlib.pyplot as plt

fig = plt.figure()

ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

unrate1948 = unrate.loc[:11]
unrate1949 = unrate.loc[12:23]

ax1.plot(unrate1948['DATE'], unrate1948['VALUE'])
ax2.plot(unrate1949['DATE'], unrate1949['VALUE'])

plt.show()
                                       

## 6. Formatting And Spacing ##

fig = plt.figure(figsize=(12, 5))

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()

## 7. Comparing Across More Years ##

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 12))

ax = []
for year in range(5):
    yrax = fig.add_subplot(5, 1, year + 1)
    yrax.plot(unrate[year * 12 : year * 12 + 12]['DATE'], unrate[year * 12 : year * 12 + 12]['VALUE'])

plt.show()

## 8. Overlaying Line Charts ##

unrate['MONTH'] = unrate['DATE'].dt.month

fig = plt.figure(figsize=(6, 3))

plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c='red')
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'], c='blue')

plt.show()

## 9. Adding More Lines ##

fig = plt.figure(figsize=(10, 6))

colors = ['red', 'blue', 'green', 'orange', 'black']
for year in range(5):
    plt.plot(unrate[year * 12 : year * 12 + 12]['MONTH'], unrate[year * 12 : year * 12 + 12]['VALUE'], c=colors[year])

plt.show()

## 10. Adding A Legend ##

fig = plt.figure(figsize=(10,6))

colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=i + 1948)
    
plt.legend(loc='upper left')
plt.show()

## 11. Final Tweaks ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc='upper left')

plt.title('Monthly Unemployment Trends, 1948-1952')
plt.xlabel('Month, Integer')
plt.ylabel('Unemployment Rate, Percent')
plt.show()