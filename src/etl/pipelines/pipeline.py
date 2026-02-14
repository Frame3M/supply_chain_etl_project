from etl.extract.extract_files import extract_from_csv
from etl.transform.normalize import standarize_columns
from etl.transform.cleaning import clean_strings, fix_dtypes, remove_duplicates, drop_rows_with_nulls, fill_missing_zipcode
from etl.transform.validate import validate_non_negative_columns, validate_date_order, validate_not_null

def run_pipeline():
    """
    Orchestrates all ETL stages.
    Each step logs its execution and allows failures to be isolated by stage
    """
    
    df_raw = extract_from_csv(path= '../../../data/raw/supply_chain_raw.csv', enconding= 'cp1252')
    
    
    df = standarize_columns(df_raw)
    df = clean_strings(df)
    df = fix_dtypes(df)
    df = remove_duplicates(df)
    df = drop_rows_with_nulls(df, subset= ['customer_lname', 'customer_zipcode'])
    df = fill_missing_zipcode(df)
    
    
    validate_non_negative_columns(df, except_cols= ['benefit_per_order', 'latitude', 'longitude', 'order_item_profit_ratio', 'order_profit_per_order'])
    validate_date_order(df, 'order_date_dateorders', 'shipping_date_dateorders')
    validate_not_null(df, columns= ['category_id', 'customer_id', 'department_id', 'order_customer_id', 'order_id', 'order_item_cardprod_id', 'order_item_id', 'product_card_id', 'product_category_id'])