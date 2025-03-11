import os
import pandas as pd

class CSVFileHandler:
    """
    A class for handling CSV file operations including creation, reading, and cleaning.
    """
    def __init__(self, csv_filename, csv_dir='.', csv_file=None):
        self.__csv_filename = csv_filename
        self.__csv_dir = csv_dir
        self.__csv_file = csv_file

    def get_csv_filename(self):
        return self.__csv_filename

    def csv_exists(self):
        return os.path.exists(self.__csv_filename)

    def get_csv_file(self):
        return self.__csv_file

    def set_csv_filename(self, csv_filename):
        self.__csv_filename = csv_filename

    def set_csv_file(self, csv_file):
        self.__csv_file = csv_file

    def create_csv(self):
        """
        Create a CSV file from a tab-delimited text file.
        """
        # Derive the base name from the CSV filename (e.g., 'optn_variants.csv' -> 'optn_variants')
        base_name = os.path.splitext(self.get_csv_filename())[0]
        # txt_file = f'{base_name}.txt'
        txt_file = os.path.join(self.__csv_dir, f'{base_name}.txt')

        # Debug: Check if the text file exists
        if not os.path.exists(txt_file):
            raise FileNotFoundError(f"Expected text file '{txt_file}' not found. Check your working directory.")
        
        print(f"Reading tab-delimited text file: {txt_file}")

        df = pd.read_csv(txt_file, delimiter='\t')
        print(f"Text file read successfully. Data shape: {df.shape}")
        
        df.to_csv(self.get_csv_filename(), index=False)
        print(f"CSV file '{self.get_csv_filename()}' created successfully.")

    def read_csv(self):
        """
        Read the CSV file and load its contents into a DataFrame.
        """
        if self.csv_exists():
            try:
                self.__csv_file = pd.read_csv(self.__csv_filename)
            except Exception as e:
                raise RuntimeError(f"Error reading CSV file '{self.__csv_filename}': {e}")
            return self.__csv_file
        else:
            raise FileNotFoundError(f"{self.__csv_filename} does not exist. Please create it first.")
              
    def clean_csv(self):
        """
        Clean the DataFrame by removing any columns with names that start with 'Unnamed'.
        """
        if self.__csv_file is not None:
            self.__csv_file = self.__csv_file.loc[:, ~self.__csv_file.columns.str.contains('^Unnamed')]
        else:
            print("No CSV data loaded to clean.")
