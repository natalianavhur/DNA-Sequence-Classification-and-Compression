import asyncio
import json
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# Set up the GraphQL transport pointing to the gnomAD API endpoint.
transport = AIOHTTPTransport(url="https://gnomad.broadinstitute.org/api")
client = Client(transport=transport, fetch_schema_from_transport=True)

# List of gene symbols.
genes = [
    "RHO", "USH2A", "RPGR", "RP1",   # Retinitis Pigmentosa & retinal dystrophies
    "CFH", "ARMS2", "HTRA1",          # Age-Related Macular Degeneration
    "MYOC", "OPTN", "CYP1B1",         # Glaucoma
    "RPE65", "CEP290", "CRB1"          # Leber Congenital Amaurosis & congenital disorders
]

async def fetch_and_save(gene_symbol):
    query = gql(f"""
    query VariantsInGene {{
      gene(gene_symbol: "{gene_symbol}", reference_genome: GRCh38) {{
        symbol
        canonical_transcript_id
        variants(dataset: gnomad_r4) {{
          variant_id
          pos
          exome {{
            ac
            ac_hemi
            ac_hom
            an
            af
          }}
        }}
      }}
    }}
    """)
    
    # Execute the query asynchronously.
    result = await client.execute_async(query)
    
    # Define the filename for saving the data.
    filename = f"{gene_symbol}_data.json"
    
    # Save the result as a formatted JSON file.
    with open(filename, "w") as outfile:
        json.dump(result, outfile, indent=2)
    
    print(f"Saved data for gene {gene_symbol} to {filename}")

async def main():
    # Loop through each gene and fetch its data.
    for gene in genes:
        try:
            await fetch_and_save(gene)
        except Exception as e:
            print(f"Error fetching data for {gene}: {e}")

if __name__ == "__main__":
    asyncio.run(main())
