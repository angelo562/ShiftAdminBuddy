import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill

# import os

from datetime import timedelta as td
import data
import helper
import processor



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
        self.beg_date = self.df.Date.min().strftime('%Y-%m-%d')
        self.end_date = (self.df.Date.max()+ td(days=1)).strftime('%Y-%m-%d')

    def count(self):
        df_b = (
            self.df_a.sort_values(by="Provider")
            .reset_index(drop=True)
            .Provider.value_counts()
        )
        return df_b
    
    def v_count_holidays(self):
        data.Data.holidays = True
        data.Data.weekends = False
        return self.count()

    def v_count_weekends(self):
        data.Data.holidays = False
        data.Data.weekends = True
        return self.count()

sab = ShiftAdminBuddy()
# print(sab.path)
# print(sab.df)
# print(sab.df_a)
print(sab.v_count_holidays())

# print(data.Data.fxn_list)
# sab.set_beg_date

# print(sab.beg_date)
# print(sab.end_date)





