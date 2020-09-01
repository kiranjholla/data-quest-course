## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)

print(mean_group_a)
print(mean_group_b)

## 4. Test statistic ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)

mean_difference = mean_group_b - mean_group_a

print(mean_difference)

## 5. Permutation test ##

from numpy.random import rand
from numpy import mean

import matplotlib.pyplot as plt


mean_difference = 2.52
print(all_values)

mean_differences = [];
for iter in range(1000):
    group_a = []
    group_b = []
    for val in all_values:
        if rand() >= 0.5:
            group_a.append(val)
        else:
            group_b.append(val)
    
    mean_differences.append(mean(group_b) - mean(group_a))
    
plt.hist(mean_differences)

## 7. Dictionary representation of a distribution ##

sampling_distribution = {}
for diff in mean_differences:
    if diff in sampling_distribution:
        sampling_distribution[diff] += 1
    else:
        sampling_distribution[diff]=1

## 8. P value ##

from numpy import sum

frequencies = []
for dist in sampling_distribution:
    if dist >= 2.52:
        frequencies.append(sampling_distribution[dist])

thesum = sum([sampling_distribution[x] for x in sampling_distribution if x >= 2.5])
therealsum = sum(frequencies)

p_value = therealsum / 1000