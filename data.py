from dataclasses import dataclass
import pandas 

@dataclass
class Data:
    path_i: str
    df : pandas.core.frame.DataFrame
    df_cleaned: pandas.core.frame.DataFrame
    fxn_list: list

