## 2. The Mean ##

distribution = [0,2,3,3,3,4,13]

mean = sum(distribution)/len(distribution)

dist_low = 0
dist_high = 0

center = ((max(distribution) - mean) == (mean - min(distribution)))
          
for x in distribution:
    if x < mean:
        dist_low += (mean - x)
    if x > mean:
        dist_high += (x - mean)

equal_distances = (dist_high == dist_low)

## 3. The Mean as a Balance Point ##

from numpy.random import randint, seed

equal_distances = 0;

def compare_distances(distribution, mean):
    dist_low = 0
    dist_high = 0
    
    for x in distribution:
        if x < mean:
            dist_low = round(dist_low + mean - x, 1)
        if x > mean:
            dist_high = round(dist_high + x - mean, 1)
    
    yo = dist_high == dist_low
    if not yo:
        dist_high = 0
        dist_low = 0
        for x in distribution:
            if x < mean:
                print (x, dist_low, round(mean - x, 1), round(dist_low + mean - x, 1))
            else:
                print(x, dist_high, round(x - mean, 1), dist_high + round(x - mean, 1)) 
            
            if x < mean:
                dist_low += round(mean - x, 1)
            if x > mean:
                dist_high += round(x - mean, 1)
        print(dist_high, dist_low, distribution, mean)
    return yo
        


for x in range(0, 5000):
    seed(x)
    distribution = randint(0, 1000, 10)
    mean = sum(distribution) / len(distribution)
    if compare_distances(distribution, mean):
        equal_distances += 1
    else:
        print(distribution, mean)
    

## 4. Defining the Mean Algebraically ##

one = False
two = False
three = False

## 5. An Alternative Definition ##

distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]


def first(distribution):
    sum_of_dist = 0;
    i = 1
    for _ in range(len(distribution)):
        sum_of_dist += distribution[i - 1]
        i += 1
    return sum_of_dist / len(distribution)


mean_1 = first(distribution_1)
mean_2 = first(distribution_2)
mean_3 = first(distribution_3)

## 6. Introducing the Data ##

import pandas as pd

houses = pd.read_table('AmesHousing_1.txt', sep='\t')

one = True
two = False
three = True


## 7. Mean House Prices ##

def mean(distribution):
    sum_distribution = 0
    for value in distribution:
        sum_distribution += value
        
    return sum_distribution / len(distribution)


function_mean = first(houses['SalePrice'].tolist())
pandas_mean = houses['SalePrice'].mean()
means_are_equal = function_mean == pandas_mean

## 8. Estimating the Population Mean ##

import matplotlib.pyplot as plt

sample_size = []
sample_error = []

mew = houses['SalePrice'].mean()

for iter in range(101):
    sample_size.append((5 + iter * 29))
    sales_sample = houses['SalePrice'].sample(n=(5 + iter * 29), random_state=iter)
    sample_mean = sales_sample.mean()
    sample_error.append(mew - sample_mean)
                       
                       
plt.scatter(x=sample_size, y=sample_error)
plt.axhline()
plt.axvline(x=2930)
plt.xlabel('Sample size')
plt.ylabel('Sampling error')
plt.show()                       
                       

## 9. Estimates from Low-Sized Samples ##

sample_mean = []
for iter in range(10000):
    sale_sample = houses['SalePrice'].sample(n=100, random_state=iter)
    sample_mean.append(sale_sample.mean())

plt.hist(sample_mean)
plt.axvline(x=houses['SalePrice'].mean())
plt.xlabel('Sample mean')
plt.ylabel('Frequency')
plt.xlim(0, 500000)

## 11. The Sample Mean as an Unbiased Estimator ##

population = [3, 7, 2]

samples = []

for x in range(len(population)):
    for y in range(len(population)):
        if x != y:
            samples.append([population[x], population[y]])


population_mean = sum(population) / len(population)

sample_means = []
for s in samples:
    sample_means.append(sum(s) / len(s))

mean_of_sample_means = sum(sample_means) / len(sample_means)

unbiased = population_mean == mean_of_sample_means