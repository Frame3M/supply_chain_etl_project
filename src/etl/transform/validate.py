import pandas as pd

#########################################################################################

def validate_non_negative_columns(df, except_cols= []):
    """
    Check numeric columns for non-negative values
    
    :param df: DataFrame
    :param except_cols: Description
    """
    
    numeric_cols = df.select_dtypes('float64','Float64','int64','Int64').columns.difference(except_cols)
    for col in numeric_cols:
        if (df[col] < 0).any():
            raise
        
#########################################################################################

def validate_date_order(df, start_date, end_date):
    invalid = (df[end_date] < df[start_date]).sum()
    if invalid > 0:
        raise
    
#########################################################################################

def validate_not_null(df, columns):
    for col in columns:
        if df[col].isnull().sum() > 0:
            raise
        
#########################################################################################

def validate_not_future_date(df):
    today = pd.Timestamp.now().normalize()
    
    columns = df.select_dtypes('datetime64').columns
    for col in columns:
        if (df[col] > today).any():
            raise

#########################################################################################
        
def validate_item_quantity_not_zero(df):
    if (df['order_item_quantity'] == 0).any():
        raise
    
#########################################################################################

