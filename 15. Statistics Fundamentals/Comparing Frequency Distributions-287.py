## 2. Grouped Bar Plots ##

import seaborn as sns

sns.countplot(x='Exp_ordinal', hue='Pos', data=wnba, order=['Rookie', 'Little experience', 'Experienced', 'Very experienced', 'Veteran'], hue_order=sorted(['C', 'F', 'G', 'G/F', 'F/C']))

## 3. Challenge: Do Older Players Play Less? ##

sns.countplot(x='age_mean_relative', hue='min_mean_relative', data=wnba)
result = 'rejection'

## 4. Comparing Histograms ##

import matplotlib.pyplot as plt

wnba[wnba.Age >= 27]['MIN'].plot.hist(histtype = 'step', label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.hist(histtype = 'step', label = 'Young', legend = True)

plt.axvline(label='Average', x=497)

## 5. Kernel Density Estimate Plots ##

wnba[wnba.Age >= 27]['MIN'].plot.kde(label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.kde(label = 'Young', legend = True)
plt.axvline(x=497, label='Average')

## 7. Strip Plots ##

sns.stripplot(x = 'Pos', y = 'Weight', data = wnba)

sns.stripplot(x = 'Pos', y = 'Weight', data = wnba, jitter = True)



## 8. Box plots ##

sns.boxplot(x = 'Pos', y = 'Weight', data = wnba)

## 9. Outliers ##

sns.boxplot(wnba['Games Played'], whis = 1.5, orient = 'vertical', width = .15)

iqr = 29 - 22
lower_bound = 22 - iqr * 1.5
upper_bound = 29 + iqr * 1.5

outliers_low = sum(wnba['Games Played'] < lower_bound)
outliers_high = sum(wnba['Games Played'] > upper_bound)