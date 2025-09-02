import pandas as pd
import numpy as np
import glob

def check_for_missing_columns(df_i, col_list):
  missing_cols = set(col_list).difference(set(df_i.columns.unique()))
  for col in missing_cols:
    df_i[col]=np.nan
  return df_i
