## 1. Functions ##

a_list = [4444, 8897, 6340, 9896, 4835, 4324, 10, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 37]


sum_manual = 0
for num in a_list:
    sum_manual += num

print(sum_manual)
print(sum(a_list))

## 2. Built-in Functions ##

ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']


content_ratings = {}

for rate in ratings:
    if rate in content_ratings:
        content_ratings[rate] += 1
    else:
        content_ratings[rate] = 1
        
        
        
print(content_ratings)

## 3. Creating Our Own Functions ##

def square(num):
    return num * num

squared_10 = square(10)
squared_16 = square(16)

## 4. The Structure of a Function ##

def add_10(num):
    return num + 10

add_30 = add_10(30)
add_90 = add_10(90)

## 5. Parameters and Arguments ##

def square(num):
    return num * num

squared_6 = square(6)
squared_11 = square(11)

## 6. Extract Values From Any Column ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)


def extract(col):
    extracted_col = []
    for record in apps_data[1:]:
        extracted_col.append(record[col])
    return extracted_col

genres = extract(11)

## 7. Creating Frequency Tables ##

# CODE FROM THE PREVIOUS SCREEN
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)    
    return column


def freq_table(lst):
    freq = {}
    for rec in lst:
        if rec in freq:
            freq[rec] += 1
        else:
            freq[rec] = 1
    return freq


genres = extract(11)
genres_ft = freq_table(genres)


print(genres)

## 8. Writing a Single Function ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)


def freq_table(col):
    ft = {}
    for rec in apps_data[1:]:
        if rec[col] in ft:
            ft[rec[col]] += 1
        else:
            ft[rec[col]] = 1

    return ft

ratings_ft = freq_table(7)

## 9. Reusability and Multiple Parameters ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# INITIAL FUNCTION
def freq_table(dataset, index):
    frequency_table = {}
    
    for row in dataset[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table


ratings_ft = freq_table(apps_data, 7)

## 10. Keyword and Positional Arguments ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(data_set, index):
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
        
    return frequency_table


content_ratings_ft = freq_table(apps_data, 10)
ratings_ft = freq_table(data_set=apps_data, index=7)
genres_ft = freq_table(data_set=apps_data, index=11)

## 11. Combining Functions ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(data_set, index):
    column = []    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length


def mean(data_set, index):
    column_data = extract(data_set, index)
    column_sum = find_sum(column_data)
    column_len = find_length(column_data)
    return column_sum / column_len

avg_price  = mean(apps_data, 4)

## 12. Debugging Functions ##

# INITIAL CODE
def extract(data_set, index):
    column = []
    
    for row in data_set[1:]:
        value = float(row[index])
        column.append(value)
    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += element
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    column = extract(data_set, index)
    return find_sum(column) / find_length(column)

avg_price = mean(apps_data, 4)
avg_rating = mean(apps_data, 7)