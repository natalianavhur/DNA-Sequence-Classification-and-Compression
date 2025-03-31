import requests
import os
from dna_seq.data.OMIM.cleaning_data.omim_client import OMIMClient
from dotenv import load_dotenv


"""
API Host: api.omim.org
API Base URL: https://api.omim.org/api
API Web Interface: https://api.omim.org/api/html/index.html
API Documentation: https://omim.org/help/api
"""

def main():
    # Load variables from .env file
    load_dotenv()
    # Get api_key from system
    api_key = os.getenv("OMIM_API_KEY")

    # Initialize the client
    client = OMIMClient(api_key)
    
    # Query data for gene
    gene_symbol = "CYP1B1"
    data = client.get_gene_data(gene_symbol)
    print(f"OMIM Data for gene {gene_symbol}:")
    print(data)
    
    # Save the data to a JSON file
    client.save_gene_data(gene_symbol)

if __name__ == "__main__":
    main()
