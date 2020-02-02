## 1. Introduction ##

import pandas as pd

houses = pd.read_table('AmesHousing_1.txt')

scale_land = 'ordinal'
scale_roof = 'nominal'
kitchen_variable = 'discrete'

## 2. The Mode for Ordinal Variables ##

def calculate_mode(lov):
    vals = {}
    for x in lov:
        if x not in vals:
            vals[x] = 0
        vals[x] += 1
    return max(vals, key=vals.get)

mode_function = calculate_mode(houses['Land Slope'].tolist())
mode_method = houses['Land Slope'].mode()
same = mode_function == mode_method

## 3. The Mode for Nominal Variables ##

def calculate_mode_with_counts(lov):
    vals = {}
    for x in lov:
        if x not in vals:
            vals[x] = 0
        vals[x] += 1
    return (max(vals, key=vals.get), vals)

mode, value_counts = calculate_mode_with_counts(houses['Roof Style'].tolist())
houses['Roof Style'].value_counts()


## 4. The Mode for Discrete Variables ##

houses['Bedroom AbvGr']

bedroom_variable = 'discrete'
bedroom_mode = houses['Bedroom AbvGr'].mode()

houses['SalePrice']
price_variable = 'continuous'
price_mode = houses['SalePrice'].mode()

## 5. Special Cases ##

intervals = pd.interval_range(start = 0, end = 800000, freq = 100000)
gr_freq_table = pd.Series([0,0,0,0,0,0,0,0], index = intervals)

for value in houses['SalePrice']:
    for interval in intervals:
        if value in interval:
            gr_freq_table.loc[interval] += 1
            break

print(gr_freq_table)

interval_max = gr_freq_table.idxmax()
mode = int(interval_max.left + (interval_max.right - interval_max.left) / 2)


mean = houses['SalePrice'].mean()
median = houses['SalePrice'].median()
sentence_1 = True
sentence_2 = True

## 6. Skewed Distributions ##

distribution_1 = {'mean': 3021 , 'median': 3001, 'mode': 2947}
distribution_2 = {'median': 924 , 'mode': 832, 'mean': 962}
distribution_3 = {'mode': 202, 'mean': 143, 'median': 199}

shape_1 = 'right skew'
shape_2 = 'right skew'
shape_3 = 'left skew'

## 7. Symmetrical Distributions ##

houses['Mo Sold'].plot.kde(xlim=(1, 12))

plt.axvline(houses['Mo Sold'].mode().iloc[0], label='Mode', color='Green')
plt.axvline(houses['Mo Sold'].median(), label='Median', color='Orange')
plt.axvline(houses['Mo Sold'].mean(), label='Mean', color='Black')
plt.legend()
