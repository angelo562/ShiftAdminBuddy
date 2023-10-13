"""module for processing"""

import data
from data import pandas as pd


def clean_df(df):
    df = df.query("not Date.isna()").reset_index(drop=True)
    df = df.rename(columns={"Work Hrs": "Work_hrs", "Sched Hrs": "Scheduled_hrs",})

    # change Date to datetime dtype
    df.Date = pd.to_datetime(df.Date)

    # Ensure df.Time is a str
    df["Time"] = df["Time"].astype(str)
    # Format Provider names to be title()
    df.Provider = df.Provider.str.title().astype(str)


    save_beginning_end_dates(df.Date)

    return df

def save_beginning_end_dates(Date_series) -> None:
    data.Data.beg_date = Date_series.min()
    data.Data.end_date = Date_series.max()

def filter_rows(df0):
    datelist = data.Data.dates_to_query
    df = df0[df0.Date.isin(datelist)]
    return df



    

