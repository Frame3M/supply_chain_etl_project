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
    """
    Check that dates are in the correct order
    
    :param df: DataFrame
    :param start_date: Earliest date
    :param end_date: Most recent date
    """
    
    invalid = (df[end_date] < df[start_date]).sum()
    if invalid > 0:
        raise
    
#########################################################################################

def validate_not_null(df, columns):
    """
    Validate that there are no null values
    
    :param df: DataFrame
    :param columns: Columns to validate
    """
    
    for col in columns:
        if df[col].isnull().sum() > 0:
            raise
        
#########################################################################################

def validate_not_future_date(df):
    """
    Validate that there are no future dates
    
    :param df: DataFrame
    """
    
    today = pd.Timestamp.now().normalize()
    
    columns = df.select_dtypes('datetime64').columns
    for col in columns:
        if (df[col] > today).any():
            raise

#########################################################################################
        
def validate_item_quantity_not_zero(df):
    """
    Validate that the 'item_quantity' column has no zero values
    
    :param df: DataFrame
    """
    
    if (df['order_item_quantity'] == 0).any():
        raise
    
#########################################################################################

