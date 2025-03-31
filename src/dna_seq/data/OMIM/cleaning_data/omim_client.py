import requests
import json
import os

class OMIMClient:
    """
    A client for querying the OMIM API.

    API Base URL: https://api.omim.org/api
    API Documentation: https://omim.org/help/api
    """
    def __init__(self, api_key=None):
        """
        Initialize the OMIMClient.
        """
        self.api_key = api_key or os.getenv("OMIM_API_KEY")
        if not self.api_key:
            raise ValueError("An OMIM API key is required. Provide it as a parameter or set the OMIM_API_KEY environment variable.")
        self.base_url = "https://api.omim.org/api"
        self.search_endpoint = "/entry/search"

    def get_gene_data(self, gene_symbol):
        """
        Query the OMIM API for entries related to a given gene symbol.
        """
        params = {
            "search": f"gene:{gene_symbol}",
            "apiKey": self.api_key,
            "format": "json"
        }
        response = requests.get(self.base_url + self.search_endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching data for gene {gene_symbol}: {response.status_code} {response.text}")

    def save_gene_data(self, gene_symbol, filename=None):
        """
        Query the OMIM API for a gene and save the output to a JSON file.
        """
        data = self.get_gene_data(gene_symbol)
        if filename is None:
            filename = f"{gene_symbol}_data.json"
        with open(filename, "w") as outfile:
            # Save the JSON data with indentation for readability
            json.dump(data, outfile, indent=2)
        print(f"Data for gene {gene_symbol} saved to {filename}")
