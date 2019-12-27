## 2. Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')

freq_distro_pos = wnba['Pos'].value_counts()
freq_distro_height = wnba['Height'].value_counts()

## 3. Sorting Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')

age_ascending = wnba['Age'].value_counts().sort_index()
age_descending = wnba['Age'].value_counts().sort_index(ascending=False)

## 4. Sorting Tables for Ordinal Variables ##

def make_pts_ordinal(row):
    if row['PTS'] <= 20:
        return 'very few points'
    if (20 < row['PTS'] <=  80):
        return 'few points'
    if (80 < row['PTS'] <=  150):
        return 'many, but below average'
    if (150 < row['PTS'] <= 300):
        return 'average number of points'
    if (300 < row['PTS'] <=  450):
        return 'more than average'
    else:
        return 'much more than average'

    
wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis = 1)

# Type your answer below
pts_ordinal_desc = wnba['PTS_ordinal_scale'].value_counts().iloc[[4, 3, 0, 2, 1, 5]]

## 5. Proportions and Percentages ##

wnba = pd.read_csv('wnba.csv')

age_proportions = wnba['Age'].value_counts(normalize=True).sort_index()

proportion_25 = age_proportions[25]
percentage_30 = age_proportions[30] * 100
percentage_over_30 = age_proportions.loc[30:].sum() * 100 #sum(wnba['Age'] >= 30) / len(wnba) * 100
percentage_below_23 = age_proportions.loc[:23].sum() * 100 #sum(wnba['Age'] <= 23) / len(wnba) * 100

#do = age_proportions[:5]
#to = age_proportions.iloc[:5]
#yo = age_proportions.loc[:5]

## 6. Percentiles and Percentile Ranks ##

from scipy.stats import percentileofscore

wnba = pd.read_csv('wnba.csv')

percentile_rank_half_less = percentileofscore(wnba['Games Played'], score=17, kind='weak')
percentage_half_more = 100 - percentile_rank_half_less

## 7. Finding Percentiles with pandas ##

wnba = pd.read_csv('wnba.csv')

age_percentiles = wnba['Age'].describe(percentiles=[.75, .5, .95])[3:]

age_upper_quartile = age_percentiles[2]
age_middle_quartile = age_percentiles[1]
age_95th_percentile = age_percentiles[3]


question1 = True
question2 = False
question3 = True


## 8. Grouped Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')

grouped_freq_table = wnba['PTS'].value_counts(normalize=True, bins=10).sort_index(ascending=False) * 100

## 10. Readability for Grouped Frequency Tables ##

wnba = pd.read_csv('wnba.csv')


intervals = pd.interval_range(start=0, end=600, freq=60)

gr_freq_table_10 = pd.Series([0 for i in range(10)], index=intervals)


for value in wnba['PTS']:
    for inter in intervals:
        if value in inter:
            gr_freq_table_10.loc[inter] += 1
            break