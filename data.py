from dataclasses import dataclass
import pandas 

@dataclass
class Data:
    path_i: str
    
    #initially from helper() 
    df : pandas.core.frame.DataFrame 

    df_cleaned: pandas.core.frame.DataFrame
    dates_to_query : list #list of strings
    beg_date : str
    end_date : str
    df_to_analyze: pandas.core.frame.DataFrame

    beg_year : str
    end_year : str
    fxn_list: list
    holidays : bool = True
    weekends : bool = False
    minor_holidays: bool = True

