import pandas as pd
import numpy as np

#########################################################################################

def clean_strings(df):
    """
    Basic text cleaning
    
    :param df: DataFrame
    """
    
    df = df.copy()
    
    types = ['object', 'string']
    for col in df.select_dtypes(include=types).columns:
        df[col] = (
            df[col]
            .str.strip()
            .str.title()
        )
        
    uppercase_cols = ['customer_state', 'type', 'order_status', 'market']
    for col in uppercase_cols:
        df[col] = (
            df[col]
            .str.upper()
        )
        
    fix_dict = {
        'Ee. Uu.': 'EE. UU.'
    }
    
    if 'customer_country' in df.columns:
        df['customer_country'] = df['customer_country'].replace(fix_dict)
        
    return df

#########################################################################################

def fix_dtypes(df):
    """
    Data type conversion
    
    :param df: DataFrame
    """
    
    df = df.copy()
    
    # Numeric
    df['customer_zipcode'] = df['customer_zipcode'].astype('Int64')
    df['late_delivery_risk'] = df['late_delivery_risk'].astype('boolean')
    
    # Date
    df['order_date_dateorders'] = pd.to_datetime(
        df['order_date_dateorders'],
        format= '%m/%d/%Y %H:%M',
        errors= 'coerce'
    )
    
    df['shipping_date_dateorders'] = pd.to_datetime(
        df['shipping_date_dateorders'],
        format= '%m/%d/%Y %H:%M',
        errors= 'coerce'
    )
    
    # Categorical
    df['order_status'] = df['order_status'].astype('category')
    df['shipping_mode'] = df['shipping_mode'].astype('category')
    df['type'] = df['type'].astype('category')
    
    return df

#########################################################################################

def remove_duplicates(df):
    """
    Drop duplicate rows
    
    :param df: DataFrame
    """
    
    df = df.copy()
    
    df = df.drop_duplicates()
    
    return df

#########################################################################################