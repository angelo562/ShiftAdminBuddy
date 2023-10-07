import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill

# import os

from datetime import timedelta as td
import data
import helper
import processor
from icecream import ic


"""Shift Admin Buddy.  Designed to give schedule stats

input: Group Shift stats in excel format
output: Excel format?

Shift Admin buddy as a Class()

Sheet with Holiday stats, for last 2 years starting fiscal 4th quarter, 10/1

Include Major holidays, minor holidays, weekends, nights

"""


class ShiftAdminBuddy:
    def __init__(self):
        self.path = data.Data.path_i
        self.df = data.Data.df_cleaned
        self.df_a = data.Data.df_to_analyze
        # self.fxn_list = self.collect_fxns()
        data.Data.beg_date = self.df.Date.min().strftime("%Y-%m-%d")
        data.Data.end_date = (self.df.Date.max() + td(days=1)).strftime("%Y-%m-%d")

    def count(self):

        df_b = (
            self.df_a.sort_values(by="Provider")
            .reset_index(drop=True)
            .Provider.value_counts()
        )
        return df_b

    def v_count_holidays(self, beg_date:str=None, end_date:str=None):
        data.Data.holidays = True
        data.Data.weekends = False
        beg_date = beg_date
        end_date = end_date
        data.Data.dates_to_query = helper.get_datelist_asstring(None, beg_date, end_date)
        return self.count()

    def v_count_weekends(self):
        data.Data.holidays = False
        data.Data.weekends = True

        return self.count()
    
    # stats
    def describe(self):
        pass

if __name__ == "__main__":
    helper.helper()
    data.Data.dates_to_query = helper.get_datelist_asstring()  # maybe insert YEAR ARGUMENT HERE
    processor.process()

    sab = ShiftAdminBuddy()
    sab.describe()

    ic(sab.v_count_holidays('2021-01-01', '2024-01-01'))
    ic(data.Data.dates_to_query)