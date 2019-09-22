## 1. Reading our MoMA Data Set ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Generic function to convert date values
def convert_dates_to_int(dataset, cols):
    if not isinstance(cols, list):
        cols = [cols]
    
    for record in dataset:
        for col in cols:
            if record[col] != "":
                record[col] = int(record[col])
                
# Now convert birth date, death date and begin date
convert_dates_to_int(moma, [3, 4, 6])


## 2. Calculating Artist Ages ##

def calculate_age(begin_date, art_date):
    return art_date - begin_date

def process_record_age(record):
    birth_date = record[3]
    art_date = record[6]
    if isinstance(birth_date, int):
        age = calculate_age(birth_date, art_date)
    else:
        age = 0
    
    return age

def process_all_ages(dataset):
    ages = []
    for record in dataset:
        ages.append(process_record_age(record))
        
    return ages

def process_final_ages(ages):
    output = []
    for age in ages:
        if age <= 20:
            output.append("Unknown")
        else:
            output.append(age)
    return output

ages = process_all_ages(moma)
final_ages = process_final_ages(ages)

## 3. Converting Ages to Decades ##

# The final_ages variable is available
# from the previous screen

def convert_to_decade_string(age):
    if age == "Unknown":
        return age
    
    return str(age)[:-1] + "0s"

def process_all_ages(dataset):
    output = []
    for age in dataset:
        output.append(convert_to_decade_string(age))
    
    return output

decades = process_all_ages(final_ages)

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen

def build_freq_table(dataset):
    table = {}
    for record in dataset:
        if record in table:
            table[record] += 1
        else:
            table[record] = 1
    return table

decade_frequency = build_freq_table(decades)

## 5. Inserting Variables Into Strings ##

artist = "Pablo Picasso"
birth_year = 1881

template = "{artist}'s birth year is {year}"
message = template.format(artist=artist, year=birth_year)
print(message)

## 6. Creating an Artist Frequency Table ##

def build_freq_table(dataset, col):
    freq_table = {}
    for record in dataset:
        if not record[col] in freq_table:
            freq_table[record[col]] = 0
        freq_table[record[col]] += 1
    return freq_table

artist_freq = build_freq_table(moma, 1)

## 7. Creating an Artist Summary Function ##

def artist_summary(artist):
    template = "There are {} artworks by {} in the data set"
    message = template.format(artist_freq[artist], artist)
    print(message)
    
artist_summary("Henri Matisse")

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]


def print_country_pop(country):
    template = "The population of {} is {:,.2f} million"
    message = template.format(country[0], country[1])
    print(message)
    
def process_countries():
    for country in pop_millions:
        print_country_pop(country)
        
        
process_countries()

## 9. Challenge: Summarizing Artwork Gender Data ##

gender_freq = build_freq_table(moma, 5)

template = "There are {:,} artworks by {} artists"

for gender in gender_freq:
    print(template.format(gender_freq[gender], gender))
         