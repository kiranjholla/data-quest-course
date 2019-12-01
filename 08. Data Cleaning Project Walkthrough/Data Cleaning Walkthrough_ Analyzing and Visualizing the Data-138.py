## 3. Finding Correlations With the r Value ##

correlations = combined.corr()
correlations = correlations['sat_score']

## 5. Plotting Enrollment With the Plot() Accessor ##

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.scatter(combined['total_enrollment'], combined['sat_score'])
plt.xlabel('total_enrollment')
plt.ylabel('sat_score')
plt.show()

## 6. Exploring Schools With Low SAT Scores and Enrollment ##

low_enrollment = combined[(combined['total_enrollment'] < 1000) & (combined['sat_score'] < 1000)]
print(low_enrollment['School Name'])

## 7. Plotting Language Learning Percentage ##

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.scatter(combined['ell_percent'], combined['sat_score'])
plt.xlabel('ell_percent')
plt.ylabel('sat_score')

plt.show()

## 9. Mapping the Schools With Basemap ##

from mpl_toolkits.basemap import Basemap

def create_map():
    m = Basemap(
        projection='merc', 
        llcrnrlat=40.496044, 
        urcrnrlat=40.915256, 
        llcrnrlon=-74.255735, 
        urcrnrlon=-73.700272,
        resolution='i'
    )

    m.drawmapboundary(fill_color='#85A6D9')
    m.drawcoastlines(color='#6D5F47', linewidth=.4)
    m.drawrivers(color='#6D5F47', linewidth=.4)
    
    return m;

m = create_map()

longitudes = combined['lon'].tolist()
latitudes = combined['lat'].tolist()

m.scatter(longitudes, latitudes, s=20, zorder=2, latlon=True)
plt.show()

## 10. Plotting Out Statistics ##

from mpl_toolkits.basemap import Basemap

m = create_map()
m.scatter(longitudes, latitudes, s=20, zorder=2, latlon=True, c=combined['ell_percent'], cmap='summer')
plt.show()

## 11. Calculating District-Level Statistics ##

import numpy as np

districts = combined.groupby('school_dist').agg(np.mean)

districts.reset_index(inplace=True)

districts.head()

## 12. Plotting Percent Of English Learners by District ##

m = create_map()

longitudes = districts['lon'].tolist()
latitudes = districts['lat'].tolist()

m.scatter(longitudes, latitudes, s=50, zorder=2, latlon=True, c=districts['ell_percent'], cmap='summer')
plt.show()