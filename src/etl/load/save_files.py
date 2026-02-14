import pandas as pd
import os
from utils.logger import get_logger

logger = get_logger(__name__)

#########################################################################################

def save_to_csv(df, save_path, index=False):
    """
    Save DataFrame to a CSV file
    
    :param df: DataFrame
    :param path_to_save: Destination path 
    :param index: (True/False)
    """
    
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=index)
    
#########################################################################################