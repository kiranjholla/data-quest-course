## 1. The Range ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

def calculate_range(lov):
    return max(lov) - min(lov)

range_by_year = {}

for yr in houses['Yr Sold'].value_counts().index.tolist():
    range_by_year[yr] = calculate_range(houses.loc[houses['Yr Sold'] == yr, 'SalePrice'].tolist())


one = False
two = True

## 2. The Average Distance ##

C = [1,1,1,1,1,1,1,1,1,21]

def calculate_mean(lov):
    return sum(lov) / len(lov)

def calculate_variability(lov):
    mean = calculate_mean(lov)
    distances = []
    for x in lov:
        distances.append(x - mean)
    return calculate_mean(distances)

avg_distance = calculate_variability(C)
print(avg_distance)

## 3. Mean Absolute Deviation ##

C = [1,1,1,1,1,1,1,1,1,21]

def calculate_mad(lov):
    #mean absolute distance
    mean = calculate_mean(lov)
    distances = []
    for x in lov:
        distances.append(abs(x - mean))
    return calculate_mean(distances)

mad = calculate_mad(C)

## 4. Variance ##

C = [1,1,1,1,1,1,1,1,1,21]

def calculate_variance(lov):
    mean = calculate_mean(lov)
    distances = []
    for x in lov:
        distances.append((x - mean) ** 2)
    return calculate_mean(distances)

variance_C = calculate_variance(C)

## 5. Standard Deviation ##

from math import sqrt
C = [1,1,1,1,1,1,1,1,1,21]

def calculate_std_deviation(lov):
    variance = calculate_variance(lov)
    return sqrt(variance)

standard_deviation_C = calculate_std_deviation(C)



## 6. Average Variability Around the Mean ##

# Dataquest implementation for Std. Deivation
def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
        
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

yearly_stats = {}
for yr in houses['Yr Sold'].value_counts().index.tolist():
    yearly_stats[yr] = calculate_std_deviation(houses.loc[houses['Yr Sold'] == yr, 'SalePrice'].tolist())

greatest_variability = max(yearly_stats, key=yearly_stats.get)
lowest_variability = min(yearly_stats, key=yearly_stats.get)

## 7. A Measure of Spread ##

sample1 = houses['Year Built'].sample(50, random_state = 1)
sample2 = houses['Year Built'].sample(50, random_state = 2)

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)


bigger_spread = 'sample 2'
st_dev1 = calculate_std_deviation(sample1)
st_dev2 = calculate_std_deviation(sample2)

## 8. The Sample Standard Deviation ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

import matplotlib.pyplot as plt



std_devs = []
for x in range(5000):
    sample = houses['SalePrice'].sample(10, random_state=x)
    std_devs.append(calculate_std_deviation(sample))
    
plt.hist(std_devs)
plt.axvline(calculate_std_deviation(houses['SalePrice']))
    

## 9. Bessel's Correction ##

from math import sqrt

def calculate_variance_with_bessels_correction(array):
    mean = calculate_mean(array)
    distances = []
    for x in array:
        distances.append((x - mean) ** 2)
    return sum(distances) / (len(array) - 1)
            
def calculate_std_deviation_with_bessels_correction(array):
    return sqrt(calculate_variance_with_bessels_correction(array))

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)


import matplotlib.pyplot as plt
st_devs = []

for x in range(5000):
    sample = houses['SalePrice'].sample(10, random_state=x)
    st_dev = calculate_std_deviation_with_bessels_correction(sample)
    st_devs.append(st_dev)

pop_stdev = calculate_std_deviation(houses['SalePrice'])
plt.hist(st_devs)
plt.axvline(pop_stdev)

## 10. Standard Notation ##

sample = houses.sample(100, random_state = 1)
from numpy import std, var


pandas_stdev = sample['SalePrice'].std()
numpy_stdev = std(sample['SalePrice'], ddof=1)
equal_stdevs = pandas_stdev == numpy_stdev

pandas_var = sample['SalePrice'].var()
numpy_var = var(sample['SalePrice'], ddof=1)
equal_vars = pandas_var == numpy_var

## 11. Sample Variance — Unbiased Estimator ##

population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]

sample_vars = []
sample_std = []
for x in samples:
    sample_vars.append(calculate_variance_with_bessels_correction(x))
    sample_std.append(calculate_std_deviation_with_bessels_correction(x))

equal_var = calculate_mean(sample_vars) == calculate_variance(population)
equal_stdev = calculate_mean(sample_std) == calculate_std_deviation(population)