from dataclasses import dataclass
import pandas 

@dataclass
class Data:
    path_i: str
    
    #initially from helper() 
    # df : pandas.core.frame.DataFrame 

    df_cleaned: pandas.core.frame.DataFrame
    dates_to_query : list #list of strings
    beg_date : pandas.DatetimeIndex
    end_date : pandas.DatetimeIndex
    df_queried: pandas.core.frame.DataFrame

    beg_year : int
    end_year : int
    fxn_list: list
    weekends : bool = False
    minor_holidays: bool = True
    major_holidays: bool = True



