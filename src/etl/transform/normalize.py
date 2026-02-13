import pandas as pd
import numpy as np

#########################################################################################

def standarize_columns(df):
    """
    Function to standarize columns
    
    :param df: DataFrame
    """
    df = df.copy()
    df.colums = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ','_')
        .str.replace(r'\(|\)','',regex=True)
    )
    
    return df

#########################################################################################