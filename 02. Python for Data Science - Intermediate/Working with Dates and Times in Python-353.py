## 1. Introduction ##

from csv import reader

NAME = 0
APPT_MADE_DATE = 1
APPT_START_DATE = 2
APPT_END_DATE = 3
VISITEE_LAST_NAME = 4
VISITEE_FIRST_NAME = 5
MEETING_ROOM = 6
DESCRIPTION = 7


file = open("potus_visitors_2015.csv")
csv_data = reader(file)
potus = list(csv_data)

potus = potus[1:]

## 3. The Datetime Module ##

import datetime as dt

## 4. The Datetime Class ##

import datetime as dt

ibm_founded = dt.datetime(1911, 6, 16)

man_on_moon = dt.datetime(1969, 7, 20, 20, 17)

## 5. Using Strptime to Parse Strings as Dates ##

# The `potus` list of lists is available from
# the earlier screen where we created it

import datetime as dt

date_format = "%m/%d/%y %H:%M"

def parse_into_dates(dataset, cols, parse_format = date_format):
    if not isinstance(cols, list):
        cols = [cols]
    
    for record in dataset:
        for col in cols:
            record[col] = dt.datetime.strptime(record[col], parse_format)

parse_into_dates(potus, [APPT_START_DATE])

## 6. Using Strftime to format dates ##

import datetime as dt

def calc_visitors_per_month(dataset, col):
    monthly_visitors = {}
    for record in dataset:
        month_of_visit = dt.datetime.strftime(record[col], "%B, %Y")
        if not month_of_visit in monthly_visitors:
            monthly_visitors[month_of_visit] = 0
        monthly_visitors[month_of_visit] += 1
    return monthly_visitors

visitors_per_month = calc_visitors_per_month(potus, 2)


## 7. The Time Class ##

def get_appt_times(dataset, col):
    times_list = []
    for record in dataset:
        times_list.append(record[2].time())
    return times_list

appt_times = get_appt_times(potus, 2)

## 8. Comparing time objects ##

min_time = min(appt_times)
max_time = max(appt_times)

## 9. Calculations with Dates and Times ##

from datetime import timedelta
dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)


answer_1 = dt_2 - dt_1
answer_2 = dt_3 + timedelta(days=56)
answer_3 = dt_4 - timedelta(seconds=3600)

## 10. Summarizing Appointment Lengths ##

for row in potus:
    end_date = row[3]
    end_date = dt.datetime.strptime(end_date, "%m/%d/%y %H:%M")
    row[3] = end_date
    
    
def build_appt_length_dict(dataset, start_col, end_col):
    length_dict = {}
    for record in dataset:
        length = record[end_col] - record[start_col]
        if not length in length_dict:
            length_dict[length] = 0
        length_dict[length] += 1
    return length_dict


appt_lengths = build_appt_length_dict(potus, 2, 3)
min_length = min(appt_lengths)
max_length = max(appt_lengths)