import pandas as pd
import numpy as np

def check_for_missing_columns(df_i, col_list):
  '''
  assigns null values to temp, humidty, dew point when HMP155 is turned off
  '''
  missing_cols = set(col_list).difference(set(df_i.columns.unique()))

  for col in missing_cols:
    df_i[col]=np.nan

  return df_i
