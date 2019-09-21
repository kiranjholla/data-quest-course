## 1. Storing Data ##

from csv import reader

opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = ['4+', '9+', '12+', '17+']
numbers = [4433, 987, 1155, 622]
content_rating_numbers = [content_ratings, numbers]

## 2. Dictionaries ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
print(content_ratings)

## 3. Indexing ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

over_9 = content_ratings['9+']
over_17 = content_ratings['17+']
print(over_9)
print(over_17)

## 4. Alternative Way of Creating a Dictionary ##

content_ratings = {}
content_ratings['4+'] = 4433
content_ratings['9+'] = 987
content_ratings['12+'] = 1155
content_ratings['17+'] = 622

over_12_n_apps = content_ratings['12+']

## 5. Key-Value Pairs ##

d_1 = {'key_1': 'first_value', 
 'key_2': 2,
 'key_3': 3.14,
 'key_4': True,
 'key_5': [4,2,1],
 'key_6': {'inner_key' : 6}
 }

error = True

## 6. Checking for Membership ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

is_in_dictionary_1 = '9+' in content_ratings
is_in_dictionary_2 = 987 in content_ratings

if '17+' in content_ratings:
    result = 'It exists'

print(result)

## 7. Counting with Dictionaries ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)


content_ratings = {
    '4+': 0,
    '9+': 0,
    '12+': 0,
    '17+': 0
}

for record in apps_data[1:]:
    # print(record[10])
    if record[10] in content_ratings:
        content_ratings[record[10]] += 1

print(content_ratings)

## 8. Finding the Unique Values ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {}

for record in apps_data[1:]:
    if record[10] in content_ratings:
        content_ratings[record[10]] += 1
    else:
        content_ratings[record[10]] = 1
        
print(content_ratings)

## 9. Proportions and Percentages ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

genre_counting = {}

for record in apps_data[1:]:
    if record[11] in genre_counting:
        genre_counting[record[11]] += 1
    else:
        genre_counting[record[11]] = 1

print(genre_counting)

for genre in genre_counting:
    print(genre + ': ' + str(genre_counting[genre] / len(apps_data[1:]) * 100))


## 10. Looping over Dictionaries ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

for rate in content_ratings:
    content_ratings[rate] /= total_number_of_apps
    content_ratings[rate] *= 100

percentage_17_plus = content_ratings['17+']
percentage_15_allowed = content_ratings['12+'] + content_ratings['9+'] + content_ratings['4+']


## 11. Keeping the Dictionaries Separate ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

c_ratings_proportions = {}
c_ratings_percentages = {}

for rate in content_ratings:
    c_ratings_proportions[rate] = content_ratings[rate] / total_number_of_apps
    c_ratings_percentages[rate] = c_ratings_proportions[rate] * 100
    


## 12. Frequency Tables for Numerical Columns ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

data_sizes = []
for record in apps_data[1:]:
    data_sizes.append(float(record[2]))
    
min_size = min(data_sizes)
max_size = max(data_sizes)

## 13. Filtering for the Intervals ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

data_sizes = []
for record in apps_data[1:]:
    data_sizes.append(float(record[5]))

min_size = min(data_sizes)
max_size = max(data_sizes)


#0 - 1000
#1001 - 5000
#5000 - 10000
#10000 - 50000
#50000 - 100000
#100000 - 500000
#500000 - 1000000
#1000000 - 5000000
#2974676

size_freq = {
    '0 - 1KB': 0,
    '1 - 10KB': 0,
    '10 - 50KB': 0,
    '50 - 100KB': 0,
    '100 - 500KB': 0,
    '500KB - 1MB': 0,
    '1 - 5MB': 0
}


for record in apps_data[1:]:
    data_size = float(record[5])
    if data_size >= 0.0 and data_size <= 1000.0:
        size_freq['0 - 1KB'] += 1
    elif data_size > 1000.0 and data_size <= 10000.0:
        size_freq['1 - 10KB'] += 1
    elif data_size > 10000.0 and data_size <= 50000.0:
        size_freq['10 - 50KB'] += 1
    elif data_size > 50000.0 and data_size <= 100000.0:
        size_freq['50 - 100KB'] += 1
    elif data_size > 100000.0 and data_size <= 500000.0:
        size_freq['100 - 500KB'] += 1
    elif data_size > 500000.0 and data_size <= 1000000.0:
        size_freq['500KB - 1MB'] += 1
    elif data_size > 1000000.0 and data_size <= 5000000.0:
        size_freq['1 - 5MB'] += 1

print(size_freq)