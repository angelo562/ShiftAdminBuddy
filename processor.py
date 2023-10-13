"""module for processing"""

import data
from data import pandas as pd


def clean_and_save_attributes(df0):
    df_cleaned = clean_df(df0)
    data.Data.df_cleaned = df_cleaned
    data.Data.beg_date = df_cleaned.Date.min()
    data.Data.end_date = df_cleaned.Date.max()
    return df_cleaned


def clean_df(df):
    df = df.query("not Date.isna()").reset_index(drop=True)
    df = df.rename(columns={"Work Hrs": "Work_hrs", "Sched Hrs": "Scheduled_hrs",})

    # change Date to datetime dtype
    df.Date = pd.to_datetime(df.Date)

    # Ensure df.Time is a str
    df["Time"] = df["Time"].astype(str)
    # Format Provider names to be title()
    df.Provider = df.Provider.str.title().astype(str)
    return df


def filter_rows(df0):
    datelist = data.Data.dates_to_query
    df_queried = df0[df0.Date.isin(datelist)]
    return df_queried

