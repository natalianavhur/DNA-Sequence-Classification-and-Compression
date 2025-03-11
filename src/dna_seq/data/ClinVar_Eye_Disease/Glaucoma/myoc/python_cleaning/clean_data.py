import pandas as pd
import os

from cleaning_data import CSVFileHandler 

def main():
    
    # Load the CSV file
    CSVFileHandler()


    # Drop Unnamed column.
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Check the data
    print(df.head())
    print(df.columns)
    



