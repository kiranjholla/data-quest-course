## 3. Populations and Samples ##

question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')

wnba.head()

parameter = wnba['Games Played'].max()

sample = wnba['Games Played'].sample(random_state=1)

statistic = sample.max()

sampling_error = parameter - statistic

## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt

wnba = pd.read_csv('wnba.csv')

sample_means = []

parameter = wnba['PTS'].mean()

for iter in range(100):
    sample = wnba['PTS'].sample(10, random_state=iter)
    sample_means.append(sample.mean())

plt.scatter(x=list(range(1,101)), y=sample_means)
plt.axhline(parameter)
plt.plot()

## 7. Stratified Sampling ##

wnba['score_per_game'] = wnba['PTS'] / wnba['Games Played']

positions = ['G', 'F', 'C', 'G/F', 'F/C']

samples = {}
points_per_game_position = {}

for pos in positions:
    samples[pos] = wnba[wnba['Pos'] == pos].sample(10, random_state=0)
    points_per_game_position[pos] = samples[pos]['score_per_game'].mean()

position_most_points = max(points_per_game_position, key=points_per_game_position.get)

## 8. Proportional Stratified Sampling ##

less_12 = wnba[wnba['Games Played'] <= 12]
from_12_22 = wnba[(wnba['Games Played'] > 12) & (wnba['Games Played'] <= 22)]
more_22 = wnba[wnba['Games Played'] > 22]


sample_means = []

parameter = wnba['PTS'].mean()

for iter in range(100):
    l12_sample = less_12['PTS'].sample(1, random_state=iter)
    f12_sample = from_12_22['PTS'].sample(2, random_state=iter)
    m22_sample = more_22['PTS'].sample(7, random_state=iter)
    
    sample = pd.concat([l12_sample, f12_sample, m22_sample])
    sample_means.append(sample.mean())

plt.scatter(x=list(range(1,101)), y=sample_means)
plt.axhline(parameter)
plt.plot()


## 10. Cluster Sampling ##

team_clusters = pd.Series(wnba['Team'].unique()).sample(4, random_state=0)

cluster_data = pd.DataFrame()

for cluster in team_clusters:
    team_data = wnba[wnba['Team'] == cluster]
    cluster_data = cluster_data.append(team_data)


sampling_error_height = wnba['Height'].mean() - cluster_data['Height'].mean()
sampling_error_age = wnba['Age'].mean() - cluster_data['Age'].mean()
sampling_error_BMI = wnba['BMI'].mean() - cluster_data['BMI'].mean()
sampling_error_points = wnba['PTS'].mean() - cluster_data['PTS'].mean()
