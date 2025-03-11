import os
import pandas as pd
from dna_seq.data.ClinVar_Eye_Disease.cleaning_data.CSVFileHandler import CSVFileHandler

def main():
    # Assuming the raw optn_variants.txt is in the optn folder.
    raw_txt_directory = "../"
    handler = CSVFileHandler("rpe65_variants.csv", csv_dir=raw_txt_directory)

    try:
        handler.create_csv()
        print("CSV file created successfully.")
    except Exception as e:
        print("An error occurred while creating the CSV:", e)
    
    try:
        df = handler.read_csv()
        print("CSV file read successfully. Here's a preview:")
        print(df.head())
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()