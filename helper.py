"""
A collection of helper methods
"""
import datetime as dt
import os
import data
from data import pandas as pd
import icecream as ic

def return_path():

    # inp1 = input(f"Please input location path of group shift stats: ")

    inp1 = r"C:\Users\Angel\Downloads\group_stats_detailed_152748_rsxaj713b9.xlsx"

    path1 = os.path.abspath(inp1.strip(' "'))
    return fr"{path1}"


# GROUP OF FXNS returning dates
def get_thanksgiving_date(year):
    # Start with November 1st of the given year
    date = dt.date(year, 11, 1)
    while date.weekday() != 3:  # Thursday is represented by 3
        date += dt.timedelta(days=1)
    date += dt.timedelta(weeks=3)
    return date


def get_thanksgiving_eve_date(year):
    date = get_thanksgiving_date(year)
    date -= dt.timedelta(days=1)
    return date


def get_christmas_eve_date(year):
    # Add year to 12-24
    return dt.date(year, 12, 24)


def get_christmas_date(year):
    # Add year to 12-25
    return dt.date(year, 12, 25)


def get_new_years_eve_date(year):
    return dt.date(year, 12, 31)


def get_new_years_date(year):
    # returns the NEXT year
    year += 1
    return dt.date(year, 1, 1)


def get_mothers_day_date(year):

    date = dt.date(year, 5, 1)
    # first Sunday in may as 6
    while date.weekday() != 6:
        date += dt.timedelta(days=1)
    # add one week to get to 2nd sunday in may
    date += dt.timedelta(weeks=1)
    return date


def get_halloween_date(year: int):
    return dt.date(year, 10, 31)


major_holiday_fxns = [
    get_thanksgiving_date,
    get_thanksgiving_eve_date,
    get_christmas_eve_date,
    get_christmas_date,
    get_new_years_eve_date,
    get_new_years_date,
]

minor_holiday_fxns = [
    get_mothers_day_date,
    get_halloween_date,
]


# collect what fxns to run
def collect_h_fxns(minor_h:bool):

    holiday_fxs = major_holiday_fxns
    # minor_h = data.Data.minor_holidays

    if minor_h:
        holiday_fxs += minor_holiday_fxns  # combine 2 lists if minor_h:

    data.Data.fxn_list = holiday_fxs
    return holiday_fxs


def get_initial_df():
    df = pd.read_excel(data.Data.path_i, header=1)
    return df

def get_list_dates(fxn_list)->list[str,str]:

    # get the range from data
    

    # get 2 years if there's no change in beg_date/end_date
    years = [dt.datetime.now().year,
             dt.datetime.now().year - 1,]
    

    date_list_asstring = []
    for fxn in fxn_list:
        for year in years:
            date_list_asstring.append(fxn(year).strftime("%Y-%m-%d"))
    return sorted(date_list_asstring)    


def if_all_holidays():
    # Gives a list of date strings if minorholidays:
    fxn_list = collect_h_fxns(minor_h=True)
    return get_list_dates(fxn_list)

def if_major_holidays():
    # then only give major holidays
    fxn_list = collect_h_fxns(minor_h=False)
    return get_list_dates(fxn_list)

def if_weekends():
    # Gives a list of date strings if_weekends:
    pass



def get_datelist_asstring():
    # default should be whole list?
    # list of holiday or weekend dates to put use with df.query()

    
    # if data.Data.Weekends:
    #     pass
    
    if data.Data.minor_holidays == True:
        data.Data.dates_to_query = if_all_holidays()
    
    else:
        data.Data.dates_to_query = if_major_holidays()
        

    # elif data.Data.weekends:
    #     # date_range = pd.date_range(start= self.beg_date, end= self.end_date)
    #     weekends = date_range[date_range.isin([5,6])]  # 5 and 6 is Sat/Sun
    #     weekend_date_list = weekends.strftime('%Y-%m-%d').tolist()
    #     return sorted(weekend_date_list)



