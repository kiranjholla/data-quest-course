## 1. Individual Values ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

houses['SalePrice'].plot.kde(xlim=(houses['SalePrice'].min(), houses['SalePrice'].max()))
plt.axvline(houses['SalePrice'].mean(), color='Black', label='Mean')

# Default ddof is 1 for Pandas Series; we are measuring for the Population here so ddof must be 0
plt.axvline(houses['SalePrice'].mean() + houses['SalePrice'].std(ddof=0), color='Red', label='Standard deviation')
plt.axvline(220000, color='Orange', label='220000')
plt.legend()

very_expensive = False

## 2. Number of Standard Deviations ##

mean = houses['SalePrice'].mean()
std = houses['SalePrice'].std(ddof=0)
distance = 220000 - mean

st_devs_away = distance / std


## 3. Z-scores ##

from numpy import std

min_val = houses['SalePrice'].min()
mean_val = houses['SalePrice'].mean()
max_val = houses['SalePrice'].max()

def calculate_mean(distribution):
    return sum(distribution) / len(distribution)

def calculate_z_score(value, distribution):
    mean = calculate_mean(distribution)
    st_dev = std(distribution, ddof=0)
    return (value - mean) / st_dev

min_z = calculate_z_score(min_val, houses['SalePrice'])
mean_z = calculate_z_score(mean_val, houses['SalePrice'])
max_z = calculate_z_score(max_val, houses['SalePrice'])


## 4. Locating Values in Different Distributions ##

def z_score(value, array, bessel = 0):
    mean = sum(array) / len(array)
    
    from numpy import std
    st_dev = std(array, ddof = bessel)
    
    distance = value - mean
    z = distance / st_dev
    
    return z


neighborhoods = ['NAmes', 'CollgCr', 'OldTown', 'Edwards', 'Somerst']
z_scores = {}

for x in neighborhoods:
    z_scores[x] = z_score(200000, houses.loc[houses['Neighborhood'] == x, 'SalePrice'])

best_investment = 'College Creek'

## 5. Transforming Distributions ##

mean = houses['SalePrice'].mean()
st_dev = houses['SalePrice'].std(ddof = 0)
houses['z_prices'] = houses['SalePrice'].apply(
    lambda x: ((x - mean) / st_dev)
    )


z_mean_price = houses['z_prices'].mean()
z_stdev_price = houses['z_prices'].std(ddof=0)

mean_area = houses['Lot Area'].mean()
stdev_area = houses['Lot Area'].std(ddof=0)
houses['z_area'] = houses['Lot Area'].apply(lambda x: (x - mean_area) / stdev_area)

z_mean_area = houses['z_area'].mean()
z_stdev_area = houses['z_area'].std(ddof=0)

## 6. The Standard Distribution ##

from numpy import std, mean
population = [0,8,0,8]

mean_pop = mean(population)
stdev_pop = std(population, ddof=0)

standardized_pop = [((x - mean_pop) / stdev_pop) for x in population]

mean_z = mean(standardized_pop)
stdev_z = std(standardized_pop, ddof=0)


## 7. Standardizing Samples ##

from numpy import std, mean
sample = [0,8,0,8]

x_bar = mean(sample)
s = std(sample, ddof = 1)

standardized_sample = []
for value in sample:
    z = (value - x_bar) / s
    standardized_sample.append(z)
    
    
stdev_sample = std(standardized_sample, ddof=1)

## 8. Using Standardization for Comparisons ##

mean_index1 = houses['index_1'].mean()
stdev_index1 = houses['index_1'].std(ddof=0)
houses['z_score1'] = houses['index_1'].apply(lambda x: (x - mean_index1) / stdev_index1)


mean_index2 = houses['index_2'].mean()
stdev_index2 = houses['index_2'].std(ddof=0)
houses['z_score2'] = houses['index_2'].apply(lambda x: (x - mean_index2) / stdev_index2)

houses.loc[0:1, ['z_score1', 'z_score2', 'SalePrice']]

better = 'first'