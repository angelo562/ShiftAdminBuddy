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

    return df

def compile_rows_to_analyze(df0):
    datelist = data.Data.dates_to_query
    df = df0[df0.Date.isin(datelist)]
    return df



    

