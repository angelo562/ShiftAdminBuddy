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
    # Calculate Thanksgiving as the fourth Thursday in November
    thanksgiving_date = pd.to_datetime(f'{year}-11-01')
    thanksgiving_date += pd.DateOffset(weekday=3)  # Move to first Thursday
    thanksgiving_date += pd.DateOffset(weeks=3)   # Move to fourth Thursday
    return thanksgiving_date


def get_black_friday(year):
    # Calculate Thanksgiving Eve as the day before Thanksgiving
    thanksgiving_date = get_thanksgiving_date(year)
    black_friday = thanksgiving_date + pd.DateOffset(days=1)
    return black_friday


def get_christmas_eve_date(year):
    # Add year to 12-24
    return pd.to_datetime(f'{year}-12-24')


def get_christmas_date(year):
    # Add year to 12-25
    return pd.to_datetime(f'{year}-12-25')


def get_new_years_eve_date(year):
    return pd.to_datetime(f'{year}-12-31')


def get_new_years_date(year):
    # returns the NEXT year
    return pd.to_datetime(f'{year+1}-01-01')


def get_mothers_day_date(year):
    # Calculate Mother's Day as the second Sunday in May
    mothers_day_date = pd.to_datetime(f'{year}-05-01')
    mothers_day_date += pd.DateOffset(weekday=6)  # Move to first Sunday
    mothers_day_date += pd.DateOffset(weeks=1)   # Move to second Sunday
    return mothers_day_date


def get_halloween_date(year: int):
    return pd.to_datetime(f'{year}-10-31')

def get_memorial_day_date(year):
    # Calculate Memorial Day as the last Monday in May
    memorial_day_date = pd.to_datetime(f'{year}-05-01')
    memorial_day_date += pd.DateOffset(weekday=0)  # Move to the first day of May
    memorial_day_date += pd.DateOffset(weeks=3)    # Move to the fourth Monday
    memorial_day_date += pd.DateOffset(weeks=1)    # Move to the last Monday
    return memorial_day_date

def get_july_4(year):
    return pd.to_datetime(f'{year}-07-04')


major_holiday_fxns = [
    get_thanksgiving_date,
    get_black_friday,
    get_christmas_eve_date,
    get_christmas_date,
    get_new_years_eve_date,
    get_new_years_date,
]

minor_holiday_fxns = [
    get_mothers_day_date,
    get_halloween_date,
    get_memorial_day_date,
    get_july_4,

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

def get_list_dates(fxn_list)->list[dt.date,dt.date]:

    # get the range from data


    # get 2 years if there's no change in beg_date/end_date
    start_date = pd.to_datetime(data.Data.beg_date)
    end_date = pd.to_datetime(data.Data.end_date)

    years = [start_date.year,
             end_date.year]
    
    # date_range = pd.date_range(start_date, end_date)
    # date_list = pd.to_datetime(data.Data.dates_to_query)
    # mask = date_list.isin(date_range)
    # d = date_list[mask]
# 
    # datelist_within_range = []
    # for fxn in fxn_list:
    #     for year in years:
    #         datelist_within_range.append(fxn(year).strftime("%Y-%m-%d"))

    datelist = []  # list of pd.datetimes
    for fxn in fxn_list:
        for year in years:
            datelist.append(fxn(year))

    # Use a list comprehension to filter datetime objects within the date range
    datelist_within_range = [date for date in datelist if start_date <= date <= end_date]
    
    return sorted(datelist_within_range)    

def get_new_datelist(datelist:list[str,str]) -> list[str,str]:
    pass


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



def get_datelist():
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



