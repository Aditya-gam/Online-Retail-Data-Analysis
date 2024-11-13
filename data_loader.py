# data_loader.py
from ucimlrepo import fetch_ucirepo
import pandas as pd

def load_online_retail_data():
    # Step 1: Fetch dataset from UCI ML repository
    online_retail = fetch_ucirepo(id=352)
    
    # Step 2: Convert features to a pandas DataFrame (excluding InvoiceNo and StockCode)
    df_features = pd.DataFrame(online_retail.data.features)
    
    # Step 3: Fetch the CSV file directly from UCI repository to obtain InvoiceNo and StockCode
    data_url = "https://archive.ics.uci.edu/static/public/352/data.csv"
    df_full = pd.read_csv(data_url, usecols=['InvoiceNo', 'StockCode'], dtype={'InvoiceNo': str, 'StockCode': str})
    
    # Step 4: Concatenate InvoiceNo and StockCode with the rest of the DataFrame
    df = pd.concat([df_full, df_features], axis=1)
    
    # Display metadata for reference
    print(online_retail.metadata)
    
    # Return the complete DataFrame with all columns
    return df
