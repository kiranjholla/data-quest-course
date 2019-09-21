## 1. Introducing Data Cleaning ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`

num_rows = len(moma)
print(num_rows)

## 2. Reading our MoMA Data Set ##

# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('artworks.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
children = list(read_file)

# remove the first row of the data, which
# contains the column names
moma = children[1:]

# Write your code here

## 3. Replacing Substrings with the replace Method ##

age1 = "I am thirty-one years old"

age2 = age1.replace("one", "two")

print(age2)

## 4. Cleaning the Nationality and Gender Columns ##

# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again

def strip_parens(str):
    return str.replace("(","").replace(")","")


def clean_data(dataset, clean_cols):
    if not isinstance(clean_cols, list):
        clean_cols = [clean_cols]
        
    for record in dataset:
        for col_num in clean_cols:
            record[col_num] = strip_parens(record[col_num])

clean_data(moma, [2, 5])

print(moma[1:5])

## 5. String Capitalization ##

def capitlize_describe(dataset, clean_cols):
    if not isinstance(clean_cols, list):
        clean_cols = [clean_cols]
    
    for col in clean_cols:
        if not col[0] and not col[1]:
            col = (col, 'Unknown')
    
    for record in dataset:
        for col in clean_cols:
            record[col[0]] = record[col[0]].title()
        
            if not record[col[0]]:
                record[col[0]] = col[1]

capitlize_describe(moma, [(5, 'Gender Unknown/Other'), (2, 'Nationality Unknown')])

## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = strip_parens(date)
        date = int(date)
    return date


def clean_dates(dataset, date_cols):
    if not isinstance(date_cols, list):
        date_cols = [date_cols]
    
    for record in dataset:
        for col in date_cols:
            record[col] = clean_and_convert(record[col])

clean_dates(moma, [3, 4])

## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]


def strip_characters(dirty_string):
    clean_string = dirty_string
    for char in bad_chars:
        clean_string = clean_string.replace(char, "")
    return clean_string

def clean_dirty_data(dataset):
    cleaned_data = []
    for record in dataset:
        cleaned_data.append(strip_characters(record))
    return cleaned_data

stripped_test_data = clean_dirty_data(test_data)

## 8. Parsing Numbers from Complex Strings, Part Two ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

def derive_average_year(range_str):
    theyears = [int(x) for x in range_str.split("-")]
    return round((theyears[0] + theyears[1]) / 2)

def process_date(year_str):
    if "-" in year_str:
        return derive_average_year(year_str)
    else:
        return int(year_str)

def process_year_data(dataset, cols = []):
    processed_dataset = []
    if not isinstance(cols, list):
        cols = [cols]
    
    for record in dataset:
        if isinstance(record, list):
            for col in cols:
                record[col] = strip_characters(record[col])
                record[col] = process_date(record[col])
        else:
            processed_dataset.append(process_date(record))
    return processed_dataset


processed_test_data = process_year_data(stripped_test_data)

# I am mutating moma itself here --- Not a good construct but works for now
process_year_data(moma, [6])

        