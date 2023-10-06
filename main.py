import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill
import data

# import os

from datetime import timedelta as td
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
        self.holidays = True
        self.weekends = False
        self.path = data.Data.path_i
        self.datelist = self.get_datelist_asstring()
        self.df = data.Data.df_cleaned
        # self.df = self.compile_df_to_analyze()
            # self.fxn_list = self.collect_fxns()
        # self.beg_date = self.df.Date.min().strftime('%Y-%m-%d')
        # self.end_date = (self.df.Date.max()+ td(days=1)).strftime('%Y-%m-%d')

    def compile_df_to_analyze(self):
        def concat_df(df_1, df_2):
            return pd.concat([df_1, df_2], axis=0)

        def query_df(date):
            date = date
            return self.df.query("Date == @date")

        df = query_df(self.datelist[0])
        for date in self.datelist[1:]:
            df = concat_df(df, query_df(date))
        return df

    # list of holiday or weekend dates to put use with df.query()
    def get_datelist_asstring(self, fxn_list=None, year=2022):
        if self.holidays:
            if fxn_list is None:
                fxn_list = helper.collect_fxns()

            date_list_asstring = []
            for fxn in fxn_list:
                date_list_asstring.append(fxn(year).strftime("%Y-%m-%d"))
            return sorted(date_list_asstring)
        
    def count_holidays(self):
        self.holidays = True
        self.weekends = False

        df_c = (
            self.df.sort_values(by="Provider")
            .reset_index(drop=True)
            .Provider.value_counts()
        )

        print(df_c)
        return df_c

    def count_weekends(self):
        self.holidays = False
        self.weekends = True


sab = ShiftAdminBuddy()
# print(sab.datelist)
print(sab.path)
print(sab.df)

# "C:\Users\Angel\Downloads\group_stats_detailed_164259_90sxeijc97.xlsx"
# print(sab.path)
# sab.df.info()
# sab.count_holidays()
# print(sab.end_date)
# print(sab.beg_date)
