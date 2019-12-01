## 4. Reading in the Data ##

import pandas as pd
import os

data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}


for file in data_files:
    name = os.path.splitext(os.path.basename(file))[0]
    data[name] = pd.read_csv('schools/{}'.format(file))


## 5. Exploring the SAT Data ##

print(data['sat_results'].head(5))

## 6. Exploring the Remaining Data ##

for hs in data:
    print(hs, data[hs].head(5))

## 8. Reading in the Survey Data ##

all_survey = pd.read_csv('schools/survey_all.txt', encoding='windows-1252', delimiter='\t')
d75_survey = pd.read_csv('schools/survey_d75.txt', delimiter='\t', encoding='windows-1252')
survey = pd.concat([all_survey, d75_survey], axis=0)
survey.head(5)

## 9. Cleaning Up the Surveys ##

list_of_cols = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]

survey['DBN'] = survey['dbn']

survey = survey.loc[:,list_of_cols]

data['survey'] = survey

print(data['survey'].shape)

## 11. Inserting DBN Fields ##

# Function to create 2 digit padded version
def pad_number(number, places=2):
    str_number = str(number);
    if len(str_number) < places:
        str_number = str_number.zfill(places)
    return str_number

# DBN Column in hs_directory
data['hs_directory']['DBN'] = data['hs_directory']['dbn']

# DBN Column in class_size
data['class_size']['padded_csd'] = data['class_size']['CSD'].apply(pad_number)
data['class_size']['DBN'] = data['class_size']['padded_csd'] + data['class_size']['SCHOOL CODE'] 

data['class_size'].head(5)

## 12. Combining the SAT Scores ##

# Convert SAT scores to numeric
for col in ['SAT Math Avg. Score', 'SAT Critical Reading Avg. Score', 'SAT Writing Avg. Score']:
    data['sat_results'][col] = pd.to_numeric(data['sat_results'][col], errors='coerce')

# Adding the SAT Scores
data['sat_results']['sat_score'] = data['sat_results']['SAT Math Avg. Score'] + data['sat_results']['SAT Critical Reading Avg. Score'] + data['sat_results']['SAT Writing Avg. Score']

data['sat_results']['sat_score'].head(5)

## 13. Parsing Geographic Coordinates for Schools ##

import re


def extract_coords(value, coord='lat'):
    match = re.search('(?<=\()(?P<lat>[\-\d\.]+)\,\s?(?P<long>[\-\d\.]+)(?=\))', value)
    return match.group(coord)

extract_coords('1110 Boston Road\nBronx, NY 10456\n(40.8276026690005, -73.90447525699966)')

data['hs_directory']['lat'] = data['hs_directory']['Location 1'].apply(extract_coords, args=('lat',))

data['hs_directory'].head(5)

## 14. Extracting the Longitude ##

import re

data['hs_directory']['lon'] = data['hs_directory']['Location 1'].apply(extract_coords, args=('long',))

data['hs_directory']['lat'] = pd.to_numeric(data['hs_directory']['lat'], errors='coerce')
data['hs_directory']['lon'] = pd.to_numeric(data['hs_directory']['lon'], errors='coerce')

data['hs_directory'].head(5)