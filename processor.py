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

def concat_df(df_1, df_2):
        return pd.concat([df_1, df_2], axis=0)

def query_df(date, df):
        date = date
        return df.query("Date == @date")

def compile_rows_to_analyze(df0):
    datelist = data.Data.dates_to_query
    df = query_df(datelist[0], df0)
    for date in datelist[1:]:
        df = concat_df(df, query_df(date, df0))
    return df

def process():
    df = data.Data.df            # pulls from Data, to clean
    
    df = clean_df(df)            # removes duplicates
    data.Data.df_cleaned = df    # saves as df_cleaned

    # all queried dates are concatenated and saved to dataclass
    data.Data.df_to_analyze = compile_rows_to_analyze(df)   


    

