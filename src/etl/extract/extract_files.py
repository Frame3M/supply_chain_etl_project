import pandas as pd

def extract_from_csv(path, enconding='utf-8'):
    """
    Function for extracting data from a CSV file
    
    :param path: File path that constains the data
    :param encoding: Encoding type (default: 'utf-8')
    """
    
    try:
        df = pd.read_csv(filepath_or_buffer=path, enconding=enconding)
        return df
    except:
        raise