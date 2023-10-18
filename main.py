import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill

# from datetime import timedelta as td
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

        df0 = self.get_initial_clean_df()
        self.get_list_of_dates()
        self.make_processor_filter_rows(df0)

        self.df_cleaned = data.Data.df_cleaned
        self.beginning_date = data.Data.beg_date
        self.end_date = data.Data.end_date
        self.df_queried = data.Data.df_queried

    def get_initial_clean_df(self)->pd.DataFrame:
        df0 = helper.get_initial_df()
        df  = processor.clean_and_save_attributes(df0)
        data.Data.df_cleaned = df
        return df


    def count(self) -> pd.Series:

        df_valuecounts = (
            self.df_queried.sort_values(by="Provider")
            .reset_index(drop=True)
            .Provider.value_counts()
        )
        return df_valuecounts

    def value_count_holidays(self, minor_holidays:bool = True) -> pd.Series:
        data.Data.minor_holidays = minor_holidays
        data.Data.weekends = False

        # I think I have to helper.get_datelist()


        return self.count()

    def value_count_weekends(self, minor_holidays:bool = False) -> pd.Series:
        data.Data.weekends = True
        data.Data.minor_holidays = minor_holidays

        return self.count()

    def set_date_range(self, beg: str, end: str):
        # checks date to not be too early or too late
        # changes data.Beg_date and data.end_date
        if type(beg) != str or type(end) != str:
            ic(f"string format is needed in style '2022-01-01")
            return False
        data.Data.beg_date = beg
        data.Data.end_date = end
        ic(f"Beginning date is now {beg} and end date is {end}")

        return True
    
    # stats
    def describe(self) -> dict:
        # Should give us earliest and latest date
        # Should give us # of Fulltime & PARTIME  providers? 

        description: {
            "beginning_date": self.beginning_date,
            "end_date": self.end_date,
        }

        # Give us shift ratios of Providers F/ BD/ S/ C
        pass

    def query_again(self):
        # Using new date parameters:
        # self.beginning date
        # self.end_date
        # can query_again and set as self.df_queried
        pass

    def clean_save_(self, df_initial):
        self.df_cleaned = processor.clean_and_save_attributes(df_initial)

    def get_list_of_dates(self) -> None:
        helper.get_datelist()
    
    def make_processor_filter_rows(self, df):
        data.Data.df_queried = processor.filter_rows(df)



def main():
    data.Data.path_i = helper.return_path()
    

    # df = processor.clean_and_save_attributes(df)

    # helper.get_datelist()  # ->  gets datelists and saves it to Data, returns none

    # all queried dates are used to filter df
    # data.Data.df_queried = processor.filter_rows(df)


if __name__ == "__main__":
    main()
    sab = ShiftAdminBuddy()

    # ic(data.Data.dates_to_query)
    # ic(data.Data.beg_date)
    # ic(data.Data.end_date)
    # sab.set_date_range('2023-01-01', 10)
    # sab.set_date_range('2023-02-02', '2023-10-10')

    ic(sab.value_count_holidays())
    # ic(sab.())
