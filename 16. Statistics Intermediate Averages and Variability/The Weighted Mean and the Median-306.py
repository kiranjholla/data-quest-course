## 1. Introduction ##

mean_new = houses_per_year['Mean Price'].mean()
mean_original = houses['SalePrice'].mean()
difference = mean_original - mean_new

## 2. Different Weights ##

houses_per_year['TotalPrice'] = houses_per_year['Mean Price'] * houses_per_year['Houses Sold']
total_price = houses_per_year['TotalPrice'].sum()
total_houses_sold = houses_per_year['Houses Sold'].sum()

weighted_mean = total_price / total_houses_sold

mean_original = houses['SalePrice'].mean()

difference = round(weighted_mean, 10) - round(mean_original, 10)

## 3. The Weighted Mean ##

import numpy as np

def compulte_weighted_mean(values, weights):
    if len(values) != len(weights):
        raise ValueError('The number of values and weights needs to be the same')
    
    weighted_sum = sum([a * b for a,b in zip(values, weights)])
    sum_of_weights = sum(weights)
    return weighted_sum / sum_of_weights


weighted_mean_function = compulte_weighted_mean(houses_per_year['Mean Price'].tolist(), houses_per_year['Houses Sold'].tolist())

weighted_mean_numpy = np.average(houses_per_year['Mean Price'], weights=houses_per_year['Houses Sold'])
equal = round(weighted_mean_function, 10) == round(weighted_mean_numpy, 10)

## 4. The Median for Open-ended Distributions ##

from math import floor

class translate_table:
  
  def __init__(self, chars_to_keep='0123456789.'):
    self.keep_dict = dict((ord(c), c) for c in chars_to_keep) 
    
  def __getitem__(self, key):
    return self.keep_dict.get(key)


def get_median(distribution):
    sorted_dist = sorted([(x, int(str(x).translate(translate_table()))) for x in distribution], key=lambda x: x[1])
    # print(sorted_dist, floor(len(sorted_dist) / 2) , sorted_dist[floor(len(sorted_dist) / 2)])
    return sorted_dist[floor(len(sorted_dist) / 2)][0]

distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']

median1 = get_median(distribution1)
median2 = get_median(distribution2)
median3 = get_median(distribution3)



## 5. Distributions with Even Number of Values ##

series_copy = houses['TotRms AbvGrd'].copy()
series_copy.replace('10 or more', 10, inplace=True)
series_copy = series_copy.astype(int)
series_copy.sort_values(inplace=True)
# series_copy.reset_index()

print(series_copy.size, int(series_copy.size / 2))
if series_copy.size % 2 == 0:
    median = series_copy.iloc[int(series_copy.size / 2)]
else:
    median = series_copy.iloc[int(series_copy.size / 2)]

## 6. The Median as a Resistant Statistic ##

fig1, ax1 = plt.subplots()
houses['Lot Area'].plot.box(ax=ax1)
lotarea_difference = houses['Lot Area'].mean() - houses['Lot Area'].median()

fig2, ax2 = plt.subplots()
houses['SalePrice'].plot.box(ax=ax2)
saleprice_difference = houses['SalePrice'].mean() - houses['SalePrice'].median()



## 7. The Median for Ordinal Scales ##

mean = houses['Overall Cond'].mean()
median = houses['Overall Cond'].median()

houses['Overall Cond'].plot.hist()

more_representative = 'mean'